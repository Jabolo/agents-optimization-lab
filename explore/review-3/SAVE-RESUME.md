# Save once, resume with evidence

Choose the browser notebook **or** the case's `RESULT.md`. Neither is a required form. Preserve enough actual evidence, its assessed version and your next move to continue; an inconclusive result is valid. Do not ask your agent to invent a personal habit or observation.

## Browser notebook → files in your working copy

1. Keep one editing tab. Browser autosave is a convenience; tabs/copies can overwrite each other before a conflict warning. Export before closing, switching browsers or moving the packet.
2. Choose **Export readable notes** and **Export backup (.json)**. Confirm the downloaded files exist. The first is readable by you and your agent; the second can restore the notebook. Neither edits `RESULT.md` automatically.
3. Move both files into a folder you create named `my-work` at the root of your extracted packet. Give copies descriptive names, such as `integration-paused.md` and `integration-paused.json`; retain earlier versions. This folder and default notebook download names are ignored by the supplied `.gitignore`. They are your local work, not shared workshop material.
4. Before moving any code, note the case folder, actual code version or clearly named copy, last command/result, remaining uncertainty and next intended move. Export identifiers describe the packet at packaging, not code you subsequently changed.
5. To resume, reopen the same packet's `index.html`, choose **Import backup**, select the JSON and review the preview. Export current notes first if you need to keep them; confirmation replaces this browser notebook. Import restores notes, not code or files.

A hosted page and a local file can use different browser storage. Download and extract the packet to work with your agent. Export/import transfers notes between those views when their packet identity matches. Work in the folder whose code you actually assessed.

## RESULT.md → files in your working copy

Write directly in the case's `RESULT.md`, with your agent's help if useful. Save the file. Keep the whole working folder, including your code, tests and any output you intentionally recorded. In a Git clone, `RESULT.md` is tracked: review staged changes before publishing a fork or sharing a commit, and keep personal notes private unless you intend to share them. No browser import is needed. You do not also need to fill the browser notebook.

## Another packet version or interrupted storage

A backup from another packet version is rejected rather than silently reinterpreted. Keep the original Markdown/JSON and working folder. Read the Markdown with your agent, explicitly identify the old and new versions and transfer only the observations you can still justify. Do not relabel an earlier run as proof about changed code.

If autosave fails or pauses, the current tab can still export its in-memory notes. Confirm the export before reloading. If the tab has already closed without a usable backup or stored state, lost text cannot be reconstructed by the workshop; record the gap honestly.

## A small resume check

After making a backup, actually close and reopen your chosen record. Can you find the same case, state what was established, identify what is still unknown and continue with one useful move? Record what happened or mark this check untried. A good result can be deciding that more work is not worth its effort.
