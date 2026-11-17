# Projectbrief Vrijzaak

## Wat is dit?

Ontwerpverslag in **Markdown** voor webwinkel **Vrijzaak**. Geen Obsidian-vereiste: bestanden zijn gewoon te openen in GitHub of een editor.

| | |
|--|--|
| **Werknaam** | Vrijzaak |
| **URL** | https://vrijzaak.nl |
| **Ontwerp** | deze repo (`SproetS/vrijzaak`) |
| **Bouw** | collega monorepo Nuxt/Directus (helling) |

## Opdracht en rollen (met z’n drieën)

| Rol | Wie / focus |
|-----|-------------|
| **Ontwerper / UX** | Jij — flows, vormgeving, kassa-ervaring; vastleggen in deze repo |
| **Zakelijk leider / winkelier** | Producten, klanten, beleid, operationeel |
| **Programmeur** | Nuxt/Directus-monorepo (helling), implementatie |

- **Source of truth techniek** (routes, checkout, API, code-tokens): **bouwrepo / programmeur**.  
- **Source of truth ontwerpintentie** (wireframes, copy, GAP Code voorlopig): **deze repo**.  
- Product van deze fase: ontwerpverslag + draadmodellen, geen app-code hier.

## Technisch traject

```
Vormgeving (Markdown / tokens / wireframes)   ← deze repo
        ↓ afstemming
Nuxt 4 storefront + shared design tokens      ← bouwrepo
        ↓
Directus 12 + PostgreSQL
        ↓
Mollie (iDEAL …) + Resend (mail)
```

Details: [00-tech-traject.md](./00-tech-traject.md) · [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md).

## Merk en product

- Platform voor **vrijplaatsen** (Ruigoord, ADM, OT301, …) en makers.
- Fysieke producten: T-shirts, boekjes, schilderijen, kunstwerken.
- B2C, anti-commercieel eerlijk, wél betrouwbare kassa.
- Opbrengstverdeling: maker + vrijplaats + winkel (+ btw), server-side basispunten.

## Winkelnamen en talen

- **UI:** NL default + **EN-toggle** (i18n). Zaak-metaforen o.a. Etalage, Magazijn, Loods, Kassa, Winkelmand.  
- **Code / keys:** Engels (`nav.warehouse`, `checkout`, …).  
- **URL’s:** huidige bouwpaden blijven tot de programmeur migreert (geen hernoem vanuit ontwerp).  

Zie [00-nomenclatuur-winkel.md](./00-nomenclatuur-winkel.md).

## Designrichting (voorlopig)

- **Font (voorlopig):** **GAP Code** — [00-design-tokens.md](./00-design-tokens.md).
- **Bouwcode nu:** kan nog GAP Mono in `tokens.ts` hebben; sync via programmeur. Kleuren: paper/ink/accent-groen als start.
- **Checkout-nav:** winkel vs kassa vs voet — [00-navigatie-omgevingen.md](./00-navigatie-omgevingen.md).

## Hoe te lezen

1. [00-index.md](./00-index.md)  
2. [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md) als je met de code-collega praat  
3. Checkout 01–08 voor kassa-UX  

Plan: [00-projectbeschrijving-en-stappenplan.md](./00-projectbeschrijving-en-stappenplan.md).
