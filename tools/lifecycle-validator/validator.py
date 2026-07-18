#!/usr/bin/env python3
"""Synthetic lifecycle transition validator.

The rules are deliberately simple and explicit so a reviewer can inspect,
challenge and change them. This is decision support, not autonomous governance.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


ALLOWED_TRANSITIONS = {
    "Anonymous": {"Known"},
    "Known": {"Engaged", "Recycled"},
    "Engaged": {"Qualified", "Recycled"},
    "Qualified": {"Accepted", "Recycled"},
    "Accepted": {"Pipeline", "Recycled"},
    "Pipeline": {"Customer", "Recycled"},
    "Customer": set(),
    "Recycled": {"Engaged", "Qualified"},
}
REQUIRED_FIELDS = ("record_id", "from_stage", "to_stage", "owner", "transition_date", "reason")


@dataclass(frozen=True)
class Finding:
    record_id: str
    rule: str
    severity: str
    message: str


def validate_rows(rows: Iterable[dict[str, str]]) -> list[Finding]:
    findings: list[Finding] = []

    for row in rows:
        record_id = (row.get("record_id") or "").strip() or "<missing>"
        from_stage = (row.get("from_stage") or "").strip()
        to_stage = (row.get("to_stage") or "").strip()
        owner = (row.get("owner") or "").strip()
        reason = (row.get("reason") or "").strip()

        for field in REQUIRED_FIELDS:
            if not (row.get(field) or "").strip():
                findings.append(Finding(record_id, "missing_required", "high", f"Missing required field: {field}"))

        if from_stage not in ALLOWED_TRANSITIONS:
            findings.append(Finding(record_id, "unknown_stage", "high", f"Unknown from_stage: {from_stage}"))
            continue
        if to_stage not in ALLOWED_TRANSITIONS:
            findings.append(Finding(record_id, "unknown_stage", "high", f"Unknown to_stage: {to_stage}"))
            continue

        if to_stage not in ALLOWED_TRANSITIONS[from_stage]:
            findings.append(
                Finding(
                    record_id,
                    "invalid_transition",
                    "high",
                    f"Transition {from_stage} -> {to_stage} is not permitted",
                )
            )

        if not owner:
            findings.append(Finding(record_id, "missing_owner", "high", "Every lifecycle transition requires an owner"))

        if to_stage == "Recycled" and not reason:
            findings.append(Finding(record_id, "missing_recycle_reason", "medium", "Recycled records require a reason"))

    return findings


def validate_file(path: Path) -> dict[str, object]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing_headers = [field for field in REQUIRED_FIELDS if field not in (reader.fieldnames or [])]
        if missing_headers:
            raise ValueError(f"Missing CSV columns: {', '.join(missing_headers)}")
        rows = list(reader)

    findings = validate_rows(rows)
    by_rule = Counter(item.rule for item in findings)
    by_severity = Counter(item.severity for item in findings)

    return {
        "input_file": path.name,
        "records_scanned": len(rows),
        "findings_count": len(findings),
        "findings_by_rule": dict(sorted(by_rule.items())),
        "findings_by_severity": dict(sorted(by_severity.items())),
        "findings": [asdict(item) for item in findings],
        "human_approval_required": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate synthetic lifecycle transitions.")
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()

    try:
        result = validate_file(args.csv_file)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
