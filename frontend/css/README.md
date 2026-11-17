# css/ — ontwerp-tokens (voorstel)

| Bestand | Rol |
|---------|-----|
| `tokens.css` | CSS-custom properties als **ontwerpvoorstel** |

## Relatie met bouw

| Ontwerp (deze map) | Bouw (helling Nuxt) |
|--------------------|---------------------|
| `--vz-*` / semantische aliases in `tokens.css` | `shared/design/tokens.ts` → `--akws-paper`, `--akws-ink`, … |
| Proef in browser/static | `app/assets/css/main.css` + layout |

Documentatie: [docs/00-design-tokens.md](../../docs/00-design-tokens.md).

Bij wijziging: **eerst docs bijwerken**, dan `tokens.css`, dan programmeur vragen code te syncen.  
Deze CSS wordt **niet** automatisch de Nuxt-build.
