"""Run from case folder: python3 support/probe.py . (or python3 probe.py /path/to/checkpoint; Python 3.11+)."""
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
candidate = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(candidate))
import sqlite3
import tempfile
from contextlib import closing
from booking import BookingService
from client import BookingClient
from transport import FakeTransport

with tempfile.TemporaryDirectory() as tmp:
    database = Path(tmp) / 'case.sqlite'
    service = BookingService(database)
    service.create_session('lab', 'Lab', 1)
    transport = FakeTransport(service, ['after', 'ok'])
    result = BookingClient(transport).book('lab', 'Ada', 'visit-a', 2)
    with closing(sqlite3.connect(database)) as db:
        rows = list(db.execute('SELECT id, attendee, status FROM reservations ORDER BY id'))
    print(json.dumps({'headers': [request['headers'] for request in transport.requests],
                      'result': result, 'rows': rows}, sort_keys=True, indent=2))
