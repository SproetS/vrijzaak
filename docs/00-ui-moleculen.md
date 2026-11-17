# UI-bouwstenen — atomen · moleculen · organismen · pagina’s

**Moleculen-werkwijze** (atomic design, licht): kleine herbruikbare delen stapelen tot schermen.  
Niet elk blok hoeft meteen een Vue-SFC te zijn; wél een **stabiele naam** (Engels) + **i18n-labels** (NL/EN).

| Laag | Engels (techniek) | Rol |
|------|-------------------|-----|
| **Atom** | kleinste UI | knop, veld, prijs, badge |
| **Molecule** | vaste combo | mandregel, zoekveld+knop, nav-link+teller |
| **Organism** | groot blok | header, CatalogueList, QuoteBlok, kassa-form |
| **Page** | route-scherm | Magazijn, Kassa, Winkelmand, … |

**SoT routes nu:** bouwrepo (nog NL-paden). **Hernoem paths:** programmeur later.  
**Labels:** [00-nomenclatuur-winkel.md](./00-nomenclatuur-winkel.md).  
**Bestaande SFC’s:** [00-inventaris-bouw-ui.md](./00-inventaris-bouw-ui.md).

Legenda status: **bouw-SFC** · **bouw-inline** · **ontwerp** (nog niet in code) · **deels**

---

## 1. Atomen

| ID (code-voorstel) | NL / EN (UI) | Bouw nu | Notes |
|--------------------|--------------|---------|--------|
| `AtomSkipLink` | Naar de inhoud / Skip to content | inline `default.vue` | a11y |
| `AtomWordmark` | Vrijzaak (+ `*`) | inline header | later `logo.svg` |
| `AtomButton` | — | `.button` in CSS | primary / ghost / busy |
| `AtomTextLink` | — | `NuxtLink` | catalogue: tekstlinks |
| `AtomLabel` | — | `<label>` | altijd zichtbaar label |
| `AtomInput` | — | `<input>` | text email number |
| `AtomSelect` | — | `<select>` | land, delivery |
| `AtomCheckbox` | — | `<input type=checkbox>` | terms |
| `AtomPrice` | EUR … incl. btw | `formatEuro` | servercenten only |
| `AtomBadge` | In de loods / On sale | ontwerp | Loods-markering |
| `AtomTag` | Maker / vrijplaats | deels | op productregel |
| `AtomSpinner` / busy | Bezig… / Working… | deels copy | disable + aria |
| `AtomAlert` | — | `role="alert"` | fouten |
| `AtomStatus` | — | `role="status"` | info |
| `AtomHeading` | h1–h3 | pages | één h1 per page |
| `AtomIcon` | — | ontwerp `frontend/svg` | currentColor |
| `AtomLangToggle` | NL \| EN | ontwerp | i18n switch |

Geen dummyprijzen als “echte” `AtomPrice` in productie-UI.

---

## 2. Moleculen

| ID | Samenstelling | NL / EN | Status |
|----|---------------|---------|--------|
| `MolNavItem` | link + optioneel active | Etalage, Magazijn, … | inline nav |
| `MolCartCount` | mand-link + teller | Winkelmand (n) / Cart (n) | deels (bouw: link zonder teller?) |
| `MolSearchField` | input + submit | Zoeken / Search | ontwerp (bouw filters op collectie) |
| `MolFieldRow` | Label + Input + hint + error | — | bouw fieldset rows |
| `MolQuantityStepper` | label + number 1–100 | Aantal / Quantity | `/mand` |
| `MolLinePrice` | titel + `AtomPrice` + qty | — | quote + cart |
| `MolProductTextLink` | link naar product | werk-titel | CatalogueList / cart |
| `MolStockHint` | korte status | Niet verkoopbaar / Unavailable | mand/product |
| `MolTermsRow` | checkbox + label + link AV | akkoord voorstel | `/afrekenen` |
| `MolTrustMollie` | tekst (+ icoon) | Veilig via Mollie / … | ontwerp |
| `MolPagination` | prev/next of page | — | CatalogueList |
| `MolFilterChip` | toggle filter | — | ontwerp / deels query |
| `MolEmptyState` | tekst + CTA-link | Mand leeg → Magazijn | mand, collectie |
| `MolNoticeBanner` | status + actie | recover checkout | `/afrekenen` |
| `MolLangSwitch` | `AtomLangToggle` + pref | — | ontwerp |
| `MolSaleBadge` | `AtomBadge` Loods | In de loods / On sale | ontwerp |

---

## 3. Organismen

| ID | Moleculen / delen | Pagina’s | Status |
|----|-------------------|----------|--------|
| `OrgSiteHeader` | wordmark, nav items, cart, account, search, lang | alle publiek | **default.vue** (beperkte items) |
| `OrgSiteFooter` | juridische links, claim | winkel | default (minimaal) |
| `OrgCheckoutHeader` | Kassa-label, mand, escape | kassa | **ontwerp** (nu = default) |
| `OrgCatalogueList` | filters, lijst links, paginatie, empty | Magazijn | **CatalogueList.vue** |
| `OrgPartyProfile` | bio + productlinks | maker / vrijplaats | **PartyProfile.vue** |
| `OrgProductDetail` | media, variant, price, CTA mand | product | **inline** `producten/[slug]` |
| `OrgCartList` | `MolQuantityStepper` × n, remove, empty | Winkelmand | **inline** `mand.vue` |
| `OrgContactAddressForm` | field rows land | Kassa | **inline** afrekenen fieldset |
| `OrgFulfillmentChoice` | select delivery | Kassa | **inline** delivery |
| `OrgQuoteBlock` | regels, shipping, btw, total, expiry, testbanner | Kassa | **inline** na quote |
| `OrgCheckoutRecover` | notice + herstelknop | Kassa | **inline** |
| `OrgCheckoutActions` | voorstel-knop, terms, submit | Kassa | **inline** |
| `OrgOrderStatus` | status, refresh, paid/pending copy | Bon/order | **inline** bestellingen |
| `OrgOrderFulfilment` | zending/fulfilment | order | **OrderFulfilment.vue** |
| `OrgAccountPanel` | login/register/profiel | Account | **inline** account |
| `OrgPartnerPanel` | ledger/proposals | Achterkamer | **inline** deelnemer |
| `OrgHomeHero` | eyebrow, h1, CTA Magazijn | Home/Etalage | **inline** index |
| `OrgHomeAbout` | over-tekst | Home | **inline** `#over` |
| `OrgSplitExplainer` | opbrengst-balken | kassa/bon | **ontwerp** |

