# Sessie 2026-11-17 — CLI-toon, radius, schaduw, mono-tracking

## Context

Gebruiker vulde `docs/00-merk-toon-en-principes.md` in (CLI/terminal-richting) en vroeg om het document **logisch en consequent** te maken, met hardere regels:

- radius **max 4px**, forms geen Bootstrap-gevoel
- **geen** (of bijna onzichtbare) shadows
- letter-spacing op mono: **0**, of bewust als tracked label (`S P A C E`)
- sfeer dichter bij **Solarized / terminal themes**; metafoor **pen & papier weg**

## Gedaan

1. Herschreven: [00-merk-toon-en-principes.md](./00-merk-toon-en-principes.md)  
   - CLI/TUI-sfeer, Solarized-referenties, harde vormregels, mono-tracking-policy, checklist, besluitenlog, open punten.
2. CSS gelijkgetrokken:
   - `frontend/css/tokens.css` — radius sm/md/lg/xl = 0 / 2 / 4 / 4; `--vz-shadow-soft: none` (light+dark+system); `--vz-tracking-normal` / `--vz-tracking-display`
   - `frontend/css/atoms.css` — knop tracking 0; inputs `border-radius: sm` (0)
   - `frontend/css/type.css` — geen negatieve/positieve decoratieve tracking op h1–h6; utility `.vz-track`
3. Docs: [00-design-tokens.md](./00-design-tokens.md) bijgewerkt (radius, shadow, tracking, toon-UI).

## Update: FigCraft + git

- `sync-css-to-figcraft.jsonl` → `style.update` + radius node.set
- `vrijzaak-storefront.figcraft`: styles uniek (18), tracking 0, buttons radius 2, swatches 4
- Export: `frontend/design/exports/PageDesignSystem.png` + styles-dump
- Commit/push op verzoek

## Niet gedaan

- (FigCraft cornerRadius was open; nu gedaan.)
- Hex-palette nog niet retuned naar een specifiek Solarized-theme (alleen houding + bestaande hex).
- Geen wijziging helling-webshop / bouw-`tokens.ts`.
- Geen commit/push tenzij gevraagd.

## Volgende (optioneel)

1. Preview: `frontend/css/preview.html` in browser controleren.
2. FigCraft radius ≤4 + tracking.
3. Commit/push ontwerprepo.
4. Programmeur: radius/shadow-beleid desgewenst in bouw meenemen.
