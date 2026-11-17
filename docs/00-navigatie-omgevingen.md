# Navigatie-omgevingen Vrijzaak

Drie gescheiden “werelden” in de UI. Doel: browsen in de **zaak** voelt anders dan bij de **kassa**; juridisch/info hoort in de voet, niet in kassa-focus.

**Winkelnamen (UI):** tweetalig NL/EN via i18n — [00-nomenclatuur-winkel.md](./00-nomenclatuur-winkel.md) (Etalage/Magazijn/Loods/Kassa …).  
**Techniek:** identifiers en *toekomstige* paths in het **Engels**.  
**Routes nu (bouw SoT, nog niet hernoemen):** `/`, `/collectie`, `/mand`, `/afrekenen`, … — programmeur plant migratie later.

## 1. Hoofdmenu — Winkel (browse)

**Waar:** home, etalage, magazijn, loods, product (“werk”), makers, vrijplaatsen, zoeken.

**Sfeer:** ontdekken, rustig, alsof je door de zaak loopt — geen kassa-afleiding.

```
Desktop
+------------------------------------------------------------------+
| [Logo Vrijzaak]   Etalage · Magazijn · Loods · Makers · Vrijplaatsen |
|                              zoek              [Account] [Winkelmand] |
+------------------------------------------------------------------+

Mobiel
+----------------------------------+
| [Logo]              [Zoek] [☰]   |
| (☰: Etalage, Magazijn, Loods,    |
|  Makers, Vrijplaatsen, Account,  |
|  Winkelmand)                     |
+----------------------------------+
```

**Items**

| UI-label | Rol | Bouw nu |
|----------|-----|---------|
| **Etalage** | Aanbevolen / in de kijker | Home-secties; route later |
| **Magazijn** | Alle artikelen | `/collectie` |
| **Loods** | Aanbieding / uitverkoop | Nog geen route; later filter of `/loods` |
| **Makers** | Kunstenaars | `/kunstenaars/…` |
| **Vrijplaatsen** | Plekken | `/vrijplaatsen/…` |
| **Winkelmand** | Meenemen naar kassa | `/mand` |
| **Account** | Balie / eigen gegevens | `/account` |

**Niet in hoofdmenu:** AV, Privacy, lange info — dat is voet.

**Bouw-header vandaag:** Collectie · Winkelmand · Account · Over — streven = tabel hierboven (copy + eventueel links).

---

## 2. Kassamenu — Kassa (focus)

**Waar:** `/afrekenen`, Mollie-return bezig/mislukt; optioneel strakke chrome op status.

**Sfeer:** rust, vertrouwen, geen Magazijn/Etalage/Loods in de top.

```
Desktop
+------------------------------------------------------------------+
| [Logo]  Kassa                 Winkelmand · Account · Terug naar winkel |
|         (optioneel stap x/3)                                         |
+------------------------------------------------------------------+

Mobiel
+----------------------------------+
| [← Winkel]  Kassa        Account |
+----------------------------------+
```

**Items:** label **Kassa** · **Winkelmand** · **Account** · escape **Terug naar de winkel** (niet “annuleer” tenzij betaling mislukt).

**Niet tonen in kassa:** Etalage | Magazijn | Loods | Makers | Vrijplaatsen.

**Hybride (bouwroutes):**

- `/mand` = nog **winkel-header** + mand-focus  
- `/afrekenen` = **kassa-header**  
- `/bestellingen/:id` = light kassa of “bon”-chrome (privé)

---

## 3. Winkelmenu — Voet (info & juridisch)

**Waar:** footer op winkelpagina’s; op kassa minimaal of weg; op bevestiging kort ok.

```
+------------------------------------------------------------------+
| Vrijzaak — makers en vrijplaatsen                                |
| Contact · Over ons · Algemene voorwaarden · Privacy              |
| … etalage / magazijn soft links optioneel …                      |
+------------------------------------------------------------------+
```

**Kassa:** hoogstens “Voorwaarden · Privacy” bij akkoord-checkbox.

---

## Matrix

| Plek | Winkelhoofd | Kassamenu | Voet |
|------|-------------|-----------|------|
| Home / Etalage / Magazijn / Loods / werk | ja | nee | ja |
| Winkelmand `/mand` | ja | nee (voorstel) | ja |
| Kassa `/afrekenen` | nee | ja | nee / minimaal |
| Mollie pending/fail | nee | ja | nee |
| Bon / bestelling (betaald) | light | light | ja (kort) |

---

## Copy en taal

- Default **NL**; toggle **EN** (zelfde i18n-keys, zie nomenclatuur).  
- NL-zaaktaal in UI; EN functioneel en helder (niet per se letterlijke vertaling van “Loods”).  
- Escape NL: “Terug naar de winkel” · EN: “Back to the shop”.  
- Loods-toon: eerlijk, geen schreeuw-sale (beide talen).  
- Geen path-hernoem in ontwerpfase.

Zie [00-nomenclatuur-winkel.md](./00-nomenclatuur-winkel.md) · [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md).
