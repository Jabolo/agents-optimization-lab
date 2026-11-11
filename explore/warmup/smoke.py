"""Portable public-test entry point; no shell environment syntax required."""
import os
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
env = dict(os.environ, BOOKING_MODULE=str(root / 'booking.py'), CANDIDATE_DIR=str(root),
           PYTHONDONTWRITEBYTECODE='1')
raise SystemExit(subprocess.run([sys.executable, '-B', '-m', 'unittest', 'discover',
                                '-s', str(root / 'tests'), '-v'], cwd=root, env=env).returncode)
