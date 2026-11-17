# fonts/ — webfont-proeven (lokaal)

**Productie-fonts in de shop:** helling-repo `public/fonts/` (self-host, `font-display: swap`).  
**Ontwerp voorlopig:** **GAP Code** als UI-font — [docs/00-design-tokens.md](../../docs/00-design-tokens.md).  
**Bouw nu:** kan nog **GAP Mono** in `shared/design/tokens.ts` hebben tot de programmeur sync’t.

## Preview in de browser

`frontend/css/fonts.css` laadt **GAP Code** via `@font-face` uit deze map.  
Zonder lokale `.woff2` hier valt de preview terug op `ui-monospace` (op macOS vaak AppleSystemUIFontMonospaced).

Zorg dat o.a. bestaan:

```text
frontend/fonts/GAP Code/GAPCode-Regular.woff2
frontend/fonts/GAP Code/GAPCode-Bold.woff2
…
```

Kopie vanaf Desktop indien nodig:

```sh
cp -R ~/Desktop/GAP\ Fonts/Web/GAP\ Code\ -\ web/. \
  "frontend/fonts/GAP Code/"
```

(Pad kan iets afwijken; check `find ~/Desktop/GAP\ Fonts -name 'GAPCode-Regular.woff2'`.)

Open daarna `frontend/css/preview.html` (liefst via lichte local server als `file://` fonts blokkeert).

## Git

Bulkfontbestanden staan in `.gitignore` (`frontend/fonts/*`, README wel getrackt).  
Niet committen of publiek zetten zonder **licentie-afspraak**. `fonts.css` wél in git.

## Lokaal

Bron op deze Mac o.a. `~/Desktop/GAP Fonts/` (OTF/Web).  
Proeven hier mogen; levering aan bouw = afstemming + juiste subset (vaak WOFF2) in **bouwrepo**.
