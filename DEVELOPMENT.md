# Development contract

Compare book editions by contents, pagination, extras, translation, identifiers, and format.

Preserve deterministic, source-safe behavior and the interpretation boundary documented in the README. Every feature release must update tests, version metadata, changelog, README claims, repository metadata, release assets, and the Forge catalog together.

## 1.0.1 acceptance

Validate edition inputs and field selectors before comparing supplied metadata.

Input is an object with left and right edition objects. Optional fields is a nonempty array of unique field names present in at least one edition. Omit fields to compare the union except name. Missing and null differ; list order is significant; the tool compares supplied metadata and does not verify bibliographic truth.

## 1.0.2 acceptance

Report boolean-to-number changes accurately in JSON comparison evidence.

JSON true differs from 1 and false differs from 0, including inside nested metadata. Numeric 1 and 1.0 compare equally; object key order does not matter, while array order does. Existing field-presence and privacy rules still apply.

## Gold Star scope review — 2026-10-17

Reviewed release: v1.0.2. Explicit comparison of supplied edition metadata with validated selected fields and field-presence evidence.

The identified useful scope gaps have been implemented and verified. This review found no remaining meaningful contribution inside the documented purpose; optionality alone is not a reason to exclude a useful in-scope feature. Bugs, compatibility and dependency maintenance remain active work, and a meaningful new idea can reopen the scope. Gold status is bound to the reviewed release in the Forge catalog. Reassess or remove that status when a new gap is identified.

Definition: https://www.loganpendragonforge.com/open-source/gold-star/
