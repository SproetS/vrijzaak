# Bouwcontract voor ontwerp (samenvatting)

Bron: collega-repo **Nuxt + Directus 12 + PostgreSQL**  
Lokaal: `Vrijzaak/03 - Bouw/webshop`  
Remote: Gitea `git.helling.pro/Vrijzaak/Vrijzaak` (spiegel GitHub `Hellingajes/Vrijzaak`)

Dit document haalt uit de bouw-docs **alleen wat UX/vormgeving** raakt. Geen worker-internals, keys of migratienummers hier herhalen. Volledige contracten blijven in de webshop-`docs/`.

Gerelateerd in deze vault: [00-index.md](./00-index.md) · [00-tech-traject.md](./00-tech-traject.md) · [00-design-tokens.md](./00-design-tokens.md) · checkout [01](./01-winkelwagen.md)–[08](./08-componenten-en-staten.md)

---

## 1. Twee repo’s (blijven gescheiden)

| Repo | Rol |
|------|-----|
| **SproetS/vrijzaak** (deze map) | Ontwerpintentie: draadmodellen, IA, UX-copy, design-tokens-voorstellen |
| **helling Vrijzaak/Vrijzaak** | **SoT techniek:** routes, checkout, API, workers, `docs/*` contracten, code-tokens |

Team: ontwerper/UX · zakelijk leider/winkelier · programmeur.  
Ontwerp wijzigt de bouwrepo niet stilzwijgend. Routing/checkout/tech: bouw wint bij conflict.

---

## 2. Stack (feitelijk in bouw)

```
Koper / gast  →  Nuxt 4 (winkel + HTTP-API)
Beheer        →  Directus 12 (+ private commands)
Data          →  PostgreSQL
Workers       →  zelfde monorepo (Mollie, Resend, herstel)
Betalen       →  Mollie hosted (testmodus; iDEAL eerst)
Mail          →  Resend + centrale templates
```

- **Niet** SvelteKit als actieve storefront (eerdere aanname in deze vault is bijgesteld).
- Centrale verkoper = Vrijzaak; één checkout; makers/vrijplaatsen = deelnemers met beperkt portal.
- Bestellen staat in bouw **standaard dicht** tot echte policy/pilot.

Zie webshop: `docs/architecture.md`, `docs/commerce.md`.

---

## 3. Publieke routes (catalogus + kassa)

Vastgelegd in bouw (`docs/catalogue.md`, `docs/checkout.md`, identity):

| Route | Betekenis voor ontwerp |
|-------|-------------------------|
| `/collectie` | Listing; filters page/q/category/party |
| `/producten/:slug` | Productdetail; `?variant=<uuid>` serverkeuze |
| `/categorieen/:slug` | Categorie |
| `/kunstenaars/:slug` | Maker-profiel |
| `/vrijplaatsen/:slug` | Vrijplaats-profiel |
| `/mand` | Winkelmand |
| `/afrekenen` | Checkout |
| `/bestellingen/:id` | Privé orderstatus |
| `/account` (+ verifieren, wachtwoord, uitnodiging) | Account |
| `/deelnemer` | Maker/vrijplaats-portal (niet kassa-UI) |

**Ontwerp-afspraak:** draadmodellen gebruiken **huidige** bouwpaden tot de programmeur migreert.  
UI-labels: **NL + EN** (i18n); zaakmetaforen in [00-nomenclatuur-winkel.md](./00-nomenclatuur-winkel.md). Code/keys Engels.  
Navigatie-omgevingen (winkel / kassa / voet) — [00-navigatie-omgevingen.md](./00-navigatie-omgevingen.md).

---

## 4. Klantreis (invarianten die de UI moet respecteren)

Uit `docs/commerce.md` + checkout/payments, in mensentaal:

1. **Ontdekken** — gepubliceerde info, prijsbetekenis, indicatieve voorraad. Mand reserveert **niets**.
2. **Mand** — browser bewaart alleen **variant-ID + aantal**. Geen gezaghebbende prijzen/%/eigenaar uit de client.
3. **Quote** — server herberekent; quote heeft revisie/vervaltijd. Prijswijziging of tekort → **nieuw voorstel + expliciete bevestiging** (geen stille POST-retry).
4. **Afrekenen** — order + snapshots + voorraadreservering + betaalintentie atomair; daarna pas Mollie.
5. **Betalen** — hosted Mollie; **browser-return is geen betaalbewijs**. UI toont pending tot serverstatus.
6. **Bevestiging** — pas na gevalideerd **paid** (+ stock-effect): bevestigingsmail, fulfilment-signaal, etc.
7. **Nazorg** — gast via beperkt bewijs (niet “e-mail + ordernummer”); claim naar account is apart; refund ≠ automatische restock.

Statussen **niet vermengen** in copy/UI:

- Order: o.a. pending_payment → confirmed → …
- Payment-attempt: pending / paid / failed / canceled / expired
- Fulfilment en mail hebben eigen statussen

---

## 5. Gast, account, privacy (UX)

- **Gast checkout** is normaal; geen verplicht account.
- Gasttoegang = ordergebonden bewijs (cookie/link-flow), **niet** gedeeld Directus-user.
- Account: registratie → e-mailverificatie → login; CSRF en HttpOnly-sessie (bouw).
- Privépaden (`/mand`, `/afrekenen`, `/bestellingen/…`, account): **noindex**, geen lekken in markup.
- Koppelen gastorder ↔ account: bewijs + verified sessie; niet stilzwijgend op gelijke e-mail.

UI-copy mag dit soft uitleggen (“Je hoeft geen account”) zonder technische details.

