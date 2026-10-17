import json
from pathlib import Path

import pytest

from edition_comparison_sheet.cli import main


def make_source(tmp_path):
    source = tmp_path / "editions.json"
    source.write_text(json.dumps({"left": {"pages": 100}, "right": {"pages": 120}}))
    return source


@pytest.mark.parametrize("output_format", ["json", "markdown"])
def test_destination_created_at_open_is_preserved(tmp_path, monkeypatch, capsys, output_format):
    source = make_source(tmp_path)
    original_source = source.read_bytes()
    output = tmp_path / "report.txt"
    original_open = Path.open
    collided = False

    def arrive_before_open(path, mode="r", *args, **kwargs):
        nonlocal collided
        if path == output and mode in {"w", "x"}:
            collided = True
            with original_open(output, "x", encoding="utf-8") as stream:
                stream.write("concurrent report\n")
        return original_open(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", arrive_before_open)
    assert main([str(source), "--format", output_format, "--output", str(output)]) == 2
    assert collided
    assert "error:" in capsys.readouterr().err
    assert output.read_text() == "concurrent report\n"
    assert source.read_bytes() == original_source


@pytest.mark.parametrize("output_format", ["json", "markdown"])
def test_new_output_and_source_collision(tmp_path, output_format):
    source = make_source(tmp_path)
    original_source = source.read_bytes()
    output = tmp_path / "report.txt"
    assert main([str(source), "--format", output_format, "--output", str(output)]) == 0
    assert output.read_text()
    assert main([str(source), "--output", str(source)]) == 2
    assert source.read_bytes() == original_source
