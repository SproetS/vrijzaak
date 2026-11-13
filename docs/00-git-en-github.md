# Git en GitHub

Lokale repo: deze map (`main`).

## Eerste koppeling aan GitHub (eenmalig)

`gh` staat (nog) niet op deze Mac. Via de website:

1. Ga naar https://github.com/new  
2. Repository name voorstel: `vrijzaak-ontwerp` (of `vrijzaak-draadmodel`)  
3. **Private** aanbevolen (ontwerp + interne keuzes)  
4. **Geen** README / .gitignore / license toevoegen (repo moet leeg zijn)  
5. Create repository  

Daarna in deze map:

```bash
cd "/Users/sjoerd/Documents/sproets/tycho/Vrijzaak/01 - Werkbestanden/Vrijzaak draadmodel"
git remote add origin git@github.com:JOUW_USER/vrijzaak-ontwerp.git
# of HTTPS:
# git remote add origin https://github.com/JOUW_USER/vrijzaak-ontwerp.git
git push -u origin main
```

Vervang `JOUW_USER` door je GitHub-username.

### SSH-key (als je SSH gebruikt)

```bash
# bestaand?
ls ~/.ssh/id_*.pub
# anders key maken en op GitHub zetten onder Settings → SSH keys
```

### Later optioneel

```bash
brew install gh
gh auth login
```

Dan kun je repos vanaf de terminal aanmaken met `gh repo create`.

## Workflow met collega

- Private repo + collega als collaborator, of  
- Organisatie-repo onder jullie gedeelde org  
- Feedback: issues / PR’s, of jij merged en publiceert later static docs op VPS
