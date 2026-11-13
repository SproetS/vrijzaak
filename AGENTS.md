# AGENTS.md — Vrijzaak ontwerpvault

Instructies voor AI-agents (en mensen) die in **deze map** werken.

## Project in één zin
Markdown-ontwerpverslag en draadmodellen voor webwinkel **Vrijzaak** (https://vrijzaak.nl): UX, vertrouwenwekkende UI-richting, fijne kassa; technisch pad **Svelte(Kit) + CSS tokens + Directus + Mollie**.

## Werkmap
Dit is de Obsidian-vault:

`…/Vrijzaak/01 - Werkbestanden/Vrijzaak draadmodel/`

Niet verwarren met latere code-repos. Hier hoort **geen** applicatiecode tenzij de gebruiker dat expliciet vraagt.

## Bron van waarheid
1. Lees eerst [[00-index]] en [[00-projectbrief]].
2. Navigatie: [[00-navigatie-omgevingen]] (winkel ≠ kassa ≠ voet).
3. Tokens: [[00-design-tokens]] (GAP Zuid VG, GAP Code; greyscale + zachte accenten).
4. Tech-rapportage: [[00-tech-traject-svelte-directus]].
5. Checkout: `01`–`08` markdown draadmodellen.
6. Kaart van alles: [[00-projectmap]].

## Doel van agent-werk hier
- Verbeteren en uitbreiden van **Markdown** (wireframes, IA, productmodel, copy).
- Consistent houden met brief: B2C, fysiek, vrijplaatsen/makers, prijzen **incl. btw**, opbrengst split, gast + account, Mollie/iDEAL.
- Obsidian-vriendelijk: bruikbare `[[wikilinks]]`, duidelijke koppen, geen onnodige bloat.

## Niet doen (tenzij gevraagd)
- Productie-Svelte/Directus-repo’s aanmaken of deployen.
- Secrets, API-keys, `.env` in deze vault.
- Grote binary dumps (raw foto’s, video) — verwijs naar contentmap of cloud.
- Destructief wissen van bestaande notes zonder bevestiging.
- Nep-schaarste, agressieve upsell-copy (past niet bij Vrijzaak).

## Stijl Markdown
- Geen emoji/iconen in notes (projectvoorkeur).
- Wel tabellen, ASCII-wireframes, genummerde stappen.
- Nederlandse UI-copy in draadmodellen (“Kassa”, “Winkelmand”, …).
- Engelse technische termen waar gangbaar (Directus, webhook, SvelteKit) zijn ok.

## Design constraints
- Fonts: **GAP Zuid VG** (primair), **GAP Code** (mono/data) — paden in design-tokens; licentie respecteren bij latere web-embed.
- Kleur: greyscale basis; accenten zacht en helder, spaarzaam (CTA/focus).
- Checkout: **kassa-navigatie** zonder Collectie/Makers-afleiding.

## Als je nieuwe notes toevoegt
1. Logische prefix (`00-` meta, `01+` flows, later `09+` winkel-IA).
2. Link vanuit [[00-index]] en zo nodig [[00-projectmap]].
3. Zet onderaan backlinks naar index / relevante parents.
4. Schrijf “Open punten” expliciet i.p.v. aannames als feiten.

## Rapportage winkelier-collega
Houd [[00-tech-traject-svelte-directus]] en de rapportage-alinea actueel als keuzes wijzigen. Focus op: wat de klant voelt, wat de winkelier beheert (Directus), wat tech bouwt.

## Session hygiene
- Bij afronden van een sessie: korte update in index of aparte `YYYY-MM-DD-*.md` sessienote + link in [[00-index]] indien relevant.
- Geen geheimen in sessienotes.

## Buiten scope van déze vault
Operatie Stofnest shop, andere VPS-projecten — alleen noemen als de gebruiker dat koppelt.
