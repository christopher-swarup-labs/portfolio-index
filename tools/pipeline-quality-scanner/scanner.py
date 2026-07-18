#!/usr/bin/env python3
"""Synthetic pipeline quality scanner for the portfolio.

Uses only Python's standard library. It is intentionally transparent:
rules are explicit, outputs are inspectable, and no decision is automated.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from dataclasses import dataclass, asdict
from datetime import date, datetime
from pathlib import Path
from typing import Iterable


REQUIRED_FIELDS = (
    "opportunity_id",
    "stage",
    "amount",
    "created_date",
    "close_date",
    "owner",
    "source",
)
CLOSED_STAGES = {"Closed Won", "Closed Lost"}


@dataclass(frozen=True)
class Issue:
    opportunity_id: str
    rule: str
    severity: str
    message: str


def parse_iso(value: str) -> date | None:
    value = (value or "").strip()
    if not value:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def scan_rows(rows: Iterable[dict[str, str]], as_of: date) -> list[Issue]:
    rows = list(rows)
    issues: list[Issue] = []
    id_counts = Counter((row.get("opportunity_id") or "").strip() for row in rows)

    for row in rows:
        oid = (row.get("opportunity_id") or "").strip() or "<missing>"

        for field in REQUIRED_FIELDS:
            if not (row.get(field) or "").strip():
                issues.append(Issue(oid, "missing_required", "high", f"Missing required field: {field}"))

        if oid != "<missing>" and id_counts[oid] > 1:
            issues.append(Issue(oid, "duplicate_id", "high", "Opportunity ID appears more than once"))

        amount_raw = (row.get("amount") or "").strip()
        if amount_raw:
            try:
                amount = float(amount_raw)
                if amount <= 0:
                    issues.append(Issue(oid, "invalid_amount", "medium", "Amount must be greater than zero"))
            except ValueError:
                issues.append(Issue(oid, "invalid_amount", "high", "Amount is not numeric"))

        created = parse_iso(row.get("created_date", ""))
        close = parse_iso(row.get("close_date", ""))

        if row.get("created_date") and created is None:
            issues.append(Issue(oid, "invalid_date", "high", "created_date must use YYYY-MM-DD"))
        if row.get("close_date") and close is None:
            issues.append(Issue(oid, "invalid_date", "high", "close_date must use YYYY-MM-DD"))

        if created and close and close < created:
            issues.append(Issue(oid, "date_sequence", "high", "close_date occurs before created_date"))

        stage = (row.get("stage") or "").strip()
        if stage not in CLOSED_STAGES and close and close < as_of:
            issues.append(Issue(oid, "stale_open", "medium", "Open opportunity has a close date in the past"))

        if not (row.get("source") or "").strip():
            issues.append(Issue(oid, "missing_source", "medium", "Source is required for attribution analysis"))

    return issues


def scan_file(path: Path, as_of: date) -> dict[str, object]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing_headers = [field for field in REQUIRED_FIELDS if field not in (reader.fieldnames or [])]
        if missing_headers:
            raise ValueError(f"Missing CSV columns: {', '.join(missing_headers)}")
        rows = list(reader)

    issues = scan_rows(rows, as_of)
    by_rule = Counter(issue.rule for issue in issues)
    by_severity = Counter(issue.severity for issue in issues)

    return {
        "input_file": path.name,
        "as_of": as_of.isoformat(),
        "records_scanned": len(rows),
        "issues_found": len(issues),
        "issues_by_rule": dict(sorted(by_rule.items())),
        "issues_by_severity": dict(sorted(by_severity.items())),
        "issues": [asdict(issue) for issue in issues],
        "human_review_required": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan synthetic pipeline data for common quality issues.")
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--as-of", default=date.today().isoformat(), help="YYYY-MM-DD, defaults to today")
    args = parser.parse_args()

    as_of = parse_iso(args.as_of)
    if as_of is None:
        parser.error("--as-of must use YYYY-MM-DD")

    try:
        result = scan_file(args.csv_file, as_of)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
