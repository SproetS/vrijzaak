# Merk, toon en ontwerpprincipes — Vrijzaak

**Doel:** de *menselijke* wet voor look & feel en houding — naast de *technische* wet in tokens/CSS.  
Technische maten (hex, px, vars): [00-design-tokens.md](./00-design-tokens.md) en `frontend/css/`.

| Gerelateerd | Inhoud |
|-------------|--------|
| [00-design-tokens.md](./00-design-tokens.md) | Kleurrollen, type 16/20, V/H-grid, light/dark, radius ≤4 |
| [00-nomenclatuur-winkel.md](./00-nomenclatuur-winkel.md) | Etalage / Magazijn / Loods / Kassa, NL+EN |
| [00-navigatie-omgevingen.md](./00-navigatie-omgevingen.md) | Winkel vs kassa vs voet |
| [00-projectbrief.md](./00-projectbrief.md) | Opdracht en rollen |
| `frontend/css/` | Implementatie van het meetbare deel |

---

## 1. Waar Vrijzaak voor staat

Vrijzaak is de centrale, rustige plek waar werk van **makers** en **vrijplaatsen** te koop is — eerlijk over herkomst en opbrengst, zonder schreeuw-webshop. De kassa moet vertrouwen wekken; de etalage mag uitnodigen zonder te pushen.

**Visuele richting:** een moderne, frisse **CLI / terminal-UI** — helder raster, monospaced typografie, dunne randen, weinig opsmuk. Niet “punk-ASCII”, niet corporate SaaS, niet image-heavy marketing.

---

## 2. Toon — visueel

### Sfeer (kernwoorden)

| Wel | Liever niet |
|-----|-------------|
| Rustig, terminal-achtig, ambachtelijk digitaal | Schreeuwerig, neon, “deal site” |
| Eerlijk, helder, fris, ruim, verzorgde mono-typografie | Nep-schaarste, countdown, fake stock |
| Moderne CLI (denk Oh My Zsh, nette TUI) | Bootstrap-formulieren, dikke afronding, elevation-cards |
| Themes als Solarized, Deus, Apprentice, Catppuccin | Gamer-RGB, 100% zwart/wit, pure luxe-glitter |
| Tekst eerst; functioneel SVG; spaarzame motion | Image-heavy one-pagers, zware schaduwen |
| Humor waar het past | Dwangmatige “fun” of keiharde krakers-esthetiek |

### Ruimte en ritme

- **Verticaal:** basislijn **20px** — alles “op de lijn” (zie tokens).
- **Horizontaal:** module **4px**, ankers **4 / 8 / 16 / 32** (primair 4 → 16 → 32).
- Gevoel: *veel adem*, **1px-randen**, **geen of nagenoeg onzichtbare schaduw**. Diepte = border + contrast, niet box-shadow.
- Kassa: nóg rustiger (minder nav, meer focus op voorstel en primaire knop).

### Vorm: radius en schaduw (hard)

| Token-idee | Regel |
|------------|--------|
| **Radius** | **Maximaal 4px** overal. Formulieren en inputs: **0–2px** (scherp, CLI — géén Bootstrap-pill/card-gevoel). |
| **Schaduw** | **Uit**, of zo licht dat het in de browser nauwelijks telt. Geen elevation-stack, geen floating cards. |
| **Randen** | Dun (`1px`), rol `--vz-border` / line. Focus via **outline/ring**, niet via glow-shadow. |

CSS-SoT: `--vz-radius-sm: 0`, `--vz-radius-md: 2px`, `--vz-radius-lg/xl: 4px`; `--vz-shadow-soft: none`.

### Kleur (houding)

