# 01 — Winkelwagen

URL-voorstel: `/winkelwagen` of `/cart`

## Navigatie-omgeving

**Winkel-hoofdmenu** + **winkel-voetmenu**.  
Nog geen kassa-chrome (dat start bij `/afrekenen`).  
Zie [00-navigatie-omgevingen.md](./00-navigatie-omgevingen.md).

## Doel

Klant ziet wat er in de mand ligt, past aantallen aan, gaat door naar checkout.

## Desktop layout

```
+------------------------------------------------------------------+
| Vrijzaak   Collectie · Makers · …     [Account] [Winkelmand (n)] |
+------------------------------------------------------------------+
|                                                                  |
|  Winkelwagen                                                     |
|                                                                  |
|  +----------------------------------------------------------+  |
|  | [img] Productnaam — Maker · Vrijplaats                    |  |
|  |       Variant (maat/kleur)                                 |  |
|  |       EUR xx,xx incl. btw                                 |  |
|  |       [ - ] 1 [ + ]          [Verwijder]                  |  |
|  +----------------------------------------------------------+  |
|  | [img] ...                                                 |  |
|  +----------------------------------------------------------+  |
|                                                                  |
|  +---------------------------+  +-----------------------------+  |
|  | Kortingscode              |  | Overzicht                   |  |
|  | [____________] [Toepassen]|  | Subtotaal      EUR …        |  |
|  |                           |  | Korting        - EUR …      |  |
|  |                           |  | Verzending     (in checkout)|  |
|  |                           |  | ─────────────────────       |  |
|  |                           |  | Totaal incl. btw  EUR …     |  |
|  |                           |  |                             |  |
|  |                           |  | [ Naar afrekenen ]          |  |
|  |                           |  | of verder winkelen          |  |
|  +---------------------------+  +-----------------------------+  |
|                                                                  |
+------------------------------------------------------------------+
```

## Mobiel layout

```
+---------------------------+
| Vrijzaak     [Zoek] [☰] [Mand] |
+---------------------------+
| Winkelwagen               |
|                           |
| [img] Naam                |
| Maker · Vrijplaats        |
| EUR xx,xx                 |
| [ - ] 1 [ + ]  Verwijder  |
| ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  |
| ...                       |
|                           |
| Kortingscode              |
| [__________] [Toepassen]  |
|                           |
| Subtotaal …               |
| Korting   …               |
| Totaal incl. btw …        |
|                           |
| [ Naar afrekenen ]        |
| Verder winkelen           |
+---------------------------+
| sticky CTA optioneel:     |
| [ Naar afrekenen  EUR … ] |
+---------------------------+
```

## Regels / gedrag

- Prijsregel altijd **incl. btw**.
- Max aantal: voorraad (indien bekend); anders redelijke max.
- Verwijderen: direct of met undo-toast (“Verwijderd — Herstel”).
- Kortingscode: succes/foutmelding onder het veld.
- Verzendkosten: “berekend in de volgende stap” (tenzij flat rate al bekend).
- CTA disabled als wagen leeg.

## Lege staat

```
| Je mand is leeg.                    |
| [Naar de winkel]                    |
```

## Notities anti-commercieel

- Geen countdown-druk of fake schaarste.
- Wel: “Je steunt maker en vrijplaats” als zachte lijn onder het overzicht (optioneel).

---
Vrijzaak · https://vrijzaak.nl · [[00-index]]
