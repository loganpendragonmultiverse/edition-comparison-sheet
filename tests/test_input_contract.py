import json
from pathlib import Path

import pytest

from edition_comparison_sheet.cli import main
from edition_comparison_sheet.core import analyze


@pytest.mark.parametrize(
    "value",
    [
        [],
        {"left": 42, "right": {"pages": 2}},
        {"left": {"pages": 1}, "right": {"pages": 2}, "fields": "pages"},
        {"left": {"pages": 1}, "right": {}, "fields": []},
        {"left": {"pages": 1}, "right": {}, "fields": ["pages", "pages"]},
        {"left": {"pages": 1}, "right": {}, "fields": ["typo"]},
        {"left": {"name": 4}, "right": {}},
        {"left": {}, "right": {}, "fields": [None]},
    ],
)
def test_invalid_input_is_an_actionable_cli_error(tmp_path: Path, capsys, value):
    source = tmp_path / "invalid.json"
    source.write_text(json.dumps(value), encoding="utf-8")
    assert main([str(source)]) == 2
    assert "error:" in capsys.readouterr().err


def test_missing_and_explicit_null_are_distinct():
    result = analyze({"left": {"extras": None}, "right": {}})
    assert result["difference_count"] == 1
    assert result["comparisons"][0]["left_present"]
    assert not result["comparisons"][0]["right_present"]
    assert (
        analyze({"left": {"extras": ["map", "essay"]}, "right": {"extras": ["essay", "map"]}})[
            "difference_count"
        ]
        == 1
    )
