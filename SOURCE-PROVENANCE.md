# Source Provenance Register

## Purpose

This register records where portfolio ideas came from and how source material was treated before publication.

It exists to prevent accidental copying of employer material, proprietary code, confidential data, personal information or third-party intellectual property.

## Source classifications

| Source type | Meaning | Allowed treatment | Direct upload allowed? |
|---|---|---|---|
| **Accumulated professional knowledge** | Experience and judgement developed across roles | Reframe into original, company-neutral content | Yes, after review |
| **Validated operator evidence** | Historic work showing diagnosis, design, implementation, governance or leadership | Extract principles privately and rebuild from scratch | No |
| **Supporting evidence** | Material that supports chronology, context or breadth | Use to validate context; do not reproduce | No |
| **Independent strategic exercise** | Assessment or hypothetical work created without implementation responsibility | Rebuild and label clearly as an exercise | No source upload |
| **CV or public professional profile** | Public role context and claims | Use after accuracy and metric review | Yes, selectively |
| **Internal dashboard or dataset** | Real operational or commercial data | Recreate with synthetic data and generic labels | No |
| **Owned venture material** | Material relating to a business or product owned or built by Christopher | Use selectively after venture-specific confidentiality review | Sometimes |
| **Third-party reference** | Training, research, templates, analyst or vendor material | Cite where material; never present as original work | No direct copying |
| **External public research** | Public sources used to validate a current fact or market claim | Summarise with attribution | No direct copying by default |
| **Source code from another repository** | Code or configuration outside the portfolio repository | Reference only unless ownership and publication rights are explicit | No by default |
| **Restricted personal or confidential material** | Credentials, identity, employment, legal, customer or production records | Exclude completely | Never |

## Evidence treatment statuses

Every artefact must carry one of these statuses during production:

- **Not started** — source family identified; no portfolio artefact exists
- **Reconstruction in progress** — independently authored draft exists
- **Evidence review required** — contribution, ownership or metrics need validation
- **Confidentiality review required** — content is not yet safe for reviewer access
- **Approved for private portfolio** — passed quality, provenance and confidentiality review
- **Approved for public adaptation** — separately reviewed for wider publication
- **Blocked** — evidence cannot safely or accurately be used

## Portfolio source map

| Portfolio collection | Primary source category | Required treatment | Current status |
|---|---|---|---|
| Revenue and Commercial Operating Systems | Validated operator evidence plus independent strategic exercises | Blend patterns across roles; separate implemented experience from exercises | Not started |
| Lifecycle, Qualification and Handoffs | Historic lifecycle, status, scoring, routing, SLA and handoff work | Rebuild in neutral language with synthetic records | Not started |
| Campaign and Platform Operations | Campaign manuals, process standards and platform-governance experience | Create a new platform-neutral operating system | Not started |
| Martech, Data and Transformation | Platform audits, migration plans, architecture and business cases | Remove company architecture and rebuild decision models | Not started |
| Analytics, Attribution and Decision Systems | Attribution, QBR, dashboard, pipeline and measurement work | Use synthetic datasets; explain model limits | Not started |
| Team and Transformation Leadership | Charters, service hubs, workstream plans and enablement work | Rebuild team and governance models; clarify personal contribution | Not started |
| AI-Assisted GTM Operations | Personal AI workflows and employer-context demonstrations | Build a new synthetic demonstration with human controls | Not started |
| Independent Strategic Exercises | Recruitment or assessment cases | Label assumptions and non-implementation status prominently | Not started |
| NXClarity Venture Retrospective | Owned venture material | Review commercial claims, market data and private founder content | Not started |
| Snugtot Concept Retrospective | Owned concept material | Treat projections as assumptions; validate market claims before reuse | Not started |
| Building Lynr | Owned venture material | Use only approved operating and commercial content | Not started |
| ThinkBud Product Build | Owned venture experience | High-level case only by default; no credentials, private data, repository migration or production detail | Not started |

## Drive audit declaration

The Google Drive evidence audit:

- Traversed the principal work archives and active-project folders
- Classified the relevant work into 26 capability domains
- Validated representative content across operating models, lifecycle, campaigns, martech, data, attribution, leadership, AI and ventures
- Identified third-party material that cannot be treated as original work
- Identified credentials, personal records, legal material, production data and confidential source artefacts that are blocked from portfolio use

The audit is a coverage and provenance control. It does not transfer ownership or publication rights.

See:

- [DRIVE-EVIDENCE-AUDIT.md](DRIVE-EVIDENCE-AUDIT.md)
- [WORKSTREAM-COVERAGE.md](WORKSTREAM-COVERAGE.md)
- [EXCLUSION-REGISTER.md](EXCLUSION-REGISTER.md)

## Required provenance entry for each artefact

Record the following in the artefact repository:

```text
Artefact name:
Repository:
Author:
Artefact type:
Source classification:
Source-era or evidence-family reference:
Personal contribution confirmed:
Implementation status:
Third-party concepts used:
Direct quotations used:
Real data used:
Synthetic data created:
Metrics status:
Employer or customer identifiers removed:
Ownership and publication basis confirmed:
Confidentiality review status:
Reviewer:
Review date:
Notes and limitations:
```

### Implementation status values

- Implemented operator work — reconstructed
- Composite of implemented experience across roles
- Independent strategic exercise
- Owned venture work
- New portfolio framework
- New synthetic demonstration

### Metrics status values

- Verified and safe to disclose
- Verified but generalised
- Directional only
- Assumption or projection
- Unverified and excluded
- No metrics used

## Private source-reference rule

A portfolio artefact may record a high-level source-era or evidence-family reference. It should not embed:

- Private Drive links
- Employer file paths
- Internal system URLs
- Customer or employee names
- Credential locations
- Production record identifiers

Where a more detailed source trail is needed for personal verification, maintain it outside the shared portfolio surface and protect it separately.

## Current declaration

The foundation and audit files in `portfolio-index` were written specifically for this private portfolio.

No historic employer document, production dataset, credential, third-party training file or external repository file has been uploaded into the organisation. The source material was used only to validate coverage and identify transferable operating patterns.