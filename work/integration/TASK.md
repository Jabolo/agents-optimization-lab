# Integration — Which check is worth doing next?

A response can be lost after the server commits. Repair `client.py` and `transport.py` to satisfy `docs/contract.md` while preserving ordinary bookings, retry limits, conflicts, and independent requests. Use the deterministic local transport (no real network or sleeps) and fresh disposable SQLite databases only (no migrations). Add a regression without weakening assertions, and run `python3 smoke.py` (Windows: `py -3 smoke.py`).

> **Before opening `NEXT.md`:** Record your initial decision or `inconclusive / no evidence` in `index.html` or `RESULT.md` first, then inspect `NEXT.md` separately as a new question to verify. If your agent already opened `NEXT.md`, record that exposure instead of inventing a prior prediction.

## Optional workflow idea

Repair the integration and add regression tests using your normal workflow. You may choose test-first.

## Examine your workflow and decide what next

- **Habit & expectation:** Record *“Usually I ___ → I expect ___”* in `index.html` or `RESULT.md` (or let your agent decide / pick one move for this attempt). Name a contract condition, choose a check, and predict what it should show—`smoke.py` covers only its examples.
- **Inspect evidence:** What was actually executed against `docs/contract.md`, and what remains uncertain? Try [prompt card 2](PROMPT-CARDS.md) or optional `support/READ-ME-FIRST.md` (`python3 support/probe.py .`) to probe the reported failure.
- **Try a workflow move:** If a gap remains, try one targeted observation or move ([prompt card 4](PROMPT-CARDS.md)) and notice what it added, repeated, or cost (`unknown` is fine).
- **Keep, change, stop, or explore:** When another step is not worth its effort, record your case decision (`accept / reject / investigate / stop / inconclusive`) and one workflow rule you will **keep, change, stop, or explore** next. A second run is optional; use [extension 5](EXTENSIONS.md) for fair side-by-side comparisons.
