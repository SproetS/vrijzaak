# 03 — Gegevens (contact en adres)

**Bouw:** onderdeel van **één** pagina `/afrekenen` (geen aparte route).  
**Blok:** **ContactAdresFieldset** in `afrekenen.vue`  
**Layout:** **default** · zie [02-checkout-overzicht.md](./02-checkout-overzicht.md)

## Doel

Contact- en aflevergegevens van de koper (B2C), gekoppeld aan de server-quote/submit.

## Velden — bouw (SoT)

| Label (UI) | Model | Notes |
|------------|-------|--------|
| E-mail | `email` | verplicht, autocomplete email |
| Naam | `name` | één veld (niet voor/achternaam gesplitst) |
| Straat | `street` | |
| Huisnummer | `houseNumber` | |
| Postcode | `postalCode` | NL-pattern als land NL |
| Plaats | `city` | |
| Land | `country` | uit `options.countries` |
| Ontvangst | `delivery` | hoort bij “verzending”; zie [04](./04-verzending.md) — zelfde fieldset-flow in bouw |

Geen telefoon, geen apart factuuradres, geen “account maken” op deze pagina in bouw.

## Ontwerp-plus (niet in bouw — open met team)

- Telefoon optioneel  
- Voornaam / achternaam gesplitst  
- Factuuradres afwijkend  
- “Maak account met dit e-mail” op checkout  
- StepHeader “Stap 1 van 3”

Markeer in UI-kit als *plus*; implementatie alleen na afspraak met programmeur/winkelier.

## Validatie

- Bouw: HTML required + NL postcode pattern; server her-valideert bij quote/submit  
- Ontwerp: inline na blur mag; fouttekst in mensentaal

## Privacy-copy (ontwerp)

Korte regel onder het fieldset: gegevens voor bestelling/verzending — afstemmen met echte privacytekst.

## Componenten

| Ontwerp | Bouw |
|---------|------|
| Field | native `<label><input>` in pagina |
| ContactAdresFieldset | fieldset “Contact en adres” |
| NavKassa | nog default layout |

---
Vrijzaak · https://vrijzaak.nl · [00-index.md](./00-index.md)
