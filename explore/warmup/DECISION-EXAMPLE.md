# Optional worked decisions

The first example below is an illustrative, hypothetical developer lab note modeled on the booking/retry domain. Its check and result are invented to show how a decision can be recorded; they are not evidence about your code. The two maintainer examples after it are from outside the lab cases. Supply your own habit and personal rule from your own work.

## Example lab note: checking a boundary after a green smoke test

- **My usual workflow and expectation:** Usually I let my agent patch the code and accept the fix once the starter check passes → I expect a passing smoke check to cover the key contract rules.
- **The condition, check and predicted result:** Pick one boundary outside the starter script: if an idempotency key is reused for a different attendee, the booking call should raise `ValueError` without adding a second reservation row.
- **What I tried or retained, and what I actually observed:** Kept my normal prompt; `python3 smoke.py` passed (`Ran 1 test ... OK`), exercising only one clean booking. A 10-line check on the conflicting-key boundary showed `ValueError` was raised and `COUNT(*) == 1` in SQLite, while retry limits and transport errors remained untested.
- **Decision and uncertainty:** accept for this boundary / investigate remaining rules — key conflicts are verified on this version; retry-limit and error-propagation rules remain unverified.
- **My personal rule:** I will stop trusting a green starter smoke check alone when a task has multi-rule error contracts, because I observed that `smoke.py` only covered one happy-path booking.

## Workflow choice: evidence before recovery

While maintaining AI Mileage, an agent proposed recovering 20 databases from backups after a legacy usage file failed to match current event IDs.

**Choice and question:** Before restoring anything, ask what previously accepted records are actually missing. A read-only check of retained state and lineage could help answer that question without restoring a backup.

**Observation and decision:** The failed match did not invalidate previously accepted counters. A read-only preservation check of already-ingested historical events reported no missing event states or changed accepted counter versions within its scope. No specific missing set of accepted events had been demonstrated, and the team did not download or restore any of the 20 backup databases. They also added an explicit evidence gate for future recovery decisions.

**Limits:** A stored-lineage check does not re-prove source authenticity or establish complete account history. Human time and cost were not measured. Decide for your own task whether a check like this is worthwhile; do not treat recovery or an extra audit as a universal next step.

**Personal rule:** I will ask for a read-only check of what accepted data is actually missing before running a backup restore when an agent flags unmatched historical rows, because the lineage check found no missing accepted records within its scope and no restore was performed. The unmatched rows remained unresolved.

## Checking a report copy on Windows

**Condition and expectation:** A command that copies a report to a fresh destination should preserve the source bytes. A byte-for-byte comparison should find the same content and line endings at both paths.

**Chosen check and observation:** The hosted Windows/Python 3.13 tests compared the destination and source reports. Two tests failed: the source contained LF line endings, while the destination contained CRLF. The command had decoded and rewritten the report in text mode. Linux/Python 3.11 passed in the same run; that pass did not establish Windows behavior.

**Decision: change and investigate.** Replace the text-mode copy with an exclusive binary copy, then check preservation, including a regression with a UTF-8 BOM, CRLF and Polish characters. The focused tests passed locally. In the next hosted run, the original two Windows failures and the new regression passed, but the whole-suite wrapper timed out later. Those results supported the specific copy fix, but did not establish a successful complete Windows release.

The wrapper's full-suite budget was increased, without removing acceptance checks. A subsequent hosted run passed all 35 Windows tests and completed release generation and verification; Linux passed too. A reasonable **scoped acceptance** is that the tested source passed that CLI/package process on those hosted configurations. It does not establish Windows browser behavior, participant-agent interaction, or behavior on every platform.

**Tentative transferable practice:** When a portability claim matters, compare the actual artifact at the boundary on the target environment, and distinguish a focused regression pass from a complete process pass. Decide whether that extra check is worth its time for your own task.

**Personal rule:** I will run a byte-for-byte check on the target platform when cross-OS file output matters, because I observed a Linux pass miss CRLF rewriting on Windows.

Time to acceptance and human effort were not measured here; no model usage or monetary cost was recorded. The tests establish software behavior, not participant learning.
