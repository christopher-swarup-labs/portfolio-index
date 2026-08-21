# Runnable Proof

This collection contains small, inspectable tools that demonstrate GTM operating logic using synthetic data.

They are intentionally transparent. The goal is to make rules, evidence requirements and control boundaries visible enough to test and challenge — not to pretend a portfolio script is a production revenue platform.

[![Portfolio tools tests](https://github.com/christopher-swarup-labs/portfolio-index/actions/workflows/portfolio-tools-tests.yml/badge.svg)](https://github.com/christopher-swarup-labs/portfolio-index/actions/workflows/portfolio-tools-tests.yml)

Every change under `tools/` is validated in GitHub Actions against Python 3.12. The CI matrix runs the unit-test suite for each demonstration independently so a broken tool does not hide behind documentation claims.

## Tools

| Tool | What it demonstrates |
|---|---|
| [GTM Ops Decision Router](gtm-ops-router/README.md) | Coordination-layer routing, evidence gates, ambiguity handling and human approval boundaries |
| [Pipeline Quality Scanner](pipeline-quality-scanner/README.md) | Explicit data-quality rules that affect pipeline and reporting trust |
| [Lifecycle Transition Validator](lifecycle-validator/README.md) | Lifecycle movements tested against explicit governance rules |

All three tools:

- Use Python's standard library only
- Operate on fictional / synthetic data
- Keep decision logic inspectable
- Produce structured outputs
- Include unit tests
- Run in GitHub Actions
- Require human review
- Contain no employer configuration, customer information or production credentials

## Why code belongs in this portfolio

Most senior MOPS and RevOps work is not software engineering. But increasingly, GTM leaders need to be able to express operating logic precisely enough for automation, agents and technical teams to implement it safely.

These tools show the bridge between an operating rule and something executable:

**business definition → explicit rule → test → structured output → human decision**

For the wider architecture, see [AI GTM Operations](../AI-GTM-OPS.md) and the [GTM Command Center](../skills/command-center/README.md).