---

## 6. Geld, btw, korting, verdeling (presentatie)

Uit checkout-policy (bouw; nu vooral **test**cijfers):

- Integer **centen**, EUR; afronding server-side, deterministisch.
- Prijzen in catalogus: revisie met incl./excl.-aanduiding + belastingcode — fiscale waarheid is **niet** “UI rekent na”.
- Klant-totaal moet aansluiten op payment-bedrag (één Mollie-charge).
- Aandelen (maker/vrijplaats/winkel) in **basispunten**, som 10 000; opgeslagen op orderregels; **oude 70/30-achtige vuistregels gelden niet**.
- Campagnes/korting: server; overlappende actieve campagnes op één variant geweigerd.
- Verzending/afhalen: uit policy (landen, tarief, eigen btw-code) — nog geen echte commerciële tarieven in productieconfig.

**Ontwerp:** sidebar blijft [07-rekensom.md](./07-rekensom.md): totaal **incl. btw**, optioneel btw-split en optionele verdeling-explainer. Bedragen altijd uit server-DTO, nooit “hardcoded demo” in componenten die productie pretenderen (`docs/design.md` verbiedt dummyprijzen/koopknoppen vóór keten).

---

## 7. Visueel contract in bouw (nu)

Uit `docs/design.md` + `shared/design/tokens.ts`:

| Token-rol | Huidige bouwwaarde |
|-----------|-------------------|
| paper | `#f5f2e9` |
| surface | `#fffdf7` |
| ink | `#202c27` |
| muted | `#58645d` |
| accent | `#245c43` |
| line | `#b7c2b5` |
| font | In code nu vaak **GAP Mono**; **ontwerp voorlopig GAP Code** (sync programmeur) |
| measure | `76rem` |

- Fonts self-hosted WOFF in `public/fonts/`; `font-display: swap`; geen externe font-CDN.
- Shell: `app/layouts/default.vue`; basis: `app/assets/css/main.css`.
- Mail deelt semantische tokens; in mail **geen** verplicht webfont (monospace-fallback).
- States eerst: laden, leeg, fout, n.v.t., form valid/invalid, busy, succes.
- a11y: semantiek, labels, focus, skiplink, contrast, ≥44px targets, mobiel.
- Collectielijst = tekstlinks; productdetail = gevalideerde beelden + variantkeuze uit contract.
- `npm run test:mobile` = Chromium/WebKit screenshots e.d. (geen fysiek device-bewijs).

**Font:** ontwerpbesluit **GAP Code (voorlopig)**. Bouw `tokens.ts` kan nog Mono tonen tot de programmeur gelijk trekt. Kleuren paper/ink/accent blijven bruikbaar startpunt — [00-design-tokens.md](./00-design-tokens.md).

---

## 8. Mails die de klant raakt (happy path)

| Moment | Ontwerpbetekenis |
|--------|------------------|
| Gast order-toegang | Link naar status **vóór** of rond betaling — **geen** “bedankt betaald”-toon |
| `orders.confirmation` | Echte bedankt/bevestiging **na** paid |
| Refundbericht | Apart van factuur; rustige copy |
| Identity (verify, reset, invite) | Accountflows, geen winkel-upsell |

Bevestigings-UI en -mail moeten **zelfde waarheid** (orderstatus van server), zie [06-bevestiging.md](./06-bevestiging.md).

---

## 9. Wat ontwerp wél / niet claimt t.o.v. bouw

**Wel afstemmen**

- Routes en nav-omgevingen  
- Mand = ID/aantal; totalen van server  
- Pending na Mollie-return  
- Lege/fout/busy states  
- Geen nep-voorraad of koop-CTA zonder backend  
- Token/typografie-richting (met open besluit Mono vs Zuid/Code)  
- Transparante verdeling als optionele UI, gevoed door server-aandelen  

**Niet nabootsen in Markdown alsof af**

- Echte btw/verzend/commerciële policy (nog open in bouw)  
- Carrier-API, live Mollie, live mail  
- Directus-licentie/rechten-acceptatie  
- Partneruitbetaling / MoneyStack-uitgifte  

---

## 10. Bronindex (webshop-docs)

| Doc | Voor ontwerp |
|-----|----------------|
| `docs/architecture.md` | Componenten, grenzen, open pilot |
| `docs/commerce.md` | Klantreis, statusscheiding |
| `docs/catalogue.md` | URL’s, publicatie, media |
| `docs/checkout.md` | Mand, quote, submit, gast |
| `docs/payments.md` | Mollie, return ≠ paid |
| `docs/identity.md` | Accountroutes, gastclaim |
| `docs/design.md` | Tokens, a11y, mail UI |
| `docs/email.md` | Welke mails wanneer |
| `docs/partners.md` | Deelnemerportal (rand) |
| `docs/workspace/README.md` | Git Gitea-first |

---

## 11. Open ontwerpvragen na lezen bouw

1. Programmeur: `tokens.ts` font → GAP Code (ontwerp voorlopig).  
2. `/mand` label “Winkelmand” is OK (bouw); geen `/winkelwagen`-route.  
3. Verdeling-explainer: tonen we basispunten-snapshot of alleen “eerlijk beeld”-copy tot policy live is?  
4. Kassa-header: past die op huidige `default.vue`-shell of aparte checkout-layout in Nuxt?  
5. Welke checkout-stappen (3-step vs single page) sluiten aan op bestaande Nuxt-pagina’s — audit in bouw-UI later.

Laatst bijgewerkt: 2026-11-17 (sessie verwerking bouwdocs → ontwerpvault).
