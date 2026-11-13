# Projectbeschrijving en stappenplan — Vrijzaak

Voor **mensen** (UX, winkelier-collega, tech) en **agents**.  
Werknaam: **Vrijzaak** · URL: https://vrijzaak.nl  
GitHub: https://github.com/SproetS/vrijzaak  
Vault: deze map.

Gerelateerd: [[00-projectbrief]] · [[00-projectmap]] · [[AGENTS]] · [[00-tech-traject-svelte-directus]] · [[00-index]]

---

## 1. Projectbeschrijving

### 1.1 Wat bouwen we (eindbeeld)

Een **B2C-webwinkel** die makers en **vrijplaatsen** (o.a. Ruigoord, ADM, OT301) verbindt met kopers. Fysieke producten (T-shirts, boekjes, schilderijen, kunstwerken). Sfeer: anti-commercieel eerlijk, wél betrouwbare kassa.

De klant ziet prijzen **inclusief btw**. Achter de schermen (en optioneel transparant voor de klant) wordt opbrengst verdeeld over **maker**, **vrijplaats** en **winkel (Vrijzaak)**, plus btw waar van toepassing.

### 1.2 Wat is het product van déze fase?

Geen live shop nog, maar een **ontwerpverslag + draadmodellen** (Markdown/Git) waarmee:

- UX en kassa-ervaring vastliggen;
- de winkelier-collega snapt scope en beheerpad;
- tech later kan bouwen zonder gissen.

### 1.3 Rollen

| Rol | Verantwoordelijkheid |
|-----|----------------------|
| UX / vormgeving | Flows, navigatie, tokens, copy, vault |
| Winkelier-collega | Producten, klanten, operationele eisen; feedback op ontwerp |
| Tech (later) | SvelteKit, Directus, Mollie, VPS/deploy |
| Agents | Markdown uitbreiden volgens [[AGENTS]]; geen secrets/deploy tenzij gevraagd |

### 1.4 Technisch doelbeeld (bouw, niet nu)

```
vrijzaak.nl          SvelteKit + CSS (GAP Zuid VG, GAP Code, tokens)
       ↕
Directus             catalogus, makers, vrijplaatsen, content, (orders?)
       ↕
Mollie               iDEAL e.d., webhook → betaald
```

- **Svelte + CSS:** lekkere UX, kassa, vertrouwen.  
- **Directus:** winkelier beheert producten/content.  
- **Mollie:** betalen; één charge van klanttotaal.

### 1.5 Ontwerpkeuzes (vast tot herzien)

- Gast-checkout + optioneel account  
- Gescheiden nav: **winkel** / **kassa** / **voet** — [[00-navigatie-omgevingen]]  
- Prijzen **incl. btw**, meerdere tarieven mogelijk — [[07-rekensom]]  
- Verzending slim bij gemengde mand (pakket vs kunst) — [[04-verzending]]  
- Checkout-stappen + happy bevestiging — [[02-checkout-overzicht]], [[06-bevestiging]]  
- Visueel: greyscale + zachte accenten, GAP-fonts — [[00-design-tokens]]  
- Geen nep-schaarste, geen agressieve upsell  

### 1.6 Succescriteria per fase

| Fase | Klaar als |
|------|-----------|
| Ontwerp (nu) | Vault dekt checkout + IA winkel + productmodel; collega kan meelezen via GitHub |
| Deelbaar web (optioneel) | Leesbare docs op bijv. ontwerp.vrijzaak.nl |
| MVP shop | Bladeren, mand, kassa, iDEAL, bevestiging, Directus-beheer producten |
| Volwassen | Verdeling/uitbetaling, verzendregels, account/orders, contentpagina’s |

---

## 2. Stappenplan

Legenda: **M** = mens (UX/winkelier), **A** = agent, **T** = tech.

### Fase 0 — Fundering (deels gedaan)

| # | Stap | Wie | Status |
|---|------|-----|--------|
| 0.1 | Projectbrief, tokens, tech-traject, navigatie | M/A | Gedaan |
| 0.2 | Checkout-draadmodellen 01–08 | M/A | Gedaan |
| 0.3 | GitHub-repo `SproetS/vrijzaak`, lokale `main` | M | Gedaan |
| 0.4 | AGENTS.md + projectmap | M/A | Gedaan |
| 0.5 | Collega uitnodigen op repo (collaborator) of org | M | Open |
| 0.6 | Afspraak: private repo, hoe feedback (issues/PR/chat) | M | Open |

### Fase 1 — Winkel vangen in Markdown

