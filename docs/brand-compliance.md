# Brand compliance and the school logo

Checked against the analysis of the *Sovereign Order of Malta Worldwide Communications Policy and Guide* (Feb 2025) and the *Guidelines for correct use of the two emblems and of the flags of the Order of Malta* (v3.3, 2023) in maltezskyrad `docs/brand-compliance.md`. The guideline PDFs themselves were not available in this session; nothing here relies on a reading that the maltezskyrad analysis does not record.

| # | Requirement | Status | How |
|---|---|---|---|
| 1 | Colours, layout and frame related to the Grand Magistry / maltezskyrad.cz | ✅ | Same tokens, red top bar, graphite menu, grey/white/red footer, Asap + EB Garamond. The header band carries the school logo over the old site's photograph of students (Project B). |
| 2 | Only the official emblems; none redrawn | ⚠️ | The school's existing logo is used as supplied (client decision); its shield is the school's drawing, not the official vector. `check.py` fails on any other file under `/img/`. |
| 3 | Order named correctly; no acronyms, never "Malta" alone | ✅ | Top bar "Maltézský řád · České velkopřevorství", footer links to orderofmalta.int and the founder. The school's registered name "…Suverénního řádu maltézských rytířů" is kept as a proper name. `check.py` flags SMOM. |
| 4 | Link to www.orderofmalta.int | ✅ | Red footer band, every page. |
| 5 | No invented facts | ✅ | All facts come from the old site; open questions are flagged in `docs/content-inventory.md`. |
| 6 | Real photographs, rights | ⚠️ | Only school photographs from the old site; theme stock and press photos dropped. Usage consent for staff portraits and students in the gallery to be confirmed by the school. |

## School logo and header photograph

On the client's instruction (19 Oct 2026) the site uses the school's existing Prague logo unchanged: `static/img/logo/vosz.png` (red shield and "Vyšší odborná škola zdravotnická", supplied by the client, transparent margin trimmed). The header band shows the photograph of students from the old site's home slider (`static/img/header/students.webp`, from `slider-voska.jpg`), faded to white behind the logo.

**Needs formal approval:** the logo's shield is the school's own drawing, not the official vector; the emblem guidelines allow only the official artwork, so the Grand Priory / Grand Magistry should confirm the logo (or supply an official-shield version). The students in the photograph need consent confirmed.

## Open approvals

1. The school logo (above).
2. Every page marked "existing" or "new" in preview builds, and the privacy notice.
3. EB Garamond for headings (same open question as maltezskyrad).
