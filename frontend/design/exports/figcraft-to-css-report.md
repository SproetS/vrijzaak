# FigCraft → CSS rapport

Gegenereerd: 2026-11-17 19:00 UTC  
Bron: `frontend/design/figcraft/vrijzaak-storefront.figcraft`  
Tool: `frontend/design/figcraft/scripts/figcraft_to_css.py`

## Checklist (na tekenen)

1. [ ] FigCraft opgeslagen (Cmd+S)
2. [ ] Dit script gedraaid / agent gevraagd “verwerk FigCraft naar CSS”
3. [ ] Kleuren Light (en Dark) gecontroleerd
4. [ ] Type H1–Body vs 16/20-basislijn
5. [ ] Nieuwe component-maten (btn, field) genoteerd → `atoms.css`
6. [ ] Exports PNG in `frontend/design/exports/`
7. [ ] CSS-diff reviewed en gecommit
8. [ ] Optioneel: `sync-css-to-figcraft.jsonl` opnieuw als CSS leidend blijft

## Variables (Theme)

| Name | Light | Dark | CSS light nu | Actie |
|------|-------|------|--------------|-------|
| `paper` | `None` | `None` | `#f5f2e9` | ok |
| `surface` | `None` | `None` | `#fffdf7` | ok |
| `ink` | `None` | `None` | `#202c27` | ok |
| `muted` | `None` | `None` | `#58645d` | ok |
| `accent` | `None` | `None` | `#245c43` | ok |
| `line` | `None` | `None` | `#b7c2b5` | ok |
| `danger` | `None` | `None` | `#8f4a4a` | ok |
| `success` | `None` | `None` | `#2f6b4f` | ok |
| `ctaText` | `None` | `None` | `#fffdf7` | ok |

## Text styles

| Style | font | size | leading | fill | vs tokens |
|-------|------|------|---------|------|-----------|
| `Type/H1` | None | None | None | None | wijkt af van type.css (verwacht 40/40) |
| `Type/H2` | None | None | None | None | wijkt af van type.css (verwacht 32/40) |
| `Type/H3` | None | None | None | None | wijkt af van type.css (verwacht 24/40) |
| `Type/H4` | None | None | None | None | wijkt af van type.css (verwacht 20/40) |
| `Type/H5` | None | None | None | None | wijkt af van type.css (verwacht 18/20) |
| `Type/H6` | None | None | None | None | wijkt af van type.css (verwacht 16/20) |
| `Type/Body` | None | None | None | None | wijkt af van type.css (verwacht 16/20) |

## Overige styles

- `Type/Button`
- `Type/ButtonGhost`
- `Type/Muted`
- `Type/Small`

## Voorgestelde CSS-patches (kleur light)

_Geen automatische kleurverschillen t.o.v. light-tokens._

## Handmatig (atoms / layout)

Na tekenen: noteer afwijkende maten hier of in de chat.

| Component | FigCraft frame | gemeten (px) | CSS-target |
|-----------|----------------|--------------|------------|
| Primary button | Btn/Primary | h=? pad-x=? radius=? | `.vz-btn` |
| Ghost button | Btn/Ghost | | `.vz-btn--ghost` |
| Field | | | `.vz-field` / `.vz-input` |
| Header | | | `.vz-site-header` |

## Commando’s

```sh
# rapport
python3 frontend/design/figcraft/scripts/figcraft_to_css.py --write-report

# alleen light color props in tokens.css bijwerken (review git diff!)
python3 frontend/design/figcraft/scripts/figcraft_to_css.py --apply-tokens

# export previews
figcraft-cli export frontend/design/figcraft/vrijzaak-storefront.figcraft \
  -o frontend/design/exports/ --format png --scale 2
```

Zie ook [docs/00-css-figcraft-sync.md](../../../docs/00-css-figcraft-sync.md).
