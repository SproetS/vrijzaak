# Inventaris UI — bron = bouwrepo (collega)

**Bron van waarheid** voor routing, checkout en technische UI:  
Gitea `Vrijzaak/Vrijzaak` / lokaal `03 - Bouw/webshop` (docs + `app/`).

Deze inventaris is afgeleid van **code** (`app/pages`, `app/components`, `app/layouts`) en **docs** (catalogue, checkout, identity, design, email, partners, seo).  
Ontwerp-wireframes in deze vault mogen afwijken in *presentatie*, niet stilzwijgend in *routes of servergedrag*.

Peildatum: 2026-11-17.

Gerelateerd: [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md) · [00-index.md](./00-index.md)

---

## 1. Componenten (bouw)

### 1.1 Vue-componenten (`app/components/`)

| Component | Bestand | Rol |
|-----------|---------|-----|
| **CatalogueList** | `CatalogueList.vue` | Lijst/zoek/paginering van gepubliceerde producten (collectie, filters) |
| **PartyProfile** | `PartyProfile.vue` | Publiek profiel maker of vrijplaats + productlinks |
| **OrderFulfilment** | `OrderFulfilment.vue` | Zichtbare fulfilment-/zendingstatus op orderdetail |

### 1.2 Layout en shell

| Stuk | Bestand | Rol |
|------|---------|-----|
| **default layout** | `layouts/default.vue` | Skip-link, header (wordmark, tagline, hoofdnav), `<main>`, footer |
| **site-shell** | CSS/layout in default | Omhulsel pagina |
| **skip-link** | default | “Naar de inhoud” |
| **wordmark** | default | Link home, merknaam + `*` |
| **site-tagline** | default | Korte claim |
| **Hoofdnavigatie** | default | Collectie, Winkelmand, Account, Over (anker) |
| **site-footer** | default | Merkregel + “in voorbereiding” |

### 1.3 Composables / client-helpers (geen Vue SFC, wél UI-gedrag)

| Helper | Bestand | Rol |
|--------|---------|-----|
| **useCart** | `composables/useCart.ts` | Mandregels (variant-ID + aantal) in de browser |
| **usePublicSeo** | `composables/usePublicSeo.ts` | Publieke SEO-meta voor open pagina’s |

### 1.4 Gedeeld design (tokens, geen component-SFC)

| Stuk | Locatie | Rol |
|------|---------|-----|
| **designTokens** | `shared/design/tokens.ts` | paper, surface, ink, muted, accent, line, font, measure |
| **themeVariables** | idem | CSS-variabelen `--akws-*` |
| **brand** | `shared/brand.ts` | Shopnaam, orderprefix |
| **main.css-patronen** | `app/assets/css/main.css` | Basisopmaak, knoppen, formulieren (o.a. `.button`, form layout) |
| **GAP-fonts** | `public/fonts/` | Self-hosted WOFF (bouw: historisch Mono; ontwerpkeuze vault: **GAP Code** voorlopig) |

### 1.5 Logische UI-blokken in pagina’s (nog geen aparte SFC)

Uit checkout/mand/account/docs — herbruikbaar voor UX-kit:

| Blok | Voorkomt o.a. op | Functie |
|------|------------------|---------|
| **Hero** | `/` | Eyebrow, H1, intro, primaire CTA |
| **Intro / over-sectie** | `/` `#over` | Uitleg makers/vrijplaatsen |
| **Collectiefilters** | `/collectie` (+ API) | `page`, `q`, `category`, `party` |
| **Productkaart / tekstlink-rij** | collectie-lijsten | Link naar product (design.md: tekstlinks) |
| **Productdetail-kop** | `/producten/:slug` | Titel, content, beelden |
| **Variantkiezer** | productdetail | `?variant=` serverkeuze |
| **Prijsweergave** | product, quote | Servercenten → euro-format |
| **Voorraadindicatie** | product/mand | Indicatief; geen reservering in mand |
| **CTA In winkelmand** | productdetail | Alleen ID/aantal naar cart |
| **Mandregel** | `/mand` | Titel-link, aantal-input 1–100, verwijderen |
| **Lege-mand staat** | `/mand` | Copy + link collectie |
| **Checkout notice (pending recover)** | `/afrekenen` | Eerdere onzekere poging herstellen |
| **Contact- en adresfieldset** | `/afrekenen` | E-mail, naam, straat, nr, postcode, plaats, land |
| **Ontvangstkeuze** | `/afrekenen` | ship / pickup uit options-API |
| **Quote / prijsvoorstel** | `/afrekenen` | Regels, korting bps, verzending, btw, totaal, expiresAt |
| **Testmodus-banner** | `/afrekenen` | Zichtbaar als `quote.testMode` |
| **Voorwaarden-checkbox** | `/afrekenen` | Akkoord prijsvoorstel + bestelopdracht |
| **Submit / herhaal-submit** | `/afrekenen` | Bestelling plaatsen of dezelfde command opnieuw |
| **Busy / alert messages** | mand, afrekenen, orders | `role="status"` / `role="alert"` |
| **Orderstatus-paneel** | `/bestellingen/:id` | Serverstatus, refresh, geen browser-paid-belofte |
| **Gast claim / account koppelen** | orderdetail, identity | Claimflow (docs checkout/identity) |
| **Account poort** | `/account` | Login, register, profielnaam, logout |
| **Account actiepagina’s** | `/account/:action` | verifieren, wachtwoord, uitnodiging |
| **Deelnemer overzicht** | `/deelnemer` | Portal entry |
| **Deelnemer detail** | `/deelnemer/:id` | Aandelen, ledger-achtige inzage, proposals (partners) |
| **E-mail document-shell** | `server/email/layout.ts` | Gedeelde HTML/tekst layout |
| **E-mailtemplates** | `templates.ts` e.d. | Zie §1.6 |

