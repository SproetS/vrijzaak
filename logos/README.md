# logos/ — Vrijzaak-merk

Handoff-bestanden voor ontwerp en programmeur (bouwrepo).

## Bestanden (verwacht)

| Bestand | Gebruik |
|---------|---------|
| `logo.svg` | Primair logo (voorkeur voor web) |
| `logo.png` | Raster-fallback / preview |
| Eventueel `logo-mark.svg` | Alleen icoon/woordmerk-kort |

## Gebruik

- Op **paper** / **surface** achtergrond (`#f5f2e9` / `#fffdf7`).  
- Contrast met **ink** (`#202c27`).  
- Header-bouw: nu wordmark-tekst in `default.vue`; SVG kan later wordmark vervangen of aanvullen.  
- Zet regels (clearspace, min. breedte) in [docs/00-design-tokens.md](../../docs/00-design-tokens.md) als die vastliggen.

## Techniek SVG

- Bij voorkeur paden (of outlines) zodat GAP niet verplicht is in elk kanaal.  
- Schone `viewBox`; vermijd overbodige Illustrator-metadata waar mogelijk.  
- Programmeur plaatst uiteindelijk in helling o.a. `public/` of `app/assets/` — pad hier blijft de ontwerpbron.
