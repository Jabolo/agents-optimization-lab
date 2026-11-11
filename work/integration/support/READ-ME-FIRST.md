# Optional case support

Some code folders include `support/READ-ME-FIRST.md`, `support/SCENARIO.md`, `support/probe.py` and `support/observation.json`. They offer one bounded scenario and an observation of an earlier run of the original case. Use them after recording your own current decision or “inconclusive / no evidence.” For any review case, first assess the `NEXT.md` report too. These are optional aids, not an answer key.

Follow the case's `support/READ-ME-FIRST.md`. Predict the scenario outcome, then run the probe if Python works or inspect the captured observation. Compare the actual result with the visible contract, record its scope and remaining uncertainty, and decide the next move. A live probe tests the version you point it at; identify that version and save its output. The saved observation is from an earlier run of the original case, not evidence that your own changes pass, and supplies no time or cost for your work. Import or setup errors are not product findings.

Cases without support can still use their visible trace and contract. Record partial or inconclusive work and resume later. `HELP.md` explains recovery and preserving copies.
