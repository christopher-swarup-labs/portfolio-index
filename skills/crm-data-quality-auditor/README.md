# CRM Data Quality Auditor

> **Evidence classification: Portfolio-safe skill specification — DRAFT, pending Christopher's verification.**
>
> This document is the **format exemplar** for every skill in this library. It is a specification of decision logic, not a reconstruction of a verified artefact. It should not be published as evidence of built tooling until Christopher confirms the underlying skill exists and the logic below matches it.

---

## Executive summary

Locates the specific data defects in a CRM that are corrupting pipeline reporting, routing and forecasting — and separates defects that matter commercially from defects that are merely untidy.

Most CRM data-quality exercises fail by treating all incompleteness as equally bad. They generate a long defect list, the business ignores it, and the underlying reporting problem persists. This skill inverts that: it starts from the broken commercial decision and works backwards to the fields that actually drive it.

## Business problem

An organisation cannot trust its pipeline numbers. Symptoms usually present as forecast misses without an obvious cause, routing complaints from reps, marketing-sourced pipeline that Sales disputes, or attribution reporting that changes depending on who runs it.

The instinct is to buy an enrichment or hygiene tool. That treats the symptom. The underlying issue is typically a small number of fields, populated inconsistently at a specific lifecycle transition, whose defects propagate into every downstream report.

## When to use it

- Reporting credibility has broken down and the cause is contested between teams
- Ahead of a lifecycle, routing or scoring redesign — to establish what the data can actually support
- During post-merger CRM consolidation, where two populated-but-incompatible datasets are being merged
- Before automating any decision that depends on a CRM field

**Prerequisites:** read access to object and field definitions; a stated list of the reports or decisions that depend on the data; a named owner per object.

**Warning signs it is needed:** teams maintaining private spreadsheets alongside the CRM; the same report producing different numbers for different people; routing exceptions handled manually as routine.

## When not to use it

- **When ownership is undefined.** If no one owns the Lead or Account object, a defect list has nowhere to go. Fix ownership first — this is an operating-model problem wearing a data costume.
- **When the real dispute is about definitions.** If Marketing and Sales disagree on what "qualified" means, the field is not defective; the agreement is missing. A data audit will produce a technically correct report that resolves nothing.
- **As a substitute for a lifecycle design.** This skill assesses whether data supports a model. It does not design the model.

## Inputs

| Input | Form | Required |
|---|---|---|
| Object and field inventory | Field name, type, picklist values, required flag | Yes |
| Dependent decisions | List of reports, routing rules and scoring inputs relying on each field | Yes |
| Population profile | Completeness and distinct-value counts by field, segmented by record source and creation period | Yes |
| Lifecycle-stage definitions | Documented entry and exit criteria per stage | Yes |
| Ownership map | Named owner per object and per critical field | Yes |
| Known exception paths | Documented manual overrides | No |

Inputs are structural and statistical. **No record-level data is required or accepted** — the skill operates on schema and aggregate profile, never on customer or prospect records.

## Outputs

- **Commercial-impact ranking** — defects ordered by the value of the decision they corrupt, not by defect volume
- **Root-cause classification** per defect: capture-point failure, integration overwrite, definitional ambiguity or process non-compliance
- **Blast-radius map** — reports and automations consuming each defective field
- **Remediation sequence** — what must be fixed at source, what can be corrected in flight and what should be accepted
- **Governance recommendations** — capture-point controls preventing recurrence
- **Evidence log** — what was observed, inferred or could not be determined

## Decision logic

1. **Anchor on decisions, not fields.** Enumerate the commercial decisions the CRM must support. A field feeding none of them is out of scope regardless of incompleteness.
2. **Trace each decision to its field dependencies**, including indirect dependencies through formulas and integrations.
3. **Profile only the dependent fields.** Examine completeness and distinct values, segmented by record source and creation period. Uniform incompleteness suggests a design gap; concentration in one source or period suggests a process or integration failure.
4. **Classify root cause** before proposing a fix. The same visible defect produced by capture failure and integration overwrite requires different remediation.
5. **Test definitional integrity.** When a field's population contradicts its documented definition, flag the definition as a potential defect rather than assuming the data is wrong.
6. **Rank by blast radius × decision value**, not row count.
7. **Separate source fixes from in-flight corrections.** Correction without source remediation guarantees recurrence.
8. **State what could not be assessed** and why.

No employer-specific field architecture, picklist taxonomy or integration configuration is reproduced.

## Human accountability

