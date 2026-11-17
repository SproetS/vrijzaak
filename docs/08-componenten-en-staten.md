# 08 — Componenten en staten

Twee lagen:

1. **Bouw (SoT implementatie)** — wat er in de helling-repo staat  
2. **Ontwerp-namen** — gewenste UX-blokken (mogen later SFC’s worden)

Volledige inventaris: [00-inventaris-bouw-ui.md](./00-inventaris-bouw-ui.md).  
**Atomic/moleculen-lijst:** [00-ui-moleculen.md](./00-ui-moleculen.md).

---

## A. Bouw — bestaande Vue / shell

| Bouw | Bestand | Gebruik in winkel |
|------|---------|-------------------|
| **default layout** | `app/layouts/default.vue` | Skip-link, wordmark, tagline, nav (Collectie, Winkelmand, Account, Over), footer |
| **CatalogueList** | `app/components/CatalogueList.vue` | `/collectie` (+ listing-patronen) |
| **PartyProfile** | `app/components/PartyProfile.vue` | `/kunstenaars/:slug`, `/vrijplaatsen/:slug` |
| **OrderFulfilment** | `app/components/OrderFulfilment.vue` | `/bestellingen/:id` |
| **useCart** | `app/composables/useCart.ts` | Mandregels variant-ID + aantal |
| **usePublicSeo** | `app/composables/usePublicSeo.ts` | Publieke meta |
| **designTokens** | `shared/design/tokens.ts` | paper/surface/ink/… ; font (nog Mono in code) |
| **brand** | `shared/brand.ts` | Shopnaam |
| **main.css** | `app/assets/css/main.css` | o.a. `.button`, form layout |

Checkout/mand/account zijn grotendeels **pagina-inline** (nog geen aparte SFC per blok).

---

## B. Mapping ontwerpblok ↔ bouw (kassa)

| Ontwerpnaam (wireframe) | Bouw nu | Notitie |
|-------------------------|---------|---------|
| **NavWinkel** | `default` header-nav | Bouw: Collectie, Winkelmand, Account, Over — nog geen Makers/Vrijplaatsen-top |
| **NavKassa** | *(nog niet)* | Ontwerp-wens; `/afrekenen` gebruikt nu ook `default` |
| **NavVoet** | `default` footer | Bouw minimaal (“in voorbereiding”); ontwerp wil Contact/AV/Privacy |
| **Mandregel** | `/mand` + `useCart` + `/api/cart` | Aantal 1–100, verwijderen, productlink |
| **LegeMand** | `/mand` | Link → `/collectie` |
| **OrderSummary / QuoteBlok** | `/afrekenen` na “Actueel voorstel” | Server-quote: regels, shipping, btw, totaal, expiresAt |
| **ContactAdresFieldset** | `/afrekenen` fieldset | e-mail, naam, straat, huisnr, postcode, plaats, land |
| **OntvangstKeuze** | `/afrekenen` select delivery | `ship` / `pickup` uit `/api/checkout/options` |
| **RecoverNotice** | `/afrekenen` | Onzekere eerdere poging herstellen |
| **TermsCheckbox** | `/afrekenen` | Akkoord prijsvoorstel + bestelopdracht |
| **CheckoutSubmit** | `/afrekenen` submit | Incl. replay dezelfde command |
| **StepHeader** (1/2/3) | *(niet in bouw)* | Bouw = **één pagina** `/afrekenen`; 3 stappen = ontwerpvoorstel |
| **TrustLine Mollie** | deels copy/flow | Hosted Mollie na betalingstraject; return ≠ paid |
| **SplitExplainer** | *(niet in bouw-UI)* | Ontwerp; data kan uit aandeel-snapshots |
| **OrderstatusPaneel** | `/bestellingen/:id` | Serverstatus |
| **OrderFulfilment** | component | Zending/fulfilment-zicht |
| **Price** | `formatEuro` + servercenten | Geen client-prijs als waarheid |

---

## C. Mapping winkel (buiten pure kassa-docs 01–07)

| Ontwerp | Bouw |
|---------|------|
| Collectielijst | **CatalogueList** |
| Maker-/vrijplaatspagina | **PartyProfile** |
| Productdetail + variant + “In winkelmand” | `producten/[slug].vue` |
| Home hero / over | `index.vue` secties |
| Account poort | `account/index.vue` + `[action].vue` |
| Deelnemerportal | `deelnemer/*` |

---

## D. Globale staten (bouw + ontwerp)

| Staat | Waar | Gedrag |
|-------|------|--------|
| Lege mand | `/mand` | CTA `/collectie` |
| Laden / busy | mand, afrekenen | Geen dubbele submit; pending recover |
| Ongeldig aantal | `/mand` | 1–100; alert |
| Quote verlopen / 409 | `/afrekenen` | Nieuw voorstel |
| Checkout uit | `/afrekenen` | “Nog niet beschikbaar”, mand blijft |
| Mollie pending | orderstatus | Geen “betaald” tot server |
| Betaald | `/bestellingen/:id` + mail | Happy path |
| Voorraadtekort | submit | Fout; geen halve order als succes |
| Lege collectie | **CatalogueList** | Eerlijke lege staat |

---

## E. Breakpoints / a11y

- Mobiel: stacked, sticky CTA-richting, ≥44px (bouw design.md)
- Desktop: summary/quote rechts of onder formulier (bouw nu vooral gestapeld in één section)
- Skip-link, labels, `role="alert"` / `status` waar bouw dat al doet

---

## F. Werkafspraak

- **Nieuwe SFC-namen in code** = programmeur / bouwrepo.  
- Ontwerp mag bloknamen in wireframes houden, met regel “bouw: …” ernaast.  
- Bij conflict over routes of checkout-velden: **bouw wint** tot er een issue/PR is.

Zie [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md).

---
Vrijzaak · https://vrijzaak.nl · [00-index.md](./00-index.md)
