# Nomenclatuur — echte winkel, geen webjargon

Vrijzaak praat als een **fysieke zaak** (vrijplaats / loods / etalage), niet als “shop, cart, checkout, sale”.  
Collega’s (winkelier + team) kozen o.a. **Etalage**, **Magazijn**, **Loods**, **Kassa**.

**Twee lagen**

| Laag | Wat | Wie bepaalt |
|------|-----|-------------|
| **UI-label (NL)** | Wat de klant leest in menu’s en knoppen | Ontwerp + winkelier (deze vault) |
| **Route / code (bouw)** | URL’s, Vue-bestanden, API | Programmeur / helling-repo (SoT techniek) |

Labels mogen “Magazijn” zeggen terwijl de route nog `/collectie` is — tot de programmeur redirects of slug-wijzigingen afspreekt.

---

## Kernwoorden (vast tot herzien)

| Label (UI) | Betekenis in de zaak | Typische inhoud | Bouw nu (route / plek) | Status |
|------------|----------------------|-----------------|------------------------|--------|
| **Etalage** | Aanbevolen / in de kijker | Curated picks, “nu mooi”, redactioneel | Deels home-hero; **geen** aparte route | Ontwerp + content; route later bv. `/etalage` of sectie op home |
| **Magazijn** | Alles wat te koop is | Volledige catalogus, zoek/filter | **`/collectie`** (`collectie.vue`, CatalogueList) | Label-wissel in UI; URL desgewenst later |
| **Loods** | Uitverkoop / aanbiedingen | Campagnes, afgeprijsd, “opruiming” | Nog **geen** vaste storefront-route (checkout kent wel campagnes server-side) | Ontwerp + policy; route bv. `/loods` of filter op magazijn |
| **Kassa** | Afrekenen | Gegevens, ontvangst, voorstel, betalen | **`/afrekenen`** | Label al deels; chrome = NavKassa |
| **Winkelmand** | Wat je meeneemt naar de kassa | Regels ID+aantal | **`/mand`** | Vast |
| **Bon** / **Bestelling** | Order na plaatsen | Status, fulfilment | **`/bestellingen/:id`** | “Bon” optioneel in copy; route blijft bestellingen |
| **Werk** / **Stuk** | Eén product | Detail + variant | **`/producten/:slug`** | “Product” intern ok; UI mag “werk” |
| **Maker** / **Kunstenaar** | Wie het maakte | Profiel | **`/kunstenaars/:slug`** | Bouw gebruikt kunstenaars |
| **Vrijplaats** | Waar het thuishoort | Profiel | **`/vrijplaatsen/:slug`** | Vast |
| **Schap** / **Rij** | Categorie | Groep in het magazijn | **`/categorieen/:slug`** | “Categorie” technisch; UI “schap” overwegen |
| **Balie** / **Account** | Jouw gegevens & orders | Login, profiel | **`/account`** | “Account” blijft helder; “balie” optioneel speels |
| **Achterkamer** | Deelnemers (makers/vrijplaatsen) | Aandelen, inzage | **`/deelnemer`** | Niet in publieke etalage-nav |
| **Voorwaarden** e.d. | Juridisch / info | Voet | Nog minimale footer in bouw | Contact, AV, Privacy |

---

## Navigatievoorstel (winkelhoofd)

```
[Logo]   Etalage · Magazijn · Loods · Makers · Vrijplaatsen     [Zoek] [Account] [Winkelmand]
```

- **Etalage** — landingscuratie (home of eigen pad).  
- **Magazijn** — alles.  
- **Loods** — alleen tonen als er actieve aanbiedingen zijn (lege Loods = verbergen of eerlijke lege staat).  
- Op **Kassa** (`/afrekenen`): geen Etalage/Magazijn/Loods in de top — wel “Terug naar de winkel” / Winkelmand.

Bouw-header nu: Collectie · Winkelmand · Account · Over — **copy-update** richting bovenstaande labels (programmeur).

---

## Kassa-flow (labels)

| Moment | Zeg | Liever niet |
|--------|-----|-------------|
| Naar betalen | **Naar de kassa** | “Proceed to checkout” |
| Pagina `/afrekenen` | **Kassa** | Alleen “Checkout” |
| Prijs ophalen | **Voorstel** / **Actueel voorstel** (bouw) | “Get quote” in UI |
| Betalen | **Betaal met iDEAL** e.d. | “Submit payment” |
| Terug | **Terug naar de winkel** of **Winkelmand** | “Back to shop” mix |

---

## Loods vs Magazijn vs Etalage (inhoud)

```text
Etalage     ⊂   wat de zaak nu wíl tonen (curatie)
Magazijn        alles verkoopbaars
Loods       ⊂   Magazijn ∩ (actie / opruim / afprijs)
```

- Een stuk kan in Etalage **en** Magazijn staan.  
- Loods is geen tweede voorraadadministratie; het is een **vitrine-label** op dezelfde catalogus (campagne/prijsrevisie in bouw).  
- Geen nep-“nog 2 stuks” of countdown tenzij echt.

---

## Copy-toon

- Kort, concreet, alsof je in de loods staat.  
- Anti-schreeuw: Loods ≠ “BLACK FRIDAY 90%”. Wel: “In de loods”, “Voor een zachte prijs”, “Laatste stuks” alleen als waar.  
- Makers en vrijplaatsen blijven zichtbaar in Magazijn/Etalage waar het klopt.

---

## Open met team

1. URL’s hernoemen (`/collectie` → `/magazijn`) of alleen UI-labels + 301 later?  
2. Etalage = alleen homepage-blok of eigen route?  
3. Loods vullen via Directus-campagne, tag, of categorie?  
4. “Schap” i.p.v. categorie in UI?

Programmeur: geen breaking route-change zonder redirects en SEO-afspraak ([docs/seo.md](bouw) / catalogue).

---

## Gerelateerd

- [00-navigatie-omgevingen.md](./00-navigatie-omgevingen.md)  
- [00-inventaris-bouw-ui.md](./00-inventaris-bouw-ui.md)  
- [02-checkout-overzicht.md](./02-checkout-overzicht.md) (Kassa)  
- Sitemap later: `09-sitemap-ia.md`
