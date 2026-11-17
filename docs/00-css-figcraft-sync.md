# CSS ↔ FigCraft — wat wel/niet “implementeren”

**Kort antwoord:** FigCraft kan **geen** `tokens.css` / `main.css` rechtstreeks importeren als stylesheets.  
Wel: **dezelfde waarden** overzetten naar FigCraft **variables**, **text styles**, **paint styles** en defaults — via CLI-script.

| CSS (repo) | FigCraft |
|------------|----------|
| `tokens.css` kleuren Light/Dark | Variable collection `Theme` + paint styles `Color/*` |
| `type.css` h1–h6, body 16/20 | Text styles `Type/H1` … `Type/Body` |
| `--vz-font-ui: GAP Code` | `fontFamily: "GAP Code"` (systeemfont op de Mac) |
| `.vz-btn` | Components `Btn/Primary`, `Btn/Ghost` + `Type/Button` |
| Cascade atoms/molecules | Handmatig / components in FigCraft; CSS blijft handoff voor Nuxt |

**Bron van waarheid voor code:** nog steeds `frontend/css/` → Nuxt.  
**FigCraft:** visuele SSOT voor schermen; styles gespiegeld, niet de live CSS-engine.

---

## Eenmalig / na token-wijziging

```sh
export PATH="$HOME/.local/bin:$PATH"
cd frontend/design/figcraft

# Bestand mag niet “vies” open staan zonder save — of werk via /tmp en kopieer
figcraft-cli run scripts/sync-css-to-figcraft.jsonl \
  --in vrijzaak-storefront.figcraft \
  --out /tmp/vz-sync.figcraft

cp /tmp/vz-sync.figcraft vrijzaak-storefront.figcraft

figcraft-cli export vrijzaak-storefront.figcraft \
  -o ../exports/PageDesignSystem.png --node PageDesignSystem --scale 2
```

Script: `frontend/design/figcraft/scripts/sync-css-to-figcraft.jsonl`.

**Voorwaarde:** **GAP Code** geïnstalleerd op de Mac (bij jou: Desktop GAP Fonts / systeem). Zonder font valt FigCraft terug op een fallback.

---

## Wat het script zet

### Text styles (GAP Code + baseline)
`Type/H1` … `Type/H6`, `Type/Body`, `Type/Muted`, `Type/Small`, `Type/Button`, `Type/ButtonGhost`, `Type/Track`

### Paint styles
`Color/paper|surface|ink|muted|accent|line` (light hex uit tokens)

### Applied op
PageDesignSystem specimens + swatches + button labels.

### Radius / knoppen
Swatches `cornerRadius` **4**; `Btn/Primary` + `Btn/Ghost` **2** (CSS max 4). Geen shadow-effects.

### Default nieuwe tekst
`edit.setDefaultProperties` vanaf body-laag → nieuwe text tools starten met **GAP Code 16/20**.

### Al eerder
Variable collection **Theme** Light/Dark (9 kleuren) — `setup-design-system.jsonl`.

---

## Font in FigCraft vs CSS

| | |
|--|--|
| CSS `@font-face` | Self-host WOFF in Nuxt `public/fonts/` (later) |
| FigCraft | Gebruikt **geïnstalleerde** desktopfonts (`GAP Code`) |
| Export PNG | Raster met dat font |
| Export SVG | Kan font-afhankelijk zijn in viewers |

Obsidian mag Zuid VG lezen; **product-UI** = GAP Code (afspraak).

---

## Typografie die FigCraft beperkt dekt

| Feature | CSS (SoT implementatie) | FigCraft |
|---------|-------------------------|----------|
| Button small caps | `font-variant-caps: all-small-caps` op `.vz-btn` | `text.case` → **`smallCaps`** (geen CSS-variant) |
| Letter-spacing | CSS default `0` (mono); `.vz-track` display | Type/* tracking 0; `Type/Track` spaarzaam |
| Echte OpenType smcp/c2sc | `font-feature-settings` | hangt van font + app-support af |

**Aanvliegen:** besluit in **CSS** vastleggen → in FigCraft zo goed mogelijk spiegelen (small caps case) → PNG-export is benadering; **browser/Nuxt** is de echte weergave.

## Workflow advies

1. Tokens wijzigen in **`frontend/css/tokens.css` + `type.css`** (+ docs).  
2. FigCraft bijwerken met **`sync-css-to-figcraft.jsonl`** (of handmatig styles panel).  
3. Schermen tekenen met **Type/** en **Color/** styles + Theme variables.  
4. Programmeur bouwt Nuxt met **echte CSS-cascade**, niet met FigCraft-DevMode-dump als wet.

---

## Gerelateerd

- [00-design-tokens.md](./00-design-tokens.md)  
- [00-figcraft-samenwerking.md](./00-figcraft-samenwerking.md)  
- [frontend/css/README.md](../frontend/css/README.md)  

## Omgekeerd (FigCraft → CSS)

Checklist: [00-figcraft-naar-css-checklist.md](./00-figcraft-naar-css-checklist.md)  
Tool: `frontend/design/figcraft/scripts/figcraft_to_css.py` → `frontend/design/exports/figcraft-to-css-report.md`
