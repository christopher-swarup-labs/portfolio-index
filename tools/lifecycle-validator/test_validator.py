import csv
import tempfile
import unittest
from pathlib import Path

from validator import validate_file


class LifecycleValidatorTests(unittest.TestCase):
    def write_csv(self, rows):
        handle = tempfile.NamedTemporaryFile("w", newline="", suffix=".csv", delete=False)
        with handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["record_id", "from_stage", "to_stage", "owner", "transition_date", "reason"],
            )
            writer.writeheader()
            writer.writerows(rows)
        return Path(handle.name)

    def test_invalid_skip_is_flagged(self):
        path = self.write_csv([{
            "record_id": "REC-001",
            "from_stage": "Known",
            "to_stage": "Pipeline",
            "owner": "Jordan Lee",
            "transition_date": "2026-02-10",
            "reason": "Synthetic test",
        }])
        result = validate_file(path)
        self.assertEqual(result["findings_by_rule"]["invalid_transition"], 1)

    def test_valid_transition_passes(self):
        path = self.write_csv([{
            "record_id": "REC-002",
            "from_stage": "Engaged",
            "to_stage": "Qualified",
            "owner": "Sam Patel",
            "transition_date": "2026-02-10",
            "reason": "Synthetic qualification",
        }])
        result = validate_file(path)
        self.assertEqual(result["findings_count"], 0)


if __name__ == "__main__":
    unittest.main()
