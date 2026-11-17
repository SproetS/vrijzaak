# 07 — Rekensom (klantzichtbaar + intern)

**Bouw-UI:** bedragen in **QuoteBlok** op `/afrekenen` (niet op `/mand`).  
**Component-ontwerp:** OrderSummary / Price · mapping [08-componenten-en-staten.md](./08-componenten-en-staten.md)


## Uitgangspunt klant (B2C)

- Alle getoonde productprijzen zijn **EUR incl. btw**.
- Meerdere btw-tarieven in één order mogelijk (bijv. 21% kleding, 9% boeken, bijzondere regels kunst — exact tarief per product in catalogus).

## Opbouw totaal (checkout-sidebar)

Volgorde voor de klant:

```
Subtotaal (incl. btw)           EUR A
Korting                         - EUR K
Verzending (incl. btw indien)   EUR V
────────────────────────────────────
Totaal                          EUR T
  waarvan btw                   EUR B   (gesplitst per tarief indien nuttig)
```

### Meerdere btw-tarieven

Optioneel uitklapbaar:

```
Btw-overzicht
  21% over grondslag …    EUR …
  9% over grondslag …     EUR …
```

Implementatie later: of prijzen intern excl. opslaan en incl. tonen, of incl. met back-out — **draadmodel eist alleen consistente incl.-presentatie**.

## Kortingscode

- Percentage of vast bedrag
- Toepassen op subtotaal (regels), niet op verzending — tenzij code dat expliciet zegt
- Na korting btw herbepalen volgens gekozen model
- Fout: “Deze code is ongeldig of niet geldig voor je mand.”

## Verdeling opbrengst (Vrijzaak-specifiek)

Elke verkoopregel voedt idealiter drie partijen (+ overheid via btw):

```
Verkoopbedrag regel (incl. of excl. — intern vastleggen welk model)
        │
        ├─ btw (indien van toepassing) → afdracht
        └─ netto verdeelbaar
                ├─ % Kunstenaar (Pietje, gekoppeld aan vrijplaats A)
                ├─ % Vrijplaats (bijv. Ruigoord)
                └─ % Winkel (Vrijzaak)
```

Percentages kunnen per product, per maker of per vrijplaats verschillen (configuratie, niet hard in UI).

### Klantzicht — “eerlijk beeld”

Niet verplicht open; wel beschikbaar:

```
| Hoe wordt de opbrengst verdeeld?                         |
|                                                          |
| Voor jouw bestelling (indicatief, na btw):               |
|                                                          |
|  Maker(s)      ████████████░░░░  ca. xx%   EUR …         |
|  Vrijplaats    ██████░░░░░░░░░░  ca. yy%   EUR …         |
|  Vrijzaak      ████░░░░░░░░░░░░  ca. zz%   EUR …         |
|                                                          |
| Exacte bedragen per maker zie je in de bevestigingsmail  |
| of op de productpagina (“bij verkoop gaat … naar …”).    |
```

Doel: anti-commerciële eerlijkheid, geen Excel-shock.

### Intern (niet op checkout-scherm)

- Bouw: aandelen in **basispunten** (som 10 000) op immutable orderregels; geen float; oude 70/30-vuistregels gelden niet.
- Btw/korting/verzend via checkout-policy + line snapshots; UI rekent niet “na”.
- Uitbetaling/partnerbatches buiten kassa-UI.
- Mollie ontvangt **één** charge van totaal T (centen, EUR).

## Voorbeeld (fictief)

Mand:

| Product | Incl. btw | Tarief | Maker | Vrijplaats |
|---------|-----------|--------|-------|------------|
| T-shirt | 35,00 | 21% | — | OT301 |
| Boekje | 18,00 | 9% | Pietje | Ruigoord |

```
Subtotaal                 53,00
Korting (code VRIJ5)      -5,00
Verzending pakket          4,95
───────────────────────────────
Totaal                    52,95
waarvan btw                … (herberekend)
```

(Exacte btw-rekenregel in implementatiefase vastzetten en testen met edge cases.)

## Edge cases voor later testen

- Alleen 0%-achtige situaties
- Korting groter dan subtotaal → totalen niet negatief; code weigeren of maxen
- Kunst “prijs op aanvraag” hoort niet in deze checkout
- Gemengde verzendklassen: verzending som van deelzendingen

---
Vrijzaak · https://vrijzaak.nl · [00-index.md](./00-index.md)
