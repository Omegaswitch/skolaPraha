#!/usr/bin/env python3
"""One-off importer from the old WordPress site (vos.mojezdravka.cz, Goodlayers "Kingster" theme).

    python3 tools/import_vos.py <crawl-dir> <api-dir>

<crawl-dir> is a `wget -r -E` mirror of https://vos.mojezdravka.cz/, <api-dir> holds the WordPress REST exports
(posts-1.json, pages-1.json, media-*.json, events.json). The importer writes
  content/pages/<slug>/index.html   pages (page-builder markup turned into plain semantic HTML)
  content/news/YYYY/MM/DD/slug.html posts (same URL as on the old site)
  content/events.json               school-year events (The Events Calendar)
  static/media/YYYY/MM/*            images and documents used by the imported content
  tools/legacy-links.json           old short links (/skolni-rad-vos) and their targets, for vercel.json
Re-running it never overwrites a file whose front matter says "imported": false.
"""
import html
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parent.parent
OLD = "https://vos.mojezdravka.cz"
UPLOADS = "/wp-content/uploads/sites/4/"
KEEP = {"p", "h2", "h3", "h4", "ul", "ol", "li", "a", "strong", "em", "u", "br", "img", "table", "thead", "tbody", "tr", "th", "td", "blockquote", "hr"}
RENAME = {"b": "strong", "i": "em"}
SKIP_BLOCKS = ("gdlr-core-revolution-slider-item", "gdlr-core-event-item", "gdlr-core-blog-item", "gdlr-core-column-service-media",
               "gdlr-core-divider-item", "kingster-page-title-wrap", "gdlr-core-social-network-item", "tribe-")


