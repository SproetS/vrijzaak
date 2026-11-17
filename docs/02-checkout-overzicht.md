# 02 — Checkout: overzicht

**Route (bouw):** `/afrekenen` · `app/pages/afrekenen.vue`  
**Ook:** `/bestellingen/:id` na submit · **OrderFulfilment** op statuspagina  
**Layout bouw:** **default** (nog geen NavKassa-shell)  
**Mapping:** [08-componenten-en-staten.md](./08-componenten-en-staten.md)

## Twee beelden (belangrijk)

| | **Bouw (SoT nu)** | **Ontwerp-draadmodel (richting UX)** |
|--|-------------------|--------------------------------------|
| Structuur | **Eén pagina** `/afrekenen` | Optioneel 3 stappen (gegevens → verzending → betalen) |
| Nav | default winkel-header | **NavKassa** (geen Collectie-afleiding) |
| Prijs | Pas na “Actueel voorstel aanvragen” (**quote**) | OrderSummary altijd zichtbaar nà quote |
| Verzending | Select **Ontvangst** ship/pickup uit options | Rijkere klassen/split-zending (zie 04) — toekomst |
| Betalen | Submit order → later Mollie hosted; return ≠ paid | Zelfde contract; copy in 05–06 |

Ontwerp mag stappen **visueel** clusteren; programmeur hoeft niet meteen routes `/afrekenen/gegevens` te maken tenzij afgesproken.

## Bouw-flow (as-is)

```
/mand  →  /afrekenen
            ├─ (optioneel) RecoverNotice: eerdere onzekere poging
            ├─ leeg? → link mand
            ├─ ContactAdresFieldset + OntvangstKeuze
            ├─ [ Actueel voorstel aanvragen ]  → QuoteBlok
            ├─ TermsCheckbox
            ├─ [ Bestelling plaatsen … ] / replay
            └─ success → /bestellingen/:id
```

API’s (bouw): CSRF, `/api/checkout/options`, `quote`, `submit`, `recover`.  
Client bewaart bij onzekerheid `commandId`/`quoteId` in `sessionStorage` (geen contact als bron van waarheid).

## Ontwerp-flow (3 stappen — optioneel bovenop)

```
(1) Gegevens  →  (2) Verzending  →  (3) Controle & betalen  →  [Mollie]  →  status/bevestiging
```

Zie [03-gegevens.md](./03-gegevens.md), [04-verzending.md](./04-verzending.md), [05-betaling.md](./05-betaling.md).  
Velden in 03/04 die **niet** in bouw staan = ontwerp-plus (issue met programmeur).

## Desktop layout (ontwerp-richting)

```
+------------------------------------------------------------------+
| [NavKassa: Logo · Kassa · Mand · Account · Terug naar winkel]   |
|                         [Stap x van 3]   ← alleen als multi-step |
+------------------------------------------------------------------+
|  +---------------------------+    +----------------------------+ |
|  | stap / formulier          |    | QuoteBlok / OrderSummary   | |
|  | ContactAdresFieldset      |    | regels, shipping, btw,     | |
|  | OntvangstKeuze            |    | totaal, expiresAt          | |
|  | …                         |    | optioneel SplitExplainer   | |
|  +---------------------------+    +----------------------------+ |
|  [Terug]  [Voorstel]  [Plaatsen / Betalen]                       |
+------------------------------------------------------------------+
```

## Mobiel

- Quote inklapbaar of onder formulier (bouw: gestapeld)
- Sticky primaire actie
- Eén CTA-focus

## Gast vs account

Bouw: checkout met e-mail in contact; account is apart `/account`.  
Ontwerp-copy mag “afrekenen als gast” houden; geen verplicht account.

## Navigatie-regels (contract)

- Geen client-bedragen als waarheid
- Prijswijziging / voorraad / 409 → nieuw voorstel, geen stille retry met andere payload
- Pending recover vóór nieuwe bestelling
- Na submit: statuspagina, niet meteen “betaald” tot server paid

## Componenten op deze flow

Zie tabel in [08](./08-componenten-en-staten.md) §B: RecoverNotice, ContactAdresFieldset, OntvangstKeuze, QuoteBlok, TermsCheckbox, CheckoutSubmit, later NavKassa / StepHeader / SplitExplainer.

---
Vrijzaak · https://vrijzaak.nl · [00-index.md](./00-index.md)
