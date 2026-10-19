#!/usr/bin/env python3
"""Static site generator for the VOŠZ website (engine from maltezskyrad.cz). Python 3.10+, standard library only.

    python3 build.py                 preview build into dist/ (noindex, content-status labels shown)
    python3 build.py --production    production build (indexable, no status labels)
    python3 build.py serve [port]    preview build, then serve dist/ with _headers and _redirects applied
"""
import html
import json
import re
import shutil
import struct
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTENT, STATIC, DIST = ROOT / "content", ROOT / "static", ROOT / "dist"
PRODUCTION = "--production" in sys.argv
SITE = json.loads((CONTENT / "site.json").read_text(encoding="utf-8"))
EVENTS = json.loads((CONTENT / "events.json").read_text(encoding="utf-8"))
ASSET_VERSION = datetime.now().strftime("%Y%m%d%H%M")
esc = lambda s: html.escape(str(s or ""), quote=True)


# ---------------------------------------------------------------- content


def _fix(v):
    return re.sub("Fra[´‘]", "Fra’", v) if isinstance(v, str) else v  # legacy texts use the acute accent or a left quote


def read_doc(path):
    text = path.read_text(encoding="utf-8")
    _, meta, body = text.split("---\n", 2)
    return {k: _fix(v) for k, v in json.loads(meta).items()}, _fix(body.strip())


def load_pages():
    pages = {}
    for f in sorted((CONTENT / "pages").rglob("index.html")):
        meta, body = read_doc(f)
        pages[meta["url"]] = {**meta, "body": body}
    return pages


def load_news():
    news = []
    for f in (CONTENT / "news").rglob("*.html"):
        meta, body = read_doc(f)
        news.append({**meta, "body": body, "src": f.relative_to(ROOT).as_posix()})
    return sorted(news, key=lambda n: n["date"], reverse=True)


PAGES, NEWS = load_pages(), load_news()
NAMES, C, L = SITE["names"], SITE["contact"], SITE["links"]
MONTHS = ["ledna", "února", "března", "dubna", "května", "června", "července", "srpna", "září", "října", "listopadu", "prosince"]
MONTHS_SHORT = ["led", "úno", "bře", "dub", "kvě", "čvn", "čvc", "srp", "zář", "říj", "lis", "pro"]
STATUS = {"existing": "Převzato ze starého webu – čeká na kontrolu", "new": "Nový text – čeká na schválení", "approval": "Čeká na schválení"}


def page_title(url):
    p = PAGES.get(url)
    return p.get("nav") or p["title"] if p else url


# navigation index: url -> {node, parent, top}
def _index(index, nodes, parent=None, top=None):
    for n in nodes:
        n.setdefault("title", page_title(n["url"]))
        index[n["url"]] = {"node": n, "parent": parent, "top": top or n["url"]}
        _index(index, n.get("children", []), n["url"], top or n["url"])


NAV = SITE["nav"]
NAV_INDEX = {}
_index(NAV_INDEX, NAV)


def breadcrumbs(url):
    trail = []
    while url in NAV_INDEX:
        trail.insert(0, (NAV_INDEX[url]["node"]["title"], url))
        url = NAV_INDEX[url]["parent"]
    return trail


# ---------------------------------------------------------------- helpers

