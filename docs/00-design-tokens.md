# Design tokens — Vrijzaak

Werknaam / site: **Vrijzaak** · https://vrijzaak.nl

**Ontwerpafspraken in Markdown**, plus spiegel van wat de **bouwrepo nu** gebruikt. Bij implementatie: één set CSS-variabelen in Nuxt (`shared/design/tokens.ts` → `--akws-*`), geen losse componentkleuren.

Zie [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md) §7.

---

## A. Bouw (feitelijk in code)

Bron: webshop `shared/design/tokens.ts` en `docs/design.md`.

| Rol | Waarde |
|-----|--------|
| paper | `#f5f2e9` |
| surface | `#fffdf7` |
| ink | `#202c27` |
| muted | `#58645d` |
| accent | `#245c43` |
| line | `#b7c2b5` |
| font | `"GAP Mono", "Courier New", monospace` |
| emailFont | `"Courier New", monospace` |
| measure | `76rem` |

- WOFF self-hosted in bouw `public/fonts/`.
- Rollen: paper / surface / ink / muted / accent / line — geen ad-hoc hex in componenten.
- Mail: zelfde semantiek, geen verplicht GAP-webfont.

---

## B. Ontwerpverkenning (deze vault)

Richting die UX mag blijven verkennen tot er een **gezamenlijk fontbesluit** is.

### Typografie

| Rol | Familie | Gebruik |
|-----|---------|---------|
| **Voorlopig productierichting (ontwerp 2026-11-17)** | **GAP Code** | UI, body, navigatie, prijzen, labels |
| Alternatief / later | GAP Zuid VG | alleen na herziening |
| Bouwcode nu | GAP Mono in `tokens.ts` | nog niet gelijkgetrokken — programmeur |

Lokaal op deze Mac: `/Users/sjoerd/Desktop/GAP Fonts/` (OTF + Web).  
In `frontend/fonts/` van deze repo: placeholder; licentie vóór commit van webfonts.

```
/* voorlopig ontwerpbesluit */
--vz-font-ui: "GAP Code", ui-monospace, monospace;
/* bouw tokens.ts heeft nog font: GAP Mono — sync via programmeur */
```

### Basislijn-typografie (16 / 20)

Zoals een **basislijn-raster in InDesign**: vaste leading-unit, koppen en alinea’s daarop gestapeld.

| | |
|--|--|
| Body size | **16px** (`1rem`) |
| Basislijn | **20px** (`--vz-baseline: 1.25rem`) |
| Body leading | **20px** (ratio 1.25) |
| CSS | `frontend/css/tokens.css` (vars) + `frontend/css/type.css` (h1–h6, body) |

| Element | font-size | line-height | basislijnen |
|---------|-----------|-------------|-------------|
| body / p | 16px | 20px | 1 |
| h1 | 40px | 40px | 2 |
| h2 | 32px | 40px | 2 |
| h3 | 24px | 40px | 2 |
| h4 | 20px | 40px | 2 |
| h5 | 18px | 20px | 1 |
| h6 | 16px | 20px | 1 (+ caps) |

**Verticaal — alles op basislijn 20px**  
`margin-block`, `padding-block`, `gap` in kolom-stacks, section spacing, line-height-boxes: alleen `n × 20px` (`--vz-space-y-*`, `--vz-baseline`, `--vz-section-gap`).  
Debug: `html.vz-baseline-debug`.

**Horizontaal — 4px-module (ankers 4 / 16 / 32)**  
`padding-inline`, gaps in een rij, icon+label, page gutters: stappen van **4px** — `--vz-space-x-1`…`16` (4, 8, 12, **16**, 20, 24, 28, **32**, 36, 40, 48, 64).  
Primair denken: **4 → 16 → 32**; daartussen alleen 4px-stappen.  
Tap-target: **48px** (12×4), niet 44. Radius: 4 / 8 / 12 / 16.

| Richting | Token-voorbeelden |
|----------|-------------------|
| Verticaal | `--vz-stack-gap`, `--vz-space-y-2`, `--vz-heading-space-*` |
| Horizontaal | `--vz-inline-gap` (16), `--vz-page-pad-inline` (32), `--vz-space-x-4` |

### Kleur (vault-voorstel boven greyscale)

```
--gray-0 … --gray-900   pagina, vlakken, randen, tekst
--accent-soft-red / yellow / blue   spaarzaam CTA/tags
```

Semantisch (align met bouw-namen waar mogelijk):

```
--bg-primary ≈ paper/surface
--text-primary ≈ ink
--text-secondary ≈ muted
--border ≈ line
--cta ≈ accent
--danger / --success   mild (Mollie fail/success)
```

### Ruimte

```
--space-1 … --space-8
--radius-sm / md / lg
tap targets ≥ 44px (bouw design.md)
```

### Knoptekst (small caps)

UI-knoppen (`.vz-btn`): **`font-variant-caps: all-small-caps`** (+ lichte `letter-spacing`).  
SoT = CSS. FigCraft: `text.case` → `smallCaps` op button-labels (geen volledige CSS OpenType-spiegel).

### Licht / donker (thema-toggle)

Naast NL/EN-taaltoggle: **Licht** (default) en **Donker**.

| | |
|--|--|
| CSS | `frontend/css/tokens.css` |
| Activeren | `html[data-theme="light"\|"dark"]` of `.theme-light` / `.theme-dark` |
| Systeem | `prefers-color-scheme: dark` alleen als nog geen `data-theme` |
| Opslag | cookie/localStorage naast taalvoorkeur (bouw) |
| UI | molecuul `MolThemeSwitch` — [00-ui-moleculen.md](./00-ui-moleculen.md) |

**Licht** = bouwhex paper/surface/ink/accent.  
**Donker** = diep groen-zwart papier, lichte ink, helderder accent (voorstel in `tokens.css`; mag nog bijgestemd).  
Componenten gebruiken semantische vars (`--vz-bg-primary`, `--vz-text-primary`, `--akws-*`), geen losse light-only hex.  
**E-mail:** geen verplicht dark theme (clients onbetrouwbaar).

---

## C. Besluit nodig

| Vraag | Opties |
|-------|--------|
| Productie-font | **GAP Code (voorlopig vast in ontwerp)** · bouw nog Mono tot PR |
| Accent | Huidig groen `#245c43` vast · of zachte multi-accent uit AI-ontwerp |
| Papierwit | Bouw paper/surface overnemen als default in vault-UI-kit |
| Donker-palette | Voorstel in tokens.css ok · of dichter op bouw-light inverted |
| Default thema | Licht · systeem · laatst gekozen |

Tot besluit: **wireframes beschrijven hiërarchie en rust**; screenshots/CSS-proeven labelen “vault” vs “bouw”.

---

## Toon in UI

- Veel papier/witruimte, dunne randen  
- Kassa nóg rustiger (minder nav)  
- Bedragen uit server-DTO; geen dummy-prijzen in “echte” componenten  
- Self-host fonts; licentie checken vóór publieke launch

## Logo en frontend-assets

| Asset | Pad |
|-------|-----|
| Primair logo | `frontend/logos/logo.svg` (en evt. `.png`) |
| CSS-voorstel | `frontend/css/main.css` (tokens → … → layout) |
| Uitleg mappen | `frontend/README.md` |

Implementatie in de shop: programmeur → helling Nuxt (`public/`, `shared/design/tokens.ts`).  
