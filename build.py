#!/usr/bin/env python3
"""Build script: reads all .py scripts and embeds them into index.html."""

import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)

CARDS = [
    {
        "id": "card-plugin-py",
        "title": "Plugin Metadata",
        "filename": "__plugin__.py",
        "badge": "Plugin",
        "path": os.path.join(ROOT, "Mesh2Srf/dev/__plugin__.py"),
    },
    {
        "id": "card-engine",
        "title": "Engine (shared core)",
        "filename": "m2s_engine.py",
        "badge": "Plugin",
        "path": os.path.join(ROOT, "Mesh2Srf/dev/m2s_engine.py"),
    },
    {
        "id": "card-panel",
        "title": "M2SPanel — Main UI",
        "filename": "M2SPanel_cmd.py",
        "badge": "Plugin",
        "path": os.path.join(ROOT, "Mesh2Srf/dev/M2SPanel_cmd.py"),
    },
    {
        "id": "card-deviation",
        "title": "M2SDeviation — Mesh vs Surface",
        "filename": "M2SDeviation_cmd.py",
        "badge": "Plugin",
        "path": os.path.join(ROOT, "Mesh2Srf/dev/M2SDeviation_cmd.py"),
    },
    {
        "id": "card-fit",
        "title": "M2SFit — Surface Fitting",
        "filename": "M2SFit_cmd.py",
        "badge": "Plugin",
        "path": os.path.join(ROOT, "Mesh2Srf/dev/M2SFit_cmd.py"),
    },
    {
        "id": "card-compare",
        "title": "M2SCompare — Mesh vs Mesh",
        "filename": "M2SCompare_cmd.py",
        "badge": "Plugin",
        "path": os.path.join(ROOT, "Mesh2Srf/dev/M2SCompare_cmd.py"),
    },
    {
        "id": "card-sections",
        "title": "M2SSections — Cross Sections",
        "filename": "M2SSections_cmd.py",
        "badge": "Plugin",
        "path": os.path.join(ROOT, "Mesh2Srf/dev/M2SSections_cmd.py"),
    },
    {
        "id": "card-primitive",
        "title": "M2SPrimitive — Shape Detection",
        "filename": "M2SPrimitive_cmd.py",
        "badge": "Plugin",
        "path": os.path.join(ROOT, "Mesh2Srf/dev/M2SPrimitive_cmd.py"),
    },
    {
        "id": "card-legend",
        "title": "M2SLegend — Toggle Legend",
        "filename": "M2SLegend_cmd.py",
        "badge": "Plugin",
        "path": os.path.join(ROOT, "Mesh2Srf/dev/M2SLegend_cmd.py"),
    },
    {
        "id": "card-vase",
        "title": "Twisted Vase",
        "filename": "twisted_vase.py",
        "badge": "Grasshopper",
        "path": os.path.join(ROOT, "twisted_vase.py"),
    },
    {
        "id": "card-square",
        "title": "Twisted Square",
        "filename": "twisted_square.py",
        "badge": "Grasshopper",
        "path": os.path.join(ROOT, "twisted_square.py"),
    },
    {
        "id": "card-circles",
        "title": "Circles on Surface",
        "filename": "circles_on_surface.py",
        "badge": "Grasshopper",
        "path": os.path.join(ROOT, "circles_on_surface.py"),
    },
    {
        "id": "card-wheel",
        "title": "Parametric Wheel",
        "filename": "parametric_wheel.py",
        "badge": "Grasshopper",
        "path": os.path.join(ROOT, "parametric_wheel.py"),
    },
    {
        "id": "card-devgh",
        "title": "Deviation Analysis (GH)",
        "filename": "deviation_analysis.py",
        "badge": "Grasshopper",
        "path": os.path.join(ROOT, "deviation_analysis.py"),
    },
    {
        "id": "card-patterns",
        "title": "Pattern Engine (150+ patterns, 20 gradients)",
        "filename": "pattern_engine.py",
        "badge": "Grasshopper",
        "path": os.path.join(ROOT, "pattern_engine.py"),
    },
]


def build():
    for c in CARDS:
        with open(c["path"], "r", encoding="utf-8") as f:
            c["code"] = f.read()

    js_entries = []
    for c in CARDS:
        entry = {
            "id": c["id"],
            "title": c["title"],
            "filename": c["filename"],
            "badge": c["badge"],
            "code": c["code"],
        }
        js_entries.append(json.dumps(entry, ensure_ascii=False))

    card_data_js = ",\n".join(js_entries)

    template_path = os.path.join(BASE, "index.html")
    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    import re
    html = re.sub(
        r"(const cards = \[)\n.*?\n(\];)",
        r"\1\n" + card_data_js + r"\n\2",
        html, count=1, flags=re.DOTALL,
    )

    out_path = os.path.join(BASE, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Built index.html with {len(CARDS)} scripts")
    total_lines = sum(c["code"].count("\n") for c in CARDS)
    print(f"Total lines of code: {total_lines}")


if __name__ == "__main__":
    build()