def image_size(rel_url):
    """Width/height of a local JPEG, PNG or WebP (for layout-stable <img>)."""
    f = STATIC / rel_url.lstrip("/").replace("%20", " ")
    if not f.exists():
        from urllib.parse import unquote
        f = STATIC / unquote(rel_url.lstrip("/"))
    try:
        b = f.read_bytes()[:65536]
    except OSError:
        return None
    if b[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", b[16:24])
    if b[:4] == b"RIFF" and b[8:12] == b"WEBP":
        c = b[12:16]
        if c == b"VP8 ":
            w, h = struct.unpack("<HH", b[26:30])
            return w & 0x3FFF, h & 0x3FFF
        if c == b"VP8L":
            v = int.from_bytes(b[21:25], "little")
            return (v & 0x3FFF) + 1, ((v >> 14) & 0x3FFF) + 1
        if c == b"VP8X":
            return int.from_bytes(b[24:27], "little") + 1, int.from_bytes(b[27:30], "little") + 1
    if b[:2] == b"\xff\xd8":
        i = 2
        while i < len(b) - 9:
            if b[i] != 0xFF:
                i += 1
                continue
            marker, length = b[i + 1], struct.unpack(">H", b[i + 2:i + 4])[0]
            if marker in (0xC0, 0xC1, 0xC2):
                h, w = struct.unpack(">HH", b[i + 5:i + 9])
                return w, h
            i += 2 + length
    return None


def img(src, alt, cls="", sizes=None, eager=False, srcset=None):
    wh = image_size(src)
    dims = f' width="{wh[0]}" height="{wh[1]}"' if wh else ""
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    responsive = f' srcset="{esc(srcset)}" sizes="{esc(sizes)}"' if srcset and sizes else ""
    return f'<img class="ph-img {cls}" src="{esc(src)}"{responsive} alt="{esc(alt)}"{dims} {load} decoding="async">'


def enhance_body(body):
    """Layout-stable lazy images and scrollable tables in imported content."""
    def fix_img(m):
        tag = m.group(0)
        src = re.search(r'src="([^"]+)"', tag)
        if not src:
            return tag
        wh = image_size(html.unescape(src.group(1))) if src.group(1).startswith("/") else None
        extra = f' width="{wh[0]}" height="{wh[1]}"' if wh else ""
        return tag[:-1] + f'{extra} loading="lazy" decoding="async" class="ph-img">'
    body = re.sub(r"<img [^>]+>", fix_img, body)
    body = re.sub(r"<table>", '<div class="table-wrap" tabindex="0"><table>', body)
    return body.replace("</table>", "</table></div>")


def plain(html_text, n=180):
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", html_text))).strip()
    return t if len(t) <= n else t[: t.rfind(" ", 0, n)] + "…"




def file_info(url):
    """('PDF', '1,2 MB') for a local download, or None."""
    from urllib.parse import unquote
    f = STATIC / unquote(url.lstrip("/"))
    if not f.is_file():
        return None
    size = f.stat().st_size
    human = f"{size / 1048576:.1f} MB".replace(".", ",") if size >= 1048576 else f"{max(1, round(size / 1024))} kB"
    return f.suffix.lstrip(".").upper(), human


def enhance_files(body):
    """Document links in lists of downloads carry their type and size (WCAG 2.4.4: the link says what it opens)."""
    def fix(m):
        url, label = m.group(1), m.group(2)
        info = file_info(url)
        if not info:
            return m.group(0)
        return f'<a class="file" href="{url}"><span>{label}</span> <span class="file-meta">{info[0]}, {info[1]}</span></a>'
    return re.sub(r'<a href="(/media/[^"]+\.(?:pdf|docx?|xlsx?|jpe?g|png))">([^<]+)</a>', fix, body)


def fmt_date(iso):
    d = datetime.fromisoformat(iso[:10])
    return f"{d.day}. {MONTHS[d.month - 1]} {d.year}"


def short_date(iso):
    d = datetime.fromisoformat(iso[:10])
    return f"{d.day}. {d.month}. {d.year}"


def event_slug(e):
    return e["url"].strip("/").split("/")[-1]


def event_when(e):
    a, b = datetime.fromisoformat(e["start"]), datetime.fromisoformat(e["end"])
    if a.date() == b.date():
        return short_date(e["start"])
    if a.year == b.year:
        return f"{a.day}. {a.month}. – {b.day}. {b.month}. {b.year}"
    return f"{short_date(e['start'])} – {short_date(e['end'])}"


def events_list(items, time=None, compact=False):
    rows = []
    for e in items:
        d = datetime.fromisoformat(e["start"])
        desc = "" if compact else plain(e.get("description", ""), 400)
        when = event_when(e) + (f", {time}" if time else "")
        rows.append(f'<li id="{event_slug(e)}"><time datetime="{e["start"][:10]}"><b>{d.day}</b>{MONTHS_SHORT[d.month - 1]} {d.year}</time>'
                    f'<div><b>{esc(e["title"])}</b><span>{esc(when)}{" · " + esc(desc) if desc else ""}</span></div></li>')
    return f'<ol class="events">{"".join(rows)}</ol>'


def upcoming(limit=4, today=None):
    today = today or datetime.now().strftime("%Y-%m-%d")
    return [e for e in EVENTS if e["end"][:10] >= today][:limit]


# ---------------------------------------------------------------- layout

FONTS_PRELOAD = ["asap-latin-400-normal", "eb-garamond-latin-500-normal"]  # first-screen body and heading; latin-ext loads on demand by unicode-range


def nav_html(current_url):
    top = NAV_INDEX.get(current_url, {}).get("top")
    if current_url.startswith("/aktuality/") or re.match(r"^/\d{4}/", current_url):
        top = "/aktuality/"
    lis = []
    for n in NAV:
        cur = ' aria-current="page"' if n["url"] == current_url else (' class="is-active"' if n["url"] == top else "")
        kids = n.get("children", [])
        sub = ""
        if kids:
            sub_items = "".join(f'<li><a href="{c["url"]}">{esc(c["title"])}</a></li>' for c in kids)
            sub = (f'<button class="sub-toggle" type="button" aria-expanded="false" aria-label="{esc(n["title"])}: další stránky">'
                   f'<span aria-hidden="true"></span></button><ul class="sub">{sub_items}</ul>')
        lis.append(f'<li class="{"has-sub" if kids else ""}"><a href="{n["url"]}"{cur}>{esc(n["title"])}</a>{sub}</li>')
    return f'<ul class="nav-list">{"".join(lis)}</ul>'


def layout(*, url, title, body, description="", image=None, status=None, main_class=""):
    full_title = f"{title} | {NAMES['site']}" if title != NAMES["site"] else title
    canonical = SITE["baseUrl"] + url
    og_image = SITE["baseUrl"] + (image or "/media/2026/08/skola.jpg")
    robots = "" if PRODUCTION else '<meta name="robots" content="noindex, nofollow">'
    preload = "".join(f'<link rel="preload" href="/fonts/{f}.woff2" as="font" type="font/woff2" crossorigin>' for f in FONTS_PRELOAD)
    ld = ""
    if url == "/":  # who we are, for search engines (data only, not executed)
        ld = '<script type="application/ld+json">' + json.dumps({
            "@context": "https://schema.org", "@type": "CollegeOrUniversity", "name": NAMES["school"], "url": canonical,
            "email": C["email"], "telephone": "+420 " + C["phone"], "logo": SITE["baseUrl"] + "/img/logo/vosz.png",
            "address": {"@type": "PostalAddress", "streetAddress": "Žerotínova 1143/38", "postalCode": "130 00", "addressLocality": "Praha 3", "addressCountry": "CZ"},
            "sameAs": [L["facebook"], L["instagram"], L["youtube"]],
            "parentOrganization": {"@type": "Organization", "name": f"{NAMES['order']} – {NAMES['founder']}", "url": L["founder"]},
        }, ensure_ascii=False).replace("</", "<\\/") + "</script>"
    status_bar = ""
    if status and not PRODUCTION:
        status_bar = f'<p class="content-status content-status--{esc(status)}"><span>{esc(STATUS.get(status, status))}</span></p>'
    footer_cols = "".join(
        f'<li><a href="{n["url"]}">{esc(n["title"])}</a>' + ("<ul>" + "".join(f'<li><a href="{c["url"]}">{esc(c["title"])}</a></li>' for c in n["children"]) + "</ul>" if n.get("children") else "") + "</li>"
        for n in NAV)
    return f"""<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(plain(description or body, 160))}">
{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(NAMES['site'])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description or plain(body, 160))}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:locale" content="cs_CZ">
<meta name="twitter:card" content="summary_large_image">
{ld}
<meta name="theme-color" content="#e31a18">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/img/favicon/apple-touch-icon-180x180.png">
<link rel="alternate" type="application/rss+xml" title="{esc(NAMES['site'])} – aktuality" href="/feed.xml">
{preload}<link rel="preload" href="/img/header/students.webp" as="image" fetchpriority="high">
<link rel="stylesheet" href="/css/site.css?v={ASSET_VERSION}">
<script src="/js/head.js?v={ASSET_VERSION}"></script>
<script src="/js/site.js?v={ASSET_VERSION}" defer></script>
</head>
<body>
<a class="skip" href="#main">Přeskočit na obsah</a>
<header class="site-header">
 <div class="topbar"><div class="wrap">
  <a class="topbar-home" href="{L['founder']}">{esc(NAMES['orderActivities'])} · {esc(NAMES['founder'])}</a>
  <span class="topbar-social"><a href="tel:+420{C['phone'].replace(' ', '')}">{C['phone']}</a><a href="mailto:{C['email']}">{C['email']}</a></span>
  <a class="topbar-bakalari" href="{L['bakalari']}">Bakaláři</a>
 </div></div>
 <div class="idband"><div class="wrap">
  <a class="idband-home" href="/"><img class="logo" src="/img/logo/vosz.png" alt="{esc(NAMES['school'])} – úvodní stránka" width="520" height="126"></a>
  <p class="idband-actions"><a href="/pro-uchazece/">Přijímací řízení</a><a href="/den-otevrenych-dveri/">Den otevřených dveří</a></p>
 </div></div>
 <nav class="mainnav" aria-label="Hlavní menu"><div class="wrap">
  <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
  <div id="menu" class="menu">{nav_html(url)}</div>
 </div></nav>
</header>
<main id="main" class="{main_class}" tabindex="-1">
{status_bar}
{body}
</main>
<footer class="site-footer">
 <div class="f-nav"><div class="wrap"><ul>{footer_cols}</ul></div></div>
 <div class="f-id"><div class="wrap">
  <p class="f-name">{esc(NAMES['school'])}</p>
  <p>{esc(C['address'])} · <a href="tel:+420{C['phone'].replace(' ', '')}">{C['phone']}</a> · <a href="mailto:{C['email']}">{C['email']}</a> · datová schránka {C['dataBox']}</p>
  <p>Sledujte nás: <a href="{L['facebook']}">Facebook</a> · <a href="{L['instagram']}">Instagram</a> · <a href="{L['youtube']}">YouTube</a></p>
 </div></div>
 <div class="f-red"><div class="wrap">
  <p>Zřizovatel: <a href="{L['founder']}">{esc(NAMES['orderActivities'])} – {esc(NAMES['founder'])}</a></p>
  <p>{esc(NAMES['orderActivities'])}: <a href="{L['order']}">www.orderofmalta.int</a></p>
  <p><a href="/ochrana-osobnich-udaju/">Ochrana osobních údajů</a></p>
 </div></div>
</footer>
</body>
</html>
"""


# ---------------------------------------------------------------- shared blocks


def news_item(n, compact=False):
    excerpt = "" if compact or not n.get("excerpt") else f'<p class="n-excerpt">{esc(n["excerpt"])}</p>'
    return (f'<li class="n-item"><time datetime="{n["date"][:10]}">{short_date(n["date"])}</time>'
            f'<div><a href="{n["url"]}">{esc(n["title"])}</a>{excerpt}</div></li>')


PROGRAMMES = [
    ("/prakticka-sestra-denni/", "Denní studium", "/media/2025/08/VOS_denni_studium.jpg",
     ["3 roky, absolutorium, titul DiS.", "školné 1 500 Kč za období (po slevě)", "praxe v předních pražských nemocnicích"]),
    ("/prakticka-sestra-dalkove/", "Kombinované studium", "/media/2025/08/VOS_dalkove_studium.jpg",
     ["3,5 roku při zaměstnání, titul DiS.", "konzultace a samostudium", "školné 5 000 Kč za pololetí"]),
]


def programmes(heading="h3"):
    items = "".join(
        f'<li><a href="{u}">{img(src, "", sizes="(max-width: 960px) 100vw, 560px")}<{heading} class="display-s">{t}</{heading}></a>'
        f'<ul class="facts-s">{"".join(f"<li>{esc(x)}</li>" for x in facts)}</ul></li>'
        for u, t, src, facts in PROGRAMMES)
    return f'<ul class="programmes">{items}</ul>'


def section_children_html(url):
    kids = NAV_INDEX.get(url, {}).get("node", {}).get("children", [])
    if not kids:
        return ""
    items = []
    for k in kids:
        p = PAGES.get(k["url"], {})
        desc = p.get("description") or plain(p.get("body", ""), 150)
        items.append(f'<li><a href="{k["url"]}"><b>{esc(k["title"])}</b>{f"<span>{esc(desc)}</span>" if desc else ""}</a></li>')
    return f'<ul class="index-list">{"".join(items)}</ul>'


def _descendants(node):
    out = set()
    for c in node.get("children", []):
        out.add(c["url"])
        out |= _descendants(c)
    return out


def side_nav(url):
    info = NAV_INDEX.get(url)
    if not info:
        return ""
    top = NAV_INDEX[info["top"]]["node"]
    if not top.get("children") or info["top"] == url:  # a section's own page already lists its children
        return ""
    items = "".join(f'<li><a href="{n["url"]}"{" aria-current=" + chr(34) + "page" + chr(34) if n["url"] == url else ""}>{esc(n["title"])}</a></li>' for n in top["children"])
    return f'<nav class="side-nav" aria-label="V této sekci"><p class="label"><a href="{top["url"]}">{esc(top["title"])}</a></p><ul>{items}</ul></nav>'


def crumbs_html(url, extra=None):
    trail = [("Úvod", "/")] + breadcrumbs(url) + (extra or [])
    if len(trail) < 2:
        return ""
    items = []
    for i, (t, u) in enumerate(trail):
        items.append(f'<li><span aria-current="page">{esc(t)}</span></li>' if i == len(trail) - 1 else f'<li><a href="{u}">{esc(t)}</a></li>')
    return f'<nav class="crumbs" aria-label="Drobečková navigace"><ol>{"".join(items)}</ol></nav>'


# ---------------------------------------------------------------- pages


def render_home():
    news = "".join(news_item(n, compact=True) for n in NEWS[:4])
    gallery = "".join(f'<li>{img(f"/media/2025/08/{g}", "", sizes="(max-width: 640px) 50vw, 380px")}</li>'
                      for g in ("galerie-vos-3.jpg", "galerie-vos-6.jpg", "galerie-vos-7.jpeg", "galerie-vos-5.jpg", "galerie-vos-4.jpg"))
    team = "".join(
        f'<li>{img(src, "", sizes="160px")}<div><b>{esc(name)}</b><span>{esc(role)}</span><a href="mailto:{mail}">{mail}</a></div></li>'
        for src, name, role, mail in (("/media/2025/08/sikova.jpg", "Mgr. Marie Šiková", "ředitelka školy", "sikova.marie@skolajecna.cz"),
                                      ("/media/2025/08/pavlikova.jpg", "PhDr. Pavla Pavlíková", "zástupkyně ředitelky", "pavlikova.pavla@skolajecna.cz"),
                                      ("/media/2026/08/kolka3.jpg", "Mgr. Luboš Kolka", "zástupce ředitelky", "kolka.lubos@skolajecna.cz")))
    body = f"""
<section class="home-open" aria-labelledby="home-title"><div class="wrap home-intro">
 <div class="home-intro-main">
  <h1 id="home-title" class="display">Vyšší odborná škola zdravotnická</h1>
  <p class="lead"><strong>Vyšší odborná škola zdravotnická Suverénního řádu maltézských rytířů</strong> je místem, kde se spojuje tradice, odbornost a osobní přístup. Studenti zde nacházejí přátelské a podporující prostředí, ve kterém se mohou rozvíjet nejen po stránce profesní, ale i lidské.</p>
  <dl class="facts">
   <div><dt>Obor</dt><dd><a href="/vyucovane-obory/">Diplomovaná všeobecná sestra</a> (53-41-N/1.)</dd></div>
   <div><dt>Forma</dt><dd>denní (3 roky) a kombinovaná (3,5 roku), titul DiS.</dd></div>
   <div><dt>Adresa</dt><dd><a href="/kontakt/">Žerotínova 1143/38, Praha 3</a></dd></div>
  </dl>
  <p class="actions"><a class="btn" href="/pro-uchazece/">Jak se přihlásit</a><a class="link-strong" href="/den-otevrenych-dveri/">Den otevřených dveří</a></p>
 </div>
 <figure class="home-photo">{img("/media/2026/08/skola.jpg", "Budova školy v Žerotínově ulici", eager=True, sizes="(max-width: 960px) 100vw, 560px")}</figure>
</div></section>

<section class="band band-grey" aria-labelledby="prog-title"><div class="wrap">
 <div class="section-head"><h2 id="prog-title" class="display-m">Studujte ošetřovatelství</h2>
  <p>Výuka je pevně propojena s praxí. Díky spolupráci s nemocnicemi a zdravotnickými zařízeními se studenti učí přímo v reálném prostředí, kde vidí, jak jejich znalosti a dovednosti pomáhají druhým.</p></div>
 {programmes()}
</div></section>

<section class="band" aria-labelledby="news-title"><div class="wrap split">
 <div><div class="split-head"><h2 id="news-title" class="display-m">Aktuality</h2><p><a class="link-strong" href="/aktuality/">Všechny aktuality</a></p></div>
  <ol class="news-list">{news}</ol></div>
 <div><div class="split-head"><h2 id="ev-title" class="display-m">Nadcházející události</h2><p><a class="link-strong" href="/organizace-skolniho-roku/">Celý školní rok</a></p></div>
  {events_list(upcoming(), compact=True)}</div>
</div></section>

<section class="band band-grey" aria-labelledby="about-title"><div class="wrap split">
 <div class="split-head"><h2 id="about-title" class="display-m">O škole</h2>
  <p>Jsme školou, která staví na vzájemném respektu, spolupráci a hodnotách, jež připravují studenty na jejich náročnou, ale krásnou profesní dráhu ve zdravotnictví. Chceme, aby každý absolvent odcházel nejen s jistotou odborné kvalifikace, ale i s vědomím, že se stal součástí poslání, které má hluboký smysl.</p>
  <p>Školu zřizuje <a href="{L['founder']}">České velkopřevorství Maltézského řádu</a>.</p>
  <p class="text-links"><a href="/vedeni-skoly/">Vedení školy</a><a href="/pedagogicky-sbor/">Pedagogický sbor</a><a href="{L['video']}">Prezentace školy (video)</a></p></div>
 <ul class="team">{team}</ul>
</div></section>

<section class="band" aria-labelledby="life-title"><div class="wrap">
 <div class="split-head"><h2 id="life-title" class="display-m">Jak to u nás vypadá</h2><p><a class="link-strong" href="{L['instagram']}">Život na škole na Instagramu</a></p></div>
 <ul class="gallery">{gallery}</ul>
 <ul class="quick">
  <li><a href="/den-otevrenych-dveri/"><b>Den otevřených dveří</b><span>Co obnáší studium na vyšší škole</span></a></li>
  <li><a href="/stravovani-a-ubytovani/"><b>Stravování a ubytování</b><span>Jídelna a domovy mládeže</span></a></li>
  <li><a href="/kontakt/"><b>Jak se k nám dostanete</b><span>Tramvají na Biskupcovu nebo Ohradu</span></a></li>
 </ul>
</div></section>
"""
    return layout(url="/", title=NAMES["site"], body=body, status="new",
                  description="Vyšší odborná škola zdravotnická Suverénního řádu maltézských rytířů v Praze 3: obor Diplomovaná všeobecná sestra, denní a kombinované studium.")


def render_page(p):
    url = p["url"]
    lead_img = p.get("image")
    figure = f'<figure class="page-figure">{img(lead_img, "", eager=True, sizes="(max-width: 960px) 100vw, 760px")}</figure>' if lead_img else ""
    body = enhance_files(enhance_body(p["body"]))
    body = body.replace('<div class="programmes" data-programmes></div>', programmes("h2"))
    m = re.search(r'<div data-events(?:="([^"]*)")?(?: data-time="([^"]*)")?></div>', body)
    if m:
        items = [e for e in EVENTS if not m.group(1) or e["title"] == m.group(1)]
        body = body.replace(m.group(0), events_list(items, time=m.group(2), compact=bool(m.group(1))))
    children = section_children_html(url) if p.get("section") else ""
    side = side_nav(url)
    html_body = f"""
<div class="wrap">{crumbs_html(url)}</div>
<article class="wrap page{' page--with-side' if side else ''}">
 <header class="page-head"><h1 class="display">{esc(p['title'])}</h1></header>
 <div class="page-main">
  {figure}
  <div class="prose">{body}</div>
  {children}
 </div>
 {f'<div class="page-side">{side}</div>' if side else ''}
</article>"""
    return layout(url=url, title=p["title"], body=html_body, description=p.get("description", ""), image=lead_img, status=p.get("status"))


def render_article(n, prev_n, next_n):
    cats = SITE["newsCategories"]
    cat_links = " · ".join(f'<a href="/aktuality/{c}/">{esc(cats[c])}</a>' for c in n.get("categories", []) if c in cats)
    figure = f'<figure class="page-figure">{img(n["image"], "", eager=True, sizes="(max-width: 960px) 100vw, 760px")}</figure>' if n.get("image") else ""
    pager = ""
    if prev_n or next_n:
        pager = '<nav class="pager" aria-label="Další články">' + \
            (f'<a class="pager-prev" href="{next_n["url"]}"><span>Novější</span>{esc(next_n["title"])}</a>' if next_n else "<span></span>") + \
            (f'<a class="pager-next" href="{prev_n["url"]}"><span>Starší</span>{esc(prev_n["title"])}</a>' if prev_n else "") + "</nav>"
    body = f"""
<div class="wrap">{crumbs_html('/aktuality/', [(n['title'], n['url'])])}</div>
<article class="wrap page page--article">
 <header class="page-head">
  <h1 class="display">{esc(n['title'])}</h1>
  <p class="byline"><time datetime="{n['date'][:10]}">{fmt_date(n['date'])}</time>{(' · ' + cat_links) if cat_links else ''}</p>
 </header>
 <div class="page-main">
  {figure}
  <div class="prose">{enhance_files(enhance_body(n['body']))}</div>
  <p><a class="link-strong" href="/aktuality/">Zpět na aktuality</a></p>
  {pager}
 </div>
</article>"""
    return layout(url=n["url"], title=n["title"], body=body, description=n.get("excerpt") or "", image=n.get("image"), status=n.get("status"))


def render_news_index(items, active="", year=None, url="/aktuality/"):
    cats = SITE["newsCategories"]
    counts = {c: sum(1 for n in NEWS if c in n.get("categories", [])) for c in cats}
    cur = ' aria-current="page"'
    tabs = [f'<a href="/aktuality/"{cur if not active and not year else ""}>Vše</a>']
    tabs += [f'<a href="/aktuality/{c}/"{cur if active == c else ""}>{esc(label)} <span class="count">{counts[c]}</span></a>' for c, label in cats.items() if counts[c]]
    years = sorted({n["date"][:4] for n in NEWS}, reverse=True)
    year_links = "".join(f'<a href="/aktuality/{y}/"{cur if year == y else ""}>{y}</a>' for y in years)
    groups, cur_year = [], None
    for n in items:
        y = n["date"][:4]
        if y != cur_year:
            if cur_year:
                groups.append("</ol></section>")
            groups.append(f'<section class="year-group"><h2 class="year">{y}</h2><ol class="news-list news-list--full">')
            cur_year = y
        groups.append(news_item(n))
    if cur_year:
        groups.append("</ol></section>")
    title = "Aktuality" + (f": {cats[active]}" if active else "") + (f" {year}" if year else "")
    body = f"""
<div class="wrap">{crumbs_html('/aktuality/', [(title, url)] if url != '/aktuality/' else None)}</div>
<div class="wrap page page--news">
 <header class="page-head"><h1 class="display">{esc(title)}</h1>
  <p class="lead-s">Zprávy ze školy a z přijímacího řízení. Zprávy pro studenty posílá škola také v systému <a href="{L['bakalari']}">Bakaláři</a> (Komens).</p></header>
 <nav class="tabs" aria-label="Rubrika">{''.join(tabs)}</nav>
 <nav class="years" aria-label="Rok">{year_links}</nav>
 {''.join(groups) or '<p class="empty">V této rubrice zatím nejsou žádné zprávy.</p>'}
</div>"""
    return layout(url=url, title=title, body=body, description="Aktuality Vyšší odborné školy zdravotnické Suverénního řádu maltézských rytířů.")


def render_simple(url, title, inner, status=None):
    body = f'<div class="wrap page page--simple"><header class="page-head"><h1 class="display">{esc(title)}</h1></header><div class="prose">{inner}</div></div>'
    return layout(url=url, title=title, body=body, status=status, description=plain(inner, 160))


NEWS_EDITOR_URL = "/pridat-aktualitu/"


def render_news_editor():
    """Staff page for publishing news (api/news.js); not linked, not indexed, behind a password."""
    body = f"""
<div class="wrap page page--simple ne" id="news-app">
 <header class="page-head"><h1 class="display">Přidat aktualitu</h1>
  <p class="lead-s">Aktualita se po zveřejnění objeví na webu v sekci <a href="/aktuality/">Aktuality</a> asi za minutu.</p></header>
 <noscript><p class="ne-msg ne-msg--error">Formulář potřebuje zapnutý JavaScript.</p></noscript>
 <form id="ne-login" class="ne-card" hidden>
  <h2 class="display-s">Přihlášení</h2>
  <label class="ne-field"><span>Jméno</span><input name="name" autocomplete="username" required></label>
  <label class="ne-field"><span>Heslo</span><input name="password" type="password" autocomplete="current-password" required></label>
  <p class="ne-msg" id="ne-login-msg" role="alert" hidden></p>
  <p><button class="btn" type="submit">Přihlásit se</button></p>
 </form>
 <div id="ne-app" hidden>
 <p class="ne-who">Přihlášen(a): <b id="ne-user"></b> · <button type="button" class="link-btn" id="ne-logout">Odhlásit</button></p>
 <div class="ne-tabs" role="tablist" aria-label="Co chcete udělat">
  <button type="button" role="tab" id="ne-tab-new" aria-selected="true" aria-controls="ne-editor">Nová aktualita</button>
  <button type="button" role="tab" id="ne-tab-list" aria-selected="false" aria-controls="ne-manage">Upravit nebo smazat</button>
 </div>
 <section id="ne-manage" role="tabpanel" aria-labelledby="ne-tab-list" hidden>
  <label class="ne-field"><span>Hledat aktualitu</span><input id="ne-search" type="search" placeholder="Část titulku nebo rok…"></label>
  <ul id="ne-list" class="ne-list"></ul>
  <p class="ne-hint">Nové a upravené aktuality se v seznamu objeví asi za minutu, až se web znovu sestaví.</p>
  <p class="ne-msg" id="ne-list-msg" role="alert" hidden></p>
 </section>
 <form id="ne-editor" role="tabpanel" aria-labelledby="ne-tab-new">
  <div class="ne-editing" id="ne-editing" hidden><p>Upravujete: <a id="ne-editing-link"></a></p><button type="button" class="link-btn" id="ne-cancel">Zrušit úpravy</button></div>
  <p class="ne-msg" id="ne-draft" hidden></p>
  <label class="ne-field"><span>Titulek <i aria-hidden="true">*</i></span><input id="ne-title" maxlength="200" required></label>
  <div class="ne-row">
   <label class="ne-field"><span>Datum a čas zveřejnění</span><input id="ne-date" type="datetime-local" required></label>
   <fieldset class="ne-field"><legend>Kategorie</legend><div id="ne-cats" class="ne-cats"></div></fieldset>
  </div>
  <div class="ne-field"><span id="ne-text-label">Text <i aria-hidden="true">*</i></span>
   <div class="ne-text-wrap"><div id="ne-text" class="prose" aria-labelledby="ne-text-label"></div></div>
   <div id="ne-locked" class="ne-locked" hidden><p class="ne-msg ne-msg--error">Text této starší aktuality obsahuje prvky, které editor neumí (například fotografie s popiskem nebo tabulku). Text proto zůstane beze změny; upravit můžete titulek, datum, kategorie, perex, fotografii a přílohy.</p><div class="prose" id="ne-locked-text"></div></div>
   <p class="ne-hint" id="ne-text-hint">Nadpis a podnadpis, tučné písmo, kurzíva, seznamy, citace, odkazy a fotografie v textu. Písmo a barvy jsou dané vzhledem webu.</p>
   <p class="ne-msg" id="ne-inline-msg" hidden></p></div>
  <label class="ne-field"><span>Perex <small>(nepovinné – krátké shrnutí v přehledu aktualit; jinak se vezme začátek textu)</small></span><textarea id="ne-excerpt" rows="2" maxlength="300"></textarea></label>
  <div class="ne-field"><span>Hlavní fotografie <small>(nepovinné – zobrazí se nad textem)</small></span>
   <label class="btn btn--ghost ne-pick">Vybrat fotografii<input id="ne-photo" type="file" accept="image/jpeg,image/png,image/webp" class="visually-hidden"></label>
   <ul id="ne-photo-box" class="ne-files ne-photo"></ul></div>
  <div class="ne-field"><span>Přílohy ke stažení <small>(PDF nebo fotografie, nejvýše 3 MB na soubor)</small></span>
   <div class="ne-drop" id="ne-drop"><p>Přetáhněte soubory sem, nebo</p>
    <label class="btn btn--ghost ne-pick">vyberte soubory<input id="ne-files" type="file" multiple accept="application/pdf,image/jpeg,image/png,image/webp" class="visually-hidden"></label></div>
   <ul id="ne-file-list" class="ne-files"></ul></div>
  <div class="ne-submit"><button class="btn" type="submit" id="ne-publish">Zveřejnit</button>
   <p class="ne-msg" id="ne-msg" role="alert" hidden></p></div>
 </form>
 </div>
 <div id="ne-done" class="ne-card" hidden role="status">
  <h2 class="display-s" id="ne-done-title">Zveřejněno</h2>
  <p id="ne-done-text">Změna bude na webu asi za minutu: <a id="ne-done-link"></a></p>
  <p><button class="btn" type="button" id="ne-again">Zpět na aktuality</button></p>
 </div>
</div>
<link rel="stylesheet" href="/js/vendor/quill-2.0.3/quill.snow.css">
<script src="/js/vendor/quill-2.0.3/quill.js"></script>
<script src="/js/news-editor.js?v={ASSET_VERSION}"></script>"""
    h = layout(url=NEWS_EDITOR_URL, title="Přidat aktualitu", body=body, description="Přidání aktuality na web školy.")
    return h.replace("<head>\n", '<head>\n<meta name="robots" content="noindex, nofollow">\n', 1) if PRODUCTION else h




# ---------------------------------------------------------------- output

def write(url, html_text):
    path = DIST / url.lstrip("/") / "index.html" if url.endswith("/") else DIST / url.lstrip("/")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html_text, encoding="utf-8")




