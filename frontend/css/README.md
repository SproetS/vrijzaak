# css/ — ontwerp-tokens en type (voorstel)

| Bestand | Rol |
|---------|-----|
| `tokens.css` | Custom properties: kleur, thema, **basislijn 20px**, type-scale, space |
| `type.css` | `body` + **h1–h6** op dat raster (laadt ná tokens) |

```html
<link rel="stylesheet" href="tokens.css" />
<link rel="stylesheet" href="type.css" />
```

## Twee rasters

| As | Module | Ankers | Gebruik |
|----|--------|--------|--------|
| **Verticaal** | **20px** basislijn | 20 · 40 · 60 · 80 | line-height, margin-block, stack/section gaps, padding-block |
| **Horizontaal** | **4px** | **4 · 16 · 32** (+ stappen 8, 12, 20, 24, 28, 36, 40, 48, 64) | padding-inline, gap in rijen, icon-spacing, page gutters |

**Niet:** verticale 10/15px-halves tenzij uitzondering; **niet** horizontale 5/10/20 uit baseline-delen — horizontaal altijd veelvoud van 4.

```css
/* voorbeelden */
padding-block: var(--vz-space-y-1);           /* 20 — verticaal */
padding-inline: var(--vz-space-x-4);        /* 16 — horizontaal */
gap: var(--vz-inline-gap);                  /* 16 rij */
margin-block: var(--vz-section-gap);        /* 40 sectie */
```

Tokens: `--vz-space-x-*` / `--vz-space-y-*` · legacy `--vz-space-*` = horizontaal 4px-schaal.

### Koppen (leading = n × 20px verticaal)

| | size | line-height | k |
|--|------|-------------|---|
| h1 | 40px | 40px | 2 |
| h2 | 32px | 40px | 2 |
| h3 | 24px | 40px | 2 |
| h4 | 20px | 40px | 2 |
| h5 | 18px | 20px | 1 |
| h6 | 16px | 20px | 1 (uppercase) |

\Debug-raster: `html.vz-baseline-debug`.

## Relatie met bouw

| Ontwerp (deze map) | Bouw (helling Nuxt) |
|--------------------|---------------------|
| `--vz-*` / type-scale | `shared/design/tokens.ts` + `app/assets/css/main.css` |
| Licht/donker | nog te mappen in Nuxt |

Documentatie: [docs/00-design-tokens.md](../../docs/00-design-tokens.md).

### Thema licht / donker

- Default: licht (`:root`).
- Donker: `html[data-theme="dark"]` of `.theme-dark`.
- Taal NL/EN = i18n, niet CSS.

Bij wijziging: docs → CSS → programmeur. **Niet** automatisch de Nuxt-build.
