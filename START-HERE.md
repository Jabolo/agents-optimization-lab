# The Agents Optimization Lab

Use the coding agent you already know, with any model, tools, skills or delegation available to you. Work individually, at your own pace. The aim is to make a useful decision about a result: choose a check, predict what it could show, inspect what actually happened, and decide what to do next. Keep the trade-offs in time, cost and quality visible where you can.

Adapting and innovating are part of professional practice: when the model, tool, task or risk changes, revisit your assumptions. An improvement may remove an obsolete step; keeping a practice supported by evidence is also a valid choice.

## Optional browser view

Open `index.html` in this complete packet for readable materials, prompt-copy buttons and an optional personal notebook. It works locally without a server. Use that notebook **or** each case’s `RESULT.md`; browser notes do not update files or run checks. Export notes before closing, moving or updating the packet. Browser save is best effort, especially with multiple tabs; keep the exported Markdown/JSON as your portable record. All instructions and exercises also work directly from these files. [SAVE-RESUME.md](SAVE-RESUME.md) explains keeping a portable record in your working copy and reopening it.

## Choose your route

After a short introduction, start wherever your interest takes you. Everything is available from the start:

- Want to **repair an integration**? Choose [work/integration](work/integration/TASK.md): a retry after a lost response, followed by a report. Integration is initially displayed in the browser; you may start anywhere.
- Want to **assess a proposal**? Choose [work/review](work/review/TASK.md): decide whether to accept a proposed change, then assess a report.
- Want a **fresh agenda decision**? Choose [work/transfer](work/transfer/TASK.md): assess an agenda-export proposal and choose your own check.
- [explore/warmup](explore/warmup/TASK.md), [explore/combined](explore/combined/TASK.md), [explore/review-1](explore/review-1/TASK.md) and [explore/review-3](explore/review-3/TASK.md): optional alternative cases. `combined` also has a report.

Open the selected folder's `TASK.md`, `README.md` and contract. Each folder is usable on its own. Record actual evidence and your decision in the browser notebook or the selected case's `RESULT.md`; you do not need both. A single complete loop is a meaningful outcome. You may choose another case, pause with a partial result, or continue later.

A suggested 45-minute slot is 0–7 minutes for the introduction, 7–40 for individual work, and 40–45 for saving your place and reflecting. These are orientation, not synchronized deadlines. No one needs to finish the same cases or move together.

## Start a loop

This is also a check of your tooling and thinking. The optional [decision example](DECISION-EXAMPLE.md) shows the shape of a record in an unrelated situation; your judgment is your own. Start with a workflow you actually use; then keep it or try a change for a reason. [PROMPT-CARDS.md](PROMPT-CARDS.md) offers optional prompts for moments such as “done”, a disputed review claim or a stalled attempt. Use, adapt or skip them and inspect what they actually contribute. You do not need to change a successful habit.

1. Note a habit you actually use and your expectation. If you have no usual move, say so and choose one for this attempt. Your agent can help express your thoughts but cannot invent them.
2. Pick a condition and a check. Predict what result would support acceptance, and what it would establish.
3. Work with your agent and inspect the real output. Save the command or evidence, its scope and remaining uncertainty. If nothing usable has returned, record partial work or **inconclusive / no evidence**.
4. Decide to accept, reject, seek another observation, change approach or stop, and explain why. Note time through the decision if observed or estimated and reliable cost or usage if available; otherwise mark unknown or N/A.
5. Where `NEXT.md` exists, first record your current decision or what remains undecided, then open it. Treat its report as a question to investigate, not an answer. Assess it separately and keep or revise your decision. An agent might read it early: record that exposure and do not invent an earlier prediction or decision.

“Works on my prompt” is a hypothesis. Agent finished already? Consider what result could change your decision and whether checking it is worth the time. You can accept within the evidence's scope, check further, record an inconclusive result or stop. Optionally note what change would make you revisit your practice, what you would check and what decision that observation might affect.

Python 3.11+ and a terminal are needed for local checks. From the extracted packet root, these commands open the integration folder and run its smoke check:

```sh
cd work/integration
python3 --version
python3 smoke.py
```

On Windows, from the packet root:

```powershell
cd work\integration
py -3 --version
py -3 smoke.py
```

For another case, replace `work/integration` with its path above; run commands from that case folder. Open that same folder in your existing agent using its usual folder-opening method, and ask it to work there. See [HELP.md](HELP.md) for setup, preserving work and recovery. [RESOURCES.md](RESOURCES.md) and [EXTENSIONS.md](EXTENSIONS.md) provide further material. Use disposable copies without secrets.

The cases share an application and some working code. You and your agent may reuse it. Record reuse or prior exposure when interpreting a comparison; verifying an assembled solution can be a useful next experiment.