def rss():
    items = "".join(
        f"<item><title>{esc(n['title'])}</title><link>{SITE['baseUrl']}{n['url']}</link><guid>{SITE['baseUrl']}{n['url']}</guid>"
        f"<pubDate>{datetime.fromisoformat(n['date']).strftime('%a, %d %b %Y %H:%M:00 +0100')}</pubDate><description>{esc(n.get('excerpt') or plain(n['body'], 200))}</description></item>"
        for n in NEWS[:30])
    return (f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{esc(NAMES["site"])}</title>'
            f'<link>{SITE["baseUrl"]}/</link><description>Aktuality {esc(NAMES["school"])}</description><language>cs</language>{items}</channel></rss>')


VERCEL = json.loads((ROOT / "vercel.json").read_text(encoding="utf-8"))  # headers and redirects live here; other hosts get _headers and _redirects
HEADERS = "".join(h["source"].replace("(.*)", "*") + "\n" + "".join(f"  {x['key']}: {x['value']}\n" for x in h["headers"]) for h in VERCEL["headers"])
# old WordPress addresses include query strings (/?p=7969); _redirects writes them in the Netlify form "/ p=7969 /dest/ 301"
REDIRECTS = [(r["source"].replace(":path*", "*"), "".join(f" {h['key']}={h['value']}" for h in r.get("has", [])), r["destination"].replace(":path*", ":splat"))
             for r in VERCEL["redirects"]]




