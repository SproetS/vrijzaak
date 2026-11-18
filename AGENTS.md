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
**CSS-proef in browser** = echte look voor vault-UI; FigCraft ≈ spiegel, geen live CSS-engine.

## Structuur

```
/ AGENTS.md, README.md
/ .obsidian/  ← vault (app/appearance/core-plugins in git; workspace lokaal)
/ docs/       ← Markdown ontwerp (start: docs/00-index.md)
/ frontend/   ← CSS-proeven, fonts, logos, svg, FigCraft
```

## Lezen en schrijven

- **Obsidian:** open de **repo-root** als vault. Wikilinks `[[…]]` zijn welkom.
- **GitHub.com:** collega’s lezen via relatieve markdown-links (README + `docs/00-index.md`). Wikilinks alleen zijn niet genoeg op github.com.
- Houd **relatieve** `[tekst](./bestand.md)`-links in kern-docs voor GitHub en agents.
- Nieuwe notes: in `docs/`, link vanuit `docs/00-index.md`, open punten expliciet.
- Geen icons/emoji in Markdown-output van agents (gebruikersregel).
- Geen destructieve acties zonder expliciete toestemming.
- Commits: co-author regel `Co-Authored-By: Warp <agent@warp.dev>` als agent commit.
- Sessie-einde: kort verslag in `docs/00-sessie-…md` + index bijwerken.

## Bron van waarheid (volgorde voor agents)

1. `docs/00-index.md`
2. `docs/00-bouwcontract-ontwerp.md` — afstemming op bouwcontracten
3. `docs/00-inventaris-bouw-ui.md` — pagina’s/componenten uit bouw (SoT UI-structuur)
3b. `docs/00-ui-moleculen.md` — atomen / moleculen / organismen / pages
4. `docs/00-projectbrief.md`
5. `docs/00-projectbeschrijving-en-stappenplan.md`
6. `docs/00-navigatie-omgevingen.md`
6b. `docs/00-nomenclatuur-winkel.md`
7. `docs/00-design-tokens.md` — maten, rank, progress-tokens
7a. `docs/00-font-grid.md` — **GAP Code = raster** (start design-bepaling)
7b. `docs/00-merk-toon-en-principes.md` — sfeer CLI/terminal, rank, progress
7c. `docs/00-gap-code-glyph-verzoek.md` — font glyphs progress
8. `docs/00-tech-traject.md`
8b. FigCraft: `docs/00-figcraft-samenwerking.md`, `docs/00-css-figcraft-sync.md`
9. `docs/01`–`docs/08` checkout-draadmodellen
10. Recente sessies: `docs/00-sessie-2026-11-17-*.md`

## Waar schrijven

| Wat | Waar |
|-----|------|
| Draadmodellen, IA, brief, inventaris | `docs/` |
| tokens-proef, logo, svg, FigCraft | `frontend/` (`css/`, `design/figcraft`, `design/exports`) |
| Agent-regels | root `AGENTS.md` |
| Gedeelde Obsidian-instellingen | `.obsidian/` (geen workspace/plugins/themes committen tenzij gevraagd) |
| Bouwcode / Directus | **niet hier** — helling webshop / programmeur |

## Niet doen tenzij gevraagd

Deploy, secrets, zware binaries, force-push, destructief wissen, upsell-copy, stilzwijgend de **bouwrepo** (`03 - Bouw/webshop` / helling) aanpassen.

GAP Code = **eigen font** van de ontwerper (geen externe licentie-blokkade); wél glyph-verzoeken documenteren i.p.v. stilletjes aannemen dat box-drawing bestaat.

## Design (geldende afspraken)

- Routes mand/checkout volgen **bouw**: `/mand`, `/afrekenen`, `/bestellingen/:id`
- UI-nomenclatuur: zaaktaal **NL + EN** (Etalage/Magazijn/Loods/Kassa …); message keys en code **Engels**
- URL-hernoem Engels: **niet** door ontwerp; wacht op programmeur
- Nav: winkel ≠ kassa ≠ voet (bouw heeft nu één `default`-shell)
- Totalen en paid-status van **server**; Mollie-return ≠ betaald
- Font UI: **GAP Code** (bouw `tokens.ts` kan nog GAP Mono hebben tot programmeur sync’t)
- **CLI / terminal-toon** (Solarized-achtig): geen “pen & papier”-metafoor; token-namen `paper`/`ink` mogen technisch blijven
- **Font-grid:** GAP Code advance **0.6em** / line **1.2**; H in `ch`; V in `1.2rem`; 4px = legacy/radius only
- **Controls:** hoogte **1 V-stap** (tussen twee baselijnen); site-breed grid incl. header/footer
- Vorm: **radius max 4px**; **shadow none**
- Hiërarchie: h1 **2rem**; h2/h3 **1rem + tracking 1ch**; h3 **accent-warm**; h4 bold; labels muted track
  - Schets: `frontend/design/illustrator-exports/`
- Progress: `.vz-progress` (equals/hash/busy) — CLI brackets, accent-fill
- Knoppen: small-caps, tracking 0
- Geen dummyprijzen/koop-CTA alsof live
- Preview: `frontend/css/preview.html` · cascade `frontend/css/main.css`
- FigCraft: `frontend/design/figcraft/vrijzaak-storefront.figcraft` · sync `scripts/sync-css-to-figcraft.jsonl` (bij voorkeur `style.update`) · export `frontend/design/exports/`

## Stand van zaken (peil 2026-11-17)

### Af

- Bouwcontracten → ontwerp-Markdown; inventaris UI; moleculen-lijst; nomenclatuur NL+EN
- Checkout-draadmodellen 01–08 gekoppeld aan bouw
- CSS-cascade tokens → type → base → atoms → molecules → organisms → layout
- Merk-toon CLI; radius/shadow/tracking in CSS + FigCraft
- Rank + AtomProgress; FigCraft DS (eerdere avond)
- **Font-grid besluit:** metrics gemeten, tokens/type op cel/line; preview ≈ typo-schets
- GitHub ontwerp: `SproetS/vrijzaak` (main)

### Open / volgende sessie (prioriteit)

1. **Winkel-IA:** `09-sitemap-ia.md`, `10-productmodel.md` (nog te schrijven)
2. Draadmodellen buiten kassa: home, listing, product, maker, vrijplaats
3. **GAP Code glyphs:** `progress.full` / `empty` / `head` (gelijke breedte) — zie `docs/00-gap-code-glyph-verzoek.md`
4. Optioneel palette dichter op gekozen terminal-theme (hex nog bouw-paper/ink)
5. FigCraft: echte componenten/progress frames verfijningen; Theme-variabele binds
6. Programmeur: font Mono→Code, radius/shadow/rank sync naar Nuxt `tokens.ts` wanneer akkoord
7. Akkoord winkelier + programmeur op toon-doc (kort)
8. Collega-toegang GitHub / dunne pointer in bouw-`docs/ontwerp/`

### Niet oppakken zonder vraag

- Operatie Stofnest / andere shops
- loesmuzi / vexy-lines
- Live deploy of Mollie/productie-data

## Snel starten (nieuwe agent)

```text
1. Lees docs/00-index.md + deze AGENTS.md (stand van zaken).
2. Toon/maten: 00-merk-toon-en-principes.md + 00-design-tokens.md.
3. CSS-proef: frontend/css/preview.html (main.css).
4. FigCraft: frontend/design/figcraft/ + docs/00-css-figcraft-sync.md.
5. Bouw niet stilzwijgend wijzigen; ontwerprepo = SproetS/vrijzaak.
```

Laatste update: font-grid (GAP Code metrics) — 2026-11-18.
