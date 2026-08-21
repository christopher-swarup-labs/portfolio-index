#!/usr/bin/env python3
"""Synthetic GTM signal normalizer for the public portfolio.

This demonstrates how events from different GTM systems can be converted into a
small, explicit signal contract before downstream routing or AI analysis. It
uses only local synthetic JSON and Python's standard library; it makes no
network calls and does not connect to production systems.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


EVENT_MAP = {
    "crm": {
        "opportunity_stage_changed": "pipeline_stage_change",
        "owner_changed": "ownership_change",
    },
    "marketing_automation": {
        "form_submitted": "intent_form_submission",
        "event_attended": "event_attendance",
        "email_clicked": "email_engagement",
    },
    "product": {
        "trial_started": "product_trial_started",
        "usage_threshold_reached": "product_usage_threshold",
    },
}

REQUIRED_FIELDS = (
    "event_id",
    "source_system",
    "event_type",
    "entity_id",
    "occurred_at",
)


def normalise_timestamp(value: str) -> str | None:
    """Return a UTC ISO timestamp or None when the input is invalid/naive."""
    raw = (value or "").strip()
    if not raw:
        return None
    if raw.endswith("Z"):
        raw = raw[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(raw)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def signal_id(source_system: str, event_id: str) -> str:
    """Create a deterministic portfolio-safe signal identifier."""
    digest = hashlib.sha256(f"{source_system}:{event_id}".encode("utf-8")).hexdigest()[:12]
    return f"sig_{digest}"


def rejection(event_id: str, reason: str) -> dict[str, str]:
    return {"event_id": event_id or "<missing>", "reason": reason}


def normalise_events(events: Iterable[dict[str, object]]) -> dict[str, object]:
    accepted: list[dict[str, object]] = []
    rejected: list[dict[str, str]] = []
    duplicates: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    for event in events:
        event_id = str(event.get("event_id") or "").strip()
        missing = [field for field in REQUIRED_FIELDS if not str(event.get(field) or "").strip()]
        if missing:
            rejected.append(rejection(event_id, f"Missing required field(s): {', '.join(missing)}"))
            continue

        source_system = str(event["source_system"]).strip()
        event_type = str(event["event_type"]).strip()
        entity_id = str(event["entity_id"]).strip()
        occurred_at = normalise_timestamp(str(event["occurred_at"]))

        if source_system not in EVENT_MAP:
            rejected.append(rejection(event_id, f"Unsupported source_system: {source_system}"))
            continue

        if event_type not in EVENT_MAP[source_system]:
            rejected.append(
                rejection(event_id, f"Unsupported event_type '{event_type}' for source_system '{source_system}'")
            )
            continue

        if occurred_at is None:
            rejected.append(rejection(event_id, "occurred_at must be an ISO-8601 timestamp with timezone"))
            continue

        dedupe_key = (source_system, event_id)
        if dedupe_key in seen:
            duplicates.append({"event_id": event_id, "source_system": source_system})
            continue
        seen.add(dedupe_key)

        payload = event.get("payload") or {}
        if not isinstance(payload, dict):
            rejected.append(rejection(event_id, "payload must be a JSON object when supplied"))
            continue

        accepted.append(
            {
                "signal_id": signal_id(source_system, event_id),
                "entity_id": entity_id,
                "signal_type": EVENT_MAP[source_system][event_type],
                "occurred_at": occurred_at,
                "source_system": source_system,
                "source_event_id": event_id,
                "payload": payload,
            }
        )

    return {
        "events_received": len(accepted) + len(rejected) + len(duplicates),
        "signals_accepted": len(accepted),
        "events_rejected": len(rejected),
        "duplicates_ignored": len(duplicates),
        "signals": accepted,
        "rejected_events": rejected,
        "duplicate_events": duplicates,
        "human_review_required_for_schema_or_mapping_changes": True,
        "note": "Synthetic portfolio demonstration only; no production system is connected or modified.",
    }


def load_events(path: Path) -> list[dict[str, object]]:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("Input must be a JSON object or list of objects")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalise synthetic GTM events into an explicit signal contract.")
    parser.add_argument("json_file", type=Path)
    args = parser.parse_args()

    try:
        events = load_events(args.json_file)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))

    print(json.dumps(normalise_events(events), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