E-mail: aparte organismen in `server/email/` (layout + templates) — zie inventaris mails; zelfde merktokens, andere runtime.

---

## 4. Pagina’s (templates)

| Page ID | UI NL | UI EN | Route nu | Organismen (hoofd) |
|---------|-------|-------|----------|--------------------|
| `PageHome` | Home / Etalage | Home / Showcase | `/` | Header, Hero, About, Footer |
| `PageWarehouse` | Magazijn | Warehouse | `/collectie` | Header, CatalogueList, Footer |
| `PageYard` | Loods | Sale | — | Header, list/filter sale, Footer (**ontwerp**) |
| `PageProduct` | Werk | Work | `/producten/:slug` | Header, ProductDetail, Footer |
| `PageCategory` | Schap | Category | `/categorieen/:slug` | Header, intro + list, Footer |
| `PageArtist` | Maker | Maker | `/kunstenaars/:slug` | Header, PartyProfile, Footer |
| `PageSite` | Vrijplaats | Free space* | `/vrijplaatsen/:slug` | Header, PartyProfile, Footer |
| `PageCart` | Winkelmand | Cart | `/mand` | Header, CartList, Footer |
| `PageCheckout` | Kassa | Checkout | `/afrekenen` | CheckoutHeader*, Recover, ContactForm, Fulfillment, Quote, Actions |
| `PageOrder` | Bestelling | Order | `/bestellingen/:id` | Status, OrderFulfilment, claim |
| `PageAccount` | Account | Account | `/account` | AccountPanel |
| `PageAccountAction` | Verifieren e.d. | Verify etc. | `/account/:action` | forms |
| `PagePartner` | Achterkamer | Partner | `/deelnemer` | Partner entry |
| `PagePartnerDetail` | — | — | `/deelnemer/:id` | PartnerPanel |
| `PagePartyRedirect` | — | — | `/partijen/:slug` | 301 only |

\*EN vrijplaats: open besluit in nomenclatuur.

---

## 5. Matrix: molecuul/organisme × pagina (kassa-kern)

| | Home | Magazijn | Product | Mand | Kassa | Order |
|--|:----:|:--------:|:-------:|:----:|:-----:|:-----:|
| OrgSiteHeader | x | x | x | x | x* | x* |
| OrgCatalogueList | | x | | | | |
| OrgProductDetail | | | x | | | |
| OrgCartList | | | | x | | |
| OrgContactAddressForm | | | | | x | |
| OrgQuoteBlock | | | | | x | |
| OrgCheckoutActions | | | | | x | |
| OrgOrderFulfilment | | | | | | x |
| MolEmptyState | | x | | x | x | |
| MolTermsRow | | | | | x | |
| MolTrustMollie | | | | | x | o |
| AtomLangToggle | x | x | x | x | o | o |

\*Kassa/order: streven `OrgCheckoutHeader` i.p.v. volle winkel-nav.

---

## 6. Bestaande Vue-SFC’s (bouw) in dit model

| Bestand | Laag | Page |
|---------|------|------|
| `layouts/default.vue` | OrgSiteHeader + Footer + shell | almost all |
| `CatalogueList.vue` | OrgCatalogueList | Magazijn (+ embeds) |
| `PartyProfile.vue` | OrgPartyProfile | Artist, Site |
| `OrderFulfilment.vue` | OrgOrderFulfilment | Order |

Rest = page-inline → kandidaten om later tot molecules/organisms te trekken (programmeur).

---

## 7. Handoff-volgorde (ontwerp → code)

1. **Page** kiezen (route nu + UI NL/EN).  
2. **Organisms** opnoemen die op die page moeten.  
3. **Molecules/atoms** alleen detail als state of variant telt (leeg, fout, busy, Loods-badge).  
4. Tokens + logo uit `frontend/`.  
5. Issue: “bouw-as-is vs ontwerp-plus”.

Wireframes `01`–`08` = vooral **PageCheckout** + **PageCart** + organisms Quote/Cart/…  
Winkel-IA later: PageHome, PageWarehouse, PageYard, PageProduct.

---

## 8. Gerelateerd

- [00-inventaris-bouw-ui.md](./00-inventaris-bouw-ui.md) — feitelijke files/routes  
- [08-componenten-en-staten.md](./08-componenten-en-staten.md) — mapping ontwerp↔bouw kassa  
- [00-nomenclatuur-winkel.md](./00-nomenclatuur-winkel.md) — i18n  
- [00-navigatie-omgevingen.md](./00-navigatie-omgevingen.md)  

Peildatum: 2026-11-17.
