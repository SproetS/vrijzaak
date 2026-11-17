# Vrijzaak (ontwerp)

Werknaam **Vrijzaak** · https://vrijzaak.nl  
GitHub: https://github.com/SproetS/vrijzaak

Markdown-ontwerp en draadmodellen. **Geen** Nuxt-app hier.  
**Technische source of truth** (routes, checkout, code): bouwrepo op Gitea helling (`Vrijzaak/Vrijzaak`), lokaal o.a. `03 - Bouw/webshop`.

## Team

| Rol | Focus |
|-----|--------|
| Ontwerper / UX | Deze repo — flows, vormgeving, copy |
| Zakelijk leider / winkelier | Producten, klanten, commercieel |
| Programmeur | Nuxt + Directus-monorepo |

## Structuur

```
.
├── README.md
├── AGENTS.md          ← regels voor AI-agents
├── .obsidian/         ← vault-instellingen (workspace lokaal)
├── docs/              ← projectbeschrijving & draadmodellen
└── frontend/          ← CSS-proeven, fonts placeholder, logo's, SVG
```

## Starten

**Obsidian:** *Open folder as vault* → deze **repo-root** (niet alleen `docs/`).  
Wikilinks en graph werken zo het best. Ook leesbaar op GitHub / in een editor.

| Wie | Start |
|-----|--------|
| Mens / UX | [docs/00-index.md](./docs/00-index.md) |
| Bouw-afstemming | [docs/00-bouwcontract-ontwerp.md](./docs/00-bouwcontract-ontwerp.md) |
| Pagina’s & componenten (bouw) | [docs/00-inventaris-bouw-ui.md](./docs/00-inventaris-bouw-ui.md) |
| Plan | [docs/00-projectbeschrijving-en-stappenplan.md](./docs/00-projectbeschrijving-en-stappenplan.md) |
| Agent | [AGENTS.md](./AGENTS.md), daarna docs |

## Ontwerp (kort)

- Font voorlopig **GAP Code** (bouwcode kan nog Mono hebben tot sync)
- Kassa-routes: `/mand`, `/afrekenen`, `/bestellingen/:id`
- Prijzen en “betaald” komen van de **server**
