# 01 — Winkelmand

**UI:** Winkelmand → daarna **Kassa**  
**Route (bouw):** `/mand` · `app/pages/mand.vue`  
**Componenten/bouw:** layout **default** · composable **useCart** · read `/api/cart` · geen aparte mand-SFC  
**Inventaris:** [00-inventaris-bouw-ui.md](./00-inventaris-bouw-ui.md) · mapping [08-componenten-en-staten.md](./08-componenten-en-staten.md)

## Navigatie-omgeving

**Bouw nu:** winkel-**default** header (Collectie, Winkelmand, Account, Over) + minimale footer.  
**Ontwerp later:** mag hybride blijven (nog geen NavKassa op `/mand`).

## Doel

Klant ziet mandinhoud, past aantallen aan, gaat naar `/afrekenen`.  
Mand **reserveert geen voorraad** (bouw-copy + contract).

## Bouw-UI (as-is)

```
[ default: wordmark | Collectie | Winkelmand | Account | Over ]

Winkelmand
Uitleg: reserveert nog geen voorraad; prijsvoorstel bij afrekenen.

Per regel (useCart line):
  [link product + variant]  titel uit /api/cart
  of “gegevens nu niet beschikbaar”
  eventueel: “niet verkoopbaar”
  Aantal [number 1–100]
  [ Verwijderen ]

Leeg:
  link → /collectie

Fout aantal → role=alert
[ Naar afrekenen ]  → /afrekenen   (als regels ok)
```

**Niet op `/mand` in bouw:** server-totaal, kortingscode-UI, verzendregel, SplitExplainer.  
Totalen zitten in de **quote** op `/afrekenen`.

## Ontwerp-plus (nog niet in bouw — voorstel)

- Visuele productthumb (bouw toont tekstlink)
- Kortingscode op mand of pas op quote
- Zachte lijn “je steunt maker en vrijplaats”
- Sticky mobiele CTA met indicatief bedrag (alleen na quote of bewust “vanaf”)

Label UI: **Winkelmand** (niet “cart”). Route blijft `/mand`.

## Desktop / mobiel (richting)

ASCII-layout mag rijkere kolommen tonen; implementatie volgt bouw tot programmeur componenten splitst.

```
Desktop: lijst links, optioneel later summary-kaart rechts (nu: geen totalen)
Mobiel: stacked regels + onderaan “Naar afrekenen”
```

## Regels

| | Bouw | Ontwerp |
|--|------|---------|
| Data client | variant-ID + aantal (`useCart`) | idem |
| Titels/prijs op regel | `/api/cart` waar beschikbaar | server-DTO |
| Max aantal | 1–100 | idem |
| CTA disabled | impliciet: geen link als leeg/ongeldig | expliciet disabled knop ok |

## Lege staat

```
| Je winkelmand is leeg.              |
| [Bekijk de collectie] → /collectie  |
```

---
Vrijzaak · https://vrijzaak.nl · [00-index.md](./00-index.md)
