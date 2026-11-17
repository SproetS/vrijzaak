# 06 — Bevestiging en orderstatus

**Route (bouw):** `/bestellingen/:id` · `app/pages/bestellingen/[id].vue`  
**Component:** **OrderFulfilment**  
**Layout:** **default** · private / noindex  
**Voorwaarde “happy bedankt”:** server **paid** (niet alleen Mollie-return)

## Doel

1. Eerlijke **status** terwijl betaling/fulfilment loopt  
2. Na paid: rust, dank, next steps (ontwerp “happy”)

## Bouw-blokken

| Blok | Rol |
|------|-----|
| **OrderstatusPaneel** | Serverstatus, refresh; geen browser-paid-belofte |
| **OrderFulfilment** | Zending / fulfilment-zicht |
| Gast **claim** / account-koppeling | Waar bouw dat toont (identity/checkout-contract) |
| Layout default | Nog winkel-nav; ontwerp wil light bedankt-chrome |

## Happy layout (ontwerp — tonen ná server-paid)

```
Gelukt — bedankt voor je bestelling
Hoi {naam}, …
Ordernummer: …
Bevestigingsmail onderweg (orders.confirmation)

Wat gebeurt er nu?
  1. …
  2. …

Je bestelling (snapshot-regels)
  Totaal betaald incl. btw: …

[optioneel] SplitExplainer — opbrengst

[ Verder rondkijken → /collectie ]
[ Account … ] (gast)
```

## Pending layout (bouw-contract)

```
We wachten op bevestiging van je betaling…
[Pagina vernieuwen]
OrderFulfilment / status alleen wat server toelaat
```

## Component-mapping

| Ontwerp | Bouw |
|---------|------|
| Bedankt-chrome | nog default; plus NavKassa-light |
| OrderSummary read-only | order DTO op statuspagina |
| OrderFulfilment | **OrderFulfilment.vue** |
| SplitExplainer | nog niet |

## Technische states

- Alleen scoped bewijs → toegang; ordernummer alleen is geen login  
- Mail confirmation ná paid-effect; UI niet blokkeren op SMTP  
- Gastclaim: bewijs + verified account, geen stil e-mailmatch  

---
Vrijzaak · https://vrijzaak.nl · [00-index.md](./00-index.md)
