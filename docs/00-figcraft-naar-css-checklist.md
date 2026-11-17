# Checklist — FigCraft tekenen → CSS verwerken

Jij tekent en muteert in FigCraft. Daarna verwerken we dat **bewust** in `frontend/css/` (niet blind genereren).

```text
FigCraft (visueel)  →  export + figcraft_to_css.py  →  rapport
                              ↓
                    review → tokens.css / type.css / atoms.css
                              ↓
                         commit + (later) Nuxt
```

---

## Elke sessie (kort)

1. **Cmd+S** in FigCraft (`vrijzaak-storefront.figcraft`).
2. In Warp: *“verwerk FigCraft naar CSS”* of zelf:

```sh
export PATH="$HOME/.local/bin:$PATH"
cd "/Users/sjoerd/Documents/sproets/tycho/Vrijzaak/01 - Werkbestanden/Vrijzaak draadmodel"

# PNG previews
figcraft-cli export frontend/design/figcraft/vrijzaak-storefront.figcraft \
  -o frontend/design/exports/ --format png --scale 2

# Rapport styles/variables vs CSS
python3 frontend/design/figcraft/scripts/figcraft_to_css.py --write-report
```

3. Open rapport: `frontend/design/exports/figcraft-to-css-report.md`
4. Agent of jij past CSS aan → **git diff bekijken** → commit.

Optioneel light-kleuren auto-patch (alleen hex in `tokens.css`):

```sh
python3 frontend/design/figcraft/scripts/figcraft_to_css.py --apply-tokens
```

---

## Wat automatisch vergeleken wordt

| FigCraft | CSS |
|----------|-----|
| Theme variables (paper, ink, …) | `--vz-paper`, `--vz-ink`, … |
| Text styles `Type/H1`…`Body` | type-tokens 16/20-schaal |
| Font family | verwacht **GAP Code** |

## Wat jij/agent handmatig noteert

| FigCraft | CSS-bestand |
|----------|-------------|
| Nieuwe button-maten | `atoms.css` `.vz-btn` |
| Field, nav, header | `molecules.css` / `organisms.css` |
| Page layout | `layout.css` of later Nuxt |

Vul de tabel in het rapport of zeg het in chat.

---

## Richting van sync

| Situatie | Richting |
|----------|----------|
| Tokens/CSS net afgesproken | CSS → FigCraft (`sync-css-to-figcraft.jsonl`) |
| Jij hebt visueel iets beters gemaakt | FigCraft → rapport → CSS (`figcraft_to_css.py`) |
| Conflict | Bespreek; implementatie-SoT voor shop blijft CSS/Nuxt |

---

## Bestanden

| Pad | Rol |
|-----|-----|
| `frontend/design/figcraft/vrijzaak-storefront.figcraft` | Master design |
| `frontend/design/exports/*.png` | Previews |
| `frontend/design/exports/figcraft-to-css-report.md` | Laatste rapport |
| `frontend/design/figcraft/scripts/figcraft_to_css.py` | Reverse tool |
| `frontend/design/figcraft/scripts/sync-css-to-figcraft.jsonl` | CSS → FigCraft |
| `frontend/css/*` | Moleculen-cascade |

---

## Zeg tegen de agent

- “Verwerk FigCraft naar CSS”
- “Export PageDesignSystem / Desktop”
- “Pas atoms toe op nieuwe knop X”

Zie ook [00-css-figcraft-sync.md](./00-css-figcraft-sync.md) · [00-figcraft-samenwerking.md](./00-figcraft-samenwerking.md).
