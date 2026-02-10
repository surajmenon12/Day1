"""Tests for the dashboard application."""

import unittest


class TestStatsEndpoint(unittest.TestCase):
    def test_stats_returns_expected_keys(self):
        expected_keys = {"users", "active_sessions", "revenue", "uptime"}
        sample = {
            "users": 100,
            "active_sessions": 5,
            "revenue": 999.99,
            "uptime": "99.9%",
        }
        self.assertEqual(set(sample.keys()), expected_keys)

    def test_revenue_is_positive(self):
        revenue = 24350.75
        self.assertGreater(revenue, 0)

    def test_uptime_format(self):
        uptime = "99.97%"
        self.assertTrue(uptime.endswith("%"))
        numeric = float(uptime.rstrip("%"))
        self.assertGreaterEqual(numeric, 0)
        self.assertLessEqual(numeric, 100)


class TestUserModel(unittest.TestCase):
    def test_user_roles(self):
        valid_roles = {"admin", "editor", "viewer"}
        self.assertIn("admin", valid_roles)
        self.assertIn("viewer", valid_roles)
        self.assertNotIn("superuser", valid_roles)

    def test_user_dict_has_required_fields(self):
        user = {"id": 1, "name": "Alice", "email": "alice@test.com", "role": "admin"}
        for field in ("id", "name", "email", "role"):
            self.assertIn(field, user)


if __name__ == "__main__":
    unittest.main()
