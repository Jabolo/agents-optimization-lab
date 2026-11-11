"""Run: python3 probe.py /path/to/checkpoint (Python 3.11+)."""
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
candidate = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(candidate))
import tempfile
from booking import BookingService

with tempfile.TemporaryDirectory() as tmp:
    service = BookingService(Path(tmp) / 'case.sqlite')
    service.create_session('lab', 'Lab', 1)
    first = service.reserve('lab', 'Ada', 'a')
    cancelled_waiter = service.reserve('lab', 'Lin', 'b')
    active_waiter = service.reserve('lab', 'Mira', 'c')
    service.cancel(cancelled_waiter['reservation_id'])
    promotion = service.cancel(first['reservation_id'])
    print(json.dumps({'cancelled_waiter_id': cancelled_waiter['reservation_id'],
                      'active_waiter_id': active_waiter['reservation_id'],
                      'promotion': promotion, 'catalog': service.list_sessions()}, sort_keys=True, indent=2))
