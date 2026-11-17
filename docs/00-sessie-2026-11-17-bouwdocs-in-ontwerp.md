# Sessie 2026-11-17 — Bouwdocs verwerkt in ontwerp-Markdown

## Context

- Ontwerprepo: GitHub `SproetS/vrijzaak` (deze vault), remote OK; lokaal was earlier 1 commit ahead.
- Bouwrepo: `03 - Bouw/webshop` → Gitea helling (niet gemengd met ontwerp).
- Vraag: collega-docs lezen en verwerken in ontwerp-Markdown; Obsidian-laag niet belangrijk; is dit logische voortgang?

## Besluit voortgang

**Ja, logisch:** eerst ontwerp gelijktrekken met bestaande bouwcontracten (routes, klantreis, tokens-spanning, stack), daarna pas nieuwe wireframes (sitemap/product) of CSS in Nuxt. Repo’s blijven gescheiden.

## Gedaan

1. Gelezen (bouw): architecture, commerce, catalogue, checkout, payments, identity, design, email, tokens.ts, workspace.
2. Nieuw: `docs/00-bouwcontract-ontwerp.md` — design-lens op bouwcontracten.
3. Nieuw: `docs/00-tech-traject.md`; oude Svelte-titel → stub `00-tech-traject-svelte-directus.md`.
4. Bijgewerkt: index, brief, stappenplan, projectmap, tokens, navigatie-paden, checkout 02/05/07/08, AGENTS, README’s, frontend README-verwijzingen waar nodig.
5. Wikilinks blijven optioneel; overal ook gewone relatieve `.md`-links voor browsen in GitHub/editor.

## Niet gedaan

- Geen bestanden in helling-webshop gewijzigd.
- Geen grote binaries, geen force-push.
- Geen volledige kopie van worker/security-docs (bewust).

## Volgende

1. Push ontwerprepo naar `origin/main` wanneer gewenst.
2. Fontbesluit Mono vs Zuid/Code.
3. Fase 1: `09-sitemap-ia.md` / `10-productmodel.md` o.b.v. catalogue-routes.
4. Optioneel dunne `docs/ontwerp/` pointer in webshop-repo (aparte afspraak met collega).


## Update later dezelfde dag

- Commit/push naar SproetS/vrijzaak aangevraagd.
- Font ontwerp **voorlopig GAP Code**.
- Team expliciet: ontwerper/UX, zakelijk leider/winkelier, programmeur; bouwrepo = SoT techniek.
- Inventaris: [00-inventaris-bouw-ui.md](./00-inventaris-bouw-ui.md).

### Draadmodellen × bouw-componenten

01–08 bijgewerkt: mapping naar default, useCart, QuoteBlok, OrderFulfilment, CatalogueList/PartyProfile in 08; bouw single-page checkout vs ontwerp 3-step expliciet.

### UI moleculen

Toegevoegd `docs/00-ui-moleculen.md` (atomic design: atoms/molecules/organisms/pages), gekoppeld aan bouw-SFC’s en i18n-nomenclatuur. Git stond al clean op i18n-nomenclatuur; deze commit pusht moleculen-lijst.
