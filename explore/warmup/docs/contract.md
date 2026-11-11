# Conference reservations: retry investigation

This is a synthetic, file-backed SQLite service. It needs Python 3.11+ and no third-party packages, accounts, or network. `booking.py` is the application. Run from the project root:

```sh
python3 smoke.py
```

## Contract

- `create_session(id, title, capacity)` adds a session with positive integer capacity; `list_sessions()` returns catalog rows, including current reserved and waitlisted counts.
- `reserve(session_id, attendee, request_key)` returns a dictionary containing `reservation_id`, `session_id`, `attendee`, and `status`. The status at creation is `reserved` when a seat is available; otherwise it is `waitlisted`.
- A request key identifies one logical reserve request. An exact retry must return **the same original result**, even if the reservation's current state later changes. Reusing the key with a different session or attendee raises `ValueError` and changes nothing. Keys are global across sessions.
- `cancel(reservation_id)` cancels an active reservation. Canceling a reserved place promotes the oldest waiter for that session. Canceling a waiter does not release a seat. It returns `cancelled` and `promoted_reservation_id`; canceling an already-cancelled or unknown ID reports `cancelled: False` and promotes nobody.
- Capacity, the queue, and request keys must remain consistent across separate service instances using the same database file. SQLite transaction boundaries are part of the service's responsibility.

## Your task

Repair the service to satisfy the contract and support your diagnosis with evidence from `docs/trace.txt` or an executable check. Keep normal reservations and queue promotion working. Add a focused regression check that reproduces the report, then run it alongside the public checks. Record elapsed time and any reliable usage/cost data your own agent exposes; compare evidence, outcome, and effort with another approach if useful.

The public checks cover ordinary workflows; passing them is not proof that the reported retry is fixed. Use a temporary database when experimenting so each run starts clean.
