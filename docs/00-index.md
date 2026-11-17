# Vrijzaak — ontwerpverslag

**Werknaam:** Vrijzaak  
**URL:** https://vrijzaak.nl  
**Ontwerprepo:** https://github.com/SproetS/vrijzaak (`docs/` + `frontend/`)  
**Bouwrepo (collega):** Gitea helling `Vrijzaak/Vrijzaak` — lokaal `03 - Bouw/webshop`

Plain Markdown: browsen in GitHub, VS Code, Warp of optioneel Obsidian. Wikilinks `[[…]]` zijn optioneel; overal ook relatieve links.

Start: [00-projectbrief.md](./00-projectbrief.md) · hub hieronder.

---

## Kern

| Document | Inhoud |
|----------|--------|
| [00-projectbrief.md](./00-projectbrief.md) | Opdracht, rollen, fase |
| [00-projectbeschrijving-en-stappenplan.md](./00-projectbeschrijving-en-stappenplan.md) | Beschrijving + fasen |
| [00-projectmap.md](./00-projectmap.md) | Mappen en twee-repo-model |
| [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md) | **Bouwdocs → ontwerptaal** (Nuxt/routes/klantreis/tokens) |
| [00-inventaris-bouw-ui.md](./00-inventaris-bouw-ui.md) | Pagina’s + componenten uit bouwrepo (SoT UI-structuur) |
| [00-tech-traject.md](./00-tech-traject.md) | Stack Nuxt + Directus + Mollie |
| [00-navigatie-omgevingen.md](./00-navigatie-omgevingen.md) | Winkel vs kassa vs voet |
| [00-design-tokens.md](./00-design-tokens.md) | GAP-fonts, greyscale; vs bouw-tokens |
| [00-git-en-github.md](./00-git-en-github.md) | Ontwerp-GitHub |
| [00-sessie-2026-11-17-bouwdocs-in-ontwerp.md](./00-sessie-2026-11-17-bouwdocs-in-ontwerp.md) | Sessieverslag |
| [../AGENTS.md](../AGENTS.md) | Agent-regels |

---

## Checkout-draadmodellen

| Note | Inhoud |
|------|--------|
| [01-winkelwagen.md](./01-winkelwagen.md) | Mand (`/mand`) |
| [02-checkout-overzicht.md](./02-checkout-overzicht.md) | Flow desktop/mobiel (`/afrekenen`) |
| [03-gegevens.md](./03-gegevens.md) | Adres / gast-account |
| [04-verzending.md](./04-verzending.md) | Pakket vs kunst |
| [05-betaling.md](./05-betaling.md) | Mollie / iDEAL (return ≠ paid) |
| [06-bevestiging.md](./06-bevestiging.md) | Happy bedankt na server-paid |
| [07-rekensom.md](./07-rekensom.md) | Btw, korting, verdeling |
| [08-componenten-en-staten.md](./08-componenten-en-staten.md) | Blokken / states |

---

## Context winkel (samenvatting)

- Fysiek, B2C; gast + account  
- Vrijplaatsen + makers; eerlijke opbrengst (server-aandelen)  
- UX: vertrouwen, fijne kassa, geen schreeuw-commerce  
- Tech: **Nuxt + Directus 12 + PostgreSQL + Mollie** (bouw); ontwerp in deze repo  

---

## Ontwerpprincipes

1. Weinig frictie; mobiel één primaire CTA per stap  
2. Orderoverzicht desktop vast; mobiel inklapbaar  
3. Prijzen **incl. btw** in presentatie; bedragen van server; split maker/vrijplaats/winkel optioneel transparant  
4. Verzending mag slim achter de schermen  
5. Mollie-states in mensentaal; **pending tot server bevestigt**  
6. **Gescheiden nav:** winkel-browse ≠ kassa-focus ≠ voet-info  
7. Geen dummyprijzen of nep-koop-CTA’s alsof productie  

---

## Volgende stap (winkel vangen)

Volledig plan: [00-projectbeschrijving-en-stappenplan.md](./00-projectbeschrijving-en-stappenplan.md).

1. `09-sitemap-ia.md` — URL’s sluiten aan op catalogue-routes *(nog te schrijven)*  
2. `10-productmodel.md` — velden o.b.v. catalogue/Directus *(nog te schrijven)*  
3. Draadmodellen: home, listing, productdetail, maker, vrijplaats  
4. Account licht + footer-pagina’s  
5. Visuele UI-kit; fontbesluit Mono vs Zuid/Code  

---

## Open punten

- Font: ontwerp **GAP Code** (voorlopig); bouwcode mogelijk nog Mono tot sync  
- Exacte accenten en commerciële verzendtarieven  
- Split-explainer default open/dicht  
- Mollie-methodes naast iDEAL  
- Collega-toegang tot `SproetS/vrijzaak` en/of dunne pointer in bouw-`docs/ontwerp/`  
