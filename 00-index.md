# Vrijzaak — ontwerpverslag (Obsidian-vault)

**Werknaam:** Vrijzaak  
**URL:** https://vrijzaak.nl  
**Vault:** deze map als Obsidian-folder openen.

Start ook via [[00-projectbrief]].

---

## Kern

- [[00-projectbrief]] — opdracht, rollen, wat “klaar” is voor deze fase
- [[00-projectbeschrijving-en-stappenplan]] — beschrijving + fasen (mens/agent)
- [[00-projectmap]] — mappen, vault, bouwbeeld
- [[AGENTS]] — regels voor AI-agents
- [[00-git-en-github]] — repo + GitHub-koppeling  
- [[00-navigatie-omgevingen]] — winkel vs kassa vs voet  
- [[00-design-tokens]] — GAP Zuid VG, GAP Code, greyscale + zachte accenten  
- [[00-tech-traject-svelte-directus]] — Svelte/CSS → Directus → Mollie (voor collega-winkelier)

---

## Checkout-draadmodellen

| Note | Inhoud |
|------|--------|
| [[01-winkelwagen]] | Mand |
| [[02-checkout-overzicht]] | Flow desktop/mobiel |
| [[03-gegevens]] | Adres / gast-account |
| [[04-verzending]] | Pakket vs kunst |
| [[05-betaling]] | Mollie / iDEAL |
| [[06-bevestiging]] | Happy bedankt |
| [[07-rekensom]] | Btw, korting, verdeling |
| [[08-componenten-en-staten]] | Blokken / states |

---

## Context winkel (samenvatting)

- Fysiek, B2C; gast + account  
- Vrijplaatsen + makers; eerlijke opbrengst  
- UX-focus: vertrouwen, fijne kassa, geen schreeuw-commerce  
- Tech-achterhoofd: **Svelte + CSS tokens + Directus**

---

## Ontwerpprincipes

1. Weinig frictie; mobiel één primaire CTA per stap  
2. Orderoverzicht desktop vast; mobiel inklapbaar  
3. Prijzen **incl. btw**; rekensom leesbaar; split maker/vrijplaats/winkel als transparantie  
4. Verzending mag slim/complex achter de schermen  
5. Mollie-states in mensentaal  
6. **Gescheiden nav:** winkel-browse ≠ kassa-focus ≠ voet-info  

---

## Volgende stap (winkel vangen)

Volledig fasenplan: [[00-projectbeschrijving-en-stappenplan]].


1. [[09-sitemap-ia]] — URL’s + menu’s *(nog te schrijven)*  
2. [[10-productmodel]] — velden voor Directus *(nog te schrijven)*  
3. Draadmodellen: home, listing, productdetail, maker, vrijplaats  
4. Account licht + footer-pagina’s  
5. Visuele UI-kit (tokens + componenten) naast AI-ontwerp `.ai`  

Checkout + navigatie + brief/tokens/tech is een goede basis om aan de winkelier te tonen: “zo voelt kopen én beheren straks.”

---

## Open punten

- Exacte accent-hex  
- Verzendtarieven / pickup-vrijplaatsen  
- Split-explainer default open of dicht  
- Mollie-methodes naast iDEAL  
