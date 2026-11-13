# Tech-traject: Svelte + CSS → Directus (rapportage)

## Waarom dit opschrijven?
Collega = **winkelier** (producten, klanten). Wij leveren UX/vormgeving/kassa-ervaring en een spoor dat bouwbaar is zonder Drupal-achtige zwaarte.

## Doelbeeld (fase bouw, niet nu coderen)

```
┌─────────────────────────────────────────────────────────┐
│  vrijzaak.nl  (SvelteKit)                               │
│  - Winkel browse (Collectie, makers, vrijplaatsen)      │
│  - Winkelwagen + Kassa (gescheiden nav)                 │
│  - Design tokens + GAP Zuid VG / GAP Code               │
└─────────────────────┬───────────────────────────────────┘
                      │ API (REST/GraphQL)
┌─────────────────────▼───────────────────────────────────┐
│  Directus                                               │
│  - Producten, varianten, media                          │
│  - Makers, vrijplaatsen, verdelings-%                   │
│  - Btw-tarief, verzendklasse                            │
│  - Content: Over ons, Contact, AV                       │
│  - Orders / klantgegevens (of orders in app-DB — keuze) │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│  Mollie (iDEAL …)                                       │
│  - Één betaling van klanttotaal                         │
│  - Webhook → order betaald                              │
└─────────────────────────────────────────────────────────┘
```

## Verantwoordelijkheden

| Laag | Wie denkt mee | Wat |
|------|----------------|-----|
| Markdown vault | UX nu | flows, IA, tokens, copy |
| Svelte + CSS | front | pixels, a11y, kassa-UX |
| Directus | winkelier + tech | catalogus, content, rollen |
| Mollie | tech | geld veilig afhandelen |

## Wat Directus winkelier-vriendelijk maakt
- Product aanmaken met prijs **incl. btw**, tarief, foto’s
- Koppeling maker + vrijplaats
- Geen deploy nodig voor tekst/productwijziging
- Rollen: winkelier vs admin

## Wat we in draadmodellen al voorbereiden
- Checkout-stappen en rekensom → orderregels + totalen
- Verzendklassen → velden op product
- Opbrengst split → velden maker/vrijplaats/shop %
- Nav-omgevingen → layout components in Svelte

## Bewust open keuzes (later met tech)
- Orders volledig in Directus vs. app-database + Directus catalogus only
- Multi-currency: nee, start EUR
- Voorraad: soft/hard
- Image pipeline (Directus assets)

## Rapportage aan winkelier-collega (één alinea)
Vrijzaak wordt ontworpen als rustige B2C-winkel voor vrijplaatsen en makers, met prijzen incl. btw en een eerlijke verdeling maker/vrijplaats/winkel. De kassa is een aparte, afleidingsarme omgeving (Mollie/iDEAL). Visueel: GAP-fonts, greyscale met zachte accenten. Technisch pad: Svelte-frontend + Directus-beheer zodat jij producten en content kunt beheren zonder door de frontend te hoeven.
