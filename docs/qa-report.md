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

## Cross-device audit and publishing workflow (21 October 2026)

Run with Playwright (Chromium) and axe-core 4.10 on the built site of all three school sites at six viewports
(phone 360 and 390 px, phone landscape 844 px, tablet 768 and 1024 px, desktop 1920 px): home, news listing, a post,
the main information page, contacts, the Grand Priory page, the editor.

| Check | Result |
|---|---|
| Horizontal overflow, layout | one bug across the sites: at 1024 px the hidden drop-down menus of the last items widened the page; fixed by right-aligning those menus (`.nav-list>li:nth-last-child(-n+3)>.sub`) |
| axe (WCAG 2 A/AA, 2.1, 2.2) | 0 violations at every viewport |
| Console errors, missing alt texts, one h1 | 0 |
| Sticky menu bar (added 20 Oct) | opens and scrolls correctly at every width; mobile menu limited to the viewport height |
| Small type and tap targets in the Grand Magistry frame (top bar, footer) | informational: the frame is the Order's prescribed template and was left as designed |

Publishing (see `docs/publishing.md`): roles (editor/admin), drafts, scheduled posts with a daily rebuild, pinned
notices, events and photo galleries were added to the shared editor and tested end to end in Chromium against the
local stand-in (`tests/news.local.js`): create with photo → draft → edit into a scheduled post → not built → admin pins a
notice → shown on the home page → event added, edited, deleted → post deleted → path traversal refused; 0 page errors.
`node tests/news.test.js`, `python3 build.py --production --offline` and `python3 check.py` pass.

Still needing authorisation: the Vercel environment variables (`NEWS_USERS`, `NEWS_SECRET`, `GITHUB_TOKEN`,
`DEPLOY_HOOK_URL`, `CRON_SECRET`) are not set on this project, so publishing is not live yet.

## Shared Supabase database (21 October 2026)

News, events, notices and galleries moved from files in the repository to the schools' shared Supabase project.
Verified:

| Check | Result |
|---|---|
| Row level security, run in SQL as anonymous, editor without second factor, editor with it (member of two sites), administrator | anonymous sees published posts only; no writes without the second factor; an editor writes only to their sites, edits only their own rows, cannot pin, cannot move a row to another site, cannot manage members; an administrator edits any row of their site, pins, lists and manages members, cannot touch another site or remove themselves |
| Auth REST: password sign-in, TOTP enrolment and verification, `aal2` claim, re-sign-in back to `aal1` | as designed |
| Storage: upload to own site folder, to another site's folder, without second factor, of an HTML file | 200 / refused / refused / refused (mime type) |
| Staff page in Chromium: administrator enrols the authenticator, publishes a pinned post with a photo, lists users; editor signs in with the code, sees no pin field or users tab, cannot delete or edit the administrator's post, saves a draft, adds, edits and deletes an event, deletes their own draft | all as designed, 0 page errors |
| Rendered pages from the database on the local stand-in: home (news band, pinned notice, events), listings, categories, years, pagination, posts (legacy and new, photo sizes), gallery, events page, event page, RSS, sitemap, search index, 404 | all rendered; axe 0 violations, no overflow, one h1, alt texts at 390/1024/1366 px |
| Output sanitiser on hostile text (script, event handlers, foreign image, javascript: link, iframe) | removed; legacy tables kept for imported (server-marked) posts |
| Supabase security advisors | one open item for the project owner: enable leaked-password protection (Authentication → Settings) |
| `python3 build.py --production --offline`, `python3 check.py` | pass |

Needs the project owner (Supabase dashboard): sign-ups off, Redirect URLs for the three domains, SMTP sender for
invitation and recovery mail (the built-in sender is limited to a few mails per hour), Czech e-mail templates,
leaked-password protection; then invite the real editors and remove the two test accounts.
