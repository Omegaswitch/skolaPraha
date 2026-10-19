# Brand compliance and the school logo

Checked against the analysis of the *Sovereign Order of Malta Worldwide Communications Policy and Guide* (Feb 2025) and the *Guidelines for correct use of the two emblems and of the flags of the Order of Malta* (v3.3, 2023) in maltezskyrad `docs/brand-compliance.md`. The guideline PDFs themselves were not available in this session; nothing here relies on a reading that the maltezskyrad analysis does not record.

| # | Requirement | Status | How |
|---|---|---|---|
| 1 | Colours, layout and frame related to the Grand Magistry / maltezskyrad.cz | ✅ | Same frame as maltezskyrad.cz and velkoprevorskypalac.eu: red top bar, the official flag banner photograph with the Grand Priory lockup (MALTÉZSKÝ ŘÁD / ČESKÁ REPUBLIKA, white, unchanged file), the school's full name in white capitals, graphite menu, grey/white/red footer. The old slider photograph of students is the background of the home introduction (Project B). |
| 2 | Only the official emblems; none redrawn | ⚠️ | The school's existing logo is used as supplied (client decision); its shield is the school's drawing, not the official vector. `check.py` fails on any other file under `/img/`. |
| 3 | Order named correctly; no acronyms, never "Malta" alone | ✅ | Top bar "Maltézský řád · České velkopřevorství", footer links to orderofmalta.int and the founder. The school's registered name "…Suverénního řádu maltézských rytířů" is kept as a proper name. `check.py` flags SMOM. |
| 4 | Link to www.orderofmalta.int | ✅ | Red footer band, every page. |
| 5 | No invented facts | ✅ | All facts come from the old site; open questions are flagged in `docs/content-inventory.md`. |
| 6 | Real photographs, rights | ⚠️ | Only school photographs from the old site; theme stock and press photos dropped. Usage consent for staff portraits and students in the gallery to be confirmed by the school. |

## School logo, banner and photographs

- Header: the Grand Priory's banner photograph and lockup, copied unchanged from maltezskyrad.cz (`static/img/banner/banner-photo.webp`, `static/img/lockup/cs.svg`), with the school's name set as text on the right, exactly as velkoprevorskypalac.eu does for the palace.
- The school's own Prague logo (`static/img/logo/vosz.png`, supplied by the client) is kept in the repository and declared as the school's logo for search engines; it is not shown in the header, because the frame carries the Grand Priory lockup. Its shield is the school's drawing, not the official vector; if it is to appear on the site, the Grand Priory should confirm it.
- The photograph of students from the old home slider (`static/img/header/students.webp`) is the background of the home introduction. Consent of the students shown to be confirmed.

## Open approvals

1. The school logo, if it is to be shown (above).
2. Every page marked "existing" or "new" in preview builds, and the privacy notice.
3. EB Garamond for headings (same open question as maltezskyrad).