### 1.6 E-mail “componenten” / templates (klant- of actiegerichte UI)

| Template / kind | Stream | Doel |
|-----------------|--------|------|
| verification | identity | E-mail bevestigen |
| password-reset | identity | Wachtwoord resetten |
| membership-invitation | identity | Deelnemer-uitnodiging |
| guest-order-access | orders | Gastlink order (geen paid-bevestiging) |
| order confirmation (`orders.confirmation`) | orders | Na paid |
| refund notice | orders | Na geverifieerde refund |
| shipment / tracking | orders | Zending (tracking-host allowlist) |
| pickup ready | orders | Afhaal klaar |
| return approved / rejected / received | orders | Retourbesluiten |

---

## 2. Webpagina’s (bouw)

### 2.1 Publieke winkel (indexeerbaar beleid via seo; dev vaak noindex)

| Route | Bestand | Doel (kort) |
|-------|---------|-------------|
| `/` | `pages/index.vue` | Home: hero + over |
| `/collectie` | `pages/collectie.vue` | Productlisting + filters |
| `/producten/:slug` | `pages/producten/[slug].vue` | Productdetail; query `variant` |
| `/categorieen/:slug` | `pages/categorieen/[slug].vue` | Categorie + producten |
| `/kunstenaars/:slug` | `pages/kunstenaars/[slug].vue` | Makerprofiel |
| `/vrijplaatsen/:slug` | `pages/vrijplaatsen/[slug].vue` | Vrijplaatsprofiel |
| `/partijen/:slug` | `pages/partijen/[slug].vue` | **301** naar juiste type-profiel (catalogue.md) |

### 2.2 Kassa en orders (privé: noindex / no-store)

| Route | Bestand | Doel (kort) |
|-------|---------|-------------|
| `/mand` | `pages/mand.vue` | Winkelmand; geen voorraadreservering |
| `/afrekenen` | `pages/afrekenen.vue` | Quote + submit checkout |
| `/bestellingen/:id` | `pages/bestellingen/[id].vue` | Orderstatus (scoped bewijs) |

### 2.3 Account (privé)

| Route | Bestand | Doel (kort) |
|-------|---------|-------------|
| `/account` | `pages/account/index.vue` | Poort: sessie, login/register, profiel |
| `/account/verifieren` | `pages/account/[action].vue` | E-mailverificatie |
| `/account/wachtwoord` | idem | Reset/wachtwoord |
| `/account/uitnodiging` | idem | Membership-uitnodiging accepteren |

(Exacte `action`-waarden volgens identity-docs / page.)

### 2.4 Deelnemersportal (maker/vrijplaats; verified membership)

| Route | Bestand | Doel (kort) |
|-------|---------|-------------|
| `/deelnemer` | `pages/deelnemer/index.vue` | Portal start |
| `/deelnemer/:id` | `pages/deelnemer/[id].vue` | Partijdetail, inzage, proposals |

### 2.5 Niet-HTML maar wel “oppervlakken” (docs)

