# frontend/ — ontwerp-assets (geen Nuxt-app)

Deze map hoort bij de **ontwerprepo** (`SproetS/vrijzaak`).  
Hier lever je tokens, logo’s, SVG en mockup-exports aan voor UX en voor de **programmeur**.

De **webshop-app** staat **niet** hier. Die is de collega-monorepo:

| | |
|--|--|
| Stack | **Nuxt 4** + Directus 12 + PostgreSQL + Mollie |
| Remote | Gitea `Vrijzaak/Vrijzaak` (helling) |
| Tokens in code | `shared/design/tokens.ts` → CSS `--akws-*` |
| Fonts in code | `public/fonts/` (self-host) |
| Shell / CSS | `app/layouts/default.vue`, `app/assets/css/main.css` |

**Source of truth techniek:** bouwrepo.  
**Source of truth ontwerpintentie:** `docs/` + exports in deze map.

Zie [docs/00-design-tokens.md](../docs/00-design-tokens.md), [docs/00-bouwcontract-ontwerp.md](../docs/00-bouwcontract-ontwerp.md), [docs/00-inventaris-bouw-ui.md](../docs/00-inventaris-bouw-ui.md).

## Mappen

| Map | Inhoud |
|-----|--------|
| `css/` | `tokens.css` + `type.css` (basislijn 16/20, h1–h6); **niet** de live Nuxt-build |
| `fonts/` | Lokale webfont-proeven; **gitignored** t.o.v. bulk — licentie vóór delen/commit |
| `logos/` | Merklogo (SVG/PNG) voor handoff |
| `svg/` | UX-iconen en overige vectoren |
| `assets/` | Screenshots / Illustrator-exports (PNG/WebP) van schermen |
| `src/` | **Geen app-source.** Optionele notities of proef-snippets; Nuxt-code = helling |

## Handoff naar programmeur

1. Waarden en keuzes in **`docs/00-design-tokens.md`** (GAP Code voorlopig, kleuren, logo-regels).  
2. Bestanden hier: `logos/logo.svg`, eventueel `css/tokens.css`, schermexports in `assets/`.  
3. Programmeur mapt naar bouw: `tokens.ts`, `public/fonts/`, `public/` of `app/assets/` — via issue/PR op **bouwrepo**, niet door hier een Nuxt-app te starten.  
4. Routes/componenten: blijf namen gebruiken uit de inventaris (`/mand`, QuoteBlok, …).

## Font (kort)

- Ontwerp **voorlopig: GAP Code** (UI).  
- Bouwcode kan nog **GAP Mono** tonen tot sync.  
- GAP Zuid VG: optioneel later / Obsidian-leesfont — niet stil als storefront-standaard claimen.

## Niet doen

- Geen `node_modules`, geen Nuxt/Directus-clone in deze map.  
- Geen secrets.  
- Geen dummyprijzen in “productie-achtige” CSS-demo’s alsof de shop live is.
