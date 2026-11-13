# 03 — Gegevens (stap 1)

## Doel

Contact- en aflevergegevens van de koper (B2C).

## Velden

**Contact**
- E-mail (verplicht) — orderbevestiging
- Telefoon (optioneel, handig bij bezorging kunst/grote zending)

**Afleveradres**
- Voornaam, achternaam
- Straat + huisnummer
- Toevoeging (optioneel)
- Postcode, plaats
- Land (default Nederland; uitbreidbaar)

**Factuuradres**
- Checkbox: “Factuuradres is hetzelfde” (default aan)
- Zo uit: zelfde veldenstructuur

**Account (optioneel, onderaan of bovenaan)**
- “Maak een account met dit e-mailadres” + wachtwoord
- Of: overslaan als gast

## Desktop / mobiel

Zie [02-checkout-overzicht.md](./02-checkout-overzicht.md): linker kolom = formulier; rechts (desktop) order summary.

## Validatie

- Inline na blur + bij “Verder”
- Postcode NL-formaat als land = NL
- E-mail syntax

## Privacy

Korte regel: “We gebruiken je gegevens alleen voor deze bestelling en verzending.”

---
Vrijzaak · https://vrijzaak.nl · [[00-index]]
