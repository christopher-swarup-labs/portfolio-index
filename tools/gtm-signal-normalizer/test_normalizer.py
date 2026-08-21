import unittest

from normalizer import normalise_events, signal_id


class SignalNormalizerTests(unittest.TestCase):
    def test_valid_event_is_normalised(self):
        result = normalise_events(
            [
                {
                    "event_id": "evt-1",
                    "source_system": "marketing_automation",
                    "event_type": "form_submitted",
                    "entity_id": "person-1",
                    "occurred_at": "2026-08-20T09:00:00Z",
                    "payload": {"form_type": "demo"},
                }
            ]
        )
        self.assertEqual(result["signals_accepted"], 1)
        self.assertEqual(result["events_rejected"], 0)
        self.assertEqual(result["signals"][0]["signal_type"], "intent_form_submission")
        self.assertEqual(result["signals"][0]["occurred_at"], "2026-08-20T09:00:00Z")

    def test_duplicate_source_event_is_ignored(self):
        event = {
            "event_id": "evt-2",
            "source_system": "crm",
            "event_type": "owner_changed",
            "entity_id": "opportunity-1",
            "occurred_at": "2026-08-20T10:00:00Z",
            "payload": {},
        }
        result = normalise_events([event, event])
        self.assertEqual(result["signals_accepted"], 1)
        self.assertEqual(result["duplicates_ignored"], 1)

    def test_unsupported_event_type_is_rejected(self):
        result = normalise_events(
            [
                {
                    "event_id": "evt-3",
                    "source_system": "product",
                    "event_type": "mystery_event",
                    "entity_id": "account-1",
                    "occurred_at": "2026-08-20T10:00:00Z",
                    "payload": {},
                }
            ]
        )
        self.assertEqual(result["signals_accepted"], 0)
        self.assertEqual(result["events_rejected"], 1)
        self.assertIn("Unsupported event_type", result["rejected_events"][0]["reason"])

    def test_naive_timestamp_is_rejected(self):
        result = normalise_events(
            [
                {
                    "event_id": "evt-4",
                    "source_system": "crm",
                    "event_type": "owner_changed",
                    "entity_id": "opportunity-2",
                    "occurred_at": "2026-08-20T10:00:00",
                    "payload": {},
                }
            ]
        )
        self.assertEqual(result["events_rejected"], 1)
        self.assertIn("timezone", result["rejected_events"][0]["reason"])

    def test_signal_id_is_deterministic(self):
        self.assertEqual(signal_id("crm", "evt-5"), signal_id("crm", "evt-5"))
        self.assertNotEqual(signal_id("crm", "evt-5"), signal_id("product", "evt-5"))

    def test_payload_must_be_object(self):
        result = normalise_events(
            [
                {
                    "event_id": "evt-6",
                    "source_system": "product",
                    "event_type": "trial_started",
                    "entity_id": "account-3",
                    "occurred_at": "2026-08-20T10:00:00Z",
                    "payload": "not-an-object",
                }
            ]
        )
        self.assertEqual(result["events_rejected"], 1)
        self.assertIn("payload must be a JSON object", result["rejected_events"][0]["reason"])

    def test_rejected_event_does_not_reserve_dedupe_key(self):
        invalid = {
            "event_id": "evt-7",
            "source_system": "crm",
            "event_type": "owner_changed",
            "entity_id": "opportunity-4",
            "occurred_at": "2026-08-20T10:00:00Z",
            "payload": "invalid",
        }
        corrected = {
            "event_id": "evt-7",
            "source_system": "crm",
            "event_type": "owner_changed",
            "entity_id": "opportunity-4",
            "occurred_at": "2026-08-20T10:00:00Z",
            "payload": {"new_owner": "synthetic-owner"},
        }
        result = normalise_events([invalid, corrected])
        self.assertEqual(result["events_rejected"], 1)
        self.assertEqual(result["signals_accepted"], 1)
        self.assertEqual(result["duplicates_ignored"], 0)


if __name__ == "__main__":
    unittest.main()
