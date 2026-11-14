# Optional case support

Some cases include `support/READ-ME-FIRST.md`, `support/SCENARIO.md`, `support/probe.py`, and `support/observation.json`. Open `support/SCENARIO.md` and run `python3 support/probe.py .` (Windows: `py -3 support/probe.py .`) from your case folder to inspect one concrete scenario against your current code.

- A live `support/probe.py .` run tests whatever code is currently in this case folder; `support/observation.json` captures an earlier run of the unmodified case (and supplies no elapsed time or cost).
- If `NEXT.md` is present and you want to preserve an uninfluenced first verdict, save your initial decision in `RESULT.md` or `index.html` before opening `NEXT.md`.

Cases without `support/` can still be checked from `docs/trace.txt` and `docs/contract.md`. See `HELP.md` for recovery and preserving copies.
