# Rebuilding a Fragmented Revenue Operating System

> **Evidence classification:** Composite implemented experience — independently reconstructed from repeated patterns across multiple roles.

## What this case is really about

The easiest way to explain this case is that the organisation did not have one revenue operating problem. It had several teams, motions and systems that each made sense on their own, but no shared model underneath them.

Marketing, Sales, outbound, partner and customer teams were using different definitions, ownership rules and reporting assumptions. The visible temptation was to fix the CRM. The real work was to create an operating spine that the systems could express.

This is a pattern I have seen more than once, which is why I have rebuilt it here as a company-neutral composite rather than presenting one employer story.

## What I was seeing

The organisation had accumulated:

- Multiple demand and sales motions
- Local lifecycle definitions
- Inconsistent handoffs
- Overlapping platform logic
- Manual exception handling
- Executive reporting that could not be reconciled

Each team could explain its own process. The organisation could not explain how the processes connected.

## My role

My role was to diagnose the operating failure, define the cross-functional design, translate it into system and data requirements, sequence implementation and establish governance.

The work required partnership across Marketing, Sales, SDR, Customer Success, Finance, Data and Technology.

## The diagnosis

The visible symptoms included:

- Pipeline figures changed between reports
- Lead quality disputes were resolved through anecdotes
- Routing exceptions had become normal operations
- Teams worked from local spreadsheets
- Tool decisions were being made before ownership decisions
- Reporting attempted to compensate for inconsistent definitions

The underlying causes were:

1. No agreed commercial-motion map
2. No shared lifecycle authority
3. Unclear ownership at transitions
4. Systems encoding different versions of the process
5. Data quality work disconnected from decision value
6. No governance mechanism for exceptions and change

## The principles I used

- One commercial language, with motion-specific rules where genuinely required
- Ownership before automation
- One authoritative state per decision
- Explicit acceptance at material handoffs
- Exceptions designed and measured
- Minimum critical data rather than universal completeness
- Reporting built from governed definitions
- Adoption treated as part of the system

## The operating model

```mermaid
flowchart TB
    A[Commercial motions]
    B[Lifecycle and ownership]
    C[Handoffs, SLAs and exceptions]
    D[Systems and integration]
    E[Data authority and quality]
    F[Reporting and decision cadence]
    G[Automation and AI readiness]

    A --> B --> C --> D --> E --> F --> G
```

## The decisions I made

### Process

- Defined the commercial motions and their legitimate differences
- Created shared lifecycle meanings
- Established entry, exit and stop conditions
- Designed acceptance, rejection and recycling
- Separated standard flow from approved exceptions

### Systems

- Identified the authoritative platform for each state
- Removed duplicate logic where different systems attempted to own the same decision
- Sequenced configuration behind approved operating definitions
- Introduced release and change controls

### Data

- Identified fields that drove ownership, money, customer treatment or executive reporting
- Prioritised those fields over broad hygiene activity
- Defined lineage and reconciliation requirements
- Established named ownership for critical definitions

### Governance

- Created a cross-functional decision forum
- Recorded rules, owners, exceptions and review dates
- Added adoption, SLA and data-quality measures
- Established escalation for unresolved definitions

## How I would sequence the work

1. Current-state mapping
2. Decision and ownership workshops
3. Target operating model
4. Minimum critical-data definition
5. System design and dependency plan
6. Controlled implementation
7. Scenario testing
8. Enablement through real workflows
9. Reporting reconciliation
10. Governance and continuous review

## What changed

The reconstructed pattern produced:

- A single operating language across functions
- Clearer ownership and acceptance
- Reduced dependence on manual interpretation
- More defensible pipeline reporting
- A practical basis for automation and AI
- A model that could evolve through governance rather than hidden configuration

I have intentionally left out exact employer metrics. The purpose of the case is to show the operating decisions and implementation logic, not to create a stronger story through numbers I cannot safely evidence here.

## What I learned

- CRM transformation without operating-model agreement creates faster inconsistency
- A shared definition that nobody accepts operationally is not shared
- Exception volume is one of the best indicators of design weakness
- Adoption improves when teams can see how the model changes their daily decisions
- AI becomes useful only after the evidence and accountability layers are explicit

## Related assets

- [Revenue Operating System framework](../../frameworks/revenue-operating-system.md)
- [Lifecycle Governance framework](../../frameworks/lifecycle-governance.md)
- [Pipeline Truth framework](../../frameworks/pipeline-truth.md)