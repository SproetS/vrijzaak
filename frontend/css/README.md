# css/ — ontwerp-tokens en type (voorstel)

| Bestand | Rol |
|---------|-----|
| `tokens.css` | Custom properties: kleur, thema, **basislijn 20px**, type-scale, space |
| `type.css` | `body` + **h1–h6** op dat raster (laadt ná tokens) |

```html
<link rel="stylesheet" href="tokens.css" />
<link rel="stylesheet" href="type.css" />
```

## Basislijn (InDesign-achtig)

| | |
|--|--|
| Body | **16px** (`1rem`) |
| Basislijn / leading-unit | **20px** (`1.25rem`) |
| Body line-height | 20px |
| Verticale ritme | margins/gaps in × 20px |

### Koppen (leading = n × 20px)

| | size | line-height | k |
|--|------|-------------|---|
| h1 | 40px | 40px | 2 |
| h2 | 32px | 40px | 2 |
| h3 | 24px | 40px | 2 |
| h4 | 20px | 30px* | 1.5 |
| h5 | 18px | 20px | 1 |
| h6 | 16px | 20px | 1 (uppercase) |

\*Half-step voor h4; class `.vz-type-strict` zet h4-leading op 40px.

Debug-raster: `html.vz-baseline-debug`.

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
