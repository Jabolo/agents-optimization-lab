# Optional challenge — Combined reservation repairs

Repair the combined historical-response and client/transport retry issues using `docs/trace.txt` and `docs/contract.md`. Pick one real workflow move to test (evidence before edits, regression reproduction, claim review, escalation trigger, handoff, delegation, or script reuse) and run `python3 smoke.py` (Windows: `py -3 smoke.py`).

> **Before opening `NEXT.md`:** Record your initial decision or `inconclusive / no evidence` in `index.html` or `RESULT.md` first, then assess `NEXT.md` separately as a new question. If your agent already opened `NEXT.md`, record that exposure instead of inventing a prior prediction.

## Examine your workflow and decide what next

- **Habit & expectation:** Record *“Usually I ___ → I expect ___”* (or choose one move for this attempt), pick a contract condition, predict the result, and inspect real output. If delegating or escalating, count coordination or trigger overhead in observed time/cost (`unknown` / `N/A` if unavailable).
- **Inspect evidence:** What did your checks verify against `docs/contract.md`, and what remains uncertain? Try [prompt card 2](PROMPT-CARDS.md) if useful.
- **Try a workflow move:** If a gap remains, try one targeted observation or move ([prompt card 4](PROMPT-CARDS.md)) and notice what it added, repeated, or cost.
- **Keep, change, stop, or explore:** Record your case decision (`accept / reject / investigate / stop / inconclusive`) and one workflow rule you will **keep, change, stop, or explore** next. A second run is optional; see [EXTENSIONS.md](EXTENSIONS.md) for fair comparisons.
