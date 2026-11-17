# Navigatie-omgevingen Vrijzaak

Drie gescheiden “werelden” in de UI. Doel: browsen in de **zaak** voelt anders dan bij de **kassa**; juridisch/info hoort in de voet, niet in kassa-focus.

**Winkelnamen (UI):** [00-nomenclatuur-winkel.md](./00-nomenclatuur-winkel.md) — Etalage, Magazijn, Loods, Kassa, Winkelmand.  
**Routes (bouw SoT):** o.a. `/`, `/collectie`, `/mand`, `/afrekenen` — labels mogen afwijken van het pad.

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

## Copy

- **Kassa** i.p.v. checkout · **Winkelmand** i.p.v. cart · **Magazijn** i.p.v. alleen “collectie” in UI  
- Escape: “Terug naar de winkel”  
- Loods-toon: eerlijk, geen schreeuw-sale  

Zie [00-nomenclatuur-winkel.md](./00-nomenclatuur-winkel.md) · [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md).
