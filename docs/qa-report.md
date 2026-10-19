# QA report (19 Oct 2026)

| Test | Result |
|---|---|
| `python3 build.py --production` and preview build | ✅ 22 pages, 4 posts, 12 events, news archive (all, 2 categories, 1 year), RSS, sitemap, robots, 404 |
| `python3 check.py` (internal links incl. downloads, redirect targets, one h1, titles, descriptions, brand files, acronym) | ✅ 34 pages, 0 problems |
| Legacy URLs: every old page, post, event, `/?p=` id and short link requested from the preview server | ✅ 116/116 end on 200 (directly or one 301) |
| `node tests/news.test.js` (login, upload type sniffing, publish, edit, delete, sanitiser, origin check) | ✅ |
| axe-core 4.10 WCAG 2 A/AA, 2.1 AA, 2.2 AA, every page at 1280 and 390 px | ✅ 0 violations |
| Keyboard: skip link to main; mobile menu and submenu toggles (aria-expanded), Escape | ✅ |
| Console errors on home, contact, editor | ✅ none |
| Visual check (screenshots) desktop and mobile: home, Vedení školy, Kontakt, Kombinované studium, Organizace školního roku, article | ✅ after fixing list indentation and mobile stacking |
| Home page weight | 878 kB, mostly lazy-loaded photographs; no third-party requests |
| CSP | `default-src 'self'`, no inline scripts (verified: injected inline script is refused) |

## Unresolved

1. **Approvals:** school logo (Grand Priory / Grand Magistry), all "existing" and "new" pages, the privacy notice.
2. **Content flags** for the school (see `docs/content-inventory.md`): donation VS 22526 vs 22627; contact mobile pairing; "Státní svátek" end date; stravování text about CSZŠ; 2025/2026 language-choice sentence.
3. **News publishing in production** needs the Vercel environment variables (README) and a GitHub token; the API was tested with GitHub stubbed, not against the live repository.
4. **Domain:** `baseUrl` is `https://vos.mojezdravka.cz`; production deployment needs the school's authorisation.
5. Photograph consent for staff portraits and students in the gallery.
6. Not rebuilt: site search, iCal export of events (see inventory).

## Pre-presentation audit (19 Oct 2026, after the header change)

Tools: the Impeccable detector (rendered scan of 9 key pages, source scan of CSS), axe-core, a Playwright sweep of all 34 pages at 1280, 768 (with reduced motion) and 390 px (console errors, failed requests, horizontal overflow, layout shift, tap-target size, image dimensions), `check.py`, the legacy URL test, the news API test, screenshots.

| Found | Fixed |
|---|---|
| Header was a white band with the school logo instead of the Grand Priory frame used by maltezskyrad.cz and the palace site | Banner photograph + official lockup + school name, as on the reference sites |
| Home gallery shifted the page while its tall photo loaded (CLS 0.23 at desktop) | Tall photo no longer sizes the grid; home CLS now 0.04 (desktop) / 0.05–0.08 (mobile), below 0.1 |
| Czech letters (š, ř, ů) swapped fonts after first paint | latin-ext subsets of Asap 400 and EB Garamond 500 preloaded |
| Top-bar links 19–22 px tall | 24 px minimum (WCAG 2.5.8) |

Verified, no change needed: no console errors and no failed requests on any public page; no horizontal overflow at any width; all images carry width and height; axe 0 violations; reduced motion stops all transitions; mobile menu, submenus, Escape and skip link work.

Accepted findings: the detector's "dark-glow" note is the banner name's text shadow, identical on maltezskyrad.cz and the palace site (part of the shared frame). Its type-ramp and colour advisories come from the inherited maltezskyrad CSS. `/pridat-aktualitu/` calls `/api/news`, which exists only on Vercel; locally it shows the sign-in form after a 404, as designed.