- Basis: **frisse terminal-palette** — zachte grond, leesbare tekstkleur, geen harde primary-blue SaaS.
- Accent: **één groen**, spaarzaam (CTA, focus, “in de loods”-badge).
- Referenties: [Solarized e.a. op terminalcolors.com](https://terminalcolors.com), [Catppuccin e.a. op terminalthemes.com](https://terminalthemes.com/themes/catppuccin-macchiato).
- **Light / dark:** zelfde *rollen* (grond, surface, tekst, muted, accent, line). Dark = diepere loods bij avond — geen gamer-RGB, geen pure `#000` / `#fff`.
- Token-*namen* in code mogen historisch `paper` / `ink` heten (bouw-aliassen); **in copy en sfeertekst** spreken we over terminal-grond / tekst of bg/text — **niet** over “pen en papier” als metafoor.
- Exacte hex: [00-design-tokens.md](./00-design-tokens.md).

### Typografie (houding)

- UI: **GAP Code** — monospaced, technisch-ambachtelijk.
- **Hiërarchie vooral via weight, caps/small-caps, kleur en witruimte** — zo min mogelijk via extreme schaal. Tussen `h1` en small body blijft het bereik bewust krap (terminal-achtig).
- Knoppen: **small caps** (CSS = waarheid; FigCraft ≈).
- Body: 16/20; geen dichte tekstmuren op productpagina’s.
- Tijds- en voortgangsbalken: ASCII-stijl mag.


### Hiërarchie (rank) en CLI-koppen

Functie bepaalt vorm. **Geen default ALL CAPS** op koppen.

| Rank | Rol | Weight | Style | Kleur | CLI-frame |
|------|-----|--------|-------|-------|-----------|
| **1** | Pagina-anker (`h1`) | bold | roman | ink | nee |
| **2** | Sectie (`h2`) | bold | roman | ink | `- Titel -` via `.vz-h--cli` |
| **3** | Sub (`h3`) | bold | *italic* | ink | `.vz-h--cli` optioneel |
| **4** | Lokaal (`h4`/`h5`) | bold | roman | ink | nee |
| **meta** | Labels (`h6`) | regular | *italic* | muted | nee |

- Sentence case in NL-UI.
- `.vz-rank-active` = spaarzaam **accent** (huidige kassa-stap).
- Zichtbaar getal (`.vz-h__index`) **alleen** in geordende flows (kassa), niet op etalage-titels.
- Tokens: `--vz-rank-*` in `tokens.css`; utilities `.vz-rank-1` … `.vz-rank-meta`.

### Progress (CLI)

Default: bracket-bar met accent-fill en tip `>` — sfeer `[=========>----------]`.

| Variant | Class | Gebruik |
|---------|-------|---------|
| Equals + tip | `.vz-progress` | laden, stappen, default |
| Hash | `.vz-progress--hash` | chunky / upload |
| Busy | `.vz-progress--busy` | onbekende duur (`prefers-reduced-motion` stil) |
| Glyph-string | `.vz-progress__glyphs` | echte `=`/`-` tekens (JS/server) |

Kleur: fill = accent · rest = line · brackets/meta = muted.  
Breedte: `--vz-progress-cols` (default 20). Waarde: `--vz-progress: 0–1` + `aria-valuenow`.  
Glyphs swappable via tokens; font-verzoek: [00-gap-code-glyph-verzoek.md](./00-gap-code-glyph-verzoek.md).

#### Letter-spacing (mono)

Monospace **heeft al vaste glyph-breedte**. Willekeurige `letter-spacing` (0.02–0.04em) oogt gauw “kapot” of mode-UI.

| Gebruik | Regel |
|---------|--------|
| Body, inputs, lopende UI | **`letter-spacing: normal` (0)** |
| Koppen | **Geen negatieve tracking** op mono |
| Small-caps knoppen | Default **0**; géén “iets ruimer voor de look” |
| Bewuste display-labels | Alleen met opzet: **tracked label** (visueel als `S P A C E` — ruime tracking *of* echte spaties), zeldzaam (eyebrow, sectielabel) |

Utility: `.vz-track` / `--vz-tracking-display` alleen waar bewust.

### Beeld en media

- UX-chrome zoveel mogelijk **SVG** (vector), in dezelfde terminal-esthetiek (eventueel Zuid later als display/icoon).
- Productbeeld: winkelier/redactie/fotografie (o.a. Photoshop); transparantie ok; **geen omlijning** (`border: 0` op het beeld).
- Alle productafbeeldingen **1:1** (vierkant).

### Motion

- Weinig; altijd `prefers-reduced-motion` respecteren.
- Wel toegestaan: spaarzame Nintendo-achtige GIFs; typewriter; knipperende cursor.
- Geen bounce-confetti op kassa tenzij bewust “happy” **ná server-paid**. Progress zoveel mogelijk ASCII/tekst.

---

## 3. Toon — verbaal (copy)

### Kern

- Nederlands default; Engels via toggle (geen “Dunglish” in NL-modus).
- Zaakmetaforen: **Etalage, Magazijn, Loods, Kassa, Winkelmand** — [nomenclatuur](./00-nomenclatuur-winkel.md).
- Loods ≠ Black Friday-taal. Wel: “In de loods”, “zachte prijs”; “laatste” alleen als waar.

### Register

| Situatie | Toon |
|----------|------|
| Etalage / home | Uitnodigend, kort, warm |
| Magazijn / product | Nuchter, feiten, maker/vrijplaats zichtbaar |
| Kassa | Duidelijk, geruststellend, geen upsell |
| Fout / pending betaling | Menselijk, geen paniek, wel eerlijk |
| Mail bevestiging | Dankbaar, concrete next steps |

### Voorbeelden (aan te vullen)

| Liever | Liever niet |
|--------|-------------|
| Naar de kassa | Proceed to checkout (in NL-UI) |
| Terug naar de winkel | Annuleer order (tenzij betaling mislukt) |
| … | … |

---

## 4. Ontwerpprincipes (checklist voor frames)

1. Eén primaire handeling per stap (zeker mobiel / kassa).
2. Server is baas over prijs en “betaald”.
3. Lege, laden, fout, succes — altijd een staat tekenen.
4. Geen dummyprijzen alsof live.
5. Toegankelijk: contrast, focus-ring, labels, tap ≥48px.
6. Winkel browsen ≠ kassa-focus (nav-omgevingen).
7. Tweede taal en dark mode meenemen bij “af”.
8. Radius ≤4px; schaduw uit/minimaal; mono-tracking alleen bewust.
9. Formulieren scherp (CLI), geen Bootstrap-card-esthetiek.

---

## 5. Wat Vrijzaak *niet* is

- Geen marketplace-lawaai
- Geen influencer-dropship look
- Geen verborgen kosten in de UI
- Geen Bootstrap-rondingen en elevation-UI
- Geen “pen & papier craft”-romantiek als merkverhaal (wel: terminal/Solarized-helderheid)

---

## 6. Referenties en anti-referenties

| Soort | Voorbeeld | Wat we overnemen / vermijden |
|-------|-----------|------------------------------|
| Wel | Solarized, nette terminal themes, Oh My Zsh-achtige helderheid | Rollen licht/donker, leesbaar contrast, één accent |
| Wel | Tekst-UI / TUI-ritme | Raster, mono, borders i.p.v. shadow |
| Niet | Bootstrap forms / Material elevation | Grote radius, soft shadows, floating cards |
| Niet | Deal-sites, confetti-checkout | Schaarse-UI, push-CTA’s |

*(Tabel mag groeien met concrete sites/apps.)*

---

## 7. Besluiten log

| Datum | Besluit | Door |
|-------|---------|------|
| 2026-11-17 | GAP Code UI; small caps op knoppen; grid 20 / 4-16-32; kleurrollen light/dark | team/ontwerp |
| 2026-11-17 | Sfeer = moderne CLI/terminal (Solarized e.a.); **geen** pen-papier-metafoor | ontwerp |
| 2026-11-17 | Rank 1–meta + CLI `- titel -` + AtomProgress equals/hash/busy | ontwerp |
| 2026-11-17 | Radius **max 4px** (forms 0–2); schaduw **none**; mono **letter-spacing 0** tenzij bewuste tracked labels (`.vz-track`) | ontwerp |

---

## 8. Open

- [ ] §1 alinea desgewenst in eigen woorden aanscherpen
- [ ] Copy-voorbeelden uitbreiden
- [ ] Referenties met concrete URLs/apps
- [ ] Palette hex dichter op gekozen terminal-theme (optioneel, tokens)
- [ ] Kort akkoord winkelier + programmeur
- [x] FigCraft cornerRadius ≤4 + tracking 0 gespiegeld (2026-11-17)

---

*Laatst aangescherpt: 2026-11-17 — CLI-toon consequent; maten in tokens/CSS.*
