# css/ — moleculen-cascade (ontwerpvoorstel)

**Idee:** vaste basisregels per laag; **uitzonderingen** alleen in `components/` of Vue scoped.

```text
tokens  →  type  →  base  →  atoms  →  molecules  →  organisms  →  layout
                                                              ↘ components/* (optioneel)
```

Entry: **`main.css`** (importeert alles in volgorde).

| Bestand | Laag | Inhoud |
|---------|------|--------|
| `fonts.css` | fonts | `@font-face` GAP Code (lokale woff2, gitignored files) |
| `tokens.css` | tokens | Kleur, thema, type-scale, V/H-space |
| `type.css` | type | body, h1–h6, baseline debug |
| `base.css` | base | box-sizing, links, `.vz-stack` / `.vz-row` |
| `atoms.css` | atoms | `.vz-btn`, `.vz-input`, `.vz-price`, … |
| `molecules.css` | molecules | `.vz-field`, `.vz-nav-item`, `.vz-empty`, … |
| `organisms.css` | organisms | `.vz-site-header`, `.vz-quote`, `.vz-cart`, … |
| `layout.css` | layout | `.vz-shell`, `.vz-main`, checkout-grid |
| `components/` | exceptions | Alleen afwijkingen |
| `main.css` | entry | `@import` cascade |

Classnamen sluiten aan op [docs/00-ui-moleculen.md](../../docs/00-ui-moleculen.md) (`Atom*` / `Mol*` / `Org*` → `.vz-*`).

## Laden

```html
<link rel="stylesheet" href="/path/to/css/main.css" />
```

Of in Nuxt later: dezelfde volgorde mappen naar `app/assets/css/`.

## Twee rasters (altijd)

| As | Module | Ankers | Tokens |
|----|--------|--------|--------|
| **Verticaal** | 20px basislijn | 20 · 40 · 60 | `--vz-space-y-*`, `--vz-baseline` |
| **Horizontaal** | 4px | **4 · 16 · 32** | `--vz-space-x-*`, `--vz-inline-gap` |

```css
padding-block: var(--vz-space-y-1);    /* 20 */
padding-inline: var(--vz-space-x-4); /* 16 */
gap: var(--vz-inline-gap);           /* 16 in een rij */
```

## Regel vs uitzondering

| Wel in basis-lagen | Wel in `components/` of SFC |
|--------------------|-----------------------------|
| Default knop, field, quote-blok | Unieke test-banner, fulfilment-tabel |
| Raster, focus, tap 48px | Eenmalige layout-hack |
| Modifiers `--ghost`, `--tight` | Page-only one-offs |

1. Kan het een **modifier** op atom/molecule? → daar.  
2. Echt uniek? → `components/<naam>.css`.  
3. Geen losse hex / 13px / verticale 15px.

## Thema & i18n

- Licht/donker: `html[data-theme="dark"]` (tokens).  
- NL/EN: i18n in Nuxt, niet CSS.  
- UI: `.vz-switch` voor lang + theme.

## Documentatie

- [docs/00-design-tokens.md](../../docs/00-design-tokens.md)  
- [docs/00-ui-moleculen.md](../../docs/00-ui-moleculen.md)  

Dit is **geen** live Nuxt-build — handoff-referentie voor de programmeur.
