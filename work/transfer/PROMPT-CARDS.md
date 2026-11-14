# Prompts for useful moments

These hints and prompt cards are optional — use, adapt, or ignore them. If your usual workflow is already working, stick with it. Use your agent fully and work at your own pace.

## Need a hint?

Pick the smallest helpful next move. Your agent can help with any of these; you decide what the observation means.

- **I don't understand the task:** Ask your agent: “Explain this case briefly. What outcome are we trying to establish?”
- **I don't know what to check:** Choose one condition in `docs/contract.md`. Ask: “What small check could tell us about this condition, and what would it leave open?”
- **My agent says it is done:** Ask: “What did you actually check on this version? Show me the result and what remains uncertain.” Card 2 below has a longer version.
- **I'm stuck or want an example:** In cases with `support/`, read the chosen case's `support/READ-ME-FIRST.md` for a scenario and runnable probe. The live probe checks your current copy; the saved observation is from an earlier run. If you or your agent saw a report or support early, note that exposure rather than inventing an earlier prediction.
- **My agent finished quickly:** Ask: “What evidence would change my decision, and is another check worth the effort?” Or stop with a scoped decision.

For setup or a fresh copy, see [HELP.md](HELP.md). For an example of a short decision, see [DECISION-EXAMPLE.md](DECISION-EXAMPLE.md). A partial or inconclusive result is useful; you do not need to use every hint.

This lab is a retrospective on your tools and thinking, using real task results as evidence. Start with the workflow you actually use. When you notice a gap, choose a card, adapt it or use your own words. If your agent already does the useful work, an extra instruction may add nothing.

Before trying a change, briefly note what you expect it to improve. Afterward inspect the actual output: did you gain decision-relevant evidence, reduce effort, or just get a longer answer? Keep a successful habit if the observations support it. Your agent may help formulate your own judgment but cannot supply your personal experience.

## Pick a moment

| Moment | Try | Inspect afterward |
| --- | --- | --- |
| I want a simple starting instruction | 1. Start normally | A real task result and the checks actually run |
| The agent says it is done | 2. Examine the evidence | What the checks establish and leave open |
| A reviewer or NEXT report makes a claim | 3. Assess the claim | Evidence for that claim, separate from the whole change |
| We are repeating work or considering a stronger setup | 4. Choose the next move | New information that could change the decision, with its cost |
| I want to resume or delegate | 5. Transfer verified state | Whether another context can verify and use the handoff |
| I have enough evidence to reflect | 6. Make a small retrospective | One personal practice to keep, change or stop and when |

## 1. Start normally

Use if a blank prompt is slowing you down. You can instead use your usual instruction.

```text
Read TASK.md and the visible contract in this case. Work on the task using
your normal tools. Run checks appropriate to the change, and show their actual
results and what remains uncertain. Identify which version you assessed.
```

**Look for:** real command output, not just a confident explanation, tied directly to the task. If NEXT.md or support was read early, note that instead of reconstructing an earlier prediction—a starter prompt shapes how you begin, not what the agent already saw.

## 2. The agent says it is done

```text
Which acceptance conditions have we actually checked on this version?
Show the commands or observations already obtained and their actual results.
Distinguish executed checks, earlier output and checks only proposed.
What important uncertainty remains? If another check is worth the remaining
time, choose and run a small one; otherwise explain why stopping is reasonable.
```

**Look for:** actual command output and a clear scope for your decision. Re-running the same passing check only helps if you changed the code or need to answer a new question; once you have enough evidence, stopping is fine.

## 3. A review claim needs assessment

Open NEXT.md according to the case's convention: first preserve your current decision or inconclusive result. If it was already read, say so.

```text
Assess this claim against the visible contract and the proposed version.
Identify the relevant condition and try to obtain reproducible evidence for
or against the claim. Show the actual result, or mark the issue inconclusive.
Decide separately what this establishes about the claim and about accepting
the entire proposal. Do not assume a defect must exist.
```

**Look for:** real evidence for or against the specific claim, not a quota of findings. A wrong review comment does not clear the rest of the change, and a separate bug can exist alongside it. Asking a fresh reviewer is optional—inspect what it actually found rather than assuming it caught everything.

## 4. We are looping or considering a stronger setup

Also useful after an agent finishes quickly: first decide whether a new move could change your decision. Use, adapt or skip this prompt.

