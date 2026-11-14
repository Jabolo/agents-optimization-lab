# Warmup — Which fact changes the solution?

Repair `booking.py` for the reservation retry issue in `docs/trace.txt` so it satisfies `docs/contract.md`, while preserving capacity, FIFO promotion, key conflicts, persistence, and ordinary bookings. Use disposable SQLite databases only (no migrations). Add a regression test and run `python3 smoke.py` (Windows: `py -3 smoke.py`); this case has no `NEXT.md`.

## Optional workflow idea

Implement the change and tests using your normal workflow. You may gather evidence before editing.

## Examine your workflow and decide what next

- **Habit & expectation:** Record *“Usually I ___ → I expect ___”* in `index.html` or `RESULT.md` (or let your agent decide / pick one move for this attempt). Pick a contract condition, predict what a check will show, and inspect real output.
- **Inspect evidence:** What did your checks cover against `docs/contract.md`, and what remains unchecked? Try [prompt card 2](PROMPT-CARDS.md) if useful.
- **Try a workflow move:** If a gap remains, try one targeted observation or move ([prompt card 4](PROMPT-CARDS.md)) and notice what it added, repeated, or cost (`unknown` is fine).
- **Keep, change, stop, or explore:** Record your case decision (`accept / reject / investigate / stop / inconclusive`) and one workflow rule you will **keep, change, stop, or explore** next. A second run is optional; see [EXTENSIONS.md](EXTENSIONS.md) for fair comparisons.
