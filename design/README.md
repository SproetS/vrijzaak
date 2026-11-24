# design/ — FigCraft + exports

Visueel ontwerp voor handoff. Gedrag en IA blijven in `/docs`.

```text
design/
  figcraft/     native .figcraft bronnen
  exports/      PNG / SVG / PDF uit figcraft-cli (voor GitHub & programmeur)
```

## Start

1. FigCraft.app → nieuw of bestaand bestand  
2. Opslaan als `figcraft/vrijzaak-storefront.figcraft` (of feature-specifiek)  
3. Frame-namen: `PageCheckout`, `PageWarehouse`, `OrgQuoteBlock`, …  
   ([docs/00-ui-moleculen.md](../../docs/00-ui-moleculen.md))  
4. Export:

```sh
figcraft-cli export figcraft/vrijzaak-storefront.figcraft \
  -o exports/ --format png --scale 2
```

Volledige CLI/MCP-workflow: [docs/00-figcraft-samenwerking.md](../../docs/00-figcraft-samenwerking.md).

## Git

- **exports/**: ja, lichte PNG/SVG  
- **figcraft/**: ja als team de bron deelt (binair)  
- Geen cloud-only “waarheid” buiten Git  
