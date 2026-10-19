# Content inventory: vos.mojezdravka.cz (crawled 19 Oct 2026)

Sources: `wget` mirror (376 files), WordPress REST API (22 pages, 4 posts, 356 media), The Events Calendar API (12 events). Old site: WordPress multisite, Kingster theme + Goodlayers page builder, Revolution Slider, Contact Form 7 (no form found on any page), The Events Calendar.

Status: **existing** = text taken over, awaiting school review (yellow bar in preview builds) · **new** = new text, awaiting approval.

## Pages

| Old URL | New URL | Status | Notes |
|---|---|---|---|
| `/` | `/` | new | Rebuilt from the old home text (O škole, obory, aktuality, události, tým, galerie, video, quick links). Slider removed; its text ("Vítejte na Vyšší odborné škole zdravotnické…") is the H1/lead. |
| `/clanky/` | `/aktuality/` (301) | generated | News archive with categories, years, RSS. |
| `/vedeni-skoly/` | same | existing | Old page showed the leadership twice (desktop + mobile blocks); merged. Portraits kept. |
| `/organizace-skolniho-roku/` | same | existing | Old page rendered the event calendar; now generated from `content/events.json`. |
| `/pedagogicky-sbor/` | same | existing | Two names normalised to first-name-first order (Džupinková, König). |
| `/skolni-kaplan/` | same | existing | |
| `/skolne/` | same | existing | **Flag:** intro gives donation VS 22526, the VS table gives 22627. Kept as on the old site. |
| `/vychovne-poradenstvi/` | same | existing | Existed but was not in the old menu; now under O škole. |
| `/vyucovane-obory/` | same | existing | Three third-party press photos (koronavirus…, jarvis…, 0fwC.jpeg) not reused (rights unknown). |
| `/prakticka-sestra-denni/` | same | existing | URL keeps the old slug although the programme is Diplomovaná všeobecná sestra. |
| `/prakticka-sestra-dalkove/` | same | existing | |
| `/prijimaci-rizeni-denni-studium/` | same | existing | Dates "bude upřesněno" as on the old site. |
| `/prijimaci-rizeni-dalkove-studium/` | same | existing | **Flag:** old text says "pro školní rok 2025/2026 bude nabídnuta možnost výběru jazyka" on a 2026/2027 page; year omitted. |
| `/den-otevrenych-dveri/` | same | existing | Dates now come from events.json (same three dates, 17:00). |
| `/denni-studium/` | same | existing | |
| `/kombinovane-studium/` | same | existing | Konzultační hodiny "bude doplněno" as on the old site. |
| `/formulare/` | same | existing | Button labels expanded to full document names. |
| `/knihovna/` | same | existing | Closed; the old opening-hours table (all "Zavřeno") replaced by the closure notice. |
| `/stravovani-a-ubytovani/` | same | existing | **Flag:** text speaks of CSZŠ Jana Pavla II.; "10 minut pěšky od školy" referred to Ječná and was dropped. |
| `/kontakt/` | same | existing | **Flag:** the old page listed roles, landlines, mobiles and e-mails in separate columns; pairing reconstructed by order and checked against Vedení školy (landlines and leadership mobiles match). The two remaining mobiles (777 142 783, 777 614 611) are assigned by order only. |
| `/ddm/` | same | existing | Not in the old menu; describes the DDM of CSZŠ Jana Pavla II.; its two "Stáhnout" buttons had no link. Kept so the address works. |
| `/maintenance/` | `/` (301) | — | Theme page. |
| — | `/o-skole/`, `/pro-uchazece/`, `/pro-studenty/` | new | Section pages (the old menu headings were not links). |
| — | `/ochrana-osobnich-udaju/` | new, approval | Privacy notice for this site. |
| — | `/pridat-aktualitu/` | new | Staff news editor (not indexed). |

## News (4 posts, all migrated, URLs unchanged)

