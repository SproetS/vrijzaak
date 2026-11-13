# Design tokens (voorlopig) — Vrijzaak

Werknaam / site: **Vrijzaak** · https://vrijzaak.nl

Dit zijn **ontwerpafspraken in Markdown**, nog geen gebouwde CSS. Bij implementatie mappen naar CSS variables / Svelte theme.

## Typografie

| Rol | Familie | Gebruik |
|-----|---------|---------|
| Primair (UI, lopende tekst, navigatie) | **GAP Zuid VG** | body, knoppen, menu, producttitels |
| Secundair / mono / data | **GAP Code** | prijzen?, labels, ordernummers, technische accenten |

### Beschikbaar op deze Mac
Bronmap: `/Users/sjoerd/Desktop/GAP Fonts/`

**GAP Zuid VG (OTF):** Regular, Italic, Bold, Bold Italic  
`…/OTF/Gap Zuid VG/`

**GAP Code (OTF):** Regular, Italic, Bold, Bold Italic  
`…/OTF/GAP Code/`

Ook **Web**-varianten onder `…/GAP Fonts/Web/` (voor latere Svelte-build).

### Schaal (voorstel, nog open)

```
--font-sans: "GAP Zuid VG", system-ui, sans-serif;
--font-mono: "GAP Code", ui-monospace, monospace;

--text-xs / sm / base / lg / xl / 2xl
```

- Koppen: Zuid VG Bold
- Body: Zuid VG Regular
- Prijzen / ordernr: Code Regular of Bold (keuze in UI-kit vastleggen)

## Kleur (voorlopig)

**Basis: greyscale** — rust, anti-schreeuw, past vrijplaats-sfeer.

```
--gray-0     bijna wit (pagina-achtergrond)
--gray-50    zachte vlakken
--gray-100   randen licht
--gray-300   randen / dividers
--gray-500   secondary tekst
--gray-800   primary tekst
--gray-900   bijna zwart (logo/tekst strong)
--white / --black
```

**Accenten:** zachte, heldere tinten van **primaire kleuren** (rood / geel / blauw — exacte hex later prikken uit ontwerp of vrijplaats-identiteiten).

```
--accent-soft-red
--accent-soft-yellow
--accent-soft-blue
```

Gebruik accent spaarzaam:
- primaire CTA (één duidelijke actie)
- focus-ringen / links hover
- optioneel: vrijplaats- of maker-tag

**Niet:** regenboog-UI of harde neon; wel warmte en leesbaarheid.

### Semantisch

```
--bg-primary / --bg-secondary
--text-primary / --text-secondary
--border
--cta-bg / --cta-text
--danger / --success (Mollie fail/success — mild, niet alarmistisch)
```

## Ruimte & radius

```
--space-1 … --space-8
--radius-sm / md / lg
--shadow-soft (optioneel, subtiel — vertrouwen zonder “webshop-gloss”)
```

## Toon in UI

- Veel witruimte / gray-0
- Dunne gray randen i.p.v. zware shadows
- Kassa: nóg rustiger (minder nav, meer focus op totalen en CTA)
- Vertrouwen: heldere totalen, GAP Code voor bedragen, rustige Mollie-stap

## Koppeling bouw

Later in Svelte:

```css
:root {
  /* tokens hier */
}
```

Fonts laden via `@font-face` uit self-hosted bestanden (licentie respecteren; niet zomaar publiek CDN zonder afspraak).
