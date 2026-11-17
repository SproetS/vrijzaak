# components/ — uitzonderingen op de regel

**Basis** leeft in:

`tokens` → `type` → `base` → `atoms` → `molecules` → `organisms` → `layout`  
(entry: `../main.css`)

Hier alleen **afwijkingen** voor één organism/page, niet de standaard opnieuw.

## Conventie

| Bestand | Voor |
|---------|------|
| `quote-test-banner.css` | alleen testmodus-styling op `.vz-quote` |
| `order-fulfilment.css` | nuances OrderFulfilment |
| `partner-panel.css` | deelnemer-tabellen e.d. |

```css
/* voorbeeld: components/quote-test-banner.css */
.vz-quote--test {
  border-color: var(--vz-warning);
}
```

In Vue (bouw): liever **scoped** CSS op de SFC; deze map = ontwerp-referentie / static proef.

## Regel

1. Past het in atom/molecule modifiers (`--ghost`, `--tight`)? → daar.  
2. Echt uniek gedrag? → hier of SFC.  
3. Nooit losse hex of willekeurige 13px — tokens + V/H-rasters.
