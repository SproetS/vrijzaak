# 04 — Verzending (stap 2)

## Probleem

Mand kan **heterogeen** zijn: T-shirt + boekje (makkelijk pakket) naast schilderij/kunstwerk (breekbaar, groter, duurder om te sturen). Eén flat rate voelt oneerlijk of te duur.

## Doel

Klant kiest een duidelijke verzendoptie (of ziet dat er meerdere zendingen nodig zijn) zonder spreadsheet-gevoel.

## Concept: slim groeperen

Systeem deelt regels intern in **verzendklassen**, bijv.:

| Klasse | Voorbeelden | Typische opties |
|--------|-------------|-----------------|
| Licht pakket | T-shirt, boekje, small merchandise | Standaard post, eventueel ophalen |
| Middel / breekbaar | Klein werk, print op steun | Pakketdienst, handtekening |
| Kunst / groot | Schilderij, object | Speciale verzending, maatwerk, of “we nemen contact op” |

## UI — happy path (alles in één zending)

```
| Hoe wil je het ontvangen?                          |
|                                                    |
| ( ) Thuisbezorging — standaard pakket              |
|     EUR x,xx · 2–5 werkdagen                       |
|                                                    |
| ( ) Thuisbezorging — zorgvuldig / breekbaar        |
|     EUR y,yy · iets langer                         |
|                                                    |
| ( ) Ophalen bij vrijplaats [keuze]                 |
|     EUR 0,00 · Je krijgt een mail als het klaar is |
|                                                    |
| [i] In je mand zitten verschillende soorten        |
|     producten; we kiezen veilige verpakking.       |
```

## UI — gesplitste zending (als nodig)

```
| Je bestelling gaat in 2 zendingen:                 |
|                                                    |
| Zending A — pakket (T-shirt, boekje)               |
|   Optie: [ Standaard  EUR … ]                      |
|                                                    |
| Zending B — kunstwerk “Titel”                      |
|   Optie: [ Speciale verzending EUR … ]             |
|   of [ Op afspraak — we mailen je ]  EUR 0 nu      |
|                                                    |
| Totaal verzending: EUR …                           |
```

“Op afspraak” mag checkout niet blokkeren: klant betaalt producten (+ eventuele vaste kosten); planning volgt offline.

## Wat de klant niet hoeft te zien

- Interne tarieftabellen per gram
- Welke carrier exact (tenzij trust helpt)

## Wat wél helder moet

- Prijs incl. btw
- Leverindicatie
- Of er nader contact komt bij kunst

## Gedrag

- Geen optie gekozen → “Verder” disabled + hint
- Wijzigt de mand later → verzendkeuze herbepalen
- Alleen ophalen-producten → ophalen default

## Open (inhoudelijk te vullen met Vrijzaak)

- Lijst vrijplaatsen voor pickup
- Zones (NL / BE / EU)
- Exacte prijzen per klasse

---
Vrijzaak · https://vrijzaak.nl · [[00-index]]
