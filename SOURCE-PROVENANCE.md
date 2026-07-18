# Source Provenance Register

## Purpose

This register records where portfolio ideas came from and how source material was treated before publication.

It exists to prevent accidental copying of employer material, private product implementation, confidential data, personal information or third-party intellectual property.

## Source classifications

| Source type | Meaning | Allowed treatment | Direct upload allowed? |
|---|---|---|---|
| **Accumulated professional knowledge** | Experience and judgement developed across roles | Reframe into original, company-neutral content | Yes, after review |
| **Validated operator evidence** | Historic work showing diagnosis, design, implementation, governance or leadership | Extract principles privately and rebuild from scratch | No |
| **Supporting evidence** | Material supporting chronology, context or breadth | Validate context; do not reproduce | No |
| **Independent strategic exercise** | Assessment or hypothetical work without implementation responsibility | Rebuild and label clearly | No source upload |
| **CV or public professional profile** | Role context, chronology and self-reported claims | Use after accuracy and metric review | Selectively |
| **Claude audit output** | Analysis produced from Claude-accessible skills or professional context | Treat as an audit input, not proof; reconcile with source evidence | No direct proof status |
| **Applied third-party methodology** | Established analyst, sales or operating methods | Attribute the base method and describe my adaptation | No copied training material |
| **Internal dashboard or dataset** | Real operational or commercial data | Recreate with synthetic data and generic labels | No |
| **Owned venture material** | Material relating to a venture I own or built | Use selectively after venture-specific review | Sometimes |
| **External public research** | Public material used to validate a current fact or claim | Summarise with attribution | No direct copying by default |
| **Source code from another repository** | Code or configuration outside this portfolio | Reference only unless publication rights and need are explicit | No by default |
| **Restricted material** | Private records, credentials, production data or information that does not belong in reviewer evidence | Exclude completely | Never |

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
| Campaign and Platform Operations | Campaign and platform-governance experience | Rebuild as a platform-neutral operating system | Approved for private portfolio |
| Martech, Data and Transformation | Audits, migrations, architecture and business cases | Remove company architecture and rebuild decision models | Not started |
| Analytics, Attribution and Decision Systems | Attribution, reporting and pipeline experience | Reconstruct with explicit limitations and synthetic data | Approved for private portfolio |
| Team and Transformation Leadership | Charters, service models and distributed-delivery experience | Composite leadership reconstruction | Approved for private portfolio |
| AI-Assisted GTM Operations | Professional AI workflows, Claude audit and architecture evidence | Separate verified architecture, draft specifications and synthetic tools | Approved with verification boundary |
| ThinkBud Venture Build | Owned ThinkBud material plus read-only verification of the separate private product repository | Describe the product, decisions and architecture at a high level; do not migrate implementation or user information | Approved for private portfolio |
| Lynr Venture Retrospective | Owned Lynr material | Exclude private commercial and delivery detail | Approved for private portfolio |
| Other Venture Retrospectives | Owned venture material | Separate publication review for each venture | Not started |

## Third-party methodology

Some historical skill material uses established methods including Forrester and SiriusDecisions demand frameworks, MEDDICC and SPICED.

Portfolio treatment:

- Attribute the base methodology.
- Describe me as a trained or certified practitioner only where supported.
- Claim originality only for independently evidenced orchestration, diagnostic sequencing, evidence classification, operating adaptation and human-accountability controls.
- Do not reproduce proprietary training content or certification material.

Attribution is a credibility control, not a concession.

## Claude portfolio audit treatment

The uploaded Claude files were used as a structured audit input. They are not treated as proof by themselves.

Until the underlying approved files are supplied:

- Reported packages remain candidate evidence.
- Their historical implementation status remains pending verification.
- They may be named in the audit catalogue.
- They must not be presented as repository-verified built tooling.
- Generated specifications must be labelled as drafts or concepts.

## ThinkBud source treatment

ThinkBud is an owned venture and a working product build, but its product repository remains a separate boundary.

For the portfolio case, I reviewed the private repository documentation read-only to verify:

