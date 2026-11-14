# Review — Would you accept this change?

Review `CHANGE.diff`, `base/booking.py`, and proposed `booking.py` against `docs/contract.md`. Keep the proposed code unchanged while reviewing it so your evidence stays tied to the exact proposal (correct proposals exist; there is no finding quota). Run `python3 smoke.py` (Windows: `py -3 smoke.py`); `REVIEW.md` is optional.

> **Before opening `NEXT.md`:** Record your initial decision or `inconclusive / no evidence` in `index.html` or `RESULT.md` first, then assess `NEXT.md` separately as an independent claim (and remember an unsupported complaint can be false even if another bug exists). If your agent already opened `NEXT.md`, record that exposure instead of inventing a prior prediction.

## Optional workflow idea

Review correctness in the published scope and justify your decision. Use the available repo tools as you normally would.

## Examine your workflow and decide what next

- **Habit & expectation:** Record *“Usually I ___ → I expect ___”* in `index.html` or `RESULT.md` (or let your agent decide / pick one move for this attempt). Pick a contract condition, state your check and prediction, and separate confirmed violations from suspicions.
- **Inspect evidence:** What was actually executed against `docs/contract.md`, and what remains unchecked? Try [prompt card 2](PROMPT-CARDS.md) or optional `support/READ-ME-FIRST.md` (`python3 support/probe.py .`) where present.
- **Try a workflow move:** If uncertainty remains, try one targeted check or workflow move ([prompt card 4](PROMPT-CARDS.md)) and notice what it added, repeated, or cost (`unknown` is fine).
- **Keep, change, stop, or explore:** When another check is not worth its effort, record your case decision (`accept / reject / investigate / stop / inconclusive`) and one workflow rule you will **keep, change, stop, or explore** next. A second run is optional; use [extension 5](EXTENSIONS.md) for fair side-by-side comparisons.
