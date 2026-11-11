"""A small public example; run with `python3 smoke.py`."""
import unittest

from agenda import order_sessions


class Smoke(unittest.TestCase):
    def test_order(self):
        sessions = [
            {"id": "b", "title": "B", "starts_at": "2026-10-24T10:00:00+02:00"},
            {"id": "a", "title": "A", "starts_at": "2026-10-24T09:00:00+02:00"},
        ]
        self.assertEqual([s["id"] for s in order_sessions(sessions)], ["a", "b"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
