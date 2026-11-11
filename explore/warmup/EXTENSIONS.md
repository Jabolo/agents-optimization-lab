# Continue the lab

Choose one path or combine paths below. The budgets are rough planning estimates, not deadlines or measured participant times. Work individually at your own pace and use your coding agent, models, tools, skills and delegation as fully as you find useful. The aim is to make a decision supported by an observation, not to complete a fixed number of tasks.

Start each path by naming a condition from the visible contract and a check whose result could affect your decision. Record your expectation before inspecting the result; then preserve the command or data and actual output, its limits, and your decision in the browser notebook or that checkpoint's `RESULT.md`. Choose one; there is no need to duplicate your record. Include elapsed time through the decision and any reliable usage or cost only when available; otherwise write unknown or N/A. Your agent may help with every step, but your own habits and expectations must come from you.

Where a checkpoint has `NEXT.md`, open it after recording your initial decision or an explicit **inconclusive / no usable evidence** and next move. This is a voluntary sequence, not a technical restriction: your agent can use all available files. Assess the report separately, preserve the earlier decision and record whether the new observation changes it. Reuse or copy a checkpoint into a fresh folder when a comparison needs the same starting point; label the folder and version behind each result. If you already changed a checkpoint, keep that work and make the distinction clear.

## 1. Follow a reservation across attempts — 15–25 minutes

**Entry:** `work/integration`, its `TASK.md`, `docs/contract.md` and `docs/trace.txt`.

**Goal:** decide whether the evidence about one logical booking is strong enough for the use you have in mind. Use your normal workflow and note what you expect it to establish. Choose a failure sequence permitted by the contract and make a deterministic check of both the request envelopes and the resulting database state. Once you have recorded your first decision or inconclusive result, assess `NEXT.md` and decide whether its scenario needs another check. Use a fresh disposable database for each run.

**Artifact:** actual check output, the relevant version of the code, and a decision in the notebook or `RESULT.md`, including what remains unchecked.

**Enough to decide:** a reproducible observation that addresses the chosen contract condition and is consistent or inconsistent with it supports a decision for that scenario; a missing or failed-to-run check supports an inconclusive decision and a next step. A smoke pass alone supports its ordinary example, not the whole contract. **Stop** when a further observation is unlikely to change your scoped decision enough to justify its time; **resume** by choosing a different allowed failure sequence or checking an unresolved condition.

## 2. Assess a review and a competing claim — 15–25 minutes

**Entry:** `work/review`, including `CHANGE.diff`, `base/booking.py`, the proposed `booking.py` and `docs/contract.md`.

**Goal:** decide whether to accept, reject or continue investigating the proposal, and assess a separate review claim. Begin with your usual review habit. Choose a contract condition, inspect the change and run a check if useful. Keep the proposed production files unchanged while reviewing so the evidence identifies the candidate. After recording your first decision or inconclusive result, read `NEXT.md` and assess its claim against the same contract. A claim and the whole proposal can have different verdicts.

**Artifact:** a finding or acceptance decision tied to a contract condition and actual output or a reproducible data path; also record the scope of what you did not check. A notebook or `RESULT.md` entry is enough.

**Enough to decide:** a reproducible contract violation supports rejecting the proposal; for acceptance, state the conditions checked and residual risk you are willing to accept. Unsupported or unfinished evidence warrants further investigation or an inconclusive result. **Stop** when your scoped decision is supported and another check is not worth its cost; **resume** with a different contract condition or another available review case in `explore/review-1` or `explore/review-3`. Cases are independent proposals; do not transfer a verdict between them.

## 3. Test an agenda release — 20–30 minutes

**Entry:** `work/transfer`, including `docs/ticket.md`, `docs/contract.md` and `sessions.json`.

**Goal:** decide if the release candidate is ready for the scope you can support. Choose a check using the visible data or construct a valid input from the contract. Calculate or otherwise establish the expected result independently enough to explain it, run the candidate and compare the actual output. Consider another contract condition if it might change the decision. A patch is optional; if you make one, assess the original and modified versions separately.

**Artifact:** input, expected and actual outputs, decision, remaining uncertainty and, if changed, the patch and its new check.

**Enough to decide:** a reproducible mismatch with the contract supports rejection of the assessed version. Passing examples support only their covered conditions; state the scope and whether more evidence is worth obtaining before release. **Stop** after a supported scoped decision or an explicit inconclusive result; **resume** with an untested boundary or recheck a modified candidate.

## 4. Combine the reservation concerns — 35–55 minutes

**Entry:** a fresh copy of `explore/combined`, its contract and trace.

**Goal:** investigate and, if useful, repair a case involving more than one reservation concern. Identify a condition and its observable consequences before choosing your approach. Let the agent investigate, test, modify or delegate as useful. Check at least one behavior at the interface and its relevant persisted state; then consider another distinct contract condition that could affect acceptance. Record an initial decision or inconclusive result before assessing `NEXT.md`.

