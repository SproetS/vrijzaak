# Projectmap Vrijzaak

Overzicht van mappen en twee repo’s. Plain Markdown; Obsidian optioneel.

## Werknaam en URL

| | |
|--|--|
| Werknaam | **Vrijzaak** |
| Productie-URL (beoogd) | https://vrijzaak.nl |
| Fase nu | Ontwerp in Markdown; bouwrepo bestaat parallel |

## Schijf (deze Mac)

```
Vrijzaak/
├── 01 - Werkbestanden/Vrijzaak draadmodel/   ← ontwerp GitHub SproetS/vrijzaak
│   ├── AGENTS.md
│   ├── README.md
│   ├── docs/           ← Markdown (start: 00-index.md)
│   └── frontend/       ← tokens/CSS-proeven, logos, svg (geen Nuxt-app)
└── 03 - Bouw/webshop/                      ← clone helling Nuxt monorepo
    ├── docs/           ← domeincontracten (bron voor 00-bouwcontract-ontwerp)
    ├── app/ shared/ server/ directus/ …
```

## Docs in deze ontwerprepo

### Start

- [README.md](../README.md)
- [AGENTS.md](../AGENTS.md)
- [00-index.md](./00-index.md)
- [00-projectbrief.md](./00-projectbrief.md)
- [00-projectbeschrijving-en-stappenplan.md](./00-projectbeschrijving-en-stappenplan.md)
- [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md)
- [00-sessie-2026-11-17-bouwdocs-in-ontwerp.md](./00-sessie-2026-11-17-bouwdocs-in-ontwerp.md)

### Ontwerpkeuzes

- [00-navigatie-omgevingen.md](./00-navigatie-omgevingen.md)
- [00-design-tokens.md](./00-design-tokens.md)
- [00-tech-traject.md](./00-tech-traject.md)

### Checkout-draadmodellen

- [01-winkelwagen.md](./01-winkelwagen.md) … [08-componenten-en-staten.md](./08-componenten-en-staten.md)

### Gepland

- `09-sitemap-ia.md` — o.a. `/collectie`, `/producten/:slug`, …
- `10-productmodel.md` — Directus/catalogue-velden voor UX
- Home / listing / productdetail / maker / vrijplaats
- Account + footer

## Bouw (niet in deze vault als app-code)

```
vrijzaak.nl (Nuxt 4 + tokens + GAP self-hosted)
    ↔  Directus 12 + PostgreSQL
    ↔  Mollie, Resend workers
```

Remote bouw: Gitea `git.helling.pro/Vrijzaak/Vrijzaak` (spiegel GitHub Hellingajes/Vrijzaak).  
Push alleen naar Gitea-origin volgens hun workspace-doc.

## Fonts (lokaal)

- `/Users/sjoerd/Desktop/GAP Fonts/…`
- Zie [00-design-tokens.md](./00-design-tokens.md)

## Rollen

| Rol | Focus |
|-----|--------|
| UX / vormgeving | Flows, tokens, kassa-ervaring, deze repo |
| Winkelier / bouw-collega | Producten, Nuxt/Directus, Gitea |
| Agents | Markdown volgens AGENTS; geen secrets/deploy hier |

## Wel / niet in ontwerprepo

**Wel:** Markdown, ASCII-wireframes, besluiten, open vragen, lichte png/svg.  
**Niet:** `node_modules`, `.env`, dumps, grote raw foto’s, hele bouwmonorepo-mirror.

## Rapportage-snelle start voor collega

1. [00-projectbrief.md](./00-projectbrief.md)  
2. [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md)  
3. [02-checkout-overzicht.md](./02-checkout-overzicht.md) + [06-bevestiging.md](./06-bevestiging.md)  
4. [00-navigatie-omgevingen.md](./00-navigatie-omgevingen.md)  
