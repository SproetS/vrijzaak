# AGENTS.md — Vrijzaak (ontwerp)

## Project

Ontwerpverslag webwinkel **Vrijzaak** (https://vrijzaak.nl): UX, kassa, IA.  
Codebase van de winkel = **aparte** repo (Nuxt 4 + Directus 12 + PostgreSQL + Mollie).  
Deze repo = Markdown + lichte frontend-assets alleen.

### Drie rollen (team)

| Rol | Focus |
|-----|--------|
| **Ontwerper / UX** (deze vault) | Flows, vormgeving, copy, component- en pagina-inventaris voor design |
| **Zakelijk leider / winkelier** | Producten, klanten, commerciële policy, operationeel |
| **Programmeur** | Nuxt/Directus-monorepo, routing, checkout, workers |

**Source of truth techniek:** Gitea-bouwrepo (helling) voor routes, checkout, API, tokens in code. Ontwerp wijzigt die niet stilzwijgend.

## Structuur

```
/ AGENTS.md, README.md
/ docs/       ← Markdown ontwerp (start: docs/00-index.md)
/ frontend/   ← CSS-proeven, fonts placeholder, logos, svg
```

Browsen: gewone `.md`-links. Obsidian optioneel, niet vereist.

## Bron van waarheid (volgorde)

1. `docs/00-index.md`
2. `docs/00-bouwcontract-ontwerp.md` — afstemming op bouwcontracten
2b. `docs/00-inventaris-bouw-ui.md` — pagina’s/componenten uit bouw
3. `docs/00-projectbrief.md`
4. `docs/00-projectbeschrijving-en-stappenplan.md`
5. `docs/00-navigatie-omgevingen.md`
6. `docs/00-design-tokens.md`
7. `docs/00-tech-traject.md`
8. `docs/01`–`docs/08` checkout-draadmodellen

## Waar schrijven

| Wat | Waar |
|-----|------|
| Draadmodellen, IA, brief | `docs/` |
| tokens-proef, logo, svg | `frontend/` |
| Agent-regels | root `AGENTS.md` |
| Bouwcode / Directus | **niet hier** — helling webshop |

## Niet doen tenzij gevraagd

Deploy, secrets, zware binaries, fonts zonder licentie, destructief wissen, upsell-copy, stilzwijgend de bouwrepo aanpassen.

## Design

- Routes mand/checkout: `/mand`, `/afrekenen`, `/bestellingen/:id`
- Nav: winkel ≠ kassa ≠ voet
- Totalen en paid-status van **server**; return Mollie ≠ betaald
- Font ontwerp **voorlopig GAP Code**; bouwcode kan nog GAP Mono hebben tot programmeur sync’t
- Inventaris UI: `docs/00-inventaris-bouw-ui.md`
- Geen dummyprijzen/koop-CTA alsof live

## Nieuwe docs

In `docs/`, link vanuit `docs/00-index.md`, open punten expliciet. Relatieve markdown-links voorkeur naast eventuele wikilinks.
