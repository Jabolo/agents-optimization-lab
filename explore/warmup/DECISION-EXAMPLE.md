# Optional worked decision: copying a report on Windows

This is a maintainer example from outside the lab cases. It shows one way to connect an observation to a bounded decision; it is not another exercise or a form you need to complete. Supply your own habit and personal rule from your own work.

**Condition and expectation:** A command that copies a report to a fresh destination should preserve the source bytes. A byte-for-byte comparison should find the same content and line endings at both paths.

**Chosen check and observation:** The hosted Windows/Python 3.13 tests compared the destination and source reports. Two tests failed: the source contained LF line endings, while the destination contained CRLF. The command had decoded and rewritten the report in text mode. Linux/Python 3.11 passed in the same run; that pass did not establish Windows behavior.

**Decision: change and investigate.** Replace the text-mode copy with an exclusive binary copy, then check preservation, including a regression with a UTF-8 BOM, CRLF and Polish characters. The focused tests passed locally. In the next hosted run, the original two Windows failures and the new regression passed, but the whole-suite wrapper timed out later. Those results supported the specific copy fix, but did not establish a successful complete Windows release.

The wrapper's full-suite budget was increased, without removing acceptance checks. A subsequent hosted run passed all 35 Windows tests and completed release generation and verification; Linux passed too. A reasonable **scoped acceptance** is that the tested source passed that CLI/package process on those hosted configurations. It does not establish Windows browser behavior, participant-agent interaction, or behavior on every platform.

**Tentative transferable practice:** When a portability claim matters, compare the actual artifact at the boundary on the target environment, and distinguish a focused regression pass from a complete process pass. Decide whether that extra check is worth its time for your own task.

Time to acceptance and human effort were not measured here; no model usage or monetary cost was recorded. The tests establish software behavior, not participant learning.
