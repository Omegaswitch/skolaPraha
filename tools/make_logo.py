#!/usr/bin/env python3
"""Builds the school lockups (a vector redraw of the school's own logo) in static/img/logo/ from the official shield vector and TeX Gyre Adventor outlines.

    python3 tools/make_logo.py <maltezskyrad>/static/img/lockup/cs.svg <texgyreadventor-bold.otf>

The shield group is copied byte for byte from the Grand Priory's approved lockup (shield master, guidelines p. 53);
only the text is new. Layout and lettering copy the school's existing logo.
"""
import re
import sys
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

OUT = Path(__file__).resolve().parent.parent / "static" / "img" / "logo"
RED, INK = "#e31818", "#1a1a1a"


def shield(svg):
    """The shield paths (the group before the lettering) and their box in the source's coordinates."""
    g = re.search(r'<g transform="translate\(-113.9 -228.2\)">(.*?)</g>', svg, re.S).group(1)
    return g, (113.9, 228.2, 107.6, 126.0)  # x, y, w, h of shield incl. its outline stroke


def text_path(font, s, x, y, cap_h, tracking=-10):
    gs, cmap = font.getGlyphSet(), font.getBestCmap()
    scale = cap_h / font["OS/2"].sCapHeight
    pen = SVGPathPen(gs)
    cx = 0
    for ch in s:
        name = cmap[ord(ch)]
        gs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x + cx, y)))
        cx += (gs[name].width + tracking) * scale
    return pen.getCommands(), cx


def lockup(svg, font, lines, fill_text, name, mono=None):
    """The school's established lockup (live site, logo-vos-male2.png): shield left, two lines of red bold
    geometric sans in sentence case, set low beside the shield. Measured on that file (x = shield height):
    opened up on request: cap height 0.16x, gap 0.18x, line pitch 0.27x, last baseline at 0.86x."""
    g, (sx, sy, sw, sh) = shield(svg)
    if mono:  # single-colour version: the shield's red becomes the mono colour, white stays the knock-out
        g = g.replace(RED, mono)
    x = sh
    tx, cap = sw + 0.18 * x, 0.16 * x
    parts, width = [], tx
    for i, line in enumerate(lines):
        y = 0.86 * x - (len(lines) - 1 - i) * 0.27 * x
        d, w = text_path(font, line, tx, y, cap, tracking=0)
        parts.append(f'<path d="{d}"/>')
        width = max(width, tx + w)
    out = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width + 2:.1f} {sh:.1f}" width="{width + 2:.1f}" height="{sh:.1f}" role="img">'
           f'<title>Vyšší odborná škola zdravotnická Suverénního řádu maltézských rytířů</title>'
           f'<g transform="translate({-sx} {-sy})">{g}</g><g fill="{fill_text}">{"".join(parts)}</g></svg>')
    (OUT / name).write_text(out, encoding="utf-8")


def compact(svg, name, mono=None):
    g, (sx, sy, sw, sh) = shield(svg)
    if mono:
        g = g.replace(RED, mono)
    (OUT / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {sw} {sh}" width="{sw}" height="{sh}" role="img">'
                            f'<title>Maltézský řád</title><g transform="translate({-sx} {-sy})">{g}</g></svg>', encoding="utf-8")


if __name__ == "__main__":
    svg, font = Path(sys.argv[1]).read_text(), TTFont(sys.argv[2])
    OUT.mkdir(parents=True, exist_ok=True)
    lines = ["Vyšší odborná", "škola zdravotnická"]
    lockup(svg, font, lines, RED, "primary.svg")
    lockup(svg, font, lines, "#ffffff", "primary-white.svg", mono="#ffffff")
    lockup(svg, font, lines, "#000000", "mono-black.svg", mono="#000000")
    compact(svg, "compact.svg")
    compact(svg, "compact-black.svg", mono="#000000")
    assert all((OUT / f).stat().st_size > 1000 for f in ("primary.svg", "compact.svg"))
    print("ok", sorted(p.name for p in OUT.iterdir()))
