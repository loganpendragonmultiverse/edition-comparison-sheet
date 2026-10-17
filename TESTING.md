# Testing

## 1.0.1 acceptance

Validate edition inputs and field selectors before comparing supplied metadata.

Verify Reject non-object input and edition values with actionable CLI errors; Validate explicit field arrays, duplicates and unknown selections; Distinguish an absent field from explicit null with presence evidence. Run the full existing quality and build gates; release only through protected PR checks and verified tag artifacts.

## 1.0.2 acceptance

Report boolean-to-number changes accurately in JSON comparison evidence.

Verify Distinguish JSON booleans from numbers recursively in objects and arrays; Retain numeric equality for 1 and 1.0, object key-order independence and list order; Add regressions against the public comparison entry point. Run the full existing quality and build gates; release only through protected PR checks and verified tag artifacts.

## 1.0.3 acceptance

Create JSON and Markdown report destinations exclusively. Verify a destination created immediately before opening is preserved, the command returns an actionable error, source input bytes stay unchanged, and new destinations still work. Run formatting, lint, typing, the full test suite, builds, and the runtime dependency audit before protected release.

## 1.1.0 readable comparison sheets

Render a side-by-side Markdown table without changing JSON comparison semantics or selected-field order. Distinguish missing, null, booleans, numbers and strings; preserve nested values. Escape user-controlled table text and choose a safe evidence fence. Retain full JSON comparison evidence and exclusive output creation.
