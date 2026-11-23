# GAP Code — glyph-verzoek (UX)

**Context:** Vrijzaak-UI zoveel mogelijk uit **GAP Code** (eigen font, eigen rechten).  
Mono-advance overal **600/1000 = 0.6em = 1ch** (zelfde als letters), tenzij expliciet anders.

**Bron intentie:** font-grid, CLI-progress, labels, panels.  
**CSS-tokens nu:** `--vz-progress-glyph-*` in `frontend/css/tokens.css`.

---

## Regel voor alle nieuwe glyphs

1. **Zelfde advance** als `n` / `0` / spatie (600 UPM), ook box-drawing.  
2. **Regular + Bold** (Italic alleen als het vanzelf meekomt; UI gebruikt vooral Roman/Bold).  
3. Optisch gecentreerd in de cel op **16px** en **32px** (h1-schaal).  
4. Geen emoji-stijl; terminal/TUI, rustig.

---

## Prioriteit 1 — meteen nodig (progress + basis UI)

### Progress-cellen (liever échte blocks dan `=` / `-`)

| Glyph | Codepoint | Naam | Rol | Fallback nu |
|-------|-----------|------|-----|-------------|
| `█` | U+2588 | FULL BLOCK | progress full / solid bar | `=` / CSS-stripes |
| `░` | U+2591 | LIGHT SHADE | progress empty (zichtbaar “leeg”) | `-` `_` |
| `▒` | U+2592 | MEDIUM SHADE | 50% / busy texture | optioneel |
| `▓` | U+2593 | DARK SHADE | 75% stap | optioneel |
| `▌` | U+258C | LEFT HALF BLOCK | fine step / half cell | optioneel |
| `▄` | U+2584 | LOWER HALF BLOCK | half verticaal | optioneel |
| `▶` | U+25B6 | BLACK RIGHT-POINTING TRIANGLE | progress head / tip | `>` |
| of `▸` | U+25B8 | SMALL RIGHT TRIANGLE | compactere tip | `>` |

**Minimaal P1:** `█` `░` `▶` (of `▸`).

### Al aanwezig in de meeste mono’s — wél checken in GAP Code

| Glyph | Code | Rol |
|-------|------|-----|
| `[` `]` | U+005B/5D | progress frame, chips |
| `-` `_` `=` | | fallbacks |
| `>` `<` `^` `v` | | chevrons / sort |
| `*` `·` `•` | U+00B7 / U+2022 | bullets, wordmark `*` |
| `│` | U+2502 | vert. rule (nav `|` mag ASCII) |
| `…` | U+2026 | truncated labels |
| `–` `—` | U+2013/2014 | en/em dash labels |
| `€` | U+20AC | prijs (AtomPrice) |
| `®` | U+00AE | Vrijzaak® in schets |

---

## Prioriteit 2 — box drawing (panels, cards, tables)

Lichte set is genoeg; niet heel IBM-set hoeft.

### Hoeken

| Glyph | Code | uni | Rol |
|-------|------|-----|-----|
| `┌` | U+250C | uni250C | hoek linksboven |
| `┐` | U+2510 | uni2510 | hoek rechtsboven |
| `└` | U+2514 | uni2514 | hoek linksonder |
| `┘` | U+2518 | uni2518 | hoek rechtsonder |

### Lijnen

| Glyph | Code | Rol |
|-------|------|-----|
| `─` | U+2500 | horizontale lijn (header-rule, sectie) |
| `│` | U+2502 | verticale lijn |
| `┄` | U+2504 | dashed horizontaal (schets stippellijn onder nav) |
| `┆` | U+2506 | dashed verticaal (optioneel) |

### T-stukken / kruis (tabellen, split layout)

| Glyph | Code | Rol |
|-------|------|-----|
| `├` | U+251C | T links |
| `┤` | U+2524 | T rechts |
| `┬` | U+252C | T boven |
| `┴` | U+2534 | T onder |
| `┼` | U+253C | kruis |

### Dubbel (optioneel, “zwaarder” panel)

| Glyph | Code | Rol |
|-------|------|-----|
| `╔` `╗` `╚` `╝` | U+2554/7/A/D | dubbele hoeken |
| `═` `║` | U+2550/1 | dubbele lijnen |

Eerst **enkele** set afmaken; dubbel alleen als single saai voelt.

---

