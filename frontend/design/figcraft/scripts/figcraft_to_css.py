#!/usr/bin/env python3
"""
FigCraft → CSS notes (and optional token patches).

Reads styles + variables from vrijzaak-storefront.figcraft via figcraft-cli,
compares to frontend/css/tokens.css + type.css expectations, writes a report.

Usage:
  python3 figcraft_to_css.py
  python3 figcraft_to_css.py --write-report
  python3 figcraft_to_css.py --apply-tokens   # only safe color hex updates in tokens.css

Does NOT rewrite atoms/molecules automatically.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# scripts/ → figcraft/ → design/ → frontend/ → repo
_FRONTEND = Path(__file__).resolve().parents[3]
_REPO = _FRONTEND.parent
FIG = _FRONTEND / "design/figcraft/vrijzaak-storefront.figcraft"
TOKENS = _FRONTEND / "css/tokens.css"
TYPE = _FRONTEND / "css/type.css"
REPORT_DIR = _FRONTEND / "design/exports"
REPO = _REPO
ROOT = _FRONTEND
CLI = "figcraft-cli"

# Expected mapping: FigCraft name → CSS custom property (light)
COLOR_MAP = {
    "paper": "--vz-paper",
    "surface": "--vz-surface",
    "ink": "--vz-ink",
    "muted": "--vz-muted",
    "accent": "--vz-accent",
    "line": "--vz-line",
    "danger": "--vz-danger",
    "success": "--vz-success",
    "ctaText": "--vz-cta-text",
}

TYPE_MAP = {
    "Type/H1": ("--vz-text-h1-size", "--vz-text-h1-leading", 40, 40),
    "Type/H2": ("--vz-text-h2-size", "--vz-text-h2-leading", 32, 40),
    "Type/H3": ("--vz-text-h3-size", "--vz-text-h3-leading", 24, 40),
    "Type/H4": ("--vz-text-h4-size", "--vz-text-h4-leading", 20, 40),
    "Type/H5": ("--vz-text-h5-size", "--vz-text-h5-leading", 18, 20),
    "Type/H6": ("--vz-text-h6-size", "--vz-text-h6-leading", 16, 20),
    "Type/Body": ("--vz-text-body-size", "--vz-text-body-leading", 16, 20),
}


def run_cli_jsonl(commands: list[dict]) -> list[dict]:
    if not FIG.exists():
        raise SystemExit(f"missing {FIG}")
    script = Path("/tmp/figcraft-to-css-cmds.jsonl")
    script.write_text("\n".join(json.dumps(c) for c in commands) + "\n")
    out = Path("/tmp/figcraft-to-css-out.figcraft")
    proc = subprocess.run(
        [CLI, "run", str(script), "--in", str(FIG), "--out", str(out)],
        capture_output=True,
        text=True,
    )
    lines = []
    for line in (proc.stdout or "").splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            lines.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "")[-2000:]
        raise SystemExit(f"figcraft-cli failed ({proc.returncode}): {err}")
    return lines


def color_to_hex(val) -> str | None:
    """FigCraft color: #hex or {r,g,b,a} 0..1 or nested."""
    if val is None:
        return None
    if isinstance(val, str):
        if val.startswith("#"):
            return val.lower() if len(val) in (4, 7, 9) else val
        return val
    if isinstance(val, dict):
        if "color" in val and isinstance(val["color"], str):
            return color_to_hex(val["color"])
        if "color" in val and isinstance(val["color"], dict):
            c = val["color"]
            if all(k in c for k in ("r", "g", "b")):
                r, g, b = (int(round(float(c[k]) * 255)) for k in ("r", "g", "b"))
                return f"#{r:02x}{g:02x}{b:02x}"
        if all(k in val for k in ("r", "g", "b")):
            r, g, b = (int(round(float(val[k]) * 255)) for k in ("r", "g", "b"))
            return f"#{r:02x}{g:02x}{b:02x}"
    return None


def parse_styles(result) -> dict:
    if isinstance(result, list):
        styles = result
    elif isinstance(result, dict):
        styles = result.get("styles") or result.get("items") or []
    else:
        styles = []
    by_name = {}
    for s in styles:
        if not isinstance(s, dict):
            continue
        name = s.get("name") or s.get("id")
        by_name[name] = s
    return by_name


def parse_variables(result) -> dict:
    if isinstance(result, list):
        vars_ = result
    elif isinstance(result, dict):
        vars_ = result.get("variables") or []
    else:
        vars_ = []
    by_name = {}
    for v in vars_:
        if not isinstance(v, dict):
            continue
        by_name[v.get("name")] = v
    return by_name


def css_get_prop(css: str, prop: str) -> str | None:
    m = re.search(rf"{re.escape(prop)}\s*:\s*([^;]+);", css)
    return m.group(1).strip() if m else None


