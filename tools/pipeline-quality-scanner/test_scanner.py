import csv
import tempfile
import unittest
from datetime import date
from pathlib import Path

from scanner import scan_file


class PipelineScannerTests(unittest.TestCase):
    def write_csv(self, rows):
        handle = tempfile.NamedTemporaryFile("w", newline="", suffix=".csv", delete=False)
        with handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["opportunity_id", "stage", "amount", "created_date", "close_date", "owner", "source"],
            )
            writer.writeheader()
            writer.writerows(rows)
        return Path(handle.name)

    def test_detects_duplicate_and_stale_open(self):
        path = self.write_csv([
            {
                "opportunity_id": "OPP-001",
                "stage": "Discovery",
                "amount": "50000",
                "created_date": "2026-01-01",
                "close_date": "2026-02-01",
                "owner": "Jordan Lee",
                "source": "Web",
            },
            {
                "opportunity_id": "OPP-001",
                "stage": "Discovery",
                "amount": "50000",
                "created_date": "2026-01-01",
                "close_date": "2026-02-01",
                "owner": "Jordan Lee",
                "source": "Web",
            },
        ])
        result = scan_file(path, date(2026, 3, 1))
        self.assertGreaterEqual(result["issues_by_rule"]["duplicate_id"], 2)
        self.assertEqual(result["issues_by_rule"]["stale_open"], 2)

    def test_clean_record_passes(self):
        path = self.write_csv([{
            "opportunity_id": "OPP-002",
            "stage": "Closed Won",
            "amount": "75000",
            "created_date": "2026-01-01",
            "close_date": "2026-02-15",
            "owner": "Sam Patel",
            "source": "Partner",
        }])
        result = scan_file(path, date(2026, 3, 1))
        self.assertEqual(result["issues_found"], 0)


if __name__ == "__main__":
    unittest.main()