class Clean(HTMLParser):
    """Page-builder HTML -> allowlisted semantic HTML. Headings keep their relative order; levels are normalised later."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.stack, self.links, self.images = [], 0, [], [], []  # stack: (tag, output tag or None, skipping)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class") or ""
        if tag in ("br", "img", "hr", "input", "meta", "link", "source"):
            return self.void(tag, a)
        out = None
        if self.skip or tag in ("script", "style", "noscript", "svg", "button", "form", "iframe", "sr7-module") or any(s in cls for s in SKIP_BLOCKS):
            self.skip += 1
            self.stack.append((tag, None, True))
            return
        if "toggle-box-item-title" in cls or "title-item-title" in cls or "column-service-title" in cls or tag in ("h1", "h2"):
            out = "h2"
        elif tag in ("h3", "h4"):
            out = "h3"
        elif tag in ("h5", "h6"):
            out = "h4"
        else:
            out = RENAME.get(tag, tag)
        if out not in KEEP:
            out = None
        elif out == "a":
            href = a.get("href") or ""
            if not href or href.startswith(("javascript:", "#")):
                out = None
            else:
                self.links.append(href)
                self.out.append(f'<a href="{html.escape(href)}">')
        else:
            self.out.append(f"<{out}>")
        self.stack.append((tag, out, False))

    def void(self, tag, a):
        if self.skip:
            return
        if tag == "br":
            self.out.append("<br>")
        elif tag == "hr":
            self.out.append("<hr>")
        elif tag == "img":
            src = a.get("src") or a.get("data-src") or ""
            if src:
                self.images.append(src)
                self.out.append(f'<img src="{html.escape(src)}" alt="{html.escape(a.get("alt") or "")}">')

    def handle_endtag(self, tag):
        if not any(t == tag for t, _, _ in self.stack):
            return
        while self.stack:
            t, out, skipping = self.stack.pop()
            if skipping:
                self.skip -= 1
            elif out:
                self.out.append(f"</{out}>")
            if t == tag:
                break

    def handle_startendtag(self, tag, attrs):
        if tag in ("br", "img", "hr"):
            self.void(tag, dict(attrs))

    def handle_data(self, data):
        if not self.skip:
            self.out.append(html.escape(data, quote=False))


def tidy(h):
    h = h.replace("\xa0", " ")
    h = re.sub(r"[ \t\r\n]+", " ", h)
    for _ in range(4):
        h = re.sub(r"<(p|h2|h3|h4|li|strong|em|u|a[^>]*)>\s*</(p|h2|h3|h4|li|strong|em|u|a)>", "", h)
        h = re.sub(r"<(ul|ol)>\s*</\1>", "", h)
    h = re.sub(r"\s*<(/?)(p|h2|h3|h4|ul|ol|li|table|tr|blockquote|hr)\b", r"\n<\1\2", h)
    h = re.sub(r"(<br>\s*)+(</(p|li|h2|h3)>)", r"\2", h)
    h = re.sub(r"(<p>)\s*(<br>\s*)+", r"\1", h)
    h = re.sub(r"\n\s+", "\n", h)
    return h.strip()


def convert(fragment):
    c = Clean()
    c.feed(fragment)
    c.close()
    return tidy("".join(c.out)), c.links, c.images


def page_fragment(path):
    h = path.read_text(encoding="utf-8")
    i, j = h.find('id="kingster-page-wrapper"'), h.find("<footer")
    return h[i + 25:j] if i > 0 else ""


# ---------------------------------------------------------------- links, files, images

_redirect_cache = {}


def resolve(href):
    """An old-site href -> a site-relative URL (pages), or the uploads URL of a document. Short links are followed."""
    u = urlsplit(href)
    if u.scheme in ("mailto", "tel"):
        return href
    if u.netloc and u.netloc not in ("vos.mojezdravka.cz",):
        return href
    path = u.path or "/"
    if UPLOADS in path:
        return path
    if path in _redirect_cache:
        return _redirect_cache[path]
    target = path if path.endswith("/") else path + "/"
    try:
        req = urllib.request.Request(OLD + path, method="HEAD")
        opener = urllib.request.build_opener(NoRedirect)
        r = opener.open(req, timeout=15)
        target = urlsplit(r.geturl()).path
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 307, 308):
            target = urlsplit(e.headers["Location"]).path
    _redirect_cache[path] = target
    return target


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def fetch(url, dest):
    if dest.exists():
        return True
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        with urllib.request.urlopen(url if url.startswith("http") else OLD + url, timeout=60) as r:
            dest.write_bytes(r.read())
        return True
    except Exception as e:  # reported in the import log; the inventory flags it
        print(f"  ! could not fetch {url}: {e}")
        return False


def local_upload(path):
    """/wp-content/uploads/sites/4/2025/08/x.pdf -> /media/2025/08/x.pdf (one prefix, so one redirect covers old links)"""
    return "/media/" + unquote(path.split(UPLOADS, 1)[1])


def original_image(path):
    """WordPress size variants (-300x200) -> the uploaded original."""
    return re.sub(r"-\d+x\d+(\.\w+)$", r"\1", path)


def relink(body, short_links, log):
    def fix_a(m):
        href = html.unescape(m.group(1))
        t = resolve(href)
        if t.startswith(("mailto:", "tel:", "http")) and not t.startswith(OLD):
            if "vos.mojezdravka.cz" in t:
                t = urlsplit(t).path
            else:
                return f'<a href="{html.escape(t)}">'
        if UPLOADS in t:
            new = local_upload(t)
            if fetch(t, ROOT / "static" / new.lstrip("/")):
                log["files"].add(new)
            else:
                log["missing"].add(t)
            p = urlsplit(href).path
            if UPLOADS not in p:
                short_links[p.rstrip("/")] = new
            t = new
        return f'<a href="{html.escape(t)}">'

    def fix_img(m):
        p = urlsplit(html.unescape(m.group(1))).path
        if UPLOADS not in p:
            return ""
        orig = original_image(p)
        new = local_upload(orig)
        if fetch(orig, ROOT / "static" / new.lstrip("/")):
            log["images"].add(new)
            return f'<img src="{html.escape(new)}" alt="{m.group(2)}">'
        log["missing"].add(orig)
        return ""

    body = re.sub(r'<a href="([^"]*)">', fix_a, body)
    return re.sub(r'<img src="([^"]*)" alt="([^"]*)">', fix_img, body)


# ---------------------------------------------------------------- writing


def write_doc(path, meta, body):
    if path.exists():
        old = path.read_text(encoding="utf-8").split("---\n", 2)
        if len(old) == 3 and json.loads(old[1]).get("imported") is False:
            print(f"  kept {path.relative_to(ROOT)} (edited by hand)")
            return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{json.dumps(meta, ensure_ascii=False, indent=1)}\n---\n{body}\n", encoding="utf-8")


def main(crawl, api):
    crawl, api = Path(crawl), Path(api)
    site = crawl / "vos.mojezdravka.cz"
    short_links, log = {}, {"files": set(), "images": set(), "missing": set()}

    pages = json.loads((api / "pages-1.json").read_text())
    for p in pages:
        slug = urlsplit(p["link"]).path.strip("/")
        if slug in ("", "maintenance", "clanky"):
            continue  # home and news index are generated; "maintenance" is a theme page
        src = site / slug / "index.html"
        if not src.exists():
            log["missing"].add(p["link"])
            continue
        body, _, _ = convert(page_fragment(src))
        body = relink(body, short_links, log)
        meta = {"title": html.unescape(p["title"]["rendered"]), "url": f"/{slug}/", "legacyId": p["id"],
                "modified": p["modified"][:10], "status": "existing", "imported": True}
        write_doc(ROOT / "content" / "pages" / slug / "index.html", meta, body)

    media = {m["id"]: m for f in sorted(api.glob("media-*.json")) for m in json.loads(f.read_text())}
    for n in json.loads((api / "posts-1.json").read_text()):
        path = urlsplit(n["link"]).path
        y, m, d, slug = path.strip("/").split("/")
        body, _, _ = convert(n["content"]["rendered"])
        body = relink(body, short_links, log)
        image = None
        if n.get("featured_media") in media:
            src = urlsplit(media[n["featured_media"]]["source_url"]).path
            image = local_upload(src)
            if not fetch(src, ROOT / "static" / image.lstrip("/")):
                image = None
        meta = {"title": html.unescape(n["title"]["rendered"]).strip(), "url": path, "date": n["date"][:16],
                "categories": ["skola"], "excerpt": "", "image": image, "legacyId": n["id"], "author": "Škola", "imported": True}
        write_doc(ROOT / "content" / "news" / y / m / d / f"{slug}.html", meta, body)

    ev = json.loads((api / "events.json").read_text())
    events = []
    for e in ev.get("events", []):
        desc, _, _ = convert(e.get("description") or "")
        events.append({"title": html.unescape(e["title"]), "start": e["start_date"][:16], "end": e["end_date"][:16],
                       "allDay": e.get("all_day", False), "url": urlsplit(e["url"]).path, "description": relink(desc, short_links, log),
                       "categories": [c["name"] for c in e.get("categories", [])], "legacyId": e["id"]})
    (ROOT / "content" / "events.json").write_text(json.dumps(events, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    (ROOT / "tools" / "legacy-links.json").write_text(json.dumps(dict(sorted(short_links.items())), ensure_ascii=False, indent=1) + "\n")
    print(f"files {len(log['files'])}, images {len(log['images'])}, short links {len(short_links)}, missing {sorted(log['missing'])}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
