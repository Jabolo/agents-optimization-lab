# Integration: retry after a lost response

Predict the headers, returned reservation, and persisted rows after a lost response. Which property must hold across attempts?

Use the supplied checkpoint and its contract. After stating your prediction, run `python3 support/probe.py .` from the case folder if Python works (Windows: `py -3 support/probe.py .`). Compare the output to the contract. If Python is unavailable, predict the output before reading the saved observation. The saved observation is from a separate prior local run; it does not verify your own code. Decide what the observation supports and identify an untested case. Record any time you actually observe; no timing is supplied by this replay.
