# 04 — Verzending / ontvangst

**Bouw nu:** op `/afrekenen` — select **Ontvangst** (`delivery`: o.a. ship / pickup) uit `/api/checkout/options`.  
Tarieven en labels komen uit **checkout-policy** (nu vooral test).  
**Geen** multi-zending-UI en geen verzendklasse-kiezer in de storefront-code.

## Probleem (ontwerp — blijft relevant)

Mand kan heterogeen zijn (T-shirt + schilderij). Flat rate of één optie kan oneerlijk voelen. Dat is een **toekomstig** UX/policy-onderwerp; SoT blijft bouw tot er policy + UI is.

## Bouw-UI (as-is)

```
Ontvangst
  [ select: labels uit options.delivery ]
  bv. verzenden / afhalen (exacte copy uit policy)
```

Hoort in dezelfde flow als contactvelden; quote herberekent bij land/delivery-wijziging (bouw wist quote).

**Bloknaam ontwerp:** **OntvangstKeuze**.

## Ontwerp-richting (plus — niet gebouwd)

### Happy path — één zending

```
| Hoe wil je het ontvangen?                          |
| ( ) Thuisbezorging — standaard     EUR …           |
| ( ) Zorgvuldig / breekbaar         EUR …           |
| ( ) Ophalen bij vrijplaats […]     EUR 0           |
```

### Gesplitste zending (als policy dat ooit kan)

```
| Zending A — pakket …                               |
| Zending B — kunst … / op afspraak                  |
```

Interne **verzendklassen** op product blijven catalogus/policy-werk (programmeur + winkelier), niet hard in Markdown verzinnen als live tarief.

## Wat de klant niet hoeft te zien

- Tarieftabellen per gram, interne carrierkeuze (tenzij trust)

## Wat wél helder moet (bouw + ontwerp)

- Prijs **incl. btw** in de **quote** (niet los gokken op deze stap)
- Of ophalen vs versturen
- Later: leverindicatie, contact bij kunst

## Gedrag

| | Bouw |
|--|------|
| Geen options | Checkout “niet beschikbaar” |
| Wijzig land/delivery | Quote reset |
| Geen multi-step lock | Alles op één form |

## Open met Vrijzaak (business)

- Vrijplaatsen voor pickup  
- Zones NL/BE/EU  
- Echte tarieven (`mode=approved` policy)  
- Of ontwerp multi-klasse ooit in UI komt  

---
Vrijzaak · https://vrijzaak.nl · [00-index.md](./00-index.md)
