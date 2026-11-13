# 06 — Bevestiging (na geslaagde betaling)

URL-voorstel: `/afrekenen/gelukt?order=…` (of order-token, geen zomaar opeenvolgende id in plain text)

## Navigatie-omgeving

Lichte **bedankt-chrome**: logo + eventueel Account; winkel-voetmenu mag kort terug (Contact, AV).  
Geen vol Collectie-menu verplicht — wel duidelijke CTA “Verder rondkijken in de winkel”.

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
|  | (eenvoudige balk of percentages — zie 07-rekensom)         |  |
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
- Duidelijk ordernummer (ook in mail hetzelfde)
- Concrete next steps, geen vaag “we verwerken het”
- Geen upsell-druk; hoogstens “meer van deze maker” als zachte link
- Toegankelijke contactroute

## Technische states

- Pagina alleen zinvol als order `paid` (of short pending met auto-refresh)
- Bij direct openen zonder betaling → nette fout of redirect wagen
- Mail: orderbevestiging parallel (niet wachten op mail om pagina te tonen)

## Mobiel

Zelfde hiërarchie; CTA’s full width; confetti/animatie optioneel later — niet nodig voor draadmodel.

---
Vrijzaak · https://vrijzaak.nl · [[00-index]]
