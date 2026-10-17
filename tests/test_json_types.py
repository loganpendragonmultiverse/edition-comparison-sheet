import pytest

from edition_comparison_sheet.json_equality import json_equal


@pytest.mark.parametrize(
    "left,right", [(True, 1), (False, 0), ({"a": [True]}, {"a": [1]}), (None, ""), ([1, 2], [2, 1])]
)
def test_json_type_or_value_change(left, right):
    assert not json_equal(left, right)


@pytest.mark.parametrize(
    "left,right", [(1, 1.0), ({"a": True, "b": [None, 1]}, {"b": [None, 1.0], "a": True}), ([], [])]
)
def test_equal_json_values(left, right):
    assert json_equal(left, right)


def test_public_comparison_distinguishes_nested_boolean_and_number():
    from edition_comparison_sheet.core import analyze

    report = analyze({"left": {"extra": {"flag": True}}, "right": {"extra": {"flag": 1}}})
    assert report["difference_count"] == 1 and not report["comparisons"][0]["same"]
