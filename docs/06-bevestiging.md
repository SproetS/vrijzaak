# 06 — Bevestiging (na geslaagde betaling)

URL (bouw-richting): privé orderstatus **`/bestellingen/:id`** (scoped bewijs; noindex).  
“Gelukt”-chrome mag dezelfde route zijn zodra server **paid** (of equivalent confirmed na paid-effect) is — niet alleen Mollie-return.

## Navigatie-omgeving

Lichte **bedankt-chrome**: logo + eventueel Account; winkel-voetmenu mag kort terug (Contact, AV).  
Geen vol Collectie-menu verplicht — wel CTA “Verder rondkijken” → `/collectie`.

## Doel

Klant voelt: het is gelukt, ik word gezien, ik weet wat er nu gebeurt. “Happy” + rust.

## Desktop / mobiel structuur

```
+------------------------------------------------------------------+
| Vrijzaak                                                         |
+------------------------------------------------------------------+
|                                                                  |
|     Gelukt — bedankt voor je bestelling                          |
|                                                                  |
|     Hoi {voornaam},                                              |
|     Je steunt makers en vrijplaatsen. Dank je wel.               |
|                                                                  |
|     Ordernummer: VZ-1042                                         |
|     Bevestiging is gestuurd naar: jij@email.nl                   |
|                                                                  |
|  +------------------------------------------------------------+  |
|  | Wat gebeurt er nu?                                         |  |
|  | 1. We (en de maker/vrijplaats) zien je bestelling.         |  |
|  | 2. Je krijgt mail bij verzending of als ophalen klaar is.  |  |
|  | 3. Bij kunstwerken nemen we contact op als dat nodig is.   |  |
|  +------------------------------------------------------------+  |
|                                                                  |
|  +------------------------------------------------------------+  |
|  | Je bestelling                                              |  |
|  | 1x … EUR …                                                 |  |
|  | Verzending: …                                              |  |
|  | Totaal betaald incl. btw: EUR …                            |  |
|  +------------------------------------------------------------+  |
|                                                                  |
|  +------------------------------------------------------------+  |
|  | [optioneel open] Hoe de opbrengst landt                    |  |
|  | Eerlijk beeld: maker / vrijplaats / Vrijzaak / btw         |  |
|  | (server-aandelen; zie 07-rekensom)                         |  |
|  +------------------------------------------------------------+  |
|                                                                  |
|  [ Verder rondkijken in de winkel ]                              |
|  [ Account maken om bestellingen te volgen ]  (als gast)         |
|                                                                  |
|  Vragen? mail@vrijzaak.example                                   |
|                                                                  |
+------------------------------------------------------------------+
```

## Happy-makers (inhoud, geen opsmuk)

- Persoonlijke aanspreekvorm met naam indien bekend
- Duidelijk ordernummer (ook in mail hetzelfde) — ordernummer is **geen** toegangsbewijs
- Concrete next steps
- Geen upsell-druk; hoogstens zachte maker-link
- Toegankelijke contactroute

## Technische states (bouw)

- “Betaald / bedankt”-inhoud alleen bij **server-paid** (na stock-effect waar van toepassing)
- Return van Mollie zonder paid → pending-UI ([05-betaling.md](./05-betaling.md)), geen confetti
- Bevestigingsmail: job `orders.confirmation` na paid — pagina niet blokkeren op mailtransport
- Gast: later claimen via bewijs + verified account, niet stil op e-mailmatch
- Openen zonder bewijs → nette weigering, geen lek via voorspelbaar id

## Mobiel

Zelfde hiërarchie; CTA’s full width; animatie optioneel later — niet nodig voor draadmodel.

---
Vrijzaak · https://vrijzaak.nl · [00-index.md](./00-index.md)
