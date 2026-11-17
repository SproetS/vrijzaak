# Navigatie-omgevingen Vrijzaak

Drie gescheiden “werelden” in de UI. Doel: winkel browsen voelt anders dan afrekenen; juridisch/info hoort bij de winkelrand, niet bij de kassa-focus.

## 1. Hoofdmenu — Winkel (browse)

**Waar:** productlijsten, productdetail, collecties, makers, vrijplaatsen, zoeken, homepage winkel.

**Sfeer:** ontdekken, rustig, anti-commercieel browsen.

```
Desktop
+------------------------------------------------------------------+
| [Logo Vrijzaak]     Collectie  |  Makers  |  Vrijplaatsen  | …   |
|                                 zoek              [Account] [Mand]|
+------------------------------------------------------------------+

Mobiel
+----------------------------------+
| [Logo]              [Zoek] [☰]   |
| (☰ opent: Collectie, Makers, …,  |
|  Account, Mand)                  |
+----------------------------------+
```

**Voorbeelditems (inhoud later vullen):**
- Collectie (of Shop / Werken)
- Makers
- Vrijplaatsen (Ruigoord, ADM, OT301, …)
- Eventueel: Thema’s / Nieuw
- Utility rechts: Account, Winkelmand (met teller)

**Niet in hoofdmenu:** lange juridische lijsten; die horen in het winkel-voetmenu.

---

## 2. Kassamenu — Checkout (focus)

**Waar:** winkelwagen (optioneel al kassa-modus), `/afrekenen/*`, Mollie-return “bezig/mislukt”, niet de bedanktpagina’s chaos.

**Sfeer:** rust, vertrouwen, geen afleiding naar browsen midden in betalen.

```
Desktop
+------------------------------------------------------------------+
| [Logo]  Kassa                    Winkelmand · Account · [Sluiten]|
|         Stap 2 van 3 · Verzending                                |
+------------------------------------------------------------------+

Mobiel
+----------------------------------+
| [←]  Kassa              Account  |
|      Stap 2/3                    |
+----------------------------------+
```

**Voorbeelditems:**
- Label/context: **Kassa** (niet het volledige Collectie-menu)
- **Winkelmand** — terug naar inhoud van de mand
- **Account** — inloggen/gast-status (discreet)
- **Terug naar winkel** / sluiten — duidelijk, maar niet als primaire navigatieboom met Collectie

**Niet tonen in kassa:** Collectie | Makers | Vrijplaatsen (voorkomt afhaken met volle mand elders).  
Wel één escape: “Verder winkelen” / “Terug naar de winkel”.

**Mand:** mag kassa-header gebruiken zodra de intent “ik ga afrekenen” is, of hybride: nog winkel-header op `/mand` en kassa-header vanaf `/afrekenen`. **Voorstel draadmodel (bouwroutes):**  
- `/mand` = nog **winkel-header** + mand-focus  
- `/afrekenen…` = **kassa-header**  
- `/bestellingen/:id` = light status/bedankt-chrome (privé)

---

## 3. Winkelmenu — Voet (info & juridisch)

**Waar:** footer op winkelpagina’s (niet storend op kassa-stappen; op bevestiging wél kort ok).

**Sfeer:** klein, secundair, betrouwbaar.

```
+------------------------------------------------------------------+
| Vrijzaak — makers en vrijplaatsen                                |
|                                                                  |
| Contact  ·  Over ons  ·  Algemene voorwaarden  ·  Privacy        |
|                                                                  |
| … credit / vrijplaatsen …                                        |
+------------------------------------------------------------------+
```

**Items:**
- Contact
- Over ons
- Algemene voorwaarden
- Privacy (aanbevolen naast AV)
- Eventueel: Verzenden & retour, Veelgestelde vragen

**Kassa:** footer weglaten of tot één regel “Voorwaarden · Privacy” reduceren naast akkoord-checkbox (zie 05-betaling).

---

## Matrix: welke nav waar?

| Pagina | Hoofdmenu winkel | Kassamenu | Voet winkelmenu |
|--------|------------------|-----------|-----------------|
| Home / collectie / product | ja | nee | ja |
| Mand `/mand` | ja | nee (voorstel) | ja |
| Afrekenen `/afrekenen` | nee | ja | nee / minimaal |
| Mollie pending/fail return | nee | ja | nee |
| Bevestiging (betaald) | nee of light | light kassa of bedankt-chrome | ja (kort) |

---

## Copy-richting

- “Kassa” i.p.v. alleen “Checkout” (NL-first, past bij Vrijzaak).
- “Winkelmand” consistent (niet mixen met cart/bag).
- Escape uit kassa: “Terug naar de winkel” — vriendelijk, niet “Annuleer order” tenzij betaling mislukt.

---
Routes en server-invarianten: [00-bouwcontract-ontwerp.md](./00-bouwcontract-ontwerp.md).
