from __future__ import annotations

import json
from typing import Any

PROJECT = "edition-comparison-sheet"


def _require(data: dict[str, Any], key: str) -> Any:
    value = data.get(key)
    if value is None or value == "" or value == []:
        raise ValueError(f"{key} is required")
    return value


def _edition_compare(data: dict[str, Any]) -> dict[str, Any]:
    left = _require(data, "left")
    right = _require(data, "right")
    fields = data.get("fields") or sorted((set(left) | set(right)) - {"name"})
    comparisons = []
    for field in fields:
        a, b = (left.get(field), right.get(field))
        comparisons.append({"field": field, "left": a, "right": b, "same": a == b})
    return {
        "left_name": left.get("name", "Left edition"),
        "right_name": right.get("name", "Right edition"),
        "comparisons": comparisons,
        "difference_count": sum(not item["same"] for item in comparisons),
    }


def analyze(data: dict[str, Any]) -> dict[str, Any]:
    return {"version": 1, "project": PROJECT, **_edition_compare(data)}


def render_json(report: dict[str, Any]) -> str:
    return json.dumps(report, indent=2, ensure_ascii=False, default=str) + "\n"


def render_markdown(report: dict[str, Any]) -> str:
    lines = [f"# {report['project'].replace('-', ' ').title()} report", ""]
    for key, value in report.items():
        if key not in {"version", "project"}:
            lines.extend(
                [
                    f"## {key.replace('_', ' ').title()}",
                    "",
                    f"```json\n{json.dumps(value, indent=2, ensure_ascii=False, default=str)}\n```",
                    "",
                ]
            )
    return "\n".join(lines).rstrip() + "\n"
