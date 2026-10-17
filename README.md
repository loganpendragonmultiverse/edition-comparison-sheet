# Edition Comparison Sheet

> ⭐ **Gold Star Project**
> I consider this project complete. Fixes, maintenance and good new ideas are still welcome.
> [About Gold Stars](https://www.loganpendragonforge.com/open-source/?gold=1)
>
> Compare information about different book editions and choose which fields to include.

## What you can do

- Compare the edition details you supply, such as publisher, format or publication date.
- Choose the fields you want in the comparison.
- See when a field is missing, empty or different between editions.


## Current release 1.1.0

Markdown reports now show a side-by-side table with your edition names, selected fields and equality results. JSON values retain their types: strings are quoted, null is explicit and an absent field is marked missing. Full JSON comparison evidence follows the table. Field names, edition names and values are escaped to keep pipes, Markdown and HTML text inside their cells; backticks cannot close the evidence block.

## Earlier release 1.0.3

File outputs are created exclusively. If another process creates the destination before the report is opened, the command reports an error and preserves that file and the source input.

## Earlier release 1.0.2

Comparisons now tell the difference between booleans and numbers, even inside nested values.

JSON true differs from 1 and false differs from 0, including inside nested metadata. Numeric 1 and 1.0 compare equally; object key order does not matter, while array order does. Existing field-presence and privacy rules still apply.

## Earlier release 1.0.1

Check the edition records and your chosen fields before comparing them.

Input is an object with left and right edition objects. Optional fields is a nonempty array of unique field names present in at least one edition. Omit fields to compare the union except name. Missing and null differ; list order is significant; the tool compares supplied metadata and does not verify bibliographic truth.

[![CI](https://github.com/loganpendragonmultiverse/edition-comparison-sheet/actions/workflows/ci.yml/badge.svg)](https://github.com/loganpendragonmultiverse/edition-comparison-sheet/actions/workflows/ci.yml)

Compare book editions by contents, pagination, extras, translation, identifiers, and format. The command uses explicit UTF-8 JSON input and produces reviewable JSON or Markdown output.

## Three-minute start

```bash
python -m pip install .
edition-compare examples/sample.json
edition-compare examples/sample.json --format json --output report.json
```

The example documents the v1 input shape. Existing report files are never overwritten. Source inputs are read-only except where the documented purpose explicitly creates a new output artifact.

## Privacy and platforms

The tool runs locally and does not upload input or include telemetry. Python 3.10 or newer is supported on Windows, macOS, and Linux.

## Interpretation boundary

The comparison reflects supplied metadata and does not establish bibliographic authority or content equivalence.

## Development

```bash
python -m pip install -e ".[dev]"
ruff format --check .
ruff check .
mypy src
pytest
python -m build
```

The project is feature-complete for its documented v1 scope. Maintenance focuses on correctness, security, compatibility, and well-supported input improvements.

Part of the [Logan Pendragon Forge open-source collection](https://www.loganpendragonforge.com/open-source/). Licensed under the [MIT License](LICENSE).
