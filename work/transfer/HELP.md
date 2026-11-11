# Help and recovery

Work individually and at your own pace. A partial result or “inconclusive / no evidence” is a useful place to save and resume. Each case has its own `TASK.md`, contract and `RESULT.md`; use that record or the complete packet's browser notebook, without duplicating notes.

## Setup

In a terminal opened at the extracted complete packet root, run the following for integration (replace the path with `work/review` or `work/transfer` for those cases):

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

Open the same chosen case folder in your existing authenticated coding agent using its usual folder-opening method; tell it which folder to work in. If it uses the wrong directory, point it back to the case and identify the folder in your record. Use disposable files without secrets.

For a standalone case ZIP, open its extracted case folder directly in your terminal and agent; run `python3 --version` and `python3 smoke.py` there (on Windows, `py -3 --version` and `py -3 smoke.py`). The browser notebook is available in the complete packet.

## Stuck or interrupted

- Read the case's trace and contract; choose a condition and predict an informative check. Save actual output, uncertainty and your next move, even if no check completes.
- For a case with `NEXT.md`, first record your current decision or what remains undecided, then assess the report. If your agent read it early, record that exposure without inventing an earlier prediction.
- Where present, `support/READ-ME-FIRST.md` explains optional scenario support after your decision or inconclusive result; for a review case, assess `NEXT.md` first. See `FALLBACK.md` in the case.
- If Python cannot run, a saved support observation describes an earlier run of the original case, not your changes. It supplies no elapsed time or cost. Without a support folder, use the visible trace and contract, record limits and resume when tools work.

## Reset without losing work

Do not delete or overwrite your existing folder. Extract `learner-lab.zip` again into a new, clearly named directory. Identify the original and new folder/version in your chosen record and associate each output and decision with the version it actually tested. Copy only the work you intentionally want to continue; retain the original as your record.

## Save and resume

Use the browser notebook or `RESULT.md`; there is no need to fill both. For browser notes, export readable Markdown and a JSON backup, confirm the downloads and keep them in a local `my-work` folder alongside your case folders. One editing tab and regular exports reduce reliance on browser storage. Restore the JSON only into the same packet version after reviewing the import preview. The backup restores notes, not code. See [SAVE-RESUME.md](SAVE-RESUME.md) for the complete procedure, version changes and a short actual reopen check.
