# 05 — Controle en betaling (stap 3) + Mollie

## Navigatie-omgeving

Kassa-header. Geen winkel-hoofdmenu. Voorwaarden-link bij checkbox volstaat i.p.v. volle footer.

## Doel

Laatste check, akkoord, door naar Mollie (iDEAL). Geen kaartgegevens op Vrijzaak-servers in deze fase.

## Inhoud stap “Betalen”

```
| Controleer je bestelling                           |
|                                                    |
| Gegevens          [Wijzig]                         |
|   Naam, adres, e-mail                              |
|                                                    |
| Verzending        [Wijzig]                         |
|   Methode · prijs · indicatie                      |
|                                                    |
| Betaling                                           |
|   ( • ) iDEAL                                      |
|   (   ) Andere methodes via Mollie (optioneel)     |
|                                                    |
| [ ] Ik ga akkoord met de voorwaarden *             |
|                                                    |
| Totaal te betalen (incl. btw): EUR …               |
|                                                    |
| [ Betaal veilig met iDEAL ]                        |
|                                                    |
| Powered by Mollie · Je wordt tijdelijk             |
| doorgestuurd om te betalen.                        |
```

## Na klikken op betalen

1. Server: order + reservering + payment_request (pending); daarna redirect Mollie hosted.
2. **Browser-return is geen betaalbewijs** (bouw payments). UI mag geen “betaald” tonen op return alleen.
3. Definitief paid via worker/webhook + serververificatie; daarna bevestigingsmail (`orders.confirmation`).
4. Return-paden:
   - open attempt + actieve hold → pending-UI + optioneel opnieuw Mollie-checkoutlink
   - geannuleerd / mislukt / verlopen → melding + opnieuw proberen
   - server-paid → happy bevestiging ([06-bevestiging.md](./06-bevestiging.md))

## Staten op terugkeer (vóór “bedankt, betaald”)

**Nog bezig / pending** (standaard na return)
```
| We wachten op bevestiging van je betaling…         |
| Dit duurt meestal maar een moment.                 |
| [Pagina vernieuwen]                                |
```
Geen belofte “het is gelukt” tot serverstatus paid.

**Geannuleerd**
```
| Je hebt de betaling afgebroken.                    |
| Je bestelling is nog niet betaald.                 |
| [Opnieuw betalen]  [Terug naar winkelmand]        |
```

**Mislukt**
```
| Betaling is niet gelukt.                           |
| Er is niets afgeschreven of het wordt teruggedraaid.|
| [Opnieuw proberen met iDEAL]                       |
```

## Mobiel

- Één grote primaire knop “Betaal met iDEAL”
- Summary inklapbaar erboven
- Akkoord-checkbox met link naar voorwaarden (niet alleen icon)

## Niet in deze fase

- Eigen betaalpagina bouwen
- Split payments naar makers in de UI van de klant (kan wél intern via Mollie Connect later)

---
Vrijzaak · https://vrijzaak.nl · [00-index.md](./00-index.md)
