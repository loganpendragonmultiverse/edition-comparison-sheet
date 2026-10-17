# Development contract

Compare book editions by contents, pagination, extras, translation, identifiers, and format.

Preserve deterministic, source-safe behavior and the interpretation boundary documented in the README. Every feature release must update tests, version metadata, changelog, README claims, repository metadata, release assets, and the Forge catalog together.

## 1.0.1 acceptance

Validate edition inputs and field selectors before comparing supplied metadata.

Input is an object with left and right edition objects. Optional fields is a nonempty array of unique field names present in at least one edition. Omit fields to compare the union except name. Missing and null differ; list order is significant; the tool compares supplied metadata and does not verify bibliographic truth.
