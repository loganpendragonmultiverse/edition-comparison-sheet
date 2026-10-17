# Testing

## 1.0.1 acceptance

Validate edition inputs and field selectors before comparing supplied metadata.

Verify Reject non-object input and edition values with actionable CLI errors; Validate explicit field arrays, duplicates and unknown selections; Distinguish an absent field from explicit null with presence evidence. Run the full existing quality and build gates; release only through protected PR checks and verified tag artifacts.

## 1.0.2 acceptance

Report boolean-to-number changes accurately in JSON comparison evidence.

Verify Distinguish JSON booleans from numbers recursively in objects and arrays; Retain numeric equality for 1 and 1.0, object key-order independence and list order; Add regressions against the public comparison entry point. Run the full existing quality and build gates; release only through protected PR checks and verified tag artifacts.
