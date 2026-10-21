# Brand compliance and the school logo

Checked against the analysis of the *Sovereign Order of Malta Worldwide Communications Policy and Guide* (Feb 2025) and the *Guidelines for correct use of the two emblems and of the flags of the Order of Malta* (v3.3, 2023) in maltezskyrad `docs/brand-compliance.md`. The guideline PDFs themselves were not available in this session; nothing here relies on a reading that the maltezskyrad analysis does not record.

| # | Requirement | Status | How |
|---|---|---|---|
| 1 | Colours, layout and frame related to the Grand Magistry / maltezskyrad.cz | ✅ | Same frame as maltezskyrad.cz and velkoprevorskypalac.eu: red top bar, the official flag banner photograph with the school's logo (which includes MALTÉZSKÝ ŘÁD / ČESKÁ REPUBLIKA in white), the school's full name in white capitals, graphite menu, grey/white/red footer. The old slider photograph of students is the background of the home introduction (Project B). |
| 2 | Only the official emblems; none redrawn | ⚠️ | The school's existing logo is used as supplied (client decision); its shield is the school's drawing, not the official vector. `check.py` fails on any other file under `/img/`. |
| 3 | Order named correctly; no acronyms, never "Malta" alone | ✅ | Top bar "Maltézský řád · České velkopřevorství", footer links to orderofmalta.int and the founder. The school's registered name "…Suverénního řádu maltézských rytířů" is kept as a proper name. `check.py` flags SMOM. |
| 4 | Link to www.orderofmalta.int | ✅ | Red footer band, every page. |
| 5 | No invented facts | ✅ | All facts come from the old site; open questions are flagged in `docs/content-inventory.md`. |
| 6 | Real photographs, rights | ⚠️ | Only school photographs from the old site; theme stock and press photos dropped. Usage consent for staff portraits and students in the gallery to be confirmed by the school. |

## School logo, banner and photographs

- Header: the official flag banner photograph from maltezskyrad.cz (`static/img/banner/banner-photo.webp`) with the school's Prague logo on it (`static/img/logo/vosz.svg`). It is the client's `logo-vos-male2.png` rebuilt as a vector by `tools/make_logo.py`, the same generator, official shield vector (from the Coat of Arms guidelines via maltezskyrad.cz) and geometry as the Kladno and Skutec school logos, so the three schools share one shield, size and spacing. Lettering: Century Gothic Bold (licensed copy supplied by the client; the font file is not in the repository, only the outlines). The logo carries "MALTÉZSKÝ ŘÁD / ČESKÁ REPUBLIKA" in white above the school's name in red, so it needs a coloured background; on white it disappears. The school's full name is set as text on the right, as on velkoprevorskypalac.eu.
- The logo's shield is the school's drawing, not the official vector; the Grand Priory should confirm the logo.
- The photograph of students from the old home slider (`static/img/header/students.webp`) is the background of the home introduction. Consent of the students shown to be confirmed.

## Open approvals

1. The school logo (above).
2. Every page marked "existing" or "new" in preview builds, and the privacy notice.
3. EB Garamond for headings (same open question as maltezskyrad).
