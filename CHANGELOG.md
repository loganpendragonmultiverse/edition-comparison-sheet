# Changelog

## 1.1.0

- Show a readable side-by-side Markdown comparison table with typed values and explicit missing fields.
- Retain complete JSON evidence and escape user-controlled table text and evidence fences.

## 1.0.3 - 2026-10-17

- Create report files exclusively so a destination arriving during export is never overwritten.
- Add JSON and Markdown collision regressions that also verify source preservation.

## 1.0.2 - 2026-10-17

- Distinguish JSON booleans from numbers recursively in objects and arrays
- Retain numeric equality for 1 and 1.0, object key-order independence and list order
- Add regressions against the public comparison entry point

## 1.0.1 - 2026-10-17

- Reject non-object input and edition values with actionable CLI errors
- Validate explicit field arrays, duplicates and unknown selections
- Distinguish an absent field from explicit null with presence evidence

## 1.0.0 - 2026-07-26

- Released the first complete Edition Comparison Sheet command-line workflow.
- Added deterministic reporting, representative examples, cross-platform tests, and explicit limitations.
