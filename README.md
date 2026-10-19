# vos.mojezdravka.cz

Website of **Vyšší odborná škola zdravotnická Suverénního řádu maltézských rytířů** (Žerotínova 1143/38, Praha 3), a nursing college founded by the Czech Grand Priory of the Order of Malta.

It uses the same engine, design system and news workflow as maltezskyrad.cz (and lurdy.eu, velkoprevorskypalac.eu): a Python script (standard library only) turns the files in `content/` into plain HTML in `dist/`. No CMS, no database, no packages to install.

## Commands

```sh
python3 build.py serve 8000      # preview build, served at http://127.0.0.1:8000 with headers and redirects applied
python3 build.py                 # preview build into dist/ (noindex, review labels shown)
python3 build.py --production    # production build (Vercel runs this)
python3 check.py                 # checks dist/: links, redirect targets, one h1, titles, descriptions, brand files, acronym
node tests/news.test.js          # news publishing API (GitHub stubbed)
```

CI (`.github/workflows/ci.yml`) runs all three on every push.

## Where things are

| Path | What |
|---|---|
| `content/pages/<url>/index.html` | Pages: JSON front matter between `---` lines, then HTML. `description`, `image`, `status`, `nav` (short menu title), `section` (lists its menu children), `note` (review note, not shown). |
| `content/news/YYYY/MM/DD/slug.html` | News posts; the URL matches the old WordPress URL. |
| `content/events.json` | School-year events (shown on Organizace školního roku, Den otevřených dveří and the home page). |
| `content/site.json` | Names, contacts, links, menu, news categories. |
| `static/media/YYYY/MM/` | Photos and documents (same paths as the old `/wp-content/uploads/sites/4/`). |
| `static/img/logo/` | School lockups (see `docs/brand-compliance.md`); built by `tools/make_logo.py`. |
| `vercel.json` | Hosting, security headers, all legacy redirects (`docs/legacy-url-map.md`). |
| `tools/import_vos.py` | One-off importer from the old WordPress site. |

## Editorial workflow

**News (no GitHub needed).** Staff publish at `/pridat-aktualitu/` (not linked, not indexed, password-protected): title, date, categories, rich text, main photo, attachments; edit and delete existing posts. `api/news.js` sanitises the text and commits the post to `main`; Vercel rebuilds in about a minute. Set in Vercel → Settings → Environment Variables, then redeploy:

| Variable | Value |
|---|---|
| `NEWS_USERS` | one `Jméno:heslo` per line, one per co-worker |
| `NEWS_SECRET` | long random string (`openssl rand -base64 32`) |
| `GITHUB_TOKEN` | fine-grained token for `Omegaswitch/skolaPraha` only, Contents: read and write |
| `GITHUB_REPO` | `Omegaswitch/skolaPraha` (the default) |
| `NEWS_NOTIFY`, `RESEND_API_KEY`, `MAIL_FROM` | optional e-mail on each post |

**Events.** Edit `content/events.json` (title, start, end, url slug, description).

**Documents.** Put the PDF in `static/media/YYYY/MM/` and link it in a list: `<ul class="files"><li><a href="/media/…pdf">Název dokumentu</a></li></ul>`. The build adds type and size.

**Pages.** Edit the file; set `"imported": false` (already set on all curated pages) so a re-import never overwrites it; remove `"status"` once the school approves the page.

**Rules** (Order of Malta communications policy): full name of the Order where it is introduced, then "Maltézský řád"; never "Malta" alone or an acronym (`check.py` flags SMOM). Never redraw or recolour the shield.

## Documentation

`docs/plan.md` (analysis, architecture, roadmap) · `docs/content-inventory.md` · `docs/legacy-url-map.md` · `docs/brand-compliance.md` · `docs/qa-report.md` · `PRODUCT.md` · `DESIGN.md`
