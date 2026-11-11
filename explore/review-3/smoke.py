import tempfile
import unittest
from pathlib import Path
from booking import BookingService


class Smoke(unittest.TestCase):
    def test_initial_booking(self):
        with tempfile.TemporaryDirectory() as tmp:
            service = BookingService(Path(tmp) / "data.sqlite")
            service.create_session("agents", "Agents", 1)
            original = service.reserve("agents", "Ada", "a")
            self.assertEqual(original["status"], "reserved")
            self.assertEqual(service.reserve("agents", "Ada", "a"), original)


if __name__ == "__main__":
    unittest.main(verbosity=2)
