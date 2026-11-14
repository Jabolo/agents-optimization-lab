# The Agents Optimization Lab

Use the coding agent you already know, with any model, tools, skills, or delegation available to you. Work individually, at your own pace, and test one real workflow choice against observed evidence instead of taking any technique on faith.

This repository is a self-contained Python 3.11+ / SQLite conference-booking and agenda-export app with zero third-party dependencies, network requirements, or API keys.

## Start here

1. **Give your coding agent the repository URL** `https://github.com/Jabolo/agents-optimization-lab` and ask it to get a local copy and guide you from `START-HERE.md`. Or set it up yourself:
   - Clone with Git:
     ```sh
     git clone https://github.com/Jabolo/agents-optimization-lab.git
     cd agents-optimization-lab
     ```
   - Or use GitHub **Code → Download ZIP**, extract the archive, and open the folder containing `START-HERE.md`.
2. **Open the local repository folder in your coding agent and pick a case.** Keep the root open and name a case folder (starting suggestion: `work/integration`), or open that case folder directly. Run `python3 smoke.py` inside the case folder (Windows: `py -3 smoke.py`) to verify Python works, or open `index.html` locally in your browser for an offline reader and optional notebook.
3. **Choose one workflow habit to watch, work on the case, and check the evidence.** Note *“Usually I ___ → I expect ___”* (or *“I let my agent decide”* / pick a move for this attempt). Pick a contract condition in `docs/contract.md`, run checks, and inspect real output—remember `smoke.py` covers only its examples. Where `NEXT.md` is present, save your initial decision or `inconclusive / no evidence` before opening it (if your agent already read it, simply note that).
4. **Keep a short record** in the browser notebook (`index.html`) or the case's `RESULT.md`—one is enough. In a Git clone, `RESULT.md` is tracked: inspect `git status` before sharing a commit or fork. Note your case decision (`accept / reject / investigate / stop / inconclusive`), what remains uncertain, time or cost if observable (`unknown` is fine), and one workflow habit you will **keep, change, stop, or explore** next. One complete loop or justified stop is meaningful progress; a second attempt is optional.

## Choose a case

Everything is available from the start—pick any case that fits your interest:

### Core cases (`work/`)
- **[work/integration](work/integration/TASK.md)**: Repair a retry after a lost response; assess a later report. *(Default starting case in `index.html`.)*
- **[work/review](work/review/TASK.md)**: Decide whether to accept a proposed change touching retry responses and key conflicts; assess a later report.
- **[work/transfer](work/transfer/TASK.md)**: Assess an agenda-export proposal and choose your own check.

### Alternative explore cases (`explore/`)
- **[explore/warmup](explore/warmup/TASK.md)**: Repair a starter booking-trace bug in reservation retries (no `NEXT.md`).
- **[explore/combined](explore/combined/TASK.md)**: Repair combined booking-trace and retry/transport issues; assess a later report.
- **[explore/review-1](explore/review-1/TASK.md)**: Decide whether to accept a proposed change touching retry response caching; assess a later report.
- **[explore/review-3](explore/review-3/TASK.md)**: Decide whether to accept a proposed change touching retry responses and cancellation queue promotion; assess a later report.

## Guides and optional resources

- **[PROMPT-CARDS.md](PROMPT-CARDS.md)**: Targeted prompts for moments like *"done"*, a disputed claim, or a stalled run.
- **[DECISION-EXAMPLE.md](DECISION-EXAMPLE.md)**: Worked examples of what a crisp workflow note and bounded check look like.
- **[SAVE-RESUME.md](SAVE-RESUME.md)** and **[HELP.md](HELP.md)**: Exporting browser notes, recovering from setup issues, or creating clean copies for follow-up runs.
- **[RESOURCES.md](RESOURCES.md)** and **[EXTENSIONS.md](EXTENSIONS.md)**: Further reading plus fair side-by-side comparison protocols if you want a controlled second run later.

*Orientation for a 45-minute slot: ~0–7 min intro, ~7–40 min solo work, ~40–45 min saving your record and next move. These are rough guides, not synchronized deadlines.*
