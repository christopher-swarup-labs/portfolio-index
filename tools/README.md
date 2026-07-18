# Runnable Proof

This collection contains small, inspectable tools that demonstrate operating logic using synthetic data.

They are intentionally simple. The goal is to make rules visible, testable and challengeable rather than to simulate a production platform.

## Tools

| Tool | Purpose |
|---|---|
| [Pipeline Quality Scanner](pipeline-quality-scanner/README.md) | Detect common data defects that undermine pipeline reporting |
| [Lifecycle Transition Validator](lifecycle-validator/README.md) | Test lifecycle movements against explicit governance rules |

Both tools:

- Use Python's standard library only
- Operate on fictional data
- Produce structured JSON
- Include unit tests
- Require human review
- Contain no employer configuration or customer information
