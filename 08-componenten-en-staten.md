# 08 — Componenten en staten

## Herbruikbare blokken

1. **OrderSummary** — regels, korting, verzending, totaal, btw-regel, optioneel verdeling
2. **StepHeader** — stap x van 3 + titel
3. **Field** — label, input, hint, fout
4. **Price** — altijd “EUR x,xx” + “incl. btw” in context
5. **TrustLine** — Mollie / iDEAL
6. **SplitExplainer** — inklapbare opbrengstverdeling
7. **NavWinkel** — hoofdmenu Collectie | …
8. **NavKassa** — Kassa | Winkelmand | Account | Terug naar winkel
9. **NavVoet** — Contact | Over ons | AV | Privacy

## Globale staten

| Staat | Waar | Gedrag |
|-------|------|--------|
| Lege mand | Wagen | CTA naar winkel |
| Ongeldige korting | Wagen / checkout | Fout onder veld |
| Geen verzendoptie | Verzending | Blokkeer verder + uitleg |
| Mollie cancel/fail | Betalen | Opnieuw proberen |
| Mollie pending | Return | Wachten / refresh |
| Betaald | Bevestiging | Happy path |
| Uitverkocht tijdens checkout | Betalen / server | “Dit product is net niet meer beschikbaar” + terug mand |

## Desktop breakpoints (indicatief)

- Mobiel: < 768px — stacked, sticky CTA
- Desktop: summary vaste kolom rechts ca. 360px

## Toegankelijkheid

- Focusvolgorde logisch
- Fouten met tekst, niet alleen kleur
- Knoppen met duidelijke namen
- Voldoende tap targets op mobiel

## Koppeling met latere bouw

- SvelteKit (of andere) front + backend orders
- Mollie payments + webhooks
- Catalogus: product, btw-tarief, maker, vrijplaats, verzendklasse, verdeel-% 

---
Vrijzaak · https://vrijzaak.nl · [[00-index]]
