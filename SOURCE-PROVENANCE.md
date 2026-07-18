# Source Provenance Register

## Purpose

This register records where portfolio ideas came from and how source material was treated before publication.

It exists to prevent accidental copying of employer material, proprietary code, confidential data, personal information or third-party intellectual property.

## Source classifications

| Source type | Meaning | Allowed treatment | Direct upload allowed? |
|---|---|---|---|
| **Accumulated professional knowledge** | Experience and judgement developed across roles | Reframe into original, company-neutral content | Yes, after review |
| **Validated operator evidence** | Historic work showing diagnosis, design, implementation, governance or leadership | Extract principles privately and rebuild from scratch | No |
| **Supporting evidence** | Material supporting chronology, context or breadth | Validate context; do not reproduce | No |
| **Independent strategic exercise** | Assessment or hypothetical work without implementation responsibility | Rebuild and label clearly | No source upload |
| **CV or public professional profile** | Role context, chronology and self-reported claims | Use after accuracy and metric review | Selectively |
| **Claude audit output** | Analysis produced from Claude-accessible skills or professional context | Treat as an audit input, not proof; reconcile with source evidence | No direct proof status |
| **Applied third-party methodology** | Forrester, SiriusDecisions, MEDDICC, SPICED or other established methods | Attribute and describe Christopher's adaptation | No copied training material |
| **Internal dashboard or dataset** | Real operational or commercial data | Recreate with synthetic data and generic labels | No |
| **Owned venture material** | Material relating to a venture owned or built by Christopher | Use selectively after venture-specific review | Sometimes |
| **Third-party reference** | Training, research, analyst or vendor material | Cite where material; never present as original work | No direct copying |
| **External public research** | Public source used to validate a current fact or claim | Summarise with attribution | No direct copying by default |
| **Source code from another repository** | Code or configuration outside this portfolio | Reference only unless publication rights are explicit | No by default |
| **Restricted personal or confidential material** | Credentials, identity, employment, legal, customer or production records | Exclude completely | Never |

## Evidence treatment statuses

- **Not started**
- **Reconstruction in progress**
- **Evidence review required**
- **Confidentiality review required**
- **Approved for private portfolio**
- **Approved for public adaptation**
- **Blocked**

## Portfolio source map

| Collection | Primary source category | Required treatment | Status |
|---|---|---|---|
| Revenue and Commercial Operating Systems | Validated operator evidence plus accumulated professional knowledge | Composite company-neutral reconstruction | Approved for private portfolio |
| Lifecycle, Qualification and Handoffs | Historic lifecycle, scoring, routing, SLA and handoff work | Rebuild with neutral language and synthetic records | Approved for private portfolio |
| Campaign and Platform Operations | Campaign and platform-governance experience | Create platform-neutral case and framework | Not started |
| Martech, Data and Transformation | Audits, migrations, architecture and business cases | Remove company architecture and rebuild decision models | Not started |
| Analytics, Attribution and Decision Systems | Attribution, reporting and pipeline experience | Reconstruct with explicit limitations and synthetic data | Approved for private portfolio |
| Team and Transformation Leadership | Charters, service models and distributed-delivery experience | Composite leadership reconstruction | Approved for private portfolio |
| AI-Assisted GTM Operations | Professional AI workflows, Claude audit and high-level architecture evidence | Separate verified architecture, draft specifications and new synthetic tools | Approved with verification boundary |
| Independent Strategic Exercises | Recruitment or assessment cases | Label assumptions and non-implementation status | Not started |
| Lynr Venture Retrospective | Owned venture material | Exclude customer claims, private economics and proprietary delivery detail | Approved for private portfolio |
| Other Venture Retrospectives | Owned venture material | Separate publication review for each venture | Not started |

## Applied third-party methodology

Several reported skill constructs originate in established Forrester / SiriusDecisions methodology, including the Demand Unit Waterfall, Programme Pendulum, Achievability Index, Cooperation Index and Demand Management Council. MEDDICC and SPICED are also established third-party sales methodologies.

Portfolio treatment:

- Attribute the base methodology.
- Describe Christopher as a trained or certified practitioner only where supported.
- Claim originality only for independently evidenced orchestration, diagnostic sequencing, evidence classification, operating adaptation and human-accountability controls.
- Do not reproduce proprietary training content, diagrams or certification material.

