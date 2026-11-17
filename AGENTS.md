# AGENTS.md — Vrijzaak (ontwerp)

## Project

Ontwerpverslag webwinkel **Vrijzaak** (https://vrijzaak.nl): UX, kassa, IA.  
Codebase van de winkel = **aparte** repo (Nuxt 4 + Directus 12 + PostgreSQL + Mollie).  
Deze repo = Markdown + lichte frontend-assets + Obsidian-vault.

### Drie rollen (team)

| Rol | Focus |
|-----|--------|
| **Ontwerper / UX** (deze vault) | Flows, vormgeving, copy, component- en pagina-inventaris voor design |
| **Zakelijk leider / winkelier** | Producten, klanten, commerciële policy, operationeel |
| **Programmeur** | Nuxt/Directus-monorepo, routing, checkout, workers |

**Source of truth techniek:** Gitea-bouwrepo (helling) voor routes, checkout, API, tokens in code. Ontwerp wijzigt die niet stilzwijgend.  
**Source of truth ontwerpintentie:** deze repo (`docs/`, wireframes, copy, fontkeuze).

## Structuur

```
/ AGENTS.md, README.md
/ .obsidian/  ← vault (app/appearance/core-plugins in git; workspace lokaal)
/ docs/       ← Markdown ontwerp (start: docs/00-index.md)
/ frontend/   ← CSS-proeven, fonts placeholder, logos, svg
```

## Lezen en schrijven

- **Obsidian:** open de **repo-root** als vault. Wikilinks `[[…]]` zijn welkom.
- **GitHub.com:** collega’s lezen via relatieve markdown-links (README + `docs/00-index.md`). Wikilinks alleen zijn niet genoeg op github.com.
- Houd **relatieve** `[tekst](./bestand.md)`-links in kern-docs voor GitHub en agents.
- Nieuwe notes: in `docs/`, link vanuit `docs/00-index.md`, open punten expliciet.

## Bron van waarheid (volgorde voor agents)

1. `docs/00-index.md`
2. `docs/00-bouwcontract-ontwerp.md` — afstemming op bouwcontracten
3. `docs/00-inventaris-bouw-ui.md` — pagina’s/componenten uit bouw (SoT UI-structuur)
4. `docs/00-projectbrief.md`
5. `docs/00-projectbeschrijving-en-stappenplan.md`
6. `docs/00-navigatie-omgevingen.md`
6b. `docs/00-nomenclatuur-winkel.md`
7. `docs/00-design-tokens.md`
8. `docs/00-tech-traject.md`
9. `docs/01`–`docs/08` checkout-draadmodellen

## Waar schrijven

| Wat | Waar |
|-----|------|
| Draadmodellen, IA, brief, inventaris | `docs/` |
| tokens-proef, logo, svg | `frontend/` |
| Agent-regels | root `AGENTS.md` |
| Gedeelde Obsidian-instellingen | `.obsidian/` (geen workspace/plugins/themes committen tenzij gevraagd) |
| Bouwcode / Directus | **niet hier** — helling webshop / programmeur |

## Niet doen tenzij gevraagd

Deploy, secrets, zware binaries, fonts zonder licentie, destructief wissen, upsell-copy, stilzwijgend de bouwrepo aanpassen, force-push.

## Design

- Routes mand/checkout volgen **bouw**: `/mand`, `/afrekenen`, `/bestellingen/:id`
- UI-nomenclatuur zaak: **Etalage · Magazijn · Loods · Kassa · Winkelmand** (`docs/00-nomenclatuur-winkel.md`); niet “checkout/cart/sale” in klantcopy
- Nav-richting: winkel ≠ kassa ≠ voet (bouw heeft nu één `default`-shell)
- Totalen en paid-status van **server**; Mollie-return ≠ betaald
- Font ontwerp **voorlopig GAP Code**; bouw `tokens.ts` kan nog GAP Mono hebben tot programmeur sync’t
- Inventaris UI: `docs/00-inventaris-bouw-ui.md`
- Geen dummyprijzen/koop-CTA alsof live
