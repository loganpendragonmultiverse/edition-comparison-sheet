import json

from edition_comparison_sheet.core import analyze, render_json, render_markdown


def test_sheet_retains_types_presence_and_full_evidence():
    report = analyze(
        {
            "left": {
                "name": "Hardcover",
                "null": None,
                "flag": True,
                "pages": 1,
                "text": "1",
                "nested": {"extras": ["map"]},
            },
            "right": {
                "name": "Paperback",
                "flag": 1,
                "pages": 1.0,
                "text": 1,
                "nested": {"extras": ["map"]},
            },
            "fields": ["null", "flag", "pages", "text", "nested"],
        }
    )
    output = render_markdown(report)
    assert "| Field | Hardcover | Paperback | Same? |" in output
    assert "| null | null | *(missing)* | No |" in output
    assert "| flag | true | 1 | No |" in output
    assert "| pages | 1 | 1.0 | Yes |" in output
    assert "| text | &quot;1&quot; | 1 | No |" in output
    assert output.index("| null |") < output.index("| flag |") < output.index("| pages |")
    evidence = output.split("```json\n")[1].rsplit("\n```", 1)[0]
    assert json.loads(evidence) == json.loads(render_json(report))


def test_untrusted_text_cannot_break_table_or_evidence_fence():
    report = analyze(
        {
            "left": {"name": "<img>|[*x*]", "field|\nline": "```\n# hostile\n</script>\\"},
            "right": {"name": "Right`", "field|\nline": "ok"},
        }
    )
    output = render_markdown(report)
    table = output.split("## JSON comparison evidence")[0]
    assert "<img>" not in table and "<script>" not in table
    assert "&#124;" in table and "&#10;" in table and "&#96;" in table
    assert all(line.count("|") == 5 for line in table.splitlines() if line.startswith("|"))
    assert "````json\n" in output
    evidence = output.split("````json\n")[1].rsplit("\n````", 1)[0]
    assert json.loads(evidence) == report


def test_empty_editions_still_produce_valid_evidence():
    report = analyze({"left": {}, "right": {}})
    output = render_markdown(report)
    assert "There are no fields to compare." in output
    assert json.loads(output.split("```json\n")[1].rsplit("\n```", 1)[0]) == report
