# Integration — Which check is worth doing next?

A response can be lost after the server commits. Repair `client.py` and `transport.py` according to `docs/contract.md`. Preserve ordinary bookings, retry limits, conflicts and independent requests. Use the deterministic local transport without a real network or sleeps. Fresh disposable databases only; no migration work. Add a regression for the reported behavior, do not weaken assertions to obtain a pass, and run public smoke.

Use your agent fully. Choose one workflow habit to watch—for example, your instructions, context, model, skill or delegation. Letting your agent decide is a valid choice too. In the browser notebook or this case's `RESULT.md` (one record is enough), record “Usually I ___ → I expect ___,” or choose a move for this attempt if you have no usual habit. Choose a business condition and a check that could establish it; predict what result would support acceptance. Inspect the actual output and record your current decision and uncertainty. A passing smoke, a regression and complete contract coverage are different claims.

## Optional workflow idea

Repair the integration and add regression tests using your normal workflow. You may choose test-first.

## Examine your workflow and decide what next

Choose a move for your current uncertainty:

- **Inspect evidence:** What was actually checked, and what could still change your decision? Try [prompt card 2](PROMPT-CARDS.md) if useful.
- **Try a workflow move:** If there is a gap, ask for one targeted observation or try another available approach. Predict what it could add, then inspect the actual result and extra effort. [Prompt card 4](PROMPT-CARDS.md) offers a way to choose the next move.
- **Keep or stop:** If the result is sufficient for your scope, explain why another step is not worth it. An inconclusive result and next move are valid too.

Look back at your chosen habit: what did it contribute, repeat or leave uncertain? Consider effort, time or cost where observable; unknown is fine. Repetition can still be useful, and you may not be able to tell what a single step contributed. Compare what happened with your expectation. A second attempt is optional; do not claim you compared approaches you did not run. To compare fairly later, use [extension 5](EXTENSIONS.md) with fresh starts and the same checks.

## Assess the report

Before opening `NEXT.md`, record your current decision or what remains undecided. If your check is unfinished or has no usable output, record the partial result or “inconclusive / no evidence” and your next move. Then assess the report as a question: choose whether another observation is worth its time, inspect any result, and retain or revise your decision separately. If your agent accessed the report early, record that exposure; do not invent a pre-report prediction or decision.

A reproducible observation of the chosen condition supports a decision for that scope; note what remains unchecked. Stop when another observation is not worth its cost, and resume with a different legal failure sequence. The optional `support/READ-ME-FIRST.md` describes a bounded scenario and prior observation after your own decision or inconclusive result.