```text
Briefly list the recent attempts and what each actually established.
Which uncertainty could change our decision? Choose one small action that
could address it and say what we expect it to establish. If worthwhile, try
it and show the actual result, its limits and any extra effort. If another
step is not worthwhile, explain why. Do not invent timing, usage or cost.
```

**Look for:** genuinely new information or a clear reason to stop. Did this move tell you something new, repeat what the agent already showed, or add more overhead than value? More effort, another model, a skill, a tool call, or a subagent can help or slow you down. If you want to change a client setting, check and change it yourself rather than assuming the agent changed it.

| Choice to inspect | A question worth testing |
| --- | --- |
| Model or reasoning effort | Does it resolve this uncertainty enough to justify time and visible usage? |
| Context or a fresh conversation | Does the relevant contract and version survive, and is the result verified? |
| Existing skill or instruction | Does it produce useful evidence beyond what the usual workflow already provides? |
| Delegation | Is there an independent question to answer, and who checks the integrated result? |
| Tools and execution access | Did the agent actually use the tool and observe the relevant state? |

For a comparison use the fresh-start experiment in [EXTENSIONS.md](EXTENSIONS.md). One attempt per approach supports a tentative personal choice, not a universal winner. Do not buy access or install something merely to use this card.

## 5. Resume in another context, or delegate a bounded question

For a handoff:

```text
Create a short handoff: task and contract, folder/version, changes made,
commands and actual results, unresolved questions, and the next useful check.
Separate verified observations from assumptions. Do not claim the work is
accepted where evidence is missing.
```

In the receiving context:

```text
Use this handoff to locate the stated version. Verify the information needed
for the next decision, then continue from the unresolved question. Report
missing or contradictory state rather than assuming the handoff is correct.
```

**Look for:** recovered state and a result that belongs to the right copy. If delegating instead, specify one bounded question, the working files, the result needed, a time budget and who integrates it. Include preparation, coordination and verification in elapsed time. You do not need another context or another agent to complete the lab.

## 6. A small retrospective

```text
From the actual record, summarize which tool or workflow choices we used,
what each established, and what remained unknown. Point to the observations
behind those statements. Separate recorded facts from estimates and
hypotheses. Leave my personal keep/change/stop judgment for me to supply;
help phrase it after I give it.
```

Then make your own short entry in the browser notebook or the case's `RESULT.md` (choose one):

> My usual choice was ___. I tried or retained ___. I observed ___.
> I will keep / change / stop ___ when ___, because ___ remains true or changes.

If you did not try a different workflow, do not claim a comparison. A finding that your usual agent already did the useful work is a valid outcome. If evidence is missing, record the observation you would need before changing your practice.

Optionally add: “Revisit when ___; I would check ___; I would keep, change or retire ___ based on ___.” A changed model, tool, task or risk might be a trigger; “no trigger yet” and an inconclusive check are valid too. Retiring an obsolete step and keeping a practice that still earns its place are both useful outcomes.

## Small command examples

Run from the selected case folder; inspect the actual output and test count.

```sh
python3 --version
python3 smoke.py
```

Windows equivalents: `py -3 --version` and `py -3 smoke.py` with Python 3.11+.

If you or your agent created root-level `test_*.py` files using Python's unittest framework:

```sh
python3 -m unittest discover -s . -p "test_*.py" -v
```

Windows: `py -3 -m unittest discover -s . -p "test_*.py" -v`.

If the tests are in an existing `tests/` folder, as in the optional warmup, use that start directory instead:

```sh
python3 -m unittest discover -s tests -p "test_*.py" -v
```

Windows: `py -3 -m unittest discover -s tests -p "test_*.py" -v`. A zero-test run does not validate the change. Other test frameworks have their own commands. Optional support has its exact command in `support/SCENARIO.md`; read the case's support guidance before using it.

## Why these examples are short

[Google's prompt design guide](https://ai.google.dev/gemini-api/docs/prompting-strategies) treats clear instructions, context and examples as starting points to iterate using observed responses. It is product guidance, not proof that a particular wording improves every coding agent. [Anthropic's agent-evaluation guide](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) emphasizes observing results and execution traces; it does not require building an evaluation platform for this lab. These prompts are optional starting templates, not proven recipes—keep, adapt, or drop them based on what actually helps in your run.
