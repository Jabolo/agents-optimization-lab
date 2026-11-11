"""Participant-visible smoke checks; run from the repository root."""
import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path

root = Path(__file__).resolve().parents[1]
default_candidate = root / "booking.py" if (root / "booking.py").is_file() else root / "starter" / "booking.py"
candidate = Path(os.environ.get("BOOKING_MODULE", default_candidate)).resolve()
sys.path.insert(0, str(candidate.parent))
spec = importlib.util.spec_from_file_location("candidate_booking", candidate)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
BookingService = module.BookingService


class PublicBookingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "conference.sqlite"
        self.service = BookingService(self.path)
        self.service.create_session("agents", "Agents lab", 1)

    def test_booking_retry_and_queue(self):
        first = self.service.reserve("agents", "Ada", "req-ada")
        self.assertEqual(first["status"], "reserved")
        self.assertEqual(self.service.reserve("agents", "Ada", "req-ada"), first)
        second = self.service.reserve("agents", "Lin", "req-lin")
        self.assertEqual(second["status"], "waitlisted")
        self.assertEqual(self.service.list_sessions()[0]["reserved"], 1)
        self.assertEqual(self.service.list_sessions()[0]["waitlisted"], 1)
        self.assertEqual(self.service.cancel(first["reservation_id"]), {
            "cancelled": True, "promoted_reservation_id": second["reservation_id"]
        })
        self.assertEqual(self.service.list_sessions()[0]["reserved"], 1)
        self.assertEqual(self.service.list_sessions()[0]["waitlisted"], 0)

    def test_key_conflict_and_waiter_cancellation(self):
        first = self.service.reserve("agents", "Ada", "one")
        waiter = self.service.reserve("agents", "Lin", "two")
        with self.assertRaises(ValueError):
            self.service.reserve("agents", "Someone else", "one")
        self.assertEqual(self.service.cancel(waiter["reservation_id"]), {
            "cancelled": True, "promoted_reservation_id": None
        })
        self.assertTrue(self.service.cancel(first["reservation_id"])["cancelled"])
        self.assertFalse(self.service.cancel(first["reservation_id"])["cancelled"])
        self.assertEqual(self.service.list_sessions()[0]["reserved"], 0)


if __name__ == "__main__":
    unittest.main()
