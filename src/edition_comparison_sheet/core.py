from __future__ import annotations

import html
import json
import re
from typing import Any

from .json_equality import json_equal

PROJECT = "edition-comparison-sheet"


def _require(data: dict[str, Any], key: str) -> Any:
    value = data.get(key)
    if value is None or value == "" or value == []:
        raise ValueError(f"{key} is required")
    return value


def _edition_compare(data: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(data, dict):
        raise TypeError("input must be a JSON object")
    left = _require(data, "left")
    right = _require(data, "right")
    for label, edition in (("left", left), ("right", right)):
        if not isinstance(edition, dict):
            raise TypeError(f"{label} edition must be an object")
        if "name" in edition and (
            not isinstance(edition["name"], str) or not edition["name"].strip()
        ):
            raise ValueError(f"{label} name must be nonempty text")
    if "fields" in data:
        fields = data["fields"]
        if (
            not isinstance(fields, list)
            or not fields
            or any(not isinstance(field, str) or not field.strip() for field in fields)
        ):
            raise TypeError("fields must be a nonempty array of field names")
        if len(set(fields)) != len(fields):
            raise ValueError("fields must not contain duplicates")
        if any(field not in left and field not in right for field in fields):
            raise ValueError("selected fields must exist in at least one edition")
    else:
        fields = sorted((set(left) | set(right)) - {"name"})
    comparisons = []
    for field in fields:
        a, b = (left.get(field), right.get(field))
        comparisons.append(
            {
                "field": field,
                "left": a,
                "right": b,
                "left_present": field in left,
                "right_present": field in right,
                "same": json_equal(a, b) and (field in left) == (field in right),
            }
        )
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


def _table_cell(value: str) -> str:
    """Keep untrusted text inside one literal Markdown table cell."""
    special = "\\`|*_[]!#~\n\r"
    return "".join(f"&#{ord(char)};" if char in special else html.escape(char) for char in value)


def render_markdown(report: dict[str, Any]) -> str:
    left = _table_cell(str(report["left_name"]))
    right = _table_cell(str(report["right_name"]))
    lines = [
        "# Edition Comparison Sheet",
        "",
        f"Differences: **{report['difference_count']}**",
        "",
        f"| Field | {left} | {right} | Same? |",
        "| --- | --- | --- | --- |",
    ]
    for item in report["comparisons"]:
        values = []
        for side in ("left", "right"):
            values.append(
                _table_cell(json.dumps(item[side], ensure_ascii=False))
                if item[side + "_present"]
                else "*(missing)*"
            )
        field = _table_cell(item["field"])
        same = "Yes" if item["same"] else "No"
        lines.append(f"| {field} | {values[0]} | {values[1]} | {same} |")
    if not report["comparisons"]:
        lines.extend(["", "There are no fields to compare."])
    evidence = render_json(report).rstrip("\n")
    fence = "`" * max(3, 1 + max((len(m.group()) for m in re.finditer(r"`+", evidence)), default=0))
    lines.extend(["", "## JSON comparison evidence", "", fence + "json", evidence, fence, ""])
    return "\n".join(lines)