`/2026/08/31/nova-budova-skoly/`, `/2026/08/31/nova-adresa-skoly-zerotinova-38/`, `/2026/09/10/3-kolo-prijimaciho-rizeni/`, `/2026/09/17/vysledky-prijimaciho-rizeni-2/`. Featured images kept. Categories assigned: Ze školy / Přijímací řízení (the old site had only "Blog").

## Events (12, all migrated)

`/udalost/<slug>/` → `/organizace-skolniho-roku/#<slug>`. **Flag:** "Státní svátek" is stored on the old site as 28. 9. – 28. 10. 2026; kept as is (probably meant one day).

## Documents

45 documents linked from pages migrated to `static/media/` with their original paths; every short link (`/skolni-rad-vos` etc., 43) redirects to the file. Labels now describe the document; type and size are shown.

Not linked from any page on the old site, migrated unchanged (old direct links keep working) but not linked on the new site; most belong to the sister secondary school (shared multisite library). To publish any of them, add a link on the relevant page:

| File | Uploaded | Title |
|---|---|---|
| `2026/08/plan-letni-obdobi-2526.docx` | 2026-08-02 | plan-letni-obdobi-2526 |
| `2026/06/vysledky-kombi-vos.pdf` | 2026-06-24 | vysledky-kombi-vos |
| `2026/06/vysledky-denni-vos.pdf` | 2026-06-24 | vysledky-denni-vos |
| `2025/11/rozvrh-zimni-3b-2627.pdf` | 2025-11-02 | rozvrh-zimni-3b-2627 |
| `2025/10/rozhodnuti-reditelske-volno-vos.pdf` | 2025-10-15 | rozhodnuti-reditelske-volno-vos |
| `2025/08/pozadavek-subjektu-na-pristup.docx` | 2025-08-18 | pozadavek-subjektu-na-pristup |
| `2025/08/inspekcni-zprava-25.pdf` | 2025-08-18 | inspekcni-zprava-25 |
| `2025/08/vyrocni-zprava-2324.pdf` | 2025-08-18 | vyrocni-zprava-2324 |
| `2025/08/ochrana-oznamovatelu-whistleblowing.pdf` | 2025-08-18 | ochrana-oznamovatelu-whistleblowing |
| `2025/08/informace-k-gdpr.docx` | 2025-08-18 | informace-k-gdpr |
| `2025/08/studium-zanechani.docx` | 2025-08-18 | studium-zanechani |
| `2025/08/studium-uznani-studijnich-povinnosti.docx` | 2025-08-18 | studium-uznani-studijnich-povinnosti |
| `2025/08/studium-prestup-na-jinou-skolu.docx` | 2025-08-18 | studium-prestup-na-jinou-skolu |
| `2025/08/studium-prestup-na-cszs.docx` | 2025-08-18 | studium-prestup-na-cszs |
| `2025/08/zadost-prijeti-do-vyssiho-rocniku.docx` | 2025-08-18 | zadost-prijeti-do-vyssiho-rocniku |
| `2025/08/zadost-prodlouzeni-klasifikace.docx` | 2025-08-18 | zadost-prodlouzeni-klasifikace |
| `2025/08/zadost-preruseni-studia.docx` | 2025-08-18 | zadost-preruseni-studia |
| `2025/08/zadost-opakovat-rocnik.docx` | 2025-08-18 | zadost-opakovat-rocnik |
| `2025/08/zadost-nahrazeni-praxe.docx` | 2025-08-18 | zadost-nahrazeni-praxe |
| `2025/08/zadost-ivp.docx` | 2025-08-18 | zadost-ivp |
| `2025/08/uvolneni-nad-3dny.docx` | 2025-08-18 | uvolneni-nad-3dny |
| `2025/08/uvolneni-do-3dny.docx` | 2025-08-18 | uvolneni-do-3dny |
| `2025/08/uvolneni-tev.docx` | 2025-08-18 | uvolneni-tev |
| `2025/08/maturitni-okruhy-nepovinne.docx` | 2025-08-15 | maturitni-okruhy-nepovinne |
| `2025/08/maturitni-okruhy-anj.docx` | 2025-08-15 | maturitni-okruhy-anj |
| `2025/08/kanon-2425.doc` | 2025-08-15 | kanon-2425 |
| `2025/08/temata-profilove-mz-dalkove.docx` | 2025-08-15 | temata-profilove-mz-dalkove |
| `2025/08/temata-profilove-mz-denni.docx` | 2025-08-15 | temata-profilove-mz-denni |
| `2025/08/kriteria-prijimaciho-rizeni-dalkove-1-kolo.pdf` | 2025-08-14 | kriteria-prijimaciho-rizeni-dalkove-1-kolo |
| `2025/08/kriteria-prijimaciho-rizeni-denni-1-kolo.pdf` | 2025-08-14 | kriteria-prijimaciho-rizeni-denni-1-kolo |
| `2025/08/ucebni-plan-prakticka-sestra-dalkove.docx` | 2025-08-14 | ucebni-plan-prakticka-sestra-dalkove |
| `2025/08/svp-prakticka-sestra-dalkove.pdf` | 2025-08-14 | svp-prakticka-sestra-dalkove |
| `2025/08/ucebni-plan-prakticka-sestra-denni.docx` | 2025-08-14 | ucebni-plan-prakticka-sestra-denni |
| `2025/08/svp-prakticka-sestra-denni.pdf` | 2025-08-14 | svp-prakticka-sestra-denni |
| `2025/08/preventivni-program.docx` | 2025-08-14 | preventivni-program |
| `2025/08/sluzby-vychovneho-poradce.docx` | 2025-08-14 | sluzby-vychovneho-poradce |
| `2025/08/jednaci-rad-skolske-rady.pdf` | 2025-08-14 | jednaci-rad-skolske-rady |
| `2025/08/zapis-skolska-rada-01-a-02-2324.pdf` | 2025-08-14 | zapis-skolska-rada-01-a-02-2324 |
| `2025/08/zapis-skolska-rada-01-2425.pdf` | 2025-08-14 | zapis-skolska-rada-01-2425 |
| `2025/08/zprava-o-cinnosti-skolske-rady.pdf` | 2025-08-14 | zprava-o-cinnosti-skolske-rady |
| `2025/08/skolni-rad-cszs.pdf` | 2025-08-14 | skolni-rad-cszs |
| `2025/08/Otazky-z-podpory.pdf` | 2025-08-06 | Otázky z podpory |

