# Pipeline Quality Scanner

> **Evidence classification:** New synthetic demonstration.

## Purpose

Scan a synthetic opportunity file for common defects that undermine reporting and forecasting.

This tool demonstrates the principle that data-quality rules should be explicit and inspectable.

## Checks

- Missing required fields
- Duplicate opportunity IDs
- Invalid or non-positive amounts
- Invalid date formats
- Close dates before created dates
- Open opportunities with past close dates
- Missing source data

## Run

```bash
python scanner.py sample_pipeline.csv --as-of 2026-03-01
```

The output is JSON containing issue counts, severity and record-level findings.

## Test

```bash
python -m unittest test_scanner.py
```

## Human accountability

The scanner does not modify data or determine commercial action. A named CRM or Revenue Operations owner must review every remediation.

## Data boundary

The included CSV is fully synthetic. Do not run the portfolio copy of this tool against production data.