def extract_text_metrics(style: dict) -> tuple[float | None, float | None, str | None, str | None]:
    """Return fontSize, lineHeight_px, fontFamily, fill_hex from style blob."""
    # shape varies: style.style or style.value
    blob = style.get("style") or style.get("value") or style
    if isinstance(blob, str):
        return None, None, None, None
    fs = blob.get("fontSize")
    ff = blob.get("fontFamily")
    lh = blob.get("lineHeight")
    lh_px = None
    if isinstance(lh, dict):
        unit = (lh.get("unit") or "").lower()
        val = lh.get("value")
        if unit == "pixels" and val is not None:
            lh_px = float(val)
        elif unit == "percent" and fs is not None and val is not None:
            lh_px = float(fs) * float(val) / 100.0
    elif isinstance(lh, (int, float)):
        lh_px = float(lh)
    fill = blob.get("fill") or blob.get("fills")
    fill_hex = None
    if isinstance(fill, list) and fill:
        fill_hex = color_to_hex(fill[0])
    else:
        fill_hex = color_to_hex(fill)
    return (
        float(fs) if fs is not None else None,
        lh_px,
        ff,
        fill_hex,
    )


def build_report(styles: dict, variables: dict, tokens_css: str) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"# FigCraft → CSS rapport",
        f"",
        f"Gegenereerd: {now}  ",
        f"Bron: `frontend/design/figcraft/vrijzaak-storefront.figcraft`  ",
        f"Tool: `frontend/design/figcraft/scripts/figcraft_to_css.py`",
        f"",
        f"## Checklist (na tekenen)",
        f"",
        f"1. [ ] FigCraft opgeslagen (Cmd+S)",
        f"2. [ ] Dit script gedraaid / agent gevraagd “verwerk FigCraft naar CSS”",
        f"3. [ ] Kleuren Light (en Dark) gecontroleerd",
        f"4. [ ] Type H1–Body vs 16/20-basislijn",
        f"5. [ ] Nieuwe component-maten (btn, field) genoteerd → `atoms.css`",
        f"6. [ ] Exports PNG in `frontend/design/exports/`",
        f"7. [ ] CSS-diff reviewed en gecommit",
        f"8. [ ] Optioneel: `sync-css-to-figcraft.jsonl` opnieuw als CSS leidend blijft",
        f"",
        f"## Variables (Theme)",
        f"",
        f"| Name | Light | Dark | CSS light nu | Actie |",
        f"|------|-------|------|--------------|-------|",
    ]

    color_actions: list[tuple[str, str]] = []

    for name, css_prop in COLOR_MAP.items():
        v = variables.get(name)
        if not v:
            lines.append(f"| `{name}` | — | — | `{css_prop}` | ontbreekt in FigCraft |")
            continue
        values = v.get("values") or {}
        # values may be {Light: ..., Dark: ...} or list
        light = dark = None
        if isinstance(values, dict):
            light = color_to_hex(values.get("Light") or values.get("light"))
            dark = color_to_hex(values.get("Dark") or values.get("dark"))
            # sometimes mode id keys
            if light is None:
                for k, val in values.items():
                    hx = color_to_hex(val)
                    if hx and light is None:
                        light = hx
                    elif hx:
                        dark = hx
        css_now = css_get_prop(tokens_css, css_prop)
        # tokens may use nested without direct --vz-cta-text on light root only
        act = "ok"
        if light and css_now and light.lower() != css_now.strip().lower():
            act = f"update CSS `{css_prop}: {light}`"
            color_actions.append((css_prop, light))
        elif light and not css_now:
            act = f"overweeg `{css_prop}: {light}`"
            color_actions.append((css_prop, light))
        lines.append(
            f"| `{name}` | `{light}` | `{dark}` | `{css_now}` | {act} |"
        )

    lines += [
        f"",
        f"## Text styles",
        f"",
        f"| Style | font | size | leading | fill | vs tokens |",
        f"|-------|------|------|---------|------|-----------|",
    ]

    for sname, (size_prop, lead_prop, exp_s, exp_l) in TYPE_MAP.items():
        s = styles.get(sname)
        if not s:
            lines.append(f"| `{sname}` | — | — | — | — | ontbreekt |")
            continue
        fs, lh, ff, fill = extract_text_metrics(s)
        ok_s = fs is not None and abs(fs - exp_s) < 0.51
        ok_l = lh is not None and abs(lh - exp_l) < 0.51
        status = "ok" if ok_s and ok_l else "wijkt af van type.css"
        if ff and "GAP" not in str(ff).upper() and "Code" not in str(ff):
            status += f"; font={ff}"
        lines.append(
            f"| `{sname}` | {ff} | {fs} | {lh} | {fill} | {status} (verwacht {exp_s}/{exp_l}) |"
        )

    # other styles
    extra = [n for n in styles if n not in TYPE_MAP and not str(n).startswith("Color/")]
    if extra:
        lines += [f"", f"## Overige styles", f""]
        for n in sorted(extra):
            lines.append(f"- `{n}`")

    lines += [
        f"",
        f"## Voorgestelde CSS-patches (kleur light)",
        f"",
    ]
    if color_actions:
        lines.append("```css")
        for prop, hx in color_actions:
            lines.append(f"{prop}: {hx};")
        lines.append("```")
    else:
        lines.append("_Geen automatische kleurverschillen t.o.v. light-tokens._")

    lines += [
        f"",
        f"## Handmatig (atoms / layout)",
        f"",
        f"Na tekenen: noteer afwijkende maten hier of in de chat.",
        f"",
        f"| Component | FigCraft frame | gemeten (px) | CSS-target |",
        f"|-----------|----------------|--------------|------------|",
        f"| Primary button | Btn/Primary | h=? pad-x=? radius=? | `.vz-btn` |",
        f"| Ghost button | Btn/Ghost | | `.vz-btn--ghost` |",
        f"| Field | | | `.vz-field` / `.vz-input` |",
        f"| Header | | | `.vz-site-header` |",
        f"",
        f"## Commando’s",
        f"",
        f"```sh",
        f"# rapport",
        f"python3 frontend/design/figcraft/scripts/figcraft_to_css.py --write-report",
        f"",
        f"# alleen light color props in tokens.css bijwerken (review git diff!)",
        f"python3 frontend/design/figcraft/scripts/figcraft_to_css.py --apply-tokens",
        f"",
        f"# export previews",
        f"figcraft-cli export frontend/design/figcraft/vrijzaak-storefront.figcraft \\\n"
        f"  -o frontend/design/exports/ --format png --scale 2",
        f"```",
        f"",
        f"Zie ook [docs/00-css-figcraft-sync.md](../../../docs/00-css-figcraft-sync.md).",
        f"",
    ]
    return "\n".join(lines)


