# Review contract

Use Python 3.11+ and a fresh disposable SQLite file; migrations are out of scope. Review `CHANGE.diff` against `base/booking.py` and the proposed `booking.py`. Run `python3 smoke.py` for a basic check. Its coverage is deliberately incomplete. Choose a fresh or existing agent conversation and ensure it uses this packet. Review options are in `TASK.md`.

A session has positive capacity. `reserve(session_id, attendee, request_key)` reserves a free place or joins a FIFO waitlist and returns `reservation_id`, `session_id`, `attendee`, and the status at creation. An exact retry with the same global request key must return the original response, even if current status has changed. Reusing a key with a different session or attendee must raise `ValueError` without changing reservations.

`cancel(reservation_id)` cancels an active reservation. Canceling a reserved place promotes the oldest *active* waiter in the same session. Canceling an already-canceled reservation changes nothing; canceling a waitlisted reservation does not free a seat. `list_sessions()` counts the current reserved and waitlisted states. Operations must remain atomic across instances sharing a database file.

Review the proposed change for violations of this contract. Justify an accept, reject or inconclusive decision against this contract, and state what you did and did not check. Passing the smoke check alone does not establish the entire contract.
