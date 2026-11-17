# Vrijzaak — ontwerpverslag

**Werknaam:** Vrijzaak  
**URL:** https://vrijzaak.nl  
**Ontwerprepo:** https://github.com/SproetS/vrijzaak (`docs/` + `frontend/`)  
**Bouwrepo (collega):** Gitea helling `Vrijzaak/Vrijzaak` — lokaal `03 - Bouw/webshop`

Obsidian-vault = **repo-root**. Ook plain Markdown op GitHub/editor. Wikilinks wél; kern-docs houden relatieve links voor agents/GitHub.

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
| [00-ui-moleculen.md](./00-ui-moleculen.md) | **Atomen · moleculen · organismen · pagina’s** |
| [00-tech-traject.md](./00-tech-traject.md) | Stack Nuxt + Directus + Mollie |
| [00-navigatie-omgevingen.md](./00-navigatie-omgevingen.md) | Winkel vs kassa vs voet |
| [00-nomenclatuur-winkel.md](./00-nomenclatuur-winkel.md) | Zaak-labels **NL+EN**; techniek Engels; paths wachten |
| [00-design-tokens.md](./00-design-tokens.md) | Maten: kleur, type, V/H-grid, thema |
| [00-merk-toon-en-principes.md](./00-merk-toon-en-principes.md) | **Toon, sfeer, copy-houding, principes** (CLI/terminal) |
| [00-git-en-github.md](./00-git-en-github.md) | Ontwerp-GitHub |
| [00-figcraft-samenwerking.md](./00-figcraft-samenwerking.md) | FigCraft + CLI/MCP samenwerken |
| [00-css-figcraft-sync.md](./00-css-figcraft-sync.md) | CSS-tokens → FigCraft styles/fonts |
| [00-figcraft-naar-css-checklist.md](./00-figcraft-naar-css-checklist.md) | FigCraft tekenen → CSS verwerken |
| [00-sessie-2026-11-17-bouwdocs-in-ontwerp.md](./00-sessie-2026-11-17-bouwdocs-in-ontwerp.md) | Sessieverslag bouwdocs |
| [00-sessie-2026-11-17-cli-toon-css.md](./00-sessie-2026-11-17-cli-toon-css.md) | Sessieverslag CLI-toon + CSS |
| [../AGENTS.md](../AGENTS.md) | Agent-regels |

---

## Checkout-draadmodellen

Gekoppeld aan bouw-componenten/routes (zie ook [08](./08-componenten-en-staten.md) en [inventaris](./00-inventaris-bouw-ui.md)). Bouw = één pagina `/afrekenen`; 3 stappen blijven UX-optie.


| Note | Inhoud |
|------|--------|
| [01-winkelwagen.md](./01-winkelwagen.md) | Winkelmand (`/mand`) |
| [02-checkout-overzicht.md](./02-checkout-overzicht.md) | **Kassa** (`/afrekenen`) |
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
- UX: vertrouwen, fijne **kassa**; vitrine-taal (Etalage/Magazijn/Loods); geen schreeuw-commerce  
- Tech: **Nuxt + Directus 12 + PostgreSQL + Mollie** (bouw); ontwerp in deze repo  

---

## Ontwerpprincipes

1. Weinig frictie; mobiel één primaire CTA per stap  
2. Orderoverzicht desktop vast; mobiel inklapbaar  
3. Prijzen **incl. btw** in presentatie; bedragen van server; split maker/vrijplaats/winkel optioneel transparant  
4. Verzending mag slim achter de schermen  
5. Mollie-states in mensentaal; **pending tot server bevestigt**  
6. **Gescheiden nav:** winkel (Etalage/Magazijn/Loods) ≠ **Kassa** ≠ voet-info  
8. UI tweetalig (NL default, EN toggle); code/keys Engels; URL-hernoem wacht op programmeur  
7. Geen dummyprijzen of nep-koop-CTA’s alsof productie  

---

## Volgende stap (winkel vangen)

Volledig plan: [00-projectbeschrijving-en-stappenplan.md](./00-projectbeschrijving-en-stappenplan.md).

1. `09-sitemap-ia.md` — IA met Etalage/Magazijn/Loods + bouwroutes *(nog te schrijven)*  
2. `10-productmodel.md` — velden o.b.v. catalogue/Directus *(nog te schrijven)*  
3. Draadmodellen: home, listing, productdetail, maker, vrijplaats  
4. Account licht + footer-pagina’s  
5. Visuele UI-kit; FigCraft radius ≤4; palette vs Solarized optioneel  

---

## Open punten

- Font: ontwerp **GAP Code** (voorlopig); bouwcode mogelijk nog Mono tot sync  
- Vorm: radius max 4px, shadow none, mono-tracking 0 (vault CSS); bouw sync open  
- Exacte accenten en commerciële verzendtarieven  
- Split-explainer default open/dicht  
- Mollie-methodes naast iDEAL  
- Collega-toegang tot `SproetS/vrijzaak` en/of dunne pointer in bouw-`docs/ontwerp/`  