| Decision | Owner |
|---|---|
| Which decisions are in scope | Revenue Operations lead |
| Accepting a defect as tolerable | Named object owner |
| Changing a field definition | Cross-functional; Marketing and Sales sign-off |
| Mass data modification | CRM owner with documented approval and rollback plan |
| Changing a capture-point control | Process owner for the affected channel |

**Cannot be automated:** mass updates to existing records, field-definition changes and decisions to accept a defect. The skill produces recommendations and an evidence trail. A named human approves and owns the outcome.

**Escalation:** where two owners disagree on a definition, the skill records the conflict and escalates rather than selecting a winner. Definitional disputes are governance decisions, not analytical ones.

## Evidence and grounding

Every finding is labelled:

- **Fact** — directly observed in schema or aggregate profile
- **Assumption** — stated explicitly with its basis
- **Inference** — conclusion drawn from pattern, with confidence stated
- **Missing evidence** — required input unavailable, with impact on the finding
- **Conflicting evidence** — sources disagree; both recorded
- **Recommendation** — proposed action, distinguished from findings

An output that cannot separate observation from inference is not usable in a governance forum.

## Failure modes

- **Volume bias** — ranking by defect count surfaces low-value fields and buries the few that matter
- **Automation bias** — a ranked, polished output invites acceptance without inspection
- **Unsupported causal claims** — correlation between incompleteness and lost deals is not causation
- **Wrong system authority** — auditing the CRM when the defect originates upstream
- **Definitional blindness** — assessing conformity to a definition that is itself wrong
- **Snapshot distortion** — profiling without segmenting by period conflates historical debt with current failure
- **Scope creep into lifecycle redesign** — discovering the model is wrong requires a separate engagement and stakeholders

## Synthetic example

*Fully fictional. No real organisation, system or data.*

**Northwind Analytics** is a 400-employee B2B SaaS company operating in EMEA and North America. Its forecast has missed three consecutive quarters and Sales disputes marketing-sourced pipeline.

Decisions in scope:

1. Marketing-sourced pipeline reporting
2. Inbound lead routing
3. Forecast-stage weighting

Profiling eleven dependent fields finds `Lead_Source_Detail` at 71% completeness overall. Segmented by source, it is 96% complete for form-fill records and 12% for records created by an events integration. Events records are also the records Sales disputes most.

The likely root cause is classified as **integration overwrite**: the events integration writes to a legacy field and nulls `Lead_Source_Detail` during update. Blast radius: one pipeline report and two routing rules.

Separately, `Qualification_Stage` has a population pattern inconsistent with its documented definition: 34% of records marked `Qualified` have no populated qualification-criteria field. This is classified as **definitional ambiguity** and escalated rather than remediated because Marketing and Sales operate different definitions.

## Expected output

```text
FINDING 01 — Lead_Source_Detail integration overwrite
Severity: High
Classification: FACT — observed in aggregate profile segmented by source

Form-fill records: 96% complete
Events records: 12% complete

Root cause: INFERENCE — high confidence
Basis: null pattern aligns with integration update timing
Not confirmed: integration field mapping requires review

Recommendation: fix the source integration mapping.
Do not backfill records until the source defect is corrected.

Owner: Revenue Operations lead
Approval required: CRM owner

FINDING 02 — Qualification_Stage definition conflict
Severity: High
Classification: CONFLICTING EVIDENCE

Documented definition requires qualification criteria.
A material share of records marked Qualified has no criteria populated.
Marketing and Sales use different working definitions.

ESCALATED — governance decision, not a data correction.
Owner: unresolved; joint Marketing and Sales sign-off required.

NOT ASSESSED
Opportunity data was not provided.
Impact: forecast-stage weighting remains incomplete.
```

## Limitations

The skill assesses whether data can support a decision. It cannot determine whether the decision is commercially right; that requires judgement about the business model, sales motion and market.

It relies on documented lifecycle definitions. When these do not exist, the audit degrades into observation without a standard to test against, and the correct output is to stop and state the gap.

Root-cause classification is inference. It narrows candidate causes but does not replace inspecting the integration or process.

Organisation-specific context — acquisitions, deliberate strategic-account exceptions or fields repurposed years earlier — can explain anomalies invisible to structural analysis. Human review is mandatory.

## Source provenance

Category: new portfolio specification informed by operator practice in enterprise and high-growth B2B environments. No employer configuration, field architecture, integration mapping or data is reproduced. The synthetic example is wholly fictional.
