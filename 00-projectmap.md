# Projectmap Vrijzaak

Overzicht van mappen, vault en beoogde bouwstructuur. Voor mensen én agents.

## Werknaam en URL

| | |
|--|--|
| Werknaam | **Vrijzaak** |
| Productie-URL (beoogd) | https://vrijzaak.nl |
| Fase nu | Ontwerpverkenning (Markdown / draadmodel), nog geen live shop |

## Schijf (deze Mac)

```
Documents/sproets/tycho/Vrijzaak/
├── 01 - Werkbestanden/
│   ├── Vrijzaak-ontwerp1.ai          ← visueel ontwerp (Illustrator)
│   └── Vrijzaak draadmodel/          ← DEZE Obsidian-vault (UX + docs)
│       ├── AGENTS.md
│       ├── README.md
│       ├── 00-*.md                   ← brief, index, tokens, tech, nav, projectmap
│       ├── 01-…08-*.md               ← checkout-draadmodellen
│       ├── assets/                   ← screenshots, exports (leeg ok)
│       └── .obsidian/                ← vault-config
├── (latere mappen naar wens)
│   ├── 02 - Content/                 ← teksten, productfoto’s van winkelier
│   └── 03 - Bouw/                    ← git repos Svelte + Directus (later)
```

Pas `02` / `03` aan als jullie andere mapnamen gebruiken; het idee is: **ontwerpvault scheiden van code en ruwe content**.

## Deze vault — inhoudelijke kaart

### Start
- [[README]] — openen van de vault
- [[AGENTS]] — regels voor AI-agents die hier werken
- [[00-index]] — hub
- [[00-projectbrief]] — opdracht en rollen
- [[00-projectmap]] — dit document

### Ontwerpkeuzes
- [[00-navigatie-omgevingen]] — winkel / kassa / voet
- [[00-design-tokens]] — GAP-fonts, greyscale, accenten
- [[00-tech-traject-svelte-directus]] — Svelte + CSS + Directus + Mollie

### Checkout-draadmodellen
- [[01-winkelwagen]] … [[08-componenten-en-staten]]

### Gepland (nog niet alles geschreven)
- [[09-sitemap-ia]] — site-structuur winkel
- [[10-productmodel]] — Directus-velden
- Home / listing / productdetail / maker / vrijplaats (draadmodellen)
- Account + footer-pagina’s

## Beoogde bouw (later, niet in deze vault als code)

```
vrijzaak.nl (SvelteKit + CSS tokens + GAP self-hosted)
    ↔  Directus (catalogus, makers, vrijplaatsen, content)
    ↔  Mollie (iDEAL, …)
```

Exacte repo-paden op VPS of lokaal: vastleggen zodra bouw start (verwijs dan hierheen).

## Fonts (lokaal)

- `/Users/sjoerd/Desktop/GAP Fonts/OTF/Gap Zuid VG/`
- `/Users/sjoerd/Desktop/GAP Fonts/OTF/GAP Code/`
- Webfonts: `/Users/sjoerd/Desktop/GAP Fonts/Web/`

Zie [[00-design-tokens]].

## Rollen

| Rol | Focus |
|-----|--------|
| UX / vormgeving (jij) | Flows, tokens, kassa-ervaring, vault |
| Winkelier (collega) | Producten, klanten, operationeel; leest brief + tech-traject |
| Tech (later) | SvelteKit, Directus, Mollie, deploy |

## Wat hoort wél / niet in deze map

**Wel:** Markdown-ontwerp, ASCII-wireframes, besluiten, open vragen, lichte assets (png/svg exports).  
**Niet:** `node_modules`, `.env`, database dumps, grote raw foto-libraries (liever `02 - Content` of cloud).

## Rapportage-snelle start voor collega

1. [[00-projectbrief]]  
2. [[00-tech-traject-svelte-directus]] (alinea onderaan)  
3. [[02-checkout-overzicht]] + [[06-bevestiging]]  
4. [[00-navigatie-omgevingen]]
