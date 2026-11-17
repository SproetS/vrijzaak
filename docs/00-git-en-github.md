# Git en GitHub — ontwerprepo

## Repo

| | |
|--|--|
| GitHub | https://github.com/SproetS/vrijzaak |
| Branch | `main` |
| Lokaal (voorbeeld) | `…/Vrijzaak draadmodel` |
| Inhoud | Ontwerp-Markdown, Obsidian-instellingen, lichte `frontend/`-assets |

**Niet** de Nuxt-webshop. Die staat op Gitea helling (`Vrijzaak/Vrijzaak`) en is SoT voor code/routes/checkout.

## Delen met collega’s

1. Nodig uit als **collaborator** op `SproetS/vrijzaak` (Settings → Collaborators), of via org-team.  
2. Rechten: meestal **write** als ze issues/PR mogen; **read** volstaat om alleen te lezen.  
3. Stuur de README: https://github.com/SproetS/vrijzaak#readme  
4. Startpunt in de browser: [docs/00-index.md](./00-index.md)

Lezen kan **zonder clone** op github.com. Clone + Obsidian is optioneel voor UX-werk.

## Lokaal (ontwerper)

```sh
git clone git@github.com:SproetS/vrijzaak.git
cd vrijzaak
# Obsidian: Open folder as vault → deze map
```

Wijzigingen:

```sh
git status
git add …
git commit -m "…"
git push origin main
```

Geen force-push op `main` tenzij team dat afspreekt. PR’s zijn welkom voor grotere stukken.

## Wat wél / niet committen

**Wel:** `docs/`, `AGENTS.md`, `README.md`, `.obsidian/app.json` / `appearance.json` / `core-plugins.json`, lichte exports.  
**Niet:** `workspace.json`, plugins/themes (gitignored), secrets, zware binaries, fonts zonder licentie-afspraak, bouwmonorepo-mirror.

## Twee repo’s onthouden

| Repo | Voor wie | Wat |
|------|----------|-----|
| `SproetS/vrijzaak` | Iedereen in het ontwerptraject | Wireframes, IA, UX-keuzes |
| helling `Vrijzaak/Vrijzaak` | Programmeur (+ wie code meekijkt) | Nuxt, Directus, workers |

Zie [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md).
