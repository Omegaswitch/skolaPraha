# Analysis, architecture and roadmap

## Tools

- **Graphify** (`/root/.local/bin/graphify`): run against the reference repository before coding (`graphify explain "render_page()"` etc. on maltezskyrad's `graphify-out/graph.json`, built from its current commit); `graphify update .` is run on this repository after changes (CLAUDE.md).
- **Ponytail**: the skill became available mid-session and was loaded before the build code was written; everything after the importer's first draft follows it (reuse the maltezskyrad engine, no new dependencies, smallest complete change).
- **Impeccable** 4.6.0: installed on request (`npx skills add pbakaus/impeccable --skill impeccable`, in `.agents/skills/`); `impeccable context` run with this repository's PRODUCT.md and DESIGN.md; the craft-floor checklist applied to the build. Its interview step was replaced by the client's instruction to base the design on the reference sites.
- **/taste**: no such skill or command exists in this environment; not run.

## Reference repositories (read only, not modified)

| Name in brief | Repository | Reused |
|---|---|---|
| maltezskyrad | Omegaswitch/maltezskyrad | Whole engine: `build.py` (layout, nav, breadcrumbs, side nav, image helpers, news index/article/RSS, preview server), `check.py`, `api/news.js` + `/pridat-aktualitu/` editor + tests, CSS/JS, fonts, favicons, security headers, CI, DESIGN.md system, shield vector |
| poutlourdy | Omegaswitch/lurdy | Same engine family; e-mail notification pattern (Resend) already in news.js |
| maltezskypalac | Omegaswitch/palacPronajem | Query-string redirects (`/?page_id=`) in vercel.json, `_redirects` and the preview server |

## Architecture

Static site, Python 3 standard library build → `dist/`, Vercel hosting (`vercel.json`: build command, CSP/HSTS/headers, 150 redirects). One serverless function, `api/news.js`, commits news posts to this repository. Content in files: pages (`content/pages`), posts (`content/news`), events (`content/events.json`), settings (`content/site.json`), media (`static/media`, same paths as the old uploads). Czech only.

Changes against maltezskyrad: no translations, AddCal calendar or Grand Magistry feed; events list, downloads with type and size, people/payment rows, section pages, school identity band, programme pair, gallery and team on the home page.

## Roadmap (all done in this session)

1. Crawl and inventory the old site; WordPress and events API export → `docs/content-inventory.md`.
2. Importer (`tools/import_vos.py`): page-builder HTML → semantic HTML, documents and images, short links.
3. Curate every page by hand (duplicates, layout labels, generic "Stáhnout" buttons).
4. Engine: adapt build.py/check.py/news API; logo; CSS deltas.
5. Redirects and legacy URL test (`docs/legacy-url-map.md`).
6. QA: check.py, news API test, axe-core WCAG 2.2 AA at 1280/390 px, interaction test, screenshots → `docs/qa-report.md`.
