# Optional reading and experiments

These resources support your own decisions in **The Agents Optimization Lab**. No reading is required: the packet's offline contract, traces and help materials are enough to work through the lab. You may use your coding agent throughout, including to explain a source or help run a check. The links need internet access; none requires a new account, tool or dependency for the suggested experiments.

For a useful comparison, first record your usual move or chosen approach, what you expect and what observation would support a decision. Then inspect the available report or trace, run a check and record what happened and what remains uncertain. This is an agreed order for the experiment, not a restriction: if you read a report early, simply record that when interpreting your result. Save actual output and identify the copy or version it came from. Report elapsed time if known and cost only if reliably visible; otherwise say unknown or N/A.

## Find a source by question

| Question | Starting point below |
| --- | --- |
| Could a generated test share the implementation's mistake? | 1. Coding before testing |
| How do I assess a review claim? | 2. CR-Bench |
| What should a safe retry establish? | 3. AWS retries |
| Where can idempotency semantics differ? | 4. Stripe API v1 |
| Is a handoff or fresh context worth trying? | 5. Context engineering |
| What do the output and trace each establish? | 6. Agent evaluations |
| How does my expectation compare with what happened? | 7. METR survey |
| How could I assess a practitioner's review workflow? | Theo / tstack below |
| How might I revise a prompt for a specific gap? | Google prompt design guide under “If you have another 1–3 hours” |

## Quick: good to know

Read one when it helps with the decision in front of you. Each experiment is optional and should be judged against the local contract.

1. **A passing test has a scope.** After your first check, skim the abstract of [On the risk of coding before testing](https://arxiv.org/abs/2607.05139v1). The authors study how errors in generated code can be reflected in tests generated with that code in context. Try deriving an input and expected outcome from the contract before inspecting the implementation, then run it on your current copy. **Visible result:** input, expected and actual outcome, and one thing the check cannot establish. **Limit:** this preprint studies particular tasks and configurations; a fresh conversation or second model does not by itself guarantee independence.

2. **A review comment is a claim to check.** When assessing a review, skim the abstract of [CR-Bench](https://arxiv.org/html/2603.11078v1). It considers both useful findings and noise in agent reviews. Pick one claim and look for a reproducible observation or counterexample. **Visible result:** the claim, the output or an inconclusive result, and separate decisions about that claim and the whole proposal. **Limit:** the benchmark uses known defects and a model-based evaluation; its results do not establish the reliability of your reviewer or prove the rest of a proposal correct.

3. **A retry needs a defined outcome.** If your case involves retrying an operation, read the introduction and the discussion of request intent in [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/). Choose a retry scenario permitted by the local contract, including an uncertain response, and inspect both the returned result and stored state. **Visible result:** the sequence attempted, observed state and whether it supports your decision. **Limit:** AWS describes its own API design; the local contract determines the expected behavior, including how to treat repeated requests.

4. **An idempotency contract has boundaries.** For another example, skim [Stripe's idempotent requests reference](https://docs.stripe.com/api/idempotent_requests). Compare its API v1 description of repeated requests, changed parameters and key retention with the contract in your packet. **Visible result:** one similarity or difference and a check derived from the local contract. **Limit:** those retention and parameter details are for Stripe API v1; v1 and v2 have different failure behavior. Neither dictates the semantics of this lab.

## Deeper reading and optional experiments

5. **Context and handoffs are choices to test.** In [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents), read the sections on compaction and subagents when you want to continue work in a fresh conversation or consider delegation. Try your usual approach on one copy and a concise handoff on another: include the contract, copy or version, observed output and unresolved question. Ask the agent to verify the relevant state. **Visible result:** what each approach recovered or missed, the checks performed, and any observed time or known usage. **Limit:** this is a provider's engineering guidance, not proof that shorter context or delegation will improve your task. Different attempts may vary for other reasons.

6. **Inspect both the result and the check.** Read the evaluation structure and transcript sections of [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents). Choose two or three contract scenarios, state the expected observable result for each, then run them on an identified copy and inspect at least one trace. **Visible result:** scenarios, expectations, actual outputs and any relevant actual state, plus what the trace shows about execution. A trace is evidence of what was recorded, not by itself proof of current state. Note whether an unexpected result points to the proposal, the check or unresolved uncertainty. **Limit:** this is practical guidance from a provider; a small local set is a bounded check, and no evaluation platform or model-based grader is required.

7. **Compare a feeling with an observation.** Read the summary and the section on surveys and other evidence in [METR's early-2026 AI usage survey](https://metr.org/blog/2026-05-11-ai-usage-survey/). Before a chosen check, note your expectation of the effort; afterward compare it with your recorded time to decision, interventions and actual outcome. **Visible result:** expectation, observation, unknowns and a practice you might keep or change. **Limit:** the survey reports perceptions from a selected technical sample, not a causal estimate for this lab or your own work.

## Practitioner perspective: inspect the mechanism

**Theo Browne / tstack.** The pinned [`sol-loop` instructions](https://github.com/t3dotgg/tstack/blob/6efae364201abc9d9f07443e9caa461f42e51090/skills/sol-loop/SKILL.md) use bounded review and tracking of findings. The [publishing commit](https://github.com/t3dotgg/tstack/commit/6efae364201abc9d9f07443e9caa461f42e51090) is dated 23 October 2026 (24 October UTC); inspected for this lab on 6 November. This is a practitioner's workflow, not evidence of an improvement in this lab, and the pinned version is not a claim about the latest release.

**Try locally, if useful:** for one existing review claim, note the claim, its contract condition, actual evidence and supported / contradicted / inconclusive status in your chosen record. Did the structure help your next decision or add work your usual approach already handled? This adapts one idea; it does not run the external skill. No installation, extra model, account or PR is needed. Model agreement alone does not establish the claim. One attempt gives a tentative personal observation.

When your tools or tasks change, revisit that observation using [the comparison path](EXTENSIONS.md), keeping a version and the actual check result. This is optional reading; the packet's offline prompts and contract are sufficient. No sponsor links or product recommendation are part of this exercise.

## If you have another 1–3 hours

For prompt examples, [Google's prompt design guide](https://ai.google.dev/gemini-api/docs/prompting-strategies) describes clear instructions, context, examples and iterative refinement. Try one optional [lab prompt card](PROMPT-CARDS.md) against your usual approach when it answers a real question. Inspect actual behavior and output, not how sophisticated the prompt sounds. This is vendor guidance and our examples are unvalidated scaffolding, not a guarantee across agents or proof that an added instruction helps.

One possible order is: (1) revisit a completed result with the independent contract-based check in item 1; (2) assess one review claim with item 2; (3) choose either retry scenario from items 3–4 or the context comparison in item 5; (4) use items 6–7 to inspect your evidence and write a personal decision rule. Stop whenever the next observation is not worth its time or cost. The duration is a suggested exploration window, not a measured completion time; one or two attempts support a personal next move, not a ranking of agents or models.
