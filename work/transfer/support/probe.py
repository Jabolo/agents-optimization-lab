"""Run from case folder: python3 support/probe.py . (or python3 probe.py /path/to/checkpoint; Python 3.11+)."""
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
candidate = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(candidate))
from agenda import order_sessions

with (candidate / 'sessions.json').open(encoding='utf-8') as stream:
    sessions = json.load(stream)
print(json.dumps({'ordered_ids': [s['id'] for s in order_sessions(sessions)]}, indent=2))
