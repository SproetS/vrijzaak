# Merk, toon en ontwerpprincipes — Vrijzaak

**Doel:** de *menselijke* wet voor look & feel en houding — naast de *technische* wet in tokens/CSS.  
Aanvullen in Obsidian; open punten expliciet laten staan.

| Gerelateerd | Inhoud |
|-------------|--------|
| [00-design-tokens.md](./00-design-tokens.md) | Kleur, type 16/20, V/H-grid, light/dark |
| [00-nomenclatuur-winkel.md](./00-nomenclatuur-winkel.md) | Etalage / Magazijn / Loods / Kassa, NL+EN |
| [00-navigatie-omgevingen.md](./00-navigatie-omgevingen.md) | Winkel vs kassa vs voet |
| [00-projectbrief.md](./00-projectbrief.md) | Opdracht en rollen |
| `frontend/css/` | Implementatie van het meetbare deel |

---

## 1. Waar Vrijzaak voor staat (één alinea)

*Invullen / aanscherpen:*

Vrijzaak is de centrale, rustige plek waar werk van **makers** en **vrijplaatsen** te koop is — eerlijk over herkomst en opbrengst, zonder schreeuw-webshop. De kassa moet vertrouwen wekken; de etalage mag uitnodigen zonder te pushen.

*(Jouw versie hieronder of vervang bovenstaande.)*

> …

---

## 2. Toon — visueel

### Sfeer (kernwoorden)

*Kies en rangschik; schrap wat niet klopt.*

| Wel | Liever niet |
|-----|-------------|
| Rustig, papierachtig, ambachtelijk digitaal | Schreeuwerig, neon, “deal site” |
| Eerlijk, helder, ruim | Nep-schaarste, countdown, fake stock |
| Vrijplaats-warmte, menselijk | Steriel corporate of pure luxe-glitter |
| … | … |

### Ruimte en ritme

- **Verticaal:** basislijn **20px** — alles “op de lijn” (zie tokens).  
- **Horizontaal:** module **4px**, ankers **4 / 16 / 32**.  
- Gevoel: *veel adem*, dunne randen, weinig zware schaduw.  
- Kassa: nóg rustiger (minder nav, meer focus op voorstel en knop).

### Kleur (houding, niet alleen hex)

- Basis: **papier + inkt** (warm off-white, donkergroen-zwart).  
- Accent: **één groen** — spaarzaam (CTA, focus, “in de loods”-badge).  
- Dark mode: zelfde rollen, diepere “loods bij avond” — geen gamer-RGB.  
- Exacte waarden: [00-design-tokens.md](./00-design-tokens.md).

### Typografie (houding)

- UI: **GAP Code** — technisch-ambachtelijk, monospaced karakter.  
- Koppen: zwaar genoeg om te dragen, niet schreeuwen.  
- Knoppen: **small caps** (CSS = waarheid; FigCraft ≈).  
- Body: leesbaar op 16/20; geen dichte muren tekst op productpagina’s.

### Beeld en media

*Nog in te vullen:*

- Fotografie: documentair / studio / maker-portret?  
- Illustratie: wel/niet?  
- Productbeeld: witte achtergrond of in context?  
- …

### Motion

- Weinig; `prefers-reduced-motion` respecteren.  
- Geen bounce-confetti op kassa tenzij bewust “happy” ná **server-paid**.

---

## 3. Toon — verbaal (copy)

### Kern

- Nederlands default; Engels via toggle (niet “Dunglish” in NL-modus).  
- Zaakmetaforen: **Etalage, Magazijn, Loods, Kassa, Winkelmand** — [nomenclatuur](./00-nomenclatuur-winkel.md).  
- Loods ≠ Black Friday-taal. Wel: “In de loods”, “zachte prijs”, alleen “laatste” als waar.

### Register

| Situatie | Toon |
|----------|------|
| Etalage / home | Uitnodigend, kort, warm |
| Magazijn / product | Nuchter, feiten, maker/vrijplaats zichtbaar |
| Kassa | Duidelijk, geruststellend, geen upsell |
| Fout / pending betaling | Menselijk, geen paniek, wel eerlijk |
| Mail bevestiging | Dankbaar, concreet next steps |

### Voorbeelden (aan te vullen)

| Liever | Liever niet |
|--------|-------------|
| Naar de kassa | Proceed to checkout (in NL-UI) |
| Actueel voorstel | Bestel nu!! |
| Terug naar de winkel | Annuleer order (tenzij betaling mislukt) |
| … | … |

---

## 4. Ontwerpprincipes (checklist voor frames)

1. Eén primaire handeling per stap (zeker mobiel / kassa).  
2. Server is baas over prijs en “betaald”.  
3. Lege, laden, fout, succes — altijd een staat tekenen.  
4. Geen dummyprijzen alsof live.  
5. Toegankelijk: contrast, focus, labels, ≥48px tap.  
6. Winkel browsen ≠ kassa-focus (nav-omgevingen).  
7. Tweede taal en dark mode niet vergeten bij “af”.  
8. …

---

## 5. Wat Vrijzaak *niet* is

*Schrap/vul bij:*

- Geen marketplace-lawaai  
- Geen influencer-dropship look  
- Geen verborgen kosten in de UI  
- …

---

## 6. Referenties en anti-referenties

| Soort | Voorbeeld | Wat we overnemen / vermijden |
|-------|-----------|------------------------------|
| Wel | … | … |
| Niet | … | … |

---

## 7. Besluiten log

| Datum | Besluit | Door |
|-------|---------|------|
| 2026-11-17 | GAP Code UI; small caps op knoppen; paper/ink/accent; grid 20 / 4-16-32 | team/ontwerp |
| | | |

---

## 8. Open (voor jou in Obsidian)

- [ ] Alinea §1 in eigen woorden  
- [ ] Kernwoorden sfeer aangescherpt  
- [ ] Beeldrichting  
- [ ] Copy-voorbeelden uitgebreid  
- [ ] Referenties  
- [ ] Akkoord winkelier + programmeur (kort lezen)

---

*Laatst gestructureerd: 2026-11-17. Jij vult de toon; tokens blijven de maten.*
