# FigCraft setup scripts

Run with `figcraft-cli` (headless). Prefer working on a copy if the file is open in the app.

```sh
export PATH="$HOME/.local/bin:$PATH"
# 1) variables + DS frame
figcraft-cli run setup-design-system.jsonl \
  --in ../vrijzaak-storefront.figcraft --out /tmp/vz-a.figcraft
# 2) specimens + button components (expects PageDesignSystem id 3)
figcraft-cli run setup-design-system-ui.jsonl \
  --in /tmp/vz-a.figcraft --out ../vrijzaak-storefront.figcraft
```

Contents match `frontend/css/tokens.css` (paper/ink/accent Light+Dark).

## CSS → FigCraft sync

```sh
figcraft-cli run sync-css-to-figcraft.jsonl \
  --in ../vrijzaak-storefront.figcraft --out /tmp/vz-sync.figcraft
cp /tmp/vz-sync.figcraft ../vrijzaak-storefront.figcraft
```

Creates/applies text styles (GAP Code, 16/20 scale) and paint styles from `frontend/css`.
See `docs/00-css-figcraft-sync.md`.
