# Design tokens — Vrijzaak

Werknaam / site: **Vrijzaak** · https://vrijzaak.nl

**Ontwerpafspraken in Markdown**, plus spiegel van wat de **bouwrepo nu** gebruikt. Bij implementatie: één set CSS-variabelen in Nuxt (`shared/design/tokens.ts` → `--akws-*`), geen losse componentkleuren.

Zie [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md) §7.

---

## A. Bouw (feitelijk in code)

Bron: webshop `shared/design/tokens.ts` en `docs/design.md`.

| Rol | Waarde |
|-----|--------|
| paper | `#f5f2e9` |
| surface | `#fffdf7` |
| ink | `#202c27` |
| muted | `#58645d` |
| accent | `#245c43` |
| line | `#b7c2b5` |
| font | `"GAP Mono", "Courier New", monospace` |
| emailFont | `"Courier New", monospace` |
| measure | `76rem` |

- WOFF self-hosted in bouw `public/fonts/`.
- Rollen: paper / surface / ink / muted / accent / line — geen ad-hoc hex in componenten.
- Mail: zelfde semantiek, geen verplicht GAP-webfont.

---

## B. Ontwerpverkenning (deze vault)

Richting die UX mag blijven verkennen tot er een **gezamenlijk fontbesluit** is.

### Typografie

| Rol | Familie | Gebruik |
|-----|---------|---------|
| **Voorlopig productierichting (ontwerp 2026-11-17)** | **GAP Code** | UI, body, navigatie, prijzen, labels |
| Alternatief / later | GAP Zuid VG | alleen na herziening |
| Bouwcode nu | GAP Mono in `tokens.ts` | nog niet gelijkgetrokken — programmeur |

Lokaal op deze Mac: `/Users/sjoerd/Desktop/GAP Fonts/` (OTF + Web).  
In `frontend/fonts/` van deze repo: placeholder; licentie vóór commit van webfonts.

```
/* voorlopig ontwerpbesluit */
--font-ui: "GAP Code", ui-monospace, monospace;
/* bouw tokens.ts heeft nog font: GAP Mono — sync via programmeur */
```

### Kleur (vault-voorstel boven greyscale)

```
--gray-0 … --gray-900   pagina, vlakken, randen, tekst
--accent-soft-red / yellow / blue   spaarzaam CTA/tags
```

Semantisch (align met bouw-namen waar mogelijk):

```
--bg-primary ≈ paper/surface
--text-primary ≈ ink
--text-secondary ≈ muted
--border ≈ line
--cta ≈ accent
--danger / --success   mild (Mollie fail/success)
```

### Ruimte

```
--space-1 … --space-8
--radius-sm / md / lg
tap targets ≥ 44px (bouw design.md)
```

---

## C. Besluit nodig

| Vraag | Opties |
|-------|--------|
| Productie-font | **GAP Code (voorlopig vast in ontwerp)** · bouw nog Mono tot PR |
| Accent | Huidig groen `#245c43` vast · of zachte multi-accent uit AI-ontwerp |
| Papierwit | Bouw paper/surface overnemen als default in vault-UI-kit |

Tot besluit: **wireframes beschrijven hiërarchie en rust**; screenshots/CSS-proeven labelen “vault” vs “bouw”.

---

## Toon in UI

- Veel papier/witruimte, dunne randen  
- Kassa nóg rustiger (minder nav)  
- Bedragen uit server-DTO; geen dummy-prijzen in “echte” componenten  
- Self-host fonts; licentie checken vóór publieke launch  
