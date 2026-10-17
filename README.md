# Edition Comparison Sheet

## Current release 1.0.1

Validate edition inputs and field selectors before comparing supplied metadata.

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
