"""Run from case folder: python3 support/probe.py . (or python3 probe.py /path/to/checkpoint; Python 3.11+)."""
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
    original = service.reserve('lab', 'Lin', 'b')
    service.cancel(first['reservation_id'])
    retry = service.reserve('lab', 'Lin', 'b')
    print(json.dumps({'original': original, 'retry': retry, 'catalog': service.list_sessions()}, sort_keys=True, indent=2))
