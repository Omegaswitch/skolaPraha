# Brand compliance and the school logo

Checked against the analysis of the *Sovereign Order of Malta Worldwide Communications Policy and Guide* (Feb 2025) and the *Guidelines for correct use of the two emblems and of the flags of the Order of Malta* (v3.3, 2023) in maltezskyrad `docs/brand-compliance.md`. The guideline PDFs themselves were not available in this session; nothing here relies on a reading that the maltezskyrad analysis does not record.

| # | Requirement | Status | How |
|---|---|---|---|
| 1 | Colours, layout and frame related to the Grand Magistry / maltezskyrad.cz | ✅ | Same tokens, red top bar, graphite menu, grey/white/red footer, Asap + EB Garamond. Banner photograph replaced by a white identity band with the school lockup (Project B). |
| 2 | Only the official emblems; none redrawn | ✅ | The shield in every lockup is the official vector copied byte for byte from the Grand Priory's lockup (`maltezskyrad/static/img/lockup/cs.svg`, shield master from the guidelines p. 53). The old site's raster shield (a redraw) is retired. `check.py` fails on any other file under `/img/`. |
| 3 | Order named correctly; no acronyms, never "Malta" alone | ✅ | Top bar "Maltézský řád · České velkopřevorství", footer links to orderofmalta.int and the founder. The school's registered name "…Suverénního řádu maltézských rytířů" is kept as a proper name. `check.py` flags SMOM. |
| 4 | Link to www.orderofmalta.int | ✅ | Red footer band, every page. |
| 5 | No invented facts | ✅ | All facts come from the old site; open questions are flagged in `docs/content-inventory.md`. |
| 6 | Real photographs, rights | ⚠️ | Only school photographs from the old site; theme stock and press photos dropped. Usage consent for staff portraits and students in the gallery to be confirmed by the school. |

## School logo (`static/img/logo/`)

The school's current logo (live site, `logo-vos-male2.png`): red shield, then "Vyšší odborná / škola zdravotnická" in red geometric sans, sentence case, set low beside the shield. On the client's instruction the new lockup copies that design, with more spacing between the shield and the type and between the lines, and with the official shield vector in place of the raster redraw. Lettering: TeX Gyre Adventor Bold (GUST font licence), the Century Gothic substitute already used for the Grand Priory lockups, set as outlines.

| File | Use |
|---|---|
| `primary.svg` | Primary lockup, red on white (site header) |
| `primary-white.svg` | Reversed, white on red or a photograph |
| `mono-black.svg` | Single colour (black) for print, stamps, forms |
| `compact.svg` | Shield only (favicon, small sizes) |
| `compact-black.svg` | Shield only, single colour |

Regenerate: `python3 tools/make_logo.py <maltezskyrad>/static/img/lockup/cs.svg texgyreadventor-bold.otf`.

**Needs formal approval (Grand Priory / Grand Magistry):** combining the official shield with the school's name is a personalised lockup; the guidelines reserve these to the Grand Magistry's standard asset. The font substitute (Adventor for Century Gothic) needs the same confirmation as for the Grand Priory lockups. The monochrome versions recolour the shield, which the emblem guidelines may not permit; use them only after approval.

## Open approvals

1. The school lockup (above).
2. Every page marked "existing" or "new" in preview builds, and the privacy notice.
3. EB Garamond for headings (same open question as maltezskyrad).