Attribution is a credibility control, not a concession.

## Claude portfolio audit treatment

The uploaded Claude files were used as a structured audit input. They are not treated as proof by themselves.

Claude reported that it inspected several skill packages in its available skill environment and identified originality and provenance issues. Until underlying files or approved exports are supplied:

- The packages remain **candidate evidence**.
- Their implementation status remains **pending verification**.
- They may be named in the audit catalogue.
- They must not be presented as repository-verified built tooling.
- Generated specifications must be labelled as drafts or concepts.

## Artefact register

| Artefact | Source classification | Status | Treatment |
|---|---|---|---|
| `PROFILE.md` | CV and public professional context | Approved for private portfolio | Public chronology only; private metrics excluded |
| `OPERATOR-THESIS.md` | Accumulated professional knowledge | Approved for private portfolio | Original thesis written for portfolio |
| `ENTREPRENEUR-JOURNEY.md` | Owned venture context and accumulated professional knowledge | Approved for private portfolio | High-level journey; no traction or financial claims |
| `SKILLS-AND-SYSTEMS.md` | Claude audit plus professional evidence | Evidence review required | Separates candidate skills, architecture and applied methodology |
| `skills/command-center/README.md` | High-level architecture evidence plus portfolio reconstruction | Approved with verification boundary | Architecture represented; historical modules not claimed as verified |
| `skills/crm-data-quality-auditor/README.md` | New portfolio specification | Evidence review required | Draft exemplar; not proof of historical built tooling |
| `frameworks/revenue-operating-system.md` | Accumulated professional knowledge | Approved for private portfolio | Original portfolio framework |
| `frameworks/lifecycle-governance.md` | Composite implemented experience | Approved for private portfolio | Company-neutral reconstruction |
| `frameworks/pipeline-truth.md` | Composite implemented experience | Approved for private portfolio | Company-neutral reconstruction |
| `frameworks/mops-operating-model.md` | Composite leadership experience | Approved for private portfolio | Company-neutral reconstruction |
| `case-studies/flagship/revenue-operating-system.md` | Composite implemented experience | Approved for private portfolio | No exact employer or customer detail |
| `case-studies/flagship/unified-lifecycle-governance.md` | Composite implemented experience | Approved for private portfolio | No real records or system configuration |
| `case-studies/flagship/pipeline-truth-and-attribution.md` | Composite implemented experience | Approved for private portfolio | No exact metrics or employer attribution |
| `case-studies/leadership/modern-mops-team-operating-model.md` | Composite implemented leadership experience | Approved for private portfolio | Company-neutral operating pattern |
| `case-studies/ventures/building-lynr.md` | Owned venture material | Approved for private portfolio | No customer claims, private economics or proprietary delivery detail |
| `tools/pipeline-quality-scanner/*` | New synthetic demonstration | Approved for private portfolio | Fictional records; standard-library Python; tested locally |
| `tools/lifecycle-validator/*` | New synthetic demonstration | Approved for private portfolio | Fictional records; explicit rules; tested locally |
| `evidence/claim-register.md` | Approved professional material | Evidence review required | Claims classified rather than asserted |
| `evidence/verification-backlog.md` | Portfolio governance | Reconstruction in progress | Records unresolved evidence and decisions |
| `README.md` | Portfolio synthesis | Approved for private portfolio | Employer and investor navigation |
| `REVIEWER-GUIDE.md` | Portfolio synthesis | Approved for private portfolio | Role-specific review paths |
| `ROADMAP.md` | Portfolio governance | Approved for private portfolio | Current state and next evidence wave |

## Required provenance entry for each artefact

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
- Draft specification pending verification

### Metrics status values

- Verified and safe to disclose
- Verified but generalised
- Directional only
- Assumption or projection
- Unverified and excluded
- No metrics used

## Private source-reference rule

Portfolio artefacts may record a high-level source family. They must not embed private Drive links, employer file paths, internal system URLs, customer or employee names, credential locations or production identifiers.

Detailed private source trails, where needed, must be maintained outside the reviewer-facing repository surface.

## Current declaration

All current case studies, frameworks, skills and tools were written specifically for this private repository.

No historic employer document, production dataset, credential, third-party training file or external repository source file has been uploaded. New tools use synthetic data only. Source material has been used only to validate chronology, identify transferable patterns, classify claims and establish the verification backlog.
