# Nomenclatuur — zaaktaal (UI) + Engels (techniek)

Vrijzaak **voelt** als een fysieke zaak. Klantcopy is menselijk en **tweetalig** (Nederlands + Engels).  
**Programmeren, identifiers en (toekomstige) paden** blijven **Engels** en stabiel.

Collega’s kozen o.a. zaak-metaforen: **Etalage**, **Magazijn**, **Loods**, **Kassa**.

---

## Drie lagen (niet door elkaar)

| Laag | Taal | Voorbeelden | Wie |
|------|------|-------------|-----|
| **1. UI-label** | NL + EN (toggle) | “Magazijn” / “Warehouse” | Ontwerp + i18n in Nuxt |
| **2. Route / path** | Engels (doel) | `/collection`, `/checkout` | Programmeur — **nu nog wachten**; huidige paden blijven SoT tot migratie |
| **3. Code** | Engels | `useCart`, `CatalogueList`, `checkout` | Programmeur / bouwrepo |

```text
UI (nl|en)  →  i18n keys (Engels)  →  pages/components (Engels)
                    ↘
                 routes: nu bouw-as-is; later Engelse slugs + redirects
```

**Niet:** Nederlandse variabelenamen (`winkelmandRegels`) of harde “Magazijn” in code zonder i18n.  
**Wel:** `t('nav.warehouse')` → NL “Magazijn” · EN “Warehouse” (of afgesproken EN-term).

---

## Huidige bouwpaden (tijdelijk SoT)

Hernoemen van URL’s doen we **niet** in deze ontwerprepo en **niet** ad hoc.  
Programmeur plant migratie + 301/SEO. Tot die tijd:

| Huidige path (bouw) | Betekenis |
|---------------------|-----------|
| `/` | Home / deels etalage |
| `/collectie` | Volledige catalogus |
| `/producten/:slug` | Productdetail |
| `/categorieen/:slug` | Categorie |
| `/kunstenaars/:slug` | Maker |
| `/vrijplaatsen/:slug` | Vrijplaats |
| `/mand` | Cart |
| `/afrekenen` | Checkout |
| `/bestellingen/:id` | Order status |
| `/account` | Account |
| `/deelnemer` | Partner portal |

---

## Labelwoordenboek (i18n)

Voorstel **message keys** (Engels) + UI-strings. EN-kolom is voorstel — winkelier/UX mogen bijsturen (tone of voice).

### Navigatie zaak

| Key (voorstel) | NL (default) | EN (toggle) | Huidige route | Toekomstige route (voorstel, wacht op programmeur) |
|----------------|--------------|-------------|---------------|-----------------------------------------------------|
| `nav.showcase` | Etalage | Showcase | `/` of sectie | `/` of `/showcase` |
| `nav.warehouse` | Magazijn | Warehouse | `/collectie` | `/collection` |
| `nav.yard` | Loods | Yard sale* | — | `/sale` of `/yard` |
| `nav.makers` | Makers | Makers | `/kunstenaars/…` | `/artists/…` (bouw heeft kunstenaars) |
| `nav.sites` | Vrijplaatsen | Free spaces* | `/vrijplaatsen/…` | `/sites/…` of keep `freeholds` — teamkiest |
| `nav.cart` | Winkelmand | Cart | `/mand` | `/cart` |
| `nav.account` | Account | Account | `/account` | `/account` |
| `nav.search` | Zoeken | Search | — | — |

\*EN voor “Loods”/“Vrijplaatsen”: liever geen letterlijke “Shed” tenzij jullie die ironie willen. Alternatieven: **Sale**, **Offers**, **Clearance** voor Loods; **Freeholds**, **Sites**, **Communities** voor vrijplaatsen. **Besluit open.**

### Kassa

