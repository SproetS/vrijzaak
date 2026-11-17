# Tech-traject: ontwerp → Nuxt + Directus + Mollie

## Waarom dit opschrijven?

Collega = **winkelier / bouw-eigenaar** (producten, klanten, monorepo).  
Wij leveren UX/vormgeving/kassa-ervaring en houden de vault gelijk met wat er **echt** gebouwd wordt.

Eerdere werknaam in deze vault (“Svelte + Directus”) is **bijgesteld**: de actieve codebase is **Nuxt 4 + Directus 12 + PostgreSQL** (modulaire monoliet). Zie [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md).

Bestandsalias: oude links naar `00-tech-traject-svelte-directus.md` mogen hierheen wijzen totdat die file een stub is.

---

## Doelbeeld (bouw bestaat al deels)

```
┌─────────────────────────────────────────────────────────┐
│  vrijzaak.nl  (Nuxt 4 — app/, server/)                  │
│  - Collectie, product, makers, vrijplaatsen             │
│  - /mand + /afrekenen (gescheiden kassa-UX gewenst)     │
│  - Design: shared/design/tokens + GAP (zie tokens-doc)  │
└─────────────────────┬───────────────────────────────────┘
                      │ private commands / API
┌─────────────────────▼───────────────────────────────────┐
│  Directus 12 + PostgreSQL                               │
│  - Catalogus, partijen, media                           │
│  - Identity; private akws_internal (orders, stock, …)   │
└─────────────────────┬───────────────────────────────────┘
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
   Mollie (iDEAL, …)            Resend (mail)
   workers + webhooks           centrale templates
```

---

## Verantwoordelijkheden

| Laag | Wie | Wat |
|------|-----|-----|
| Markdown vault (deze repo) | UX | flows, IA, tokens-voorstellen, copy |
| Nuxt UI | front / collega-stack | pixels, a11y, kassa-UX op echte routes |
| Directus | winkelier + tech | catalogus, content, rollen (na licentie-acceptatie) |
| Mollie / Resend | tech | geld en mail duurzaam, idempotent |

---

## Wat Directus winkelier-vriendelijk maakt

- Product als draft → publiceren met checks (variant, prijsrevisie, beelden, attributies)
- Makers/vrijplaatsen als publieke profielen (geen bankgegevens in publieke velden)
- Prijs = immutable revisies (nieuw tarief = nieuwe revisie)
- Geen deploy voor tekst/productwijziging
- Rollen strikt; storefront is geen admin-proxy

---

## Wat draadmodellen voorbereiden t.o.v. bouw

| Vault | Bouwcontract |
|-------|----------------|
| Checkout-stappen + summary | quote/submit, server-totalen |
| Rekensom incl. btw + split | policy + line snapshots + basispunten |
| Verzendklassen | policy ship/pickup (tarieven nog commercieel open) |
| Mollie pending/fail/success | return ≠ paid; confirmation na effect |
| Nav winkel/kassa/voet | layouts boven `/collectie`…`/afrekenen` |
| Product/maker/vrijplaats IA | catalogue routes |

---

## Bewust open (bouw + business)

- Echte btw-, verzend-, aandeel- en kortingspolicy (`mode=approved`)
- Directus-licentie en native rechtenproeven
- Live providers, VPS, monitoring
- Font: ontwerp **GAP Code** voorlopig; code mogelijk nog Mono tot sync
- Of kassa een eigen Nuxt-layout krijgt t.o.v. `default.vue`

---

## Rapportage aan winkelier-collega (één alinea)

Vrijzaak is een rustige B2C-winkel voor vrijplaatsen en makers: centrale checkout, prijzen en totalen van de server, iDEAL via Mollie, bevestiging pas na échte betaalregistratie. Visueel werken we aan GAP/ greyscale met zachte accenten; in code staan nu GAP Mono en gedeelde tokens. Beheer via Directus; ontwerpvoortgang in GitHub `SproetS/vrijzaak`, code op Gitea helling. Ontwerp en bouwrepo blijven bewust gescheiden.
