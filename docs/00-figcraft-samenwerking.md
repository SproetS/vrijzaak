# FigCraft — samenwerken (ontwerp + agent/CLI)

Je ontwerpt in **FigCraft** (ArtCraft). Markdown + CSS in deze repo blijven de **afspraken**; FigCraft is het **visuele canvas**.  
CLI/MCP laat ons (mens + agent) frames inspecteren, exporteren en desgewenst meekijken.

FigCraft is **alpha** — werk op kopieën, pin exports in Git, reken niet op perfecte multiplayer-cloud.

---

## Rollen

| Wie | Tool |
|-----|------|
| Jij (UX) | FigCraft.app — tekenen, components, Light/Dark vars |
| Agent / CLI | `figcraft-cli` — export, info, scripts, MCP |
| Programmeur | PNG/SVG + `docs/` + `frontend/css` → Nuxt |

---

## Als je Framer + CSS kent (deze workflow)

| Jij kent | Hier |
|----------|------|
| Framer canvas / breakpoints | FigCraft frames (Desktop 1440, later Mobile) |
| Framer components | FigCraft components + variants |
| CSS variables / themes | FigCraft variables Light/Dark ≈ `data-theme` in `tokens.css` |
| Spacing in CSS | V: 20px-basislijn · H: 4/16/32 (`frontend/css`) |
| Klassen `.btn` | Moleculen `.vz-btn` — agent helpt mapping |
| “Publish” naar web | Bij ons: **export PNG/SVG + Git** + Nuxt (geen Framer-site) |

Je hoeft de CLI niet uit je hoofd te leren. **Jij ontwerpt; de agent exporteert, checkt en stuurt bij.**

### Meesturen in de praktijk (simpel)

**Modus A — opslaan + agent kijkt mee (aanbevolen start)**  
1. Jij werkt in FigCraft, **Cmd+S** regelmatig.  
2. Je zegt in Warp: “kijk even” / “export Desktop”.  
3. Agent doet `figcraft-cli info` / `export` op het bestand op schijf.  
4. Feedback in chat (layout, namen, tokens, moleculen).

**Modus B — live sturen (control-poort)**  
1. Jij start eenmaal:  
   `frontend/design/start-figcraft-collab.sh`  
   (opent FigCraft + poort **7979** + jouw storefront-file).  
2. Je zegt: “poort 7979 is open, stuur mee”.  
3. Agent attach’t en kan **in jouw open document** frames zetten (jij ziet het live).  
4. Jij blijft de designer: agent stelt voor, jij keurt goed of stuurt bij.

Poort = alleen op jouw Mac (`localhost`), geen cloud.

---

## Mappen in deze repo

```text
frontend/design/figcraft/     ← bron .figcraft (native)
frontend/design/exports/      ← PNG/SVG/PDF uit CLI (handoff)
frontend/css/                 ← moleculen-cascade (tokens … layout)
docs/                         ← gedrag, nomenclatuur, IA
```

**Naamgeving frames** bij voorkeur = page/organism-IDs:

- `PageWarehouse`, `PageCheckout`, `OrgQuoteBlock`, …
- of routes: `mand`, `afrekenen`, …

Zie [00-ui-moleculen.md](./00-ui-moleculen.md).

---

## CLI installeren (macOS)

App: `/Applications/FigCraft.app`  
CLI (eenmalig), bv. release-zip →:

```sh
mkdir -p ~/.local/bin
# pad naar uitgepakte binary:
cp /pad/naar/figcraft-cli ~/.local/bin/figcraft-cli
chmod +x ~/.local/bin/figcraft-cli
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc   # indien nog niet
figcraft-cli --version
```

Hulp: `figcraft-cli --help` · subcommands: `info`, `export`, `render`, `convert`, `run`, `commands`, `mcp`.

---

## Dagelijkse workflow

### 1. Jij tekent

1. Open FigCraft → bestand opslaan als  
   `frontend/design/figcraft/vrijzaak-storefront.figcraft` (of per feature een file).  
2. Frames/pages labelen als hierboven.  
3. Variables: Light/Dark (sluit aan op `data-theme` in CSS).  
4. Commit `.figcraft` als het team dat wil (binair; of alleen exports committen).

### 2. Export voor GitHub / programmeur

```sh
cd "/pad/naar/Vrijzaak draadmodel"
mkdir -p frontend/design/exports

# Overzicht document
figcraft-cli info frontend/design/figcraft/vrijzaak-storefront.figcraft

# Alle top-level frames → PNG @2x
figcraft-cli export frontend/design/figcraft/vrijzaak-storefront.figcraft \
  -o frontend/design/exports/ \
  --format png --scale 2

# Eén frame SVG (vector-handoff)
figcraft-cli export frontend/design/figcraft/vrijzaak-storefront.figcraft \
  -o frontend/design/exports/PageCheckout.svg \
  --node "PageCheckout" --format svg
```

Exports koppelen in de bijbehorende `docs/0x-….md` of issue.

### 3. Samen met agent (optioneel)

**Headless** (geen venster — scripts/CI):

```sh
figcraft-cli mcp \
  --automation-read-root "$PWD" \
  --automation-write-root "$PWD/frontend/design"
```

**Live meekijken** (jij hebt het bestand open):

```sh
# Terminal 1 — app met control-poort (alleen localhost)
open -a FigCraft   # of:
# /Applications/FigCraft.app/Contents/MacOS/FigCraft --control 7979

# Terminal 2
figcraft-cli mcp --attach 7979
```

In Warp/Claude: MCP-server `figcraft` met command `figcraft-cli` args `mcp` (of attach-variant).  
Gebruik **absolute path** naar `~/.local/bin/figcraft-cli` in GUI-clients.

Beperk altijd read/write roots tot deze ontwerprepo (of `frontend/design`), niet heel `$HOME`.

---

## Wat wél / niet in Git

| Wel | Niet verplicht / voorzichtig |
|-----|------------------------------|
| `frontend/design/exports/*.png` (gecomprimeerd) | Gigantische @4x dumps |
| SVG van iconen/frames | Elk tussen-export |
| Korte note in docs + frame-namen | Alleen `.figcraft` zonder exports (collega zonder FigCraft ziet niks) |
| `.figcraft` als bron (teamafspraak) | Secrets in collab-server |

---

## Koppeling CSS / moleculen

| FigCraft | Repo |
|----------|------|
| Color variables Light/Dark | `frontend/css/tokens.css` `data-theme` |
| Text 16 / leading 20 | `tokens.css` + `type.css` |
| Components | `atoms` / `molecules` / `organisms` classes `.vz-*` |
| Auto layout spacing | V: ×20px · H: ×4 (ankers 4/16/32) |

Dev Mode code-export uit FigCraft = **schets**; Nuxt volgt bouwcontract + onze cascade.

---

## Alpha-realiteit

- Multiplayer/cloud is preview — liever Git + exports.  
- `.fig` import best-effort.  
- Pin CLI-versie (`figcraft-cli --version`) in issues als iets breekt.  

---

## Gerelateerd

- [00-ui-moleculen.md](./00-ui-moleculen.md)  
- [00-design-tokens.md](./00-design-tokens.md)  
- [frontend/css/README.md](../frontend/css/README.md)  
- [frontend/design/README.md](../frontend/design/README.md)  
