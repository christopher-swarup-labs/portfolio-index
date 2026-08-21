#!/usr/bin/env python3
"""Deterministic GTM Ops request router for the public portfolio.

The router demonstrates an inspectable coordination layer: it classifies an
operating request, exposes the signals used, checks evidence requirements and
forces human review. It uses synthetic inputs and Python's standard library.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


SPECIALISTS = {
    "pipeline_truth": {
        "signals": (
            "pipeline",
            "forecast",
            "attribution",
            "source",
            "influence",
            "opportunity",
        ),
        "required_evidence": (
            "pipeline_definition",
            "opportunity_data",
            "forecast_definition",
        ),
    },
    "lifecycle_governance": {
        "signals": (
            "lifecycle",
            "mql",
            "sal",
            "sql",
            "stage",
            "qualification",
            "recycle",
        ),
        "required_evidence": (
            "lifecycle_definition",
            "stage_history",
            "ownership_rules",
        ),
    },
    "routing_and_sla": {
        "signals": (
            "routing",
            "route",
            "handoff",
            "sla",
            "response time",
            "ignored",
            "acceptance",
            "owner",
        ),
        "required_evidence": (
            "routing_rules",
            "ownership_rules",
            "sla_definition",
        ),
    },
    "crm_data_quality": {
        "signals": (
            "duplicate",
            "missing field",
            "data quality",
            "crm data",
            "incomplete",
            "invalid",
            "field hygiene",
        ),
        "required_evidence": (
            "field_dictionary",
            "sample_records",
            "system_of_record",
        ),
    },
    "campaign_operations": {
        "signals": (
            "campaign",
            "event",
            "qa",
            "launch",
            "intake",
            "readiness",
            "follow-up",
        ),
        "required_evidence": (
            "campaign_brief",
            "readiness_criteria",
            "owner_and_deadline",
        ),
    },
    "ai_workflow_design": {
        "signals": (
            "agent",
            "ai workflow",
            "automation",
            "copilot",
            "ai sdr",
            "llm",
            "prompt",
        ),
        "required_evidence": (
            "decision_to_improve",
            "authoritative_sources",
            "action_boundary",
            "accountable_owner",
        ),
    },
}


@dataclass(frozen=True)
class RouteResult:
    request_id: str
    route: str
    matched_signals: tuple[str, ...]
    route_score: int
    tied_routes: tuple[str, ...]
    required_evidence: tuple[str, ...]
    evidence_provided: tuple[str, ...]
    missing_evidence: tuple[str, ...]
    accountable_owner: str
    status: str
    next_action: str
    human_review_required: bool = True


def normalise(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").lower()).strip()


def score_request(text: str) -> dict[str, tuple[str, ...]]:
    haystack = normalise(text)
    scores: dict[str, tuple[str, ...]] = {}
    for route, config in SPECIALISTS.items():
        matched = tuple(signal for signal in config["signals"] if signal in haystack)
        scores[route] = matched
    return scores


def choose_route(text: str) -> tuple[str, tuple[str, ...], tuple[str, ...]]:
    scores = score_request(text)
    best_score = max((len(signals) for signals in scores.values()), default=0)

    if best_score == 0:
        return "decision_validation", (), ()

    winners = tuple(sorted(route for route, signals in scores.items() if len(signals) == best_score))
    selected = winners[0] if len(winners) == 1 else "decision_validation"
    matched = scores[winners[0]] if len(winners) == 1 else ()
    tied = winners if len(winners) > 1 else ()
    return selected, matched, tied


def route_request(payload: dict[str, object]) -> RouteResult:
    request_id = str(payload.get("request_id") or "<missing>")
    text = str(payload.get("request") or "")
    owner = str(payload.get("owner") or "").strip()
    evidence = tuple(sorted({str(item) for item in (payload.get("evidence") or [])}))

    route, matched, tied = choose_route(text)

    if route == "decision_validation":
        required: tuple[str, ...] = ("decision_to_improve", "authoritative_sources", "accountable_owner")
    else:
        required = tuple(SPECIALISTS[route]["required_evidence"])

    missing = tuple(item for item in required if item not in evidence)

    if not owner:
        status = "owner_required"
        next_action = "Name an accountable human owner before routing the request."
    elif tied:
        status = "decision_clarification_required"
        next_action = "Clarify the operating decision before choosing a specialist route."
    elif missing:
        status = "evidence_required"
        next_action = "Collect the missing evidence before specialist analysis or automation."
    else:
        status = "ready_for_specialist_review"
        next_action = f"Route to {route} for analysis, then require human review before material action."

    return RouteResult(
        request_id=request_id,
        route=route,
        matched_signals=matched,
        route_score=len(matched),
        tied_routes=tied,
        required_evidence=required,
        evidence_provided=evidence,
        missing_evidence=missing,
        accountable_owner=owner,
        status=status,
        next_action=next_action,
    )


def process_requests(requests: Iterable[dict[str, object]]) -> dict[str, object]:
    results = [route_request(request) for request in requests]
    return {
        "requests_processed": len(results),
        "results": [asdict(result) for result in results],
        "human_review_required": True,
        "note": "Portfolio demonstration only. No production system is modified.",
    }


def load_requests(path: Path) -> list[dict[str, object]]:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("Input must be a JSON object or list of objects")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="Route synthetic GTM Ops requests using explicit rules.")
    parser.add_argument("json_file", type=Path)
    args = parser.parse_args()

    try:
        requests = load_requests(args.json_file)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))

    print(json.dumps(process_requests(requests), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