def build():
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(STATIC, DIST)
    write("/", render_home())
    for url, p in PAGES.items():
        write(url, render_page(p))
    for i, n in enumerate(NEWS):
        write(n["url"], render_article(n, NEWS[i + 1] if i + 1 < len(NEWS) else None, NEWS[i - 1] if i else None))
    write("/aktuality/", render_news_index(NEWS[:40]))
    for c in SITE["newsCategories"]:
        items = [n for n in NEWS if c in n.get("categories", [])]
        if items:
            write(f"/aktuality/{c}/", render_news_index(items, active=c, url=f"/aktuality/{c}/"))
    for y in sorted({n["date"][:4] for n in NEWS}):
        write(f"/aktuality/{y}/", render_news_index([n for n in NEWS if n["date"].startswith(y)], year=y, url=f"/aktuality/{y}/"))
    write(NEWS_EDITOR_URL, render_news_editor())
    (DIST / NEWS_EDITOR_URL.strip("/") / "news.json").write_text(json.dumps(  # the editor's list of posts to edit or delete
        [{"path": n["src"], "url": n["url"], "title": n["title"], "date": n["date"][:16], "author": n.get("author")} for n in NEWS],
        ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    write("/ochrana-osobnich-udaju/", render_simple("/ochrana-osobnich-udaju/", "Ochrana osobních údajů", PRIVACY, status="approval"))
    write("/404.html", render_simple("/404.html", "Stránka nenalezena",
                                     '<p>Tato stránka neexistuje nebo byla přesunuta.</p><p><a class="link-strong" href="/">Úvodní stránka</a> · <a class="link-strong" href="/aktuality/">Aktuality</a> · <a class="link-strong" href="/kontakt/">Kontakt</a></p>'))
    urls = ["/", "/aktuality/", "/ochrana-osobnich-udaju/"] + [u for u, p in PAGES.items()] + [n["url"] for n in NEWS]
    (DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' +
                                      "".join(f"<url><loc>{SITE['baseUrl']}{u}</loc></url>" for u in urls) + "</urlset>", encoding="utf-8")
    (DIST / "robots.txt").write_text(("User-agent: *\nAllow: /\nDisallow: /pridat-aktualitu/\nDisallow: /api/\n\nSitemap: " + SITE["baseUrl"] + "/sitemap.xml\n") if PRODUCTION
                                     else "User-agent: *\nDisallow: /\n", encoding="utf-8")
    (DIST / "feed.xml").write_text(rss(), encoding="utf-8")
    (DIST / "_headers").write_text(HEADERS + ("" if PRODUCTION else "/*\n  X-Robots-Tag: noindex, nofollow\n"), encoding="utf-8")
    (DIST / "_redirects").write_text("".join(f"{a}{q} {b} 301\n" for a, q, b in REDIRECTS), encoding="utf-8")
    print(f"built {len(PAGES)} pages, {len(NEWS)} news, {len(EVENTS)} events, {'production' if PRODUCTION else 'preview'} → {DIST}")


PRIVACY = """<h2>Správce</h2>
<p>Správcem osobních údajů je Vyšší odborná škola zdravotnická Suverénního řádu maltézských rytířů, Žerotínova 1143/38, 130 00 Praha 3. Dotazy a žádosti týkající se osobních údajů posílejte na <a href="mailto:skolajecna@skolajecna.cz">skolajecna@skolajecna.cz</a> nebo pověřenci pro ochranu osobních údajů, Mgr. Pavlu Havránkovi (<a href="mailto:havranek@gdprgov.cz">havranek@gdprgov.cz</a>, 732 278 308, ID datové schránky 2v7awpy).</p>
<h2>Cookies a měření návštěvnosti</h2>
<p>Tento web nepoužívá cookies ani analytické a reklamní nástroje a nesleduje návštěvníky. Písma a obrázky se načítají přímo z tohoto webu. Výjimkou je neveřejná stránka pro zaměstnance, která po přihlášení ukládá nezbytné přihlašovací cookie.</p>
<h2>Provoz webu</h2>
<p>Web běží na serverech společnosti Vercel Inc. (USA). Při každé návštěvě se zpracovávají údaje nutné k doručení stránky a k ochraně webu před zneužitím (IP adresa, čas a adresa požadavku, údaje o prohlížeči). Právním základem je oprávněný zájem na bezpečném provozu webu (čl. 6 odst. 1 písm. f) GDPR). Předání do USA se řídí rámcem EU–USA pro ochranu osobních údajů (Data Privacy Framework).</p>
<h2>E-mail a telefon</h2>
<p>Napíšete-li nám nebo zavoláte-li, použijeme vaše údaje jen k vyřízení vaší zprávy a uchováme je po dobu, kterou to vyžaduje.</p>
<h2>Odkazy na jiné weby</h2>
<p>Odkazy na Bakaláři, Facebook, Instagram, YouTube a další weby jsou obyčejné odkazy: dokud na ně neklepnete, těmto službám se nic nepředává.</p>
<h2>Vaše práva</h2>
<p>Máte právo na přístup ke svým osobním údajům, na jejich opravu nebo výmaz, na omezení zpracování a na přenositelnost údajů a právo vznést námitku. Máte také právo podat stížnost u Úřadu pro ochranu osobních údajů, <a href="https://uoou.gov.cz/">uoou.gov.cz</a>. Další informace o zpracování osobních údajů ve škole najdete v dokumentu <a href="/media/2025/08/informace-k-gdpr-vos.docx">Informace k GDPR</a>.</p>"""


# ---------------------------------------------------------------- local preview server


def serve(port=8000):
    import http.server
    import functools
    from urllib.parse import unquote
    from urllib.parse import parse_qsl
    rules = []  # (compiled path pattern, {query}, destination); ":name" is one segment, "*" the rest
    for line in (DIST / "_redirects").read_text().splitlines():
        parts = line.split()
        if parts:
            pat = re.escape(parts[0]).replace(r"\*", "(?P<splat>.*)")
            pat = re.sub(r":(\w+)", r"(?P<\1>[^/]+)", pat)
            rules.append((re.compile(pat + "$"), dict(p.split("=", 1) for p in parts[1:-2]), parts[-2]))
    headers, types = {}, {}  # site-wide headers; exact-path Content-Type overrides
    block = None
    for line in (DIST / "_headers").read_text().splitlines():
        if line and not line.startswith(" "):
            block = line.strip()
        elif line.strip():
            k, v = line.strip().split(":", 1)
            if block == "/*":
                headers[k] = v.strip()
            elif k == "Content-Type":
                types[block] = v.strip()

    class H(http.server.SimpleHTTPRequestHandler):
        def guess_type(self, path):
            return types.get(self.path.split("?")[0]) or super().guess_type(path)

        def end_headers(self):
            for k, v in headers.items():
                if k == "Strict-Transport-Security":
                    continue  # local server is plain HTTP
                if k == "Content-Security-Policy":
                    v = v.replace("; upgrade-insecure-requests", "")
                self.send_header(k, v)
            super().end_headers()

        def do_GET(self):
            path = self.path.split("?")[0]
            query = dict(parse_qsl(self.path.partition("?")[2]))
            for pat, need, dst in rules:
                m = pat.match(path)
                if not m or (need and any(query.get(k) != v for k, v in need.items())) or (not need and path == "/"):
                    continue
                for k, v in m.groupdict().items():
                    dst = dst.replace(":" + k, v)
                self.send_response(301)
                self.send_header("Location", dst)
                self.end_headers()
                return
            fs_path = unquote(path).lstrip("/")  # media file names carry diacritics; the URL is percent-encoded
            if not (DIST / fs_path).exists() and not (DIST / fs_path / "index.html").exists():
                self.send_response(404)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write((DIST / "404.html").read_bytes())
                return
            super().do_GET()

        do_HEAD = do_GET

    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(H, directory=str(DIST)))
    print(f"serving http://127.0.0.1:{port}/")
    httpd.serve_forever()


if __name__ == "__main__":
    build()
    if len(sys.argv) > 1 and sys.argv[1] == "serve":
        serve(int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 8000)
