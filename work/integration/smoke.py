"""Public smoke check; execute from this checkpoint directory."""
import tempfile
import unittest
from pathlib import Path
from booking import BookingService
from client import BookingClient
from transport import FakeTransport


class Smoke(unittest.TestCase):
    def test_one_booking(self):
        with tempfile.TemporaryDirectory() as tmp:
            service = BookingService(Path(tmp) / "data.sqlite")
            service.create_session("agents", "Agents", 1)
            result = BookingClient(FakeTransport(service)).book("agents", "Ada", "ada")
            self.assertEqual(result["status"], "reserved")
            self.assertEqual(service.list_sessions()[0]["reserved"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
