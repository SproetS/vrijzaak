# Projectbrief Vrijzaak

## Wat is dit?
Verkenning / ontwerpverslag in **Markdown** (Obsidian of gelijk) voor webwinkel **Vrijzaak**.

| | |
|--|--|
| **Werknaam** | Vrijzaak |
| **URL** | https://vrijzaak.nl |
| **Map** | `Vrijzaak draadmodel` (deze vault) |

## Opdracht en rollen
- **Jij / UX-design:** super lekkere UX, vertrouwenwekkende vormgeving, fijne kassa-ervaring.
- **Collega (winkelier):** producten, klanten, operationele winkel — jij rapporteert richting hem.
- **Product van déze verkenning:** geen productiecode per se, maar een **ontwerpverslag + draadmodellen** dat de winkel vangt én een helder traject naar bouw.

## Technisch traject (achterhoofd → rapportage)
Richting die we aanhouden:

```
Vormgeving (Markdown / tokens / wireframes)
        ↓
Svelte(Kit) frontend  +  CSS (design tokens, GAP-fonts)
        ↓
Directus (catalogus, content, orders-config, media)
        ↓
Mollie (iDEAL e.d.) voor betalen
```

- **Svelte/SvelteKit + CSS:** UI, checkout-flow, vertrouwen, performance.
- **Directus:** winkelier-vriendelijk beheer (producten, makers, vrijplaatsen, content) — past bij “collega is de winkelier”.
- **Niet nu:** volledige implementatie; wél keuzes documenteren zodat bouw geen verrassing is.

Zie ook [[00-tech-traject-svelte-directus]].

## Merk & product
- Platform voor **vrijplaatsen** (Ruigoord, ADM, OT301, …) en makers.
- Fysieke producten: T-shirts, boekjes, schilderijen, kunstwerken.
- B2C, sfeer: anti-commercieel / eerlijk, wél betrouwbare kassa.
- Opbrengstverdeling: maker + vrijplaats + winkel (+ btw).

## Designrichting (voorlopig)
- **Fonts:** GAP Zuid VG (tekst/UI), GAP Code (accent/mono/tech) — lokaal op deze Mac, zie [[00-design-tokens]].
- **Kleur:** greyscale basis + zachte, heldere accenten van primaire kleuren (niet schreeuwerig).
- **Checkout:** gescheiden navigatie winkel vs kassa — [[00-navigatie-omgevingen]].

## Hoe deze map te openen
1. Obsidian → *Open folder as vault* → deze map `Vrijzaak draadmodel`.
2. Start bij [[00-index]].
3. Alles is plain Markdown: ook te lezen in VS Code, Git, Warp, etc.

Zie ook [[00-projectmap]] en [[AGENTS]].
