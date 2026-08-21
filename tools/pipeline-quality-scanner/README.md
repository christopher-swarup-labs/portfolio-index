# Pipeline Quality Scanner

> **Evidence classification:** Synthetic portfolio demonstration. This is not employer production code or production data.

## Business problem

Pipeline reporting can look sophisticated while being built on records that are structurally unreliable.

Before debating attribution models, forecast methodology or AI-generated pipeline insight, I want to know whether the underlying opportunity data can support the decision being asked of it.

This tool makes a small set of pipeline-quality rules explicit and inspectable.

## What it checks

| Rule | Why it matters |
|---|---|
| Missing required fields | A record cannot support reliable ownership, value, timing or source analysis when core fields are absent |
| Duplicate opportunity IDs | Duplicate commercial objects distort pipeline totals and conversion analysis |
| Invalid / non-positive amounts | Revenue reporting needs a usable monetary value |
| Invalid dates | Broken dates make velocity, ageing and forecast timing unreliable |
| Close date before created date | Impossible sequencing is a strong data-quality signal |
| Open opportunity with past close date | Stale timing weakens forecast and pipeline pacing |
| Missing source | Source / attribution analysis cannot be defended without the agreed source field |

The rules are deliberately simple. The point is to show how an operating definition becomes a testable control.

## Run

Requires Python 3.11+ and only the standard library.

```bash
python scanner.py sample_pipeline.csv --as-of 2026-03-01
```

Run the tests:

```bash
python -m unittest
```

The repository's GitHub Actions matrix runs the tool's unit tests whenever `tools/` changes.

## Output contract

The scanner returns structured JSON rather than a narrative opinion.

Example shape:

```json
{
  "records_scanned": 8,
  "issues_found": 5,
  "issues_by_rule": {
    "duplicate_id": 1,
    "missing_required": 2,
    "stale_open": 2
  },
  "issues_by_severity": {
    "high": 3,
    "medium": 2
  },
  "human_review_required": true
}
```

Counts above illustrate the output contract; the included sample file is the source of truth for an actual run.

## Operating interpretation

The scanner does **not** say “fix every error automatically.” It helps a Revenue Operations owner decide which defects affect a commercial decision.

For example:

- A missing source may block source-attribution reporting but not a forecast value check
- A stale close date may be more urgent when the opportunity is material and late-stage
- A duplicate opportunity ID may require investigation before any pipeline aggregate is trusted

The business decision determines remediation priority.

## Human accountability

A named CRM or Revenue Operations owner should approve remediation because a technically obvious correction can still change pipeline, attribution, territory or executive reporting.

The tool therefore reports findings and always returns `human_review_required: true`; it does not write back to a CRM.

## What this demonstrates

- Translating pipeline-governance rules into executable controls
- Making data-quality logic visible rather than hidden in a dashboard or automation platform
- Separating detection from commercial decision-making
- Structured outputs that another workflow, analyst or agent could consume
- Testable logic without requiring access to employer systems

## What it does not prove

- Production deployment
- Forecast-model accuracy
- A complete enterprise data-quality framework
- Automated CRM remediation
- Access to any former employer data or configuration

## Data boundary

`sample_pipeline.csv` is fully synthetic. The public portfolio should never be used as a production-data processing environment.

## Related portfolio evidence

- [Pipeline Truth](../../frameworks/pipeline-truth.md)
- [Pipeline Truth & Attribution case](../../case-studies/flagship/pipeline-truth-and-attribution.md)
- [AI GTM Operations](../../AI-GTM-OPS.md)
- [GTM Ops Decision Router](../gtm-ops-router/README.md)