## Prioriteit 3 — UI-chrome & status

### Selectie / UI-controls in tekst

| Glyph | Code | Rol |
|-------|------|-----|
| `☑` | U+2611 | checked (of teken zelf) |
| `☐` | U+2610 | unchecked |
| `✓` | U+2713 | success / done |
| `✗` | U+2717 | error / remove (of `×` U+00D7) |
| `•` | U+2022 | list |
| `○` `●` | U+25CB/CF | radio leeg/vol |
| `◇` `◆` | U+25C7/C6 | loods/badge accent |
| `⚠` | U+26A0 | warning (spaarzaam) |
| `ℹ` | U+2139 | info (spaarzaam) |

### Navigatie / disclosure

| Glyph | Code | Rol |
|-------|------|-----|
| `‹` `›` | U+2039/A | breadcrumb / pager |
| `«` `»` | U+00AB/BB | pager hard |
| `▾` `▸` | U+25BE/B8 | expand/collapse |
| `↑` `↓` | U+2191/3 | sort |
| `→` | U+2192 | “naar kassa” inline |
| `↩` | U+21A9 | terug (optioneel) |

### Spinners (ASCII-achtig, animeerbaar in CSS)

Liever **één** slot met wisselende glyphs of bestaande `/` `-` `\` `|` :

| Glyph | Code | Rol |
|-------|------|-----|
| `⠋` … of simpel | braille spinners | busy (optioneel zwaar) |
| of behoud | `\|` `/` `-` `\` | AtomSpinner frames |

Braille-spinners (`U+2800+`) alleen als je ze toch mooi tekent; anders ASCII volstaat.

---

## Prioriteit 4 — winkel / content (nice)

| Glyph | Code | Rol |
|-------|------|-----|
| `°` | U+00B0 | maten |
| `±` | U+00B1 | toleranties |
| `×` | U+00D7 | “2 × product” |
| `÷` | U+00F7 | zeldzaam |
| `≤` `≥` | U+2264/5 | filters |
| `∞` | U+221E | oneindig stock? spaarzaam |
| `†` `‡` | U+2020/1 | footnotes copy |
| `※` | U+203B | noot / “in de loods” mark (of eigen) |
| `□` | U+25A1 | image placeholder 1:1 frame |
| `▣` | U+25A3 | selected tile |

---

## Bewust *niet* (tenzij je ze wilt)

- Hele block-element set U+2580–259F (behalve P1)
- Hele box-drawing heavy/double/arc (U+2550–2570 bulk)
- Emoji / color emoji
- Private-use alleen als Unicode-equivalent ontbreekt; documenteer dan PUA-code

---

## Aanbevolen tekensvolgorde (praktisch tekenen)

1. `█ ░ ▶` (of `▸`)  
2. `─ │ ┌ ┐ └ ┘`  
3. `├ ┤ ┬ ┴ ┼`  
4. `┄` (stippellijn header)  
5. `✓ ✗ × • · … – — € ®`  
6. `☐ ☑ ○ ● ▾ › →`  
7. Halve blocks / shades / double box  

---

## CSS-mapping (na font-update)

```text
--vz-progress-glyph-full: "█";
--vz-progress-glyph-empty: "░";
--vz-progress-glyph-head: "▶";
```

Panels later bv. class `.vz-box` met `::before` content uit hoeken, of echte tekstnodes in FigCraft/HTML.

---

## Checklijst per glyph

- [ ] Advance = 600  
- [ ] Regular (+ Bold)  
- [ ] 16px UI leesbaar  
- [ ] 32px (h1-schaal) niet “gebroken”  
- [ ] Light + dark (glyph zelf is 1-bit; kleur = CSS `color`)  
- [ ] Geen overlap met bestaande contouren  

---

*Uitgebreid 2026-11-21 — UX-first Unicode-lijst voor GAP Code.*


## Export-check Regular (2026-11-23)

In `frontend/fonts/GAP Code/GAPCode-Regular.ttf` o.a. aanwezig:
`█ ░ ☐ ☑ ○ ● ✓ ✗ ⚠ 🛒 ┌┐└┘─│ ▸ ▾` …

Nog niet / dun: `▶ ▓`, pijlen `→←↑↓`, lock, Bold UX-set.

CSS tokens + preview gebruiken de aanwezige glyphs (`frontend/css/tokens.css`).
