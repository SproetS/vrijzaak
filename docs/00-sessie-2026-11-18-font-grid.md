# Sessie 2026-11-18 — Font-grid

## Besluit

GAP Code **bepaalt** H- en V-raster. 4px was startpunt. Browser-font/zoom schaalt grid mee.

## Metrics (Regular.ttf)

- UPM 1000, advance **600** (0.6em = 1ch), line **1.2em**
- h1 = 2× body (2rem), box 2 baselines
- h2/h3 tracking **1ch**; h3 kleur `--vz-accent-warm`

## Gedaan

- `docs/00-font-grid.md`
- `tokens.css` / `type.css` / preview
- index, merk-toon, design-tokens, AGENTS

## Schets

`frontend/design/illustrator-exports/Typo - licht.png` · donker

## Update: controls + inspring

- Controls: hoogte `2 × baseline − 2px`, pad-inline `2ch`, pad-block 0
- Inspring: h4 `1ch`, p/lists/fields `2ch`, h1–h3 `0`
- Quiet button = tekstlink (geen control-box)

## Update: control = 1 gridstap

Buttons/inputs: hoogte tussen **twee** horizontale baselijnen (`--vz-control-lines: 1`).  
Grid geldt hele shell (header/footer meegenomen in debug).

## Update: line 1.333 + schetskleuren

- `--vz-line: 1.333` / baseline `1.333rem` (font-metric 1.2 blijft als `--vz-line-font`)
- Palette light/dark uit Typo SVG’s in tokens.css