def apply_token_colors(tokens_css: str, actions: list[tuple[str, str]]) -> str:
    css = tokens_css
    for prop, hx in actions:
        # only replace first occurrence in :root light section — simple global replace of prop line
        css, n = re.subn(
            rf"({re.escape(prop)}\s*:\s*)([^;]+)(;)",
            rf"\g<1>{hx}\g<3>",
            css,
            count=1,
        )
        if n == 0:
            # insert after --vz-line in :root if missing
            pass
    return css


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-report", action="store_true", default=True)
    ap.add_argument("--no-report", action="store_true")
    ap.add_argument("--apply-tokens", action="store_true")
    ap.add_argument("--json-dump", type=Path, help="Write raw styles/vars JSON")
    args = ap.parse_args()

    results = run_cli_jsonl(
        [
            {"command": "style.list", "params": {}},
            {"command": "variable.list", "params": {}},
        ]
    )
    styles_res = next((r for r in results if r.get("command") == "style.list"), {})
    vars_res = next((r for r in results if r.get("command") == "variable.list"), {})
    if not styles_res.get("ok"):
        raise SystemExit(styles_res)
    if not vars_res.get("ok"):
        raise SystemExit(vars_res)

    styles = parse_styles(styles_res.get("result") or {})
    variables = parse_variables(vars_res.get("result") or {})
    tokens_css = TOKENS.read_text() if TOKENS.exists() else ""

    if args.json_dump:
        args.json_dump.write_text(
            json.dumps(
                {"styles": styles_res.get("result"), "variables": vars_res.get("result")},
                indent=2,
            )
        )
        print(f"wrote {args.json_dump}")

    report = build_report(styles, variables, tokens_css)
    if args.no_report:
        print(report)
    else:
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        out = REPORT_DIR / "figcraft-to-css-report.md"
        out.write_text(report)
        print(f"wrote {out}")

    if args.apply_tokens:
        # rebuild actions
        actions = []
        for name, css_prop in COLOR_MAP.items():
            v = variables.get(name)
            if not v:
                continue
            values = v.get("values") or {}
            light = None
            if isinstance(values, dict):
                light = color_to_hex(values.get("Light") or values.get("light"))
                if light is None:
                    for val in values.values():
                        light = color_to_hex(val)
                        if light:
                            break
            css_now = css_get_prop(tokens_css, css_prop)
            if light and css_now and light.lower() != css_now.strip().lower():
                actions.append((css_prop, light))
            elif light and css_prop == "--vz-cta-text" and not css_now:
                # cta-text may only appear once
                if f"{css_prop}:" not in tokens_css:
                    tokens_css = tokens_css.replace(
                        "  --vz-cta-bg: var(--vz-accent);",
                        f"  --vz-cta-bg: var(--vz-accent);\n  {css_prop}: {light};",
                        1,
                    )
        new_css = apply_token_colors(tokens_css, actions)
        if new_css != tokens_css and actions:
            TOKENS.write_text(new_css)
            print(f"updated {TOKENS} ({len(actions)} props) — review git diff")
        else:
            print("no token color changes applied")


if __name__ == "__main__":
    main()
