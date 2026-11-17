# 08 — Componenten en staten

## Herbruikbare blokken

1. **OrderSummary** — regels, korting, verzending, totaal, btw-regel, optioneel verdeling
2. **StepHeader** — stap x van 3 + titel
3. **Field** — label, input, hint, fout
4. **Price** — altijd “EUR x,xx” + “incl. btw” in context (server-DTO)
5. **TrustLine** — Mollie / iDEAL
6. **SplitExplainer** — inklapbare opbrengstverdeling
7. **NavWinkel** — hoofdmenu Collectie | …
8. **NavKassa** — Kassa | Winkelmand | Account | Terug naar winkel
9. **NavVoet** — Contact | Over ons | AV | Privacy

## Globale staten

Bouw vraagt expliciet: laden, leeg, fout, niet beschikbaar, form valid/invalid, busy, succes (`docs/design.md` in webshop).

| Staat | Waar | Gedrag |
|-------|------|--------|
| Lege mand | `/mand` | CTA naar `/collectie` |
| Laden / busy | mand, checkout, return | Geen dubbele submit; bevries onzekere poging |
| Ongeldige korting | mand / checkout | Fout onder veld (server) |
| Quote verlopen / prijs gewijzigd | checkout | Nieuw voorstel + bevestiging |
| Geen verzendoptie | Verzending | Blokkeer verder + uitleg |
| Mollie cancel/fail/expired | return | Opnieuw proberen |
| Mollie pending | return | Wachten / refresh — geen “betaald” |
| Betaald (server) | bevestiging | Happy path + mail confirmation |
| Voorraadtekort | submit / paid-late | Duidelijke fout; geen halve order als succes |
| Lege zoek/collectie | listing | Eerlijke lege staat, geen nepproducten |

## Desktop breakpoints (indicatief)

- Mobiel: < 768px — stacked, sticky CTA, ≥44px targets
- Desktop: summary vaste kolom rechts ca. 360px

## Toegankelijkheid

- Focusvolgorde logisch; zichtbare focus; skiplink
- Fouten met tekst, niet alleen kleur
- Knoppen met duidelijke namen; geen nepknoppen
- Voldoende tap targets op mobiel

## Koppeling met bouw

- Nuxt `app/` + `shared/design/tokens.ts`
- Routes: catalogue + `/mand` + `/afrekenen` + `/bestellingen/:id`
- Mollie worker/webhooks; return ≠ paid
- Catalogus: variant, prijsrevisie, btw-code, partijen, media

Zie [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md).

---
Vrijzaak · https://vrijzaak.nl · [00-index.md](./00-index.md)
