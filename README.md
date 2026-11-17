# Vrijzaak (ontwerp)

Werknaam **Vrijzaak** · https://vrijzaak.nl  
**Deze repo:** https://github.com/SproetS/vrijzaak  

Markdown-ontwerp en draadmodellen. **Geen** Nuxt-app hier.  
**Technische source of truth** (routes, checkout, code): bouwrepo op Gitea helling (`Vrijzaak/Vrijzaak`).

Je kunt alles lezen op **GitHub.com** (links in de bestanden) en in **Obsidian** (dezelfde map als vault).

## Voor collega's (delen via GitHub)

1. Open de repo: https://github.com/SproetS/vrijzaak  
2. Begin bij **[docs/00-index.md](./docs/00-index.md)** (inhoudsopgave).  
3. Kort pad per rol:

| Rol | Lees vooral |
|-----|-------------|
| **Zakelijk / winkelier** | [00-projectbrief](./docs/00-projectbrief.md) · [00-bouwcontract-ontwerp](./docs/00-bouwcontract-ontwerp.md) (samenvatting) · checkout [02](./docs/02-checkout-overzicht.md) + [06](./docs/06-bevestiging.md) |
| **Programmeur** | [00-bouwcontract-ontwerp](./docs/00-bouwcontract-ontwerp.md) · [00-inventaris-bouw-ui](./docs/00-inventaris-bouw-ui.md) · [00-tech-traject](./docs/00-tech-traject.md) · eigen helling-repo blijft SoT voor code |
| **Ontwerp / UX** | Hele `docs/` + optioneel clone + Obsidian |

**Feedback:** GitHub Issues of PR op deze repo, of afgesproken chat — liever geen parallelle “waarheid” buiten Git.

**Obsidian (optioneel lokaal):** clone/repo-map → *Open folder as vault* op de **repo-root**.  
Op GitHub.com werken de **blauwe markdown-links**; `[[wikilinks]]` zijn vooral handig in Obsidian.

## Team

| Rol | Focus |
|-----|--------|
| Ontwerper / UX | Deze repo — flows, vormgeving, copy |
| Zakelijk leider / winkelier | Producten, klanten, commercieel |
| Programmeur | Nuxt + Directus-monorepo (helling) |

## Structuur

```
.
├── README.md          ← je bent hier
├── AGENTS.md          ← regels voor AI-agents
├── .obsidian/         ← gedeelde vault-instellingen
├── docs/              ← ontwerp-Markdown
└── frontend/          ← CSS-proeven, fonts placeholder, logo's, SVG
```

## Starten (snel)

| Wie | Start |
|-----|--------|
| Iedereen | [docs/00-index.md](./docs/00-index.md) |
| Bouw-afstemming | [docs/00-bouwcontract-ontwerp.md](./docs/00-bouwcontract-ontwerp.md) |
| Pagina’s & componenten | [docs/00-inventaris-bouw-ui.md](./docs/00-inventaris-bouw-ui.md) |
| Atomen / moleculen | [docs/00-ui-moleculen.md](./docs/00-ui-moleculen.md) |
| FigCraft + CLI | [docs/00-figcraft-samenwerking.md](./docs/00-figcraft-samenwerking.md) |
| Plan | [docs/00-projectbeschrijving-en-stappenplan.md](./docs/00-projectbeschrijving-en-stappenplan.md) |
| Agent | [AGENTS.md](./AGENTS.md) |

## Ontwerp (kort)

- Font voorlopig **GAP Code** (bouwcode kan nog Mono hebben tot sync)
- UI **NL + EN** (zaaknamen Etalage/Magazijn/Loods/Kassa); code/keys Engels ([nomenclatuur](./docs/00-nomenclatuur-winkel.md))
- Routes nu bouw-SoT (`/collectie`, `/mand`, `/afrekenen`, …); Engelse paths later via programmeur
- Prijzen en “betaald” komen van de **server**
