# 02 — Checkout: overzicht flow (desktop + mobiel)

URL-voorstel: `/afrekenen`

## Navigatie-omgeving

**Kassamenu alleen** — geen Collectie/Makers/Vrijplaatsen in de topbar.  
Escape: “Terug naar de winkel”. Footer weg of minimaal (Voorwaarden bij akkoord).  
Zie [00-navigatie-omgevingen.md](./00-navigatie-omgevingen.md).

## Doel

Eén vriendelijke flow van wagen → betaald, met zo weinig mogelijk hobbels. Gast standaard; account optioneel.

## Stappen (voorgesteld)

```
(1) Gegevens  →  (2) Verzending  →  (3) Controle & betalen  →  [Mollie]  →  (4) Bevestiging
```

Alternatief later: één lange pagina met ankers; voor draadmodel houden we **3 stappen + Mollie + bedankt**.

## Voortgangsindicator

```
Desktop:  o Gegevens  ---  o Verzending  ---  o Betalen
Mobiel:   Stap 2 van 3 · Verzending
```

## Desktop layout (alle checkout-stappen)

```
+------------------------------------------------------------------+
| Vrijzaak · Kassa     Winkelmand · Account · Terug naar winkel    |
|                         [Stap x van 3]                             |
+------------------------------------------------------------------+
|                                                                  |
|  +---------------------------+    +----------------------------+ |
|  |                           |    | Je bestelling          [v] | |
|  |  (stap-inhoud)            |    |                            | |
|  |                           |    | 1x Product …    EUR …      | |
|  |                           |    | 1x Product …    EUR …      | |
|  |                           |    |                            | |
|  |                           |    | Subtotaal       EUR …      | |
|  |                           |    | Korting         - EUR …    | |
|  |                           |    | Verzending      EUR … / —  | |
|  |                           |    | waarvan btw     EUR …      | |
|  |                           |    | ──────────────────         | |
|  |                           |    | Totaal incl. btw EUR …     | |
|  |                           |    |                            | |
|  |                           |    | [i] Hoe wordt de opbrengst | |
|  |                           |    |     verdeeld? (inklappen)  | |
|  +---------------------------+    +----------------------------+ |
|                                                                  |
|  [ Terug ]                              [ Verder / Betalen ]     |
+------------------------------------------------------------------+
```

## Mobiel layout

```
+-----------------------------+
| [← Winkel]  Kassa · Stap x/3 |
+-----------------------------+
| [ v Je bestelling  EUR … ]  |  <- inklapbaar, default dicht
|     (regels + totalen)      |     open bij eerste land of op tap
+-----------------------------+
|                             |
| (stap-inhoud full width)    |
|                             |
+-----------------------------+
| sticky onder:               |
| [ Primaire actie ]          |
| Terug                       |
+-----------------------------+
```

## Gast vs account

Bij start van checkout (boven gegevens):

```
| Afrekenen als gast (standaard)                    |
| of [Inloggen] / [Account maken] — optioneel       |
| “Je hoeft geen account. Wel handig voor later.”   |
```

Na inloggen: adresboek voorinvullen indien aanwezig.

## Vriendelijkheid (copy-richting)

- Knoppen: “Verder”, “Naar betalen”, niet “Submit order”.
- Geen verplichte nieuwsbrief.
- Fouten: “Dit veld hebben we nog nodig” i.p.v. alleen rood sterretje.
- Trust: “Veilig betalen via Mollie / iDEAL” pas op de betaalstap.

## Navigatie-regels

- Terug behoudt ingevulde data (session).
- Verversen mag draft behouden (session/local).
- Mand wijzigen tijdens checkout: terug naar wagen of inline edit later.

---
Vrijzaak · https://vrijzaak.nl · [[00-index]]
