# 01 — Winkelmand

URL (bouw): **`/mand`**  
(Nederlands label in UI: “Winkelmand”. Oude voorstellen `/winkelwagen` of `/cart` vermijden.)

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
|  Winkelmand                                                      |
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
| Winkelmand                |
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

- Client bewaart **variant-ID + aantal**; titels/prijzen via storefront-read / server (bouw checkout).
- Getoonde prijsregel **incl. btw** indien catalogus zo presenteert; totalen niet “hard” uit de browser vertrouwen.
- Mand **reserveert geen voorraad**.
- Max aantal: server/beschikbaarheid; ongeldig aantal blokkeert afrekenen tot correctie (bouw: ≥44px steppers).
- Verwijderen: direct of undo-toast.
- Kortingscode: succes/fout van server onder het veld.
- Verzendkosten: “berekend in de volgende stap” tenzij policy al flat toont.
- CTA disabled als mand leeg; primaire knop → `/afrekenen`.

## Lege staat

```
| Je mand is leeg.                    |
| [Naar de collectie]  → /collectie   |
```

## Notities anti-commercieel

- Geen countdown-druk of fake schaarste.
- Wel: “Je steunt maker en vrijplaats” als zachte lijn onder het overzicht (optioneel).

---
Vrijzaak · https://vrijzaak.nl · [00-index.md](./00-index.md)