| Key | NL | EN | Huidige route | Toekomst (voorstel) |
|-----|----|----|---------------|---------------------|
| `nav.checkout` | Kassa | Checkout | `/afrekenen` | `/checkout` |
| `checkout.title` | Kassa | Checkout | | |
| `checkout.toCheckout` | Naar de kassa | To checkout | | |
| `checkout.quote` | Actueel voorstel | Current quote | | |
| `checkout.backToShop` | Terug naar de winkel | Back to the shop | | |
| `checkout.backToCart` | Terug naar de winkelmand | Back to cart | | |
| `cart.title` | Winkelmand | Cart | `/mand` | `/cart` |
| `order.title` | Bestelling | Order | `/bestellingen/:id` | `/orders/:id` |
| `order.receipt` | Bon | Receipt | optionele copy | |

### Catalogus

| Key | NL | EN | Huidige route | Toekomst (voorstel) |
|-----|----|----|---------------|---------------------|
| `product.title` | Werk / Stuk* | Work / Piece* | `/producten/:slug` | `/products/:slug` |
| `category.title` | Schap* | Shelf* / Category | `/categorieen/:slug` | `/categories/:slug` |
| `sale.badge` | In de loods | On sale | — | — |

\*“Werk” vs “Product”: UI mag “werk”; code blijft `product`.

---

## Taal-toggle (frontend)

| | |
|--|--|
| Default | **Nederlands** (`nl`) |
| Tweede | **Engels** (`en`) |
| Opslag | voorkeur in cookie/localStorage (bouw-implementatie) + eventueel account later |
| Scope | Zichtbare UI-strings, foutmeldingen, knoppen, nav |
| Niet vertalen in UI-toggle | Technische order-ID’s, SKU’s, e-mail van providers tenzij templates i18n hebben |

**Implementatie (richting programmeur):** Nuxt i18n (of bestaande pattern in monorepo) — keys zoals hierboven; geen losse hardcode “Magazijn” in Vue behalve via `t()`.

**SEO:** `hreflang` / locale paths (`/en/...` vs query) = bouwbesluit; ontwerp eist alleen dat labels wisselen en content-strategie duidelijk is.

---

## Zaak-metaforen (inhoud, taalneutraal)

```text
showcase (Etalage)  ⊂  curated subset
warehouse (Magazijn)   = full catalogue
yard/sale (Loods)   ⊂  warehouse ∩ offers
```

- Loods is geen tweede stockboek; het is presentatie op dezelfde catalogus (campagne/prijs in bouw).  
- Lege Loods: item verbergen in nav of eerlijke lege staat (beide talen).  
- Geen nep-schaarste.

---

## Navigatieschets (labels = i18n)

**NL**
```text
[Logo]  Etalage · Magazijn · Loods · Makers · Vrijplaatsen    [Zoek] [Account] [Winkelmand]
```

**EN**
```text
[Logo]  Showcase · Warehouse · Sale · Makers · …            [Search] [Account] [Cart]
```

**Kassa** (geen magazijn-nav): NL “Kassa” · EN “Checkout”.

Bouw-header nu (één taal, andere labels): Collectie · Winkelmand · Account · Over — migratie = i18n keys + copy, **niet** per se path-rename.

---

## Wat ontwerp wél / niet doet

| Wel | Niet |
|-----|------|
| NL+EN copy in docs en wireframes | Zelf routes in helling hernoemen |
| i18n-key-voorstellen (Engels) | Nederlandse function/file names eisen |
| Mapping huidige path ↔ label | Breaking URL-change zonder programmeur |
| Tone of voice Loods/Etalage | “BLACK FRIDAY”-schreeuw |

---

## Open besluiten (team)

1. EN-term **Loods**: Sale / Clearance / Yard / Offers?  
2. EN-term **Vrijplaatsen**: Free spaces / Sites / Freeholds?  
3. Locale strategy: prefix `/en` vs één path + language cookie?  
4. Wanneer path-migratie (`/collectie` → `/collection`)? — **wacht op programmeur**  
5. “Schap” in NL UI of gewoon “Categorie”?  

---

## Gerelateerd

- [00-navigatie-omgevingen.md](./00-navigatie-omgevingen.md)  
- [00-inventaris-bouw-ui.md](./00-inventaris-bouw-ui.md)  
- [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md)  
- Kassa-flow: [02-checkout-overzicht.md](./02-checkout-overzicht.md)  
- Sitemap later: `09-sitemap-ia.md` (keys + paths + beide talen)