Not migrated: 4 CSV import test files (`CSV-file-for-example-*.csv`, `import-vos.csv`).

## Images

Migrated: school photographs and staff portraits used by the old pages (2025/08, 2025/09, 2026/04, 2026/08). Not migrated: Kingster theme demo stock (201 files from 2018/08 and 2019/06, shutterstock/unsplash/pexels), icon PNGs, the three third-party press photos above. The old logo is kept (`static/img/logo/vosz.png`); the home slider photograph is the header background.

## Interactive functionality on the old site

| Feature | New site |
|---|---|
| Search (WordPress) | Not rebuilt: 22 pages are reachable in two clicks from the menu and footer. |
| Event calendar (list, iCal export, Google Calendar add) | Dated list; iCal export not rebuilt (12 events). |
| Social share links on events | Dropped. |
| Bakaláři button | Top bar. |
| Video (YouTube) | Linked from the home page (no embed: no third-party requests). |
| Instagram, Facebook, YouTube links | Footer. |

## External links

skolajecna.bakalari.cz, instagram.com/skolajecna, facebook.com/skolyjecna, youtube.com/@skolajecna7126, youtu.be/4hgAQGaXTkI, maltezskyrad.cz, kds.op.cz, cssjb.cz, dmlovosicka.cz.

## Inaccessible or missing source material

- DDM "Aktuální rozpis kroužků" and "Vnitřní řád DDM": buttons without files on the old site.
- Konzultační hodiny vyučujících: "bude doplněno" on the old site.
- Project poster (/projekt-2-vos) is a JPEG, not a document.
