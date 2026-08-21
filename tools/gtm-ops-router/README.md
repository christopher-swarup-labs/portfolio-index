# GTM Ops Decision Router

> **Evidence classification:** Synthetic portfolio demonstration. This is not employer production code.

A small deterministic router that demonstrates how I think about the coordination layer in AI-assisted GTM Operations.

The point is not to make a clever classifier. The point is to make the **routing logic, evidence requirements and human-control boundary inspectable**.

## What it does

Given a synthetic GTM operating request, the router:

1. Looks for explicit operating signals in the request
2. Routes to the narrowest specialist category when one is clear
3. Surfaces the signals that caused the route
4. Checks whether the evidence required for that route is present
5. Stops if an accountable owner is missing
6. Forces clarification when two routes tie
7. Requires human review before any material action

Current specialist routes:

- Pipeline truth
- Lifecycle governance
- Routing and SLA
- CRM data quality
- Campaign operations
- AI workflow design
- Decision validation / clarification fallback

## Why this matters

A generic assistant can answer “pipeline is weak” with recommendations that sound plausible.

An operating system should first determine whether the issue is pipeline data quality, lifecycle conversion, source/influence logic, ownership, SLA failure, forecast definition or something else. If the evidence is incomplete, it should say so before recommending automation.

That distinction is central to the wider [AI GTM Operations model](../../AI-GTM-OPS.md).

## Run it

Requires Python 3.11+ and uses only the standard library.

```bash
python router.py sample_requests.json
```

Run the tests:

```bash
python -m unittest
```

The repository's GitHub Actions workflow runs these tests alongside the other portfolio tools.

## Example output contract

Each result returns fields including:

```json
{
  "route": "routing_and_sla",
  "matched_signals": ["handoff", "sla", "ignored"],
  "required_evidence": ["routing_rules", "ownership_rules", "sla_definition"],
  "missing_evidence": [],
  "status": "ready_for_specialist_review",
  "human_review_required": true
}
```

The `route_score` is the number of explicit matched signals. It is deliberately **not called confidence**; a keyword count is not a probabilistic confidence estimate.

## Design choices

### Deterministic on purpose

This demonstration uses explicit rules rather than an LLM so a reviewer can see exactly why a route was selected. A production implementation could use probabilistic classification, but the output still needs an inspectable contract and escalation path.

### Evidence gates before automation

Each specialist route declares the minimum evidence it expects. Missing evidence changes the status to `evidence_required` rather than allowing the system to bluff its way through the request.

### Ambiguity is a valid outcome

If multiple routes tie, the router returns `decision_validation` and asks for clarification. Forcing certainty where the operating problem is ambiguous is a failure mode, not a feature.

### Human accountability is mandatory

No request is considered ready without an accountable owner, and every output includes `human_review_required: true`.

## What this proves — and what it does not

It demonstrates:

- Coordination-layer thinking
- Explicit routing rules
- Evidence contracts
- Human approval boundaries
- Testable GTM operating logic
- Version-controlled AI/GTM architecture

It does **not** claim:

- Production deployment
- Autonomous CRM changes
- Machine-learning accuracy
- Access to employer data
- A replacement for human Revenue Operations judgement

## Related proof

- [AI GTM Operations](../../AI-GTM-OPS.md)
- [GTM Command Center](../../skills/command-center/README.md)
- [Pipeline Quality Scanner](../pipeline-quality-scanner/README.md)
- [Lifecycle Transition Validator](../lifecycle-validator/README.md)