| # | Stap | Wie | Deliverable |
|---|------|-----|-------------|
| 1.1 | Sitemap / IA | A/M | `09-sitemap-ia.md` |
| 1.2 | Productmodel (Directus-velden) | A/M | `10-productmodel.md` |
| 1.3 | Draadmodel home + collectie/listing | A/M | `11-…` notes |
| 1.4 | Draadmodel productdetail | A/M | incl. maker/vrijplaats/btw/verdeling-teaser |
| 1.5 | Draadmodel maker- en vrijplaats-pagina | A/M | |
| 1.6 | Account licht (login, orders) | A/M | |
| 1.7 | Footer-landings: Contact, Over ons, AV-structuur | A/M | |
| 1.8 | Review met winkelier-collega | M | Akkoord of wijziglijst |

### Fase 2 — Visueel en deelbaar

| # | Stap | Wie | Deliverable |
|---|------|-----|-------------|
| 2.1 | Accent-hex en UI-kit naast `Vrijzaak-ontwerp1.ai` | M | Update [[00-design-tokens]] |
| 2.2 | Optioneel: VitePress/static site uit deze md | T/A | Build-pipeline |
| 2.3 | Optioneel: VPS `ontwerp.vrijzaak.nl` | T | nginx static |
| 2.4 | Rapportage-moment collega (demo vault of web) | M | |

### Fase 3 — Bouw MVP (na ontwerp-akkoord)

| # | Stap | Wie | Deliverable |
|---|------|-----|-------------|
| 3.1 | Repo(s) SvelteKit + Directus-schema | T | Code buiten deze vault |
| 3.2 | Design tokens → CSS; GAP self-hosted | T | |
| 3.3 | Catalogus Directus (product, maker, vrijplaats) | T + winkelier | |
| 3.4 | Winkel browse + productdetail | T | |
| 3.5 | Winkelwagen + kassa-flow (nav-split) | T | |
| 3.6 | Mollie iDEAL + webhooks + bevestiging | T | |
| 3.7 | Verzendregels v1 (klassen) | T + M | |
| 3.8 | Content AV/Privacy/Contact | M + T | |
| 3.9 | Staging op VPS, daarna vrijzaak.nl | T | |

### Fase 4 — Nazorg

| # | Stap | Wie |
|---|------|-----|
| 4.1 | Monitoring, backups Directus/media | T |
| 4.2 | Handleiding winkelier (producten beheren) | M/A |
| 4.3 | Iteratie UX op echte orders | M |
| 4.4 | Uitbetaling/verdeling operationeel (buiten pure kassa-UI) | T + M |

---

## 3. Werkafspraken (mens + agent)

1. **Bron ontwerp:** deze Git-repo / vault. Wijzigingen committen op `main` of via PR.  
2. **Agents:** volgen [[AGENTS]]; geen productie-deploy of secrets hier.  
3. **Besluiten:** korte “Besluit”-sectie in de relevante note; open vragen blijven “Open”.  
4. **Scope creep:** nieuwe wensen → Open punten of nieuwe note, niet stilzwijgend checkout omgooien.  
5. **Taal UI:** Nederlands in wireframes.  
6. **Definition of done (ontwerp-note):** gelinkt vanuit [[00-index]], backlinks, geen aannames als feiten.

---

## 4. Risico’s en mitigeratie

| Risico | Mitigeratie |
|--------|-------------|
| Verzending te complex | Klassen + “op afspraak” voor kunst; tarieven later invullen |
| Btw/verdeling juridisich/boekhoudkundig | Model in [[07-rekensom]]; validatie met boekhouder vóór live |
| Collega kan Git niet | Static docs-site of issues; jij blijft editor |
| Twee CMS-paden (Tina + Directus) | Docs static/wiki; shop = Directus |
| Te vroeg bouwen | Fase 1–2 af vóór fase 3 |

---

## 5. Directe volgende acties (nu)

1. **Mens:** collega uitnodigen op `SproetS/vrijzaak` (als gewenst).  
2. **Agent/mens:** `09-sitemap-ia.md` en `10-productmodel.md` schrijven.  
3. **Mens:** feedbackronde op checkout-draadmodellen (01–08).  
4. **Later:** static publish of VPS zodra deelomgeving gekozen is.

---

## 6. Checklist “ontwerp fase compleet”

- [ ] Sitemap IA af  
- [ ] Productmodel af (Directus-klaar)  
- [ ] Alle kern-winkelpagina’s als draadmodel  
- [ ] Tokens + accenten concreet  
- [ ] Collega-akkoord op kassa + verdeling-transparantie  
- [ ] Tech-traject ongewijzigd of bijgewerkt in vault  
- [ ] GitHub bij  
- [ ] (Optioneel) Web-leesomgeving live  

Einde checklist = groene licht voor bouwfase.