**Artifact:** your observations and decision, plus the patch and runnable checks if you made them. Identify the version and database used for each observation.

**Enough to decide:** a repeatable observation tied to a published condition supports a scoped decision; a repair also needs a passing check of the behavior it claims to repair. Passing one scenario does not establish the combined contract. **Stop** with a supported decision or a named uncertainty and reason for stopping; **resume** by testing an independent condition or by checking whether a later change affected an earlier result.

## 5. Compare one practice on a fresh start — 35–55 minutes

The optional [prompt cards](PROMPT-CARDS.md) can supply one alternative: compare your usual instruction with a card for a gap you actually encountered. Record the wording you used and whether it changed the evidence, effort or decision. Equivalent behavior and added overhead are valid observations; you do not have to run a prompt comparison.

**Entry:** two fresh copies of the same checkpoint, such as `explore/warmup` or `explore/combined`. Pick one practice you might actually change: a model or effort setting, context or handoff, an existing skill, evidence gathering, or delegation. Availability depends on your own tools; no installation is required.

**Goal:** learn whether that choice is worth trying in your work. Before observing outcomes, record your usual choice, a plausible alternative, and what difference would matter. Use the same starting files, task and visible acceptance conditions in both copies. You and your agents may use all capabilities in each attempt; record other meaningful differences and interventions. Compare actual artifacts and evidence, time through your decision including repairs and coordination, and cost or usage only if reliable and visible. After a tool or model change, you can return to the same fresh start, change that one choice, label versions and run the same relevant check; use its actual output to decide whether to keep, change or retire a step.

**Artifact:** two labeled attempts, their checks and outcomes, observed timing or unknown, and a short decision about whether and when to use the practice again.

**Enough to decide:** actual comparable observations can justify a tentative personal choice for this task; a failed, unfinished or unmeasured attempt may instead justify an inconclusive result. One run per approach, order effects and changing agent behavior cannot establish a general winner or causal advantage. **Stop** when the comparison answers your practical question or its added cost is no longer worthwhile; **resume** by repeating with reversed order or another task if that evidence could change your choice.

## 6. Transfer to your own work — 20–40 minutes

**Entry:** a small synthetic example you create or a project you are authorized to use. Keep private project material within your own environment and do not publish it as part of this exercise.

**Goal:** apply the decision process to a condition that matters in your work. State an observable acceptance condition, your usual move and what you expect; choose a check, inspect its actual result, and decide whether to accept, investigate, change approach or stop. Optionally name a model, tool, task or risk change that would bring you back. If you compare on return, use the same fresh start with one changed choice, label the versions, inspect an actual check and decide whether to keep, change or retire a step. Use an agent as needed. If sharing an example later, use a synthetic or appropriately redacted version.

**Artifact:** a local record of the condition, check, observation, uncertainty and decision. End with one personal rule: **I will keep / change / stop ___ when ___, because I observed ___**. If the evidence is inconclusive, say what observation would be needed before changing your habit.

**Enough to decide:** the result must address the chosen condition and its limitation must be clear enough for your scoped decision. A later comparison is tentative: record version and other differences, and do not claim a comparison you did not run. **Stop** when you can explain that decision and the next observation, if any; **resume** when a changed risk or new evidence makes another check worthwhile.

## Suggested routes

- **About 60 minutes beyond the core lab:** revisit integration (path 1), assess the review claim (path 2), then extend your agenda assessment (path 3). If you have already completed a step, spend the time on an unchecked condition or move to path 6.
- **About 180 minutes beyond the core lab:** take the 60-minute route, then combined reservations (path 4), a comparison of one practice (path 5), and transfer to your own work (path 6). Choose the longer or shorter end of each budget to suit your question and remaining time.

These routes are working hypotheses, not guarantees of timing or learning. A quick solve is a chance to decide whether another check is worth its cost; an unfinished experiment can still produce an evidence-based next move.

## Material used and limits

The paths use `work/integration`, `work/review`, `work/transfer`, `explore/combined`, `explore/warmup`, `explore/review-1` and `explore/review-3` in the learner package, especially their visible tasks, contracts, code, traces, smoke checks and local `NEXT.md` reports where supplied. Create checks from those public materials; no private grading tool or hidden answer is required. Smoke checks and individual examples are bounded evidence, not proof of every contract condition. The supplied cases use synthetic data; results on them and any personal comparison do not establish a provider ranking or a lasting change in skill.

Some working code is shared across cases. Reuse is allowed; record where it came from and assess the assembled result rather than calling it an independent discovery. If this makes a repair quick, choose a new valid scenario or a useful comparison whose result could change your decision.
