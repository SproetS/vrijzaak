# Font-grid — GAP Code bepaalt het raster

**Besluit (2026-11-18):** het UI-raster volgt de **metrics van GAP Code**, niet een losse 4px-module.  
Browser-tekst vergroten/zoomen schaalt **corps én grid** mee (`rem` / `em` / `ch`).

Illustrator-schets: `frontend/design/illustrator-exports/Typo - licht|donker.png`.

## Gemeten (GAPCode-Regular.ttf)

| Metric | Waarde | Bij body 1rem (≈16px default) |
|--------|--------|-------------------------------|
| unitsPerEm | 1000 | |
| Advance (mono, o.a. n/0/=) | **600** | **0.6em** = **1ch** |
| Typo asc/desc/lineGap | 642 / −223 / 335 | som **1200** → **line-height 1.2** |
| Regel @ 1rem | | **1.2rem** (≈19.2px @ 16) |
| Celbreedte @ 1rem | | **0.6rem** (≈9.6px @ 16) |
| xHeight / capHeight | 440 / 640 | |

Unieke advances in font: 0, 250 (specials), **600** (tekens) — UI rekent op **600**.

## Afgeleide eenheden (CSS)

```
--vz-font-upem: 1000
--vz-font-advance: 600
--vz-cell: 0.6em          /* = 1ch bij mono 0 */
--vz-line: 1.2            /* unitless line-height factor */
--vz-baseline: 1.2rem     /* 1 body-regel @ root 1rem body */
```

- **Verticaal:** margins/gaps/line-boxes in `n × --vz-baseline` (of `n × 1.2em` op body-niveau).
- **Horizontaal:** padding/gaps bij voorkeur in **`ch`** (1 cel) of `n * 0.6rem`.
- Oude **4px-ladder** = startpunt; blijft alleen als benadering voor radius (max 4px) en legacy aliases.

## Type-ladder (schets)

| Element | Size | Leading | Tracking | Weight / kleur |
|---------|------|---------|----------|----------------|
| `p` / body | **1rem** | **1.2** | 0 | regular / ink |
| `h1` | **2rem** (= 2× body) | **1.2** → box **2.4rem** = **2 body-regels** | 0 | bold / ink — glyphs ook **2× celbreed** |
| `h2` | **1rem** | 1.2 | **1ch** (tracked display) | regular of bold / muted |
| `h3` | **1rem** | 1.2 | **1ch** (eert H-grid) | regular/bold / **accent-warm (oranje)** |
| `h4` | **1rem** | 1.2 | 0 | bold / ink — strak op alinea |
| label / meta | **1rem** | 1.2 | tracked of `NAME - LABEL` | muted; small-caps spaarzaam op knoppen |

Hiërarchie zonder extreme schaal: **size (h1) · tracking (h2/h3) · kleur (h3) · weight (h4/body) · small-caps (knoppen)**.

## Inspring (H-hiërarchie)

| Element | `padding-inline-start` |
|---------|------------------------|
| h1–h3 | 0 |
| h4 | **1ch** |
| p / lists / labels / fields | **2ch** |

Tokens: `--vz-indent-0|1|2`. Utilities: `.vz-indent-*`.

## Plaatsing t.o.v. het grid (site-breed)

Het font-grid geldt voor **hele pagina**: main, **header**, **footer**, forms, knoppen.  
Debug in preview toont lijnen over `.vz-shell` (dus ook chrome).

| As | Eenheid | Rol |
|----|---------|-----|
| V (horizontale lijnen) | `1 × --vz-baseline` (1.2rem @ body) | stap tussen twee gridlijnen |
| H (verticale lijnen) | `1ch` | mono-cel |

**Gedrag (werkregel):**

1. Blokken starten bij voorkeur **op** een basislijn, niet ertussen.
2. Hoogtes bij voorkeur **hele** V-stappen (`n × baseline`), minus borders indien nodig.
3. Breedtes/paddings/inspring in **hele** H-stappen (`n × ch`).
4. Optische uitzonderingen (1px border, hairline) documenteren; niet stiekem half-stappen stapelen.

### Controls (input / button)

Hoogte = **één** V-stap (“tussen twee horizontale gridlijnen”) − 2px border:

```
--vz-control-lines: 1
--vz-control-height: calc(1 * baseline - 2px)
padding-inline: 2ch
padding-block: 0
```

Quiet/tekst-CTA’s: geen control-box (schets “Terug naar winkel”).

## Zoom / a11y

`html { font-size: 100% }` — user/browser font size wijzigt `rem` → cel, baseline, h1 (2rem) schalen mee.  
Tap-minimaal blijft ≥ 2.5rem-ish of 3× baseline; niet vast 48px-only.

## Bron

- Font lokaal: Desktop `GAP Fonts/Web/GAP Code - web/` · preview `frontend/fonts/GAP Code/` (gitignored)
- CSS: `frontend/css/tokens.css`, `type.css`
- Toon: [00-merk-toon-en-principes.md](./00-merk-toon-en-principes.md)

*Gemeten 2026-11-18 met fontTools op GAPCode-Regular.ttf.*
