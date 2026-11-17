# GAP Code — glyph-verzoek (UX)

**Context:** Vrijzaak UI is monospaced (GAP Code, eigen font, bewerkbaar).  
Progress en TUI-chrome mogen **custom glyphs** gebruiken i.p.v. kale `=` / `-` als die optisch ongelijk zijn.

## Prioriteit 1 (progress)

Alle drie **zelfde advance width** (idealiter = figuur-/spatiebreedte van de mono).

| Werknaam | Rol | Huidige fallback | Gewenst |
|----------|-----|------------------|---------|
| `progress.full` | gevulde cel | `=` of block via CSS | vaste cel, leesbaar op 16px |
| `progress.empty` | lege cel | `-` / `_` | zelfde breedte, lichter/optisch leeg |
| `progress.head` | kop/tip in-progress | `>` | duidelijke “head”, centreerbaar op cel |

Optioneel later: half-full cellen (25/50/75%) voor fijnere stappen.

## Prioriteit 2 (chrome)

| Werknaam | Rol | Nu |
|----------|-----|-----|
| `rule.section` | sectiestreep in `- titel -` | ASCII `-` is ok |
| `bracket.left` / `bracket.right` | progress/panel frame | `[` `]` ok als mono klopt |

## Prioriteit 3 (later panels)

Box-drawing (`─ │ ┌ …`) alleen als bold/regular stabiel blijven op UI-corps.

## Techniek CSS

Tokens in `frontend/css/tokens.css`:

- `--vz-progress-glyph-full|empty|head`
- `--vz-progress-glyph-full-alt|empty-alt` (hash-variant)

Na font-update: codepoints of `content`/ligatures documenteren hier en in `fonts.css`.

## Check

- [ ] full/empty/head zelfde width in Regular + Bold
- [ ] Italic niet nodig voor progress-glyphs
- [ ] Light + dark leesbaar t.o.v. accent/line
- [ ] Geen clash met bestaande ASCII in GAP Code

*Aangemaakt 2026-11-17 — ontwerpverzoek aan fontmaker (zelfde persoon).*