| Oppervlak | Voorbeeld | Voor ontwerp |
|-----------|-----------|--------------|
| Catalogue API/HTML | `/api/catalogue`, image proxy | Geen losse designpagina; voedt listing |
| Mollie hosted checkout | externe URL | Geen Vrijzaak-chrome |
| Webhooks | `/api/webhooks/mollie`, Resend | Geen UI |
| Directus Studio | beheer | Winkelier/programmeur; buiten storefront-UX |
| E-mail clients | templates | Eigen layout + tokens |

### 2.6 Nog niet als vaste contentpagina in `app/pages` (wel in ontwerp-voet wenselijk)

Contact, AV, Privacy, FAQ — **footer in default is nu minimaal** (“in voorbereiding”). Ontwerp mag ze plannen; route pas na afspraak met bouw.

---

## 3. Componenten per webpagina

Bron: Vue-templates + docs. “Layout” = altijd `default.vue` tenzij later aparte checkout-layout.

### `/` Home

- Layout: skip-link, header/nav, footer  
- **Hero** (eyebrow, H1, intro, knop → collectie)  
- **Intro-grid / Over** (`#over`)

### `/collectie`

- Layout  
- **CatalogueList** (zoek, filters, paginering, productlinks)  
- Staten: laden, leeg, fout/503 (docs)

### `/producten/:slug`

- Layout  
- Productkop, beschrijving, beelden (via catalogue image API)  
- **Variantkiezer**  
- Prijs + beschikbaarheid (server)  
- **In winkelmand**  
- Staten: 404/503, ongeldige variant

### `/categorieen/:slug`

- Layout  
- Categorie-intro  
- Productlinks / list-patroon (catalogue)

### `/kunstenaars/:slug` en `/vrijplaatsen/:slug`

- Layout  
- **PartyProfile**  
- Productlinks naar collectie/producten

### `/partijen/:slug`

- Redirect-gedrag (geen eigen langetermijn-UI)

### `/mand`

- Layout (nu zelfde hoofdnav — ontwerp wil later eventueel hybride)  
- H1 Winkelmand + uitleg geen reservering  
- **Mandregels** (link product, aantal, verwijderen)  
- Lege staat → collectie  
- Fout/alert aantal  
- Link **Naar afrekenen**  
- Geen server-totaal op mand (totaal zit in quote op afrekenen)

### `/afrekenen`

- Layout (ontwerp: kassa-nav gewenst; bouw nu default shell)  
- H1 Afrekenen  
- **Recover-notice** + knop herstel  
- Lege-mand link  
- **Checkout-form**: contact/adres, land, ontvangst  
- Knop **Actueel voorstel aanvragen**  
- **Quote-blok** (regels, shipping, btw, totaal, expiry, testbanner)  
- **Voorwaarden-checkbox**  
- Submit (plaatsen / opnieuw controleren)  
- Link terug mand  
- Alerts / checkout niet beschikbaar

### `/bestellingen/:id`

- Layout  
- Orderstatus (server)  
- **OrderFulfilment**  
- Refresh/status copy (pending tot paid)  
- Account-claim acties waar van toepassing  
- noindex/private

### `/account`

- Layout  
- Sessiestatus / actor  
- Login- en registratievelden (e-mail, wachtwoord, naam)  
- Profiel: displayName opslaan  
- Logout  
- Links naar verify/reset flows

### `/account/:action` (verifieren, wachtwoord, uitnodiging)

- Layout  
- Token/fragment-flow (POST, CSRF)  
- Bevestigings- of foutstaten  
- Geen token in query long-term (docs: fragment)

### `/deelnemer`

- Layout  
- Portal-entry, membership-gate  
- Navigatie naar partijdetail

### `/deelnemer/:id`

- Layout  
- Partij-/aandelenprojectie  
- Datumfilters / paginering (UI aanwezig)  
- Proposal-acties, goedkeuren, retry (partners-domein)  
- Geen algemene order-admin

---

## 4. Navigatie nu vs ontwerp-wens

| | Bouw `default.vue` nu | Ontwerp-vault (richting) |
|--|------------------------|---------------------------|
| Header | Home wordmark, Collectie, Winkelmand, Account, Over | Winkelbrowse vs **kassa-chrome** gescheiden |
| Footer | Minimaal | Contact, AV, Privacy, … |
| Font tokens | GAP Mono in code | **Voorlopig GAP Code** (ontwerpbesluit 2026-11-17) |

Wijzigingen aan routes of checkout-stappen: eerst bouwrepo/programmeur; ontwerp documenteert voorstel hier.

---

## 5. Onderhoud

Bij pull van helling-webshop: dit bestand bijwerken als `app/pages` of `app/components` wijzigt.  
Geen second source of truth — bij twijfel wint de bouwrepo.
