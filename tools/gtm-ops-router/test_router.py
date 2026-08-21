import unittest

from router import choose_route, route_request


class RouterTests(unittest.TestCase):
    def test_pipeline_request_routes_to_pipeline_truth(self):
        result = route_request(
            {
                "request_id": "P1",
                "request": "Pipeline forecast and attribution do not reconcile.",
                "owner": "Revenue Operations",
                "evidence": ["pipeline_definition", "opportunity_data", "forecast_definition"],
            }
        )
        self.assertEqual(result.route, "pipeline_truth")
        self.assertEqual(result.status, "ready_for_specialist_review")
        self.assertEqual(result.missing_evidence, ())
        self.assertTrue(result.human_review_required)

    def test_routing_request_surfaces_missing_evidence(self):
        result = route_request(
            {
                "request_id": "R1",
                "request": "Leads are ignored after handoff and SLA response time is poor.",
                "owner": "GTM Operations",
                "evidence": ["routing_rules"],
            }
        )
        self.assertEqual(result.route, "routing_and_sla")
        self.assertEqual(result.status, "evidence_required")
        self.assertIn("ownership_rules", result.missing_evidence)
        self.assertIn("sla_definition", result.missing_evidence)

    def test_ai_request_requires_action_boundary(self):
        result = route_request(
            {
                "request_id": "A1",
                "request": "Design an AI SDR automation workflow.",
                "owner": "Revenue Operations",
                "evidence": ["decision_to_improve", "authoritative_sources", "accountable_owner"],
            }
        )
        self.assertEqual(result.route, "ai_workflow_design")
        self.assertIn("action_boundary", result.missing_evidence)
        self.assertEqual(result.status, "evidence_required")

    def test_unknown_request_routes_to_decision_validation(self):
        route, matched, tied = choose_route("Something feels wrong with the operating model.")
        self.assertEqual(route, "decision_validation")
        self.assertEqual(matched, ())
        self.assertEqual(tied, ())

    def test_missing_owner_blocks_progress(self):
        result = route_request(
            {
                "request_id": "O1",
                "request": "Pipeline forecast is wrong.",
                "evidence": ["pipeline_definition", "opportunity_data", "forecast_definition"],
            }
        )
        self.assertEqual(result.status, "owner_required")

    def test_tied_routes_force_clarification(self):
        result = route_request(
            {
                "request_id": "T1",
                "request": "Pipeline stage is wrong.",
                "owner": "Revenue Operations",
                "evidence": ["decision_to_improve", "authoritative_sources", "accountable_owner"],
            }
        )
        self.assertEqual(result.route, "decision_validation")
        self.assertEqual(result.status, "decision_clarification_required")
        self.assertGreaterEqual(len(result.tied_routes), 2)


if __name__ == "__main__":
    unittest.main()
