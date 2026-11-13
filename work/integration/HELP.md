# Help and recovery

Work individually and at your own pace. A partial result or “inconclusive / no evidence” is a useful place to save and resume. Each case has its own `TASK.md`, contract and `RESULT.md`; use that record or the complete packet's browser notebook (`index.html`), without duplicating notes.

## Setup

Give your agent the [public repository](https://github.com/Jabolo/agents-optimization-lab), or clone it with `git clone https://github.com/Jabolo/agents-optimization-lab`. If Git is unavailable, GitHub's **Code → Download ZIP** provides a snapshot; extract it and open the folder containing `START-HERE.md`. A snapshot does not include Git history.

### Browser companion

Open `index.html` locally in your web browser (double-click the file or open `file:///.../index.html`). Do **not** view `index.html` directly on GitHub: it is an offline companion designed to run locally without a web server or network connection. It includes prompt cards, reference documents, and an optional decision notebook.

### Terminal smoke check

In a terminal opened at the local repository folder, choose a case and run its smoke check:
- **Core cases:** `work/integration`, `work/review`, `work/transfer`
- **Exploration cases:** `explore/warmup`, `explore/combined`, `explore/review-1`, `explore/review-3`

On macOS / Linux:

```sh
cd work/integration   # or work/review, work/transfer, explore/warmup, etc.
python3 --version     # Python 3.11+ recommended
python3 smoke.py
```

On Windows (PowerShell or Command Prompt):

```powershell
cd work\integration   # or work\review, work\transfer, explore\warmup, etc.
py -3 --version       # Python 3.11+ recommended
py -3 smoke.py
```

### Open in your coding agent

In your existing authenticated coding agent (VS Code, Cursor, Windsurf, Claude Code, Antigravity, Gemini CLI, etc.), either keep the repository root open and name the chosen case folder (for example, `work/integration/`) or open that case folder directly. Ask your agent to read its `TASK.md` and `docs/contract.md`, and confirm the case directory for commands and results. Use disposable local files without credentials or secrets.

## Stuck or interrupted

- Read the case's trace and contract; choose a condition and predict an informative check. Save actual output, uncertainty and your next move, even if no check completes.
- For a case with `NEXT.md`, first record your current decision or what remains undecided, then assess the report. If your agent read it early, record that exposure without inventing an earlier prediction.
- Where present (`work/integration`, `work/review`, `work/transfer`, `explore/review-1`, `explore/review-3`), `support/READ-ME-FIRST.md` explains optional scenario support after your decision or inconclusive result; for a review case, assess `NEXT.md` first. See `FALLBACK.md` in the case folder.
- If Python cannot run, a saved support observation describes an earlier run of the original case, not your changes. It supplies no elapsed time or cost. Without a support folder, use the visible trace and contract, record limits and resume when tools work.

## Reset without losing work

Do not delete or overwrite your existing folder. A new branch carries the current working-tree edits; a normal stash can leave untracked files. Neither alone guarantees a fresh start.
- **Git clone:** Ask your agent to create a separate fresh clone or Git worktree at the same recorded starting commit, in a new directory. If the public repository has changed, identify and use the original commit rather than assuming its latest version is the same.
- **GitHub snapshot:** Save the original downloaded snapshot and extract it again into a new, clearly named directory. A later download of the main branch may contain different files.
For a comparison, verify that both starting copies contain the same task, contract and relevant files before running either approach. Identify the folders and versions in your record and associate each output and decision with the version it actually tested. A copy of your changed folder preserves that work, but is not a fresh starting point. Copy only work you intentionally want to continue; retain the original as your record.

## Save and resume

Use the browser notebook or `RESULT.md`; there is no need to fill both. For browser notes, export readable Markdown and a JSON backup, confirm the downloads and keep them in a local `my-work` folder alongside your case folders. One editing tab and regular exports reduce reliance on browser storage. Restore the JSON only into the same packet version after reviewing the import preview. The backup restores notes, not code. See [SAVE-RESUME.md](SAVE-RESUME.md) for the complete procedure, version changes and a short actual reopen check.