- Controlled-beta status
- Adaptive and spaced-review design
- Event-sourced learning architecture
- Parent and learner boundaries
- Server-side grading and access controls
- Testing and release approach

No ThinkBud source code, production configuration, private learner records or internal identifiers were copied into this repository.

The published case uses a first-person, portfolio-safe description of what I built, the decisions I made, what the platform currently proves and what remains unproven.

## Artefact register

| Artefact | Source classification | Status | Treatment |
|---|---|---|---|
| `PROFILE.md` | CV, public professional context and owned venture context | Approved for private portfolio | Public chronology and portfolio-safe ThinkBud summary |
| `OPERATOR-THESIS.md` | Accumulated professional knowledge | Approved for private portfolio | Original thesis written for the portfolio |
| `ENTREPRENEUR-JOURNEY.md` | Owned venture context and accumulated professional knowledge | Approved for private portfolio | ThinkBud represented as the primary completed product build |
| `SKILLS-AND-SYSTEMS.md` | Professional evidence, Claude audit and ThinkBud build context | Evidence review required | Separates practical product evidence, candidate skills and applied methodology |
| `skills/command-center/README.md` | High-level architecture evidence plus portfolio reconstruction | Approved with verification boundary | Architecture represented; historical modules not claimed as verified |
| `skills/crm-data-quality-auditor/README.md` | New portfolio specification | Evidence review required | Draft exemplar; not proof of historical built tooling |
| `case-studies/ventures/building-thinkbud.md` | Owned ThinkBud venture material and read-only repository verification | Approved for private portfolio | No source migration, private configuration or user information |
| `case-studies/ventures/building-lynr.md` | Owned Lynr venture material | Approved for private portfolio | No customer claims or private commercial detail |
| `frameworks/revenue-operating-system.md` | Accumulated professional knowledge | Approved for private portfolio | Original portfolio framework |
| `frameworks/lifecycle-governance.md` | Composite implemented experience | Approved for private portfolio | Company-neutral reconstruction |
| `frameworks/campaign-operations.md` | Composite campaign and platform experience | Approved for private portfolio | Company-neutral operating framework |
| `frameworks/pipeline-truth.md` | Composite implemented experience | Approved for private portfolio | Company-neutral reconstruction |
| `frameworks/mops-operating-model.md` | Composite leadership experience | Approved for private portfolio | Company-neutral operating pattern |
| `case-studies/flagship/*` | Composite implemented experience | Approved for private portfolio | No named employer or private operational detail |
| `case-studies/leadership/*` | Composite implemented leadership experience | Approved for private portfolio | Company-neutral operating pattern |
| `tools/pipeline-quality-scanner/*` | New synthetic demonstration | Approved for private portfolio | Fictional records and tested logic |
| `tools/lifecycle-validator/*` | New synthetic demonstration | Approved for private portfolio | Fictional records and tested logic |
| `evidence/claim-register.md` | Approved professional material | Evidence review required | Claims classified rather than asserted |
| `evidence/verification-backlog.md` | Portfolio governance | Reconstruction in progress | Records unresolved evidence and decisions |
| `README.md` | Portfolio synthesis | Approved for private portfolio | ThinkBud, employer and investor navigation |
| `REVIEWER-GUIDE.md` | Portfolio synthesis | Approved for private portfolio | Role-specific review paths |
| `ROADMAP.md` | Portfolio governance | Approved for private portfolio | Current state and next evidence wave |

## Required provenance entry for each new artefact

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
Identifiers removed:
Ownership and publication basis confirmed:
Confidentiality review status:
Reviewer:
Review date:
Notes and limitations:
```

## Private source-reference rule

Portfolio artefacts may record a high-level source family. They must not embed private Drive links, private repository paths, internal system URLs, user names, credential locations or production identifiers.

Detailed private source trails, where needed, remain outside the reviewer-facing repository surface.

## Current declaration

All current case studies, frameworks, skills and tools were written specifically for this private portfolio.

No historic employer document or ThinkBud implementation file has been uploaded. Source material has been used only to validate chronology, identify transferable patterns, verify the ThinkBud product state, classify claims and establish the evidence boundary.