# 05 — Controle, voorstel en betalen

**Bouw:** zelfde pagina `/afrekenen` na quote; daarna orderstatus `/bestellingen/:id` en Mollie hosted.  
**Blokken:** **QuoteBlok**, **TermsCheckbox**, **CheckoutSubmit**, **RecoverNotice** · later **TrustLine** / iDEAL-keuze

## Doel

Laatste check op **server-voorstel**, akkoord, order plaatsen, veilig betalen via Mollie.  
Geen kaartgegevens op Vrijzaak.

## Bouw-volgorde (as-is)

1. (Indien nodig) **RecoverNotice** — eerdere onzekere poging eerst afronden  
2. Contact + ontvangst ingevuld  
3. **Actueel voorstel aanvragen** → **QuoteBlok**  
4. **TermsCheckbox** — bevestig voorstel + opdracht tot bestellen  
5. **CheckoutSubmit** — test- of echte bestelling met betalingsverplichting / replay  
6. Navigate `/bestellingen/:id` — **nog niet** “betaald” tot server  
7. Mollie hosted wanneer payment-attempt dat vereist; **return ≠ paid**

## QuoteBlok (bouw-inhoud)

```
[testbanner als quote.testMode]

regels: titel × aantal — EUR … incl. btw  (+ korting bps indien)
shipping.label — EUR … incl. btw
Btw: … · Totaal: …
Geldig tot … (Europe/Amsterdam)
```

Ontwerp mag dit rechts als **OrderSummary** stylen; data = quote-DTO.

## Terms + submit (bouw-copy richting)

```
[ ] Ik bevestig dit prijsvoorstel en geef opdracht tot bestellen.

[ Bestelling plaatsen met betalingsverplichting ]
  of testvariant / “Dezelfde bestelling opnieuw controleren”
```

## iDEAL / Mollie (ontwerp-chrome)

Op wireframe mag:

```
Betaling: ( • ) iDEAL    TrustLine: Veilig via Mollie
```

Bouw: eerste methode iDEAL in payments-contract; UI op afrekenen is nu vooral order-plaatsen, niet een rijke methodenlijst.

## Staten na return / op orderpagina

| Staat | UI |
|-------|-----|
| Pending | Wachten / vernieuwen — geen confetti |
| Cancel / fail / expired | Opnieuw proberen, terug mand |
| Server paid | Happy bevestiging · mail `orders.confirmation` |

Zie [06-bevestiging.md](./06-bevestiging.md).

## Componenten

| Ontwerp | Bouw |
|---------|------|
| OrderSummary | QuoteBlok inline |
| TrustLine | copy / later component |
| StepHeader “Betalen” | optioneel; bouw single page |
| NavKassa | nog default |

---
Vrijzaak · https://vrijzaak.nl · [00-index.md](./00-index.md)
