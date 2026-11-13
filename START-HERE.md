# The Agents Optimization Lab

Use the coding agent you already know, with any model, tools, skills, or delegation available to you. Work individually, at your own pace. Explore whether the way you work with your agent helps you reach a result worth accepting—and what you would keep or change next time. Choose a check, predict what it will show, inspect what actually happened, and decide what to do next while keeping time, cost, and quality trade-offs visible.

Adapting and innovating are part of professional practice: when the model, tool, task, or risk changes, revisit your assumptions. An improvement may remove an obsolete step; keeping a practice supported by evidence is also a valid choice.

## Start here

This codebase is a small, self-contained conference-booking and agenda-export service built with Python 3.11+ and SQLite. It has zero third-party dependencies, network requirements, or external API keys.

1. **Give your coding agent the repository URL** `https://github.com/Jabolo/agents-optimization-lab` and ask it to help you get a local copy and start from `START-HERE.md`. Or get the code yourself:
   - Clone the public repository:
     ```sh
     git clone https://github.com/Jabolo/agents-optimization-lab.git
     cd agents-optimization-lab
     ```
   - If Git is unavailable, GitHub's **Code → Download ZIP** provides a repository snapshot. Extract it and open the folder containing `START-HERE.md`.

2. **Open the local repository folder in your coding agent.** Ask it to help you choose a case, then name that case folder when asking it to read the task and contract. You may keep the root open or open the chosen case directly; use your agent's usual folder-opening method. You can also follow these instructions yourself.
3. **Choose one workflow habit to watch.** Note what you expect it to help with, then work on the case. When you have a result, inspect the evidence and decide what to do next.
4. **Keep a short record** in the browser notebook or the case's `RESULT.md`—one is enough. In a Git clone, `RESULT.md` is tracked: review staged changes before sharing a commit or fork. Stop or resume when useful; one complete decision loop is meaningful progress.

For local checks, run `python3 smoke.py` from the chosen case folder (Windows: `py -3 smoke.py`). A passing smoke covers its examples, not the whole contract. The optional browser companion is `index.html` in the local packet; GitHub displays its source rather than running it.

## Optional browser companion

Open `index.html` locally in your web browser for readable materials, prompt-copy buttons, and an optional personal notebook. It works offline without a server. Use that notebook **or** each case’s `RESULT.md`; browser notes do not update files or run checks. Export notes before closing, moving, or updating the packet. Browser storage is best effort, especially across tabs; keep the exported Markdown/JSON as your portable record. All instructions and exercises also work directly from these Markdown files. [SAVE-RESUME.md](SAVE-RESUME.md) explains keeping a portable record in your working copy and reopening it.

## Choose your route

Start wherever your interest takes you—everything is available from the beginning:

### Core cases (`work/`)
- **[work/integration](work/integration/TASK.md)**: Repair a retry after a lost response; assess a later report. (Default starting case displayed in the browser companion).
- **[work/review](work/review/TASK.md)**: Decide whether to accept a proposed change touching retry responses and key conflicts; assess a later report.
- **[work/transfer](work/transfer/TASK.md)**: Assess a new agenda-export proposal and choose your own check.

### Alternative explore cases (`explore/`)
- **[explore/warmup](explore/warmup/TASK.md)**: Repair a starter booking-trace bug in reservation retries; this case has no later report.
- **[explore/combined](explore/combined/TASK.md)**: Repair combined booking-trace and retry/transport issues; assess a later report.
- **[explore/review-1](explore/review-1/TASK.md)**: Decide whether to accept a proposed change touching retry response caching; assess a later report.
- **[explore/review-3](explore/review-3/TASK.md)**: Decide whether to accept a proposed change touching retry responses and cancellation queue promotion; assess a later report.

Open your selected case folder to inspect its `TASK.md`, `README.md`, and contract. Each case folder is self-contained. Record actual evidence and your decision in the browser notebook or the case's `RESULT.md` (one record is enough). A single complete loop is a meaningful outcome; you can complete one case, leave a partial result, switch cases, or continue later.

A suggested 45-minute slot is 0–7 minutes for introduction and orientation, 7–40 for individual work, and 40–45 for saving your place and reflecting. These are orientation, not synchronized deadlines. No one needs to finish the same cases or move together.

## Start a loop

Examine your own engineering habits and tooling under real conditions. The optional [decision examples](DECISION-EXAMPLE.md) show a workflow choice and a bounded check in unrelated situations; your judgment is your own. Start with a workflow you actually use, then keep it or test a deliberate change. [PROMPT-CARDS.md](PROMPT-CARDS.md) offers optional prompts for moments such as “done”, a disputed review claim, or a stalled attempt. You do not need to change a successful habit.

1. **Habit & expectation:** Choose one part of your usual agent workflow to pay attention to. For example: short or detailed instructions; asking for evidence before edits; a skill, fresh session, model or delegation; or how you review tests. Note “Usually I ___ → I expect ___.” “I let my agent decide” and “I have no usual move” are valid; in the latter case choose a move for this attempt. Your agent can help express your thoughts, but cannot invent them.
2. **Condition & prediction:** Pick a contract condition and an executable check. Predict what result would support acceptance, and what it would establish.
3. **Execute & inspect evidence:** Work with your agent and inspect the real output. Save the command, evidence, scope, and remaining uncertainty (or record **inconclusive / no evidence** if nothing usable returned).
4. **Decide & evaluate trade-offs:** Decide to accept, reject, seek another observation, change approach, or stop, and explain why. Note time through the decision if observed or estimated, and reliable cost or usage if available; otherwise mark unknown or N/A.
5. **Assess `NEXT.md` (where present):** Where `NEXT.md` exists, first record your current decision or what remains undecided, then open it. Treat its report as a question to investigate, not an answer. Assess it separately with evidence and keep or revise your decision. (If your agent accessed it early, record that exposure; do not invent an earlier prediction or decision).

“Works on my prompt” is a hypothesis. When your agent has a result, compare what your workflow actually did with your expectation. You may inspect the evidence, try a small workflow move if it addresses a gap, or stop if the result is sufficient for your scope. Record what happened and whether any extra effort was worthwhile. A justified stop or an inconclusive result is a complete, valid loop; you need not run a second attempt.

For example, if you use a separate reviewer, look for a specific finding it reported and whether that changed your next decision. You may not know whether you would have found it another way; record that uncertainty rather than guessing.

An observation of your usual workflow, a small intervention, and a comparison of two approaches are different things. For a direct comparison, use equivalent fresh starts and checks; [EXTENSIONS.md](EXTENSIONS.md) explains how. One attempt per approach supports only a tentative choice for this task.

For another case, name its folder in your existing agent or open that folder directly; run commands from the chosen case folder. See [HELP.md](HELP.md) for setup, preserving work, and recovery. [RESOURCES.md](RESOURCES.md) and [EXTENSIONS.md](EXTENSIONS.md) provide further material. Use disposable copies without secrets.

The cases share an application and some working code. You and your agent may reuse it. Record reuse or prior exposure when interpreting a comparison; verifying an assembled solution can be a useful next experiment.
