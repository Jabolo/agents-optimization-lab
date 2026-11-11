# Open challenge: reservation retries

Python 3.11+, standard library only. Use a fresh disposable SQLite file for each run; migration is out of scope. `python3 smoke.py` checks ordinary booking.

`BookingClient(transport).book(session, attendee, request_key, max_attempts=2)` makes one logical reservation. It sends the caller's stable global request key unchanged in the `Idempotency-Key` header on every attempt and uses a different `X-Request-ID` for each attempt. The transport passes the idempotency header to the service. It can fail before delivery or after the service commits; retry only `TransientTransportError`, at most `max_attempts` attempts. Return the original response after an exact retry, even if the reservation later changes state. Reusing a key for different session or attendee raises `ValueError` without mutation. Distinct keys identify distinct reservations.

A session has positive capacity. New bookings reserve a free seat or join its FIFO waitlist. Canceling an active reserved place promotes the oldest active waiter for that session; canceling a waiter does not release a seat. Catalog counts report current states. `FakeTransport.requests` captures envelopes; `before`, `after`, and `ok` script failures deterministically.

Investigate `trace.txt`. Choose a workflow, gather evidence, repair the system, and show reproducible checks for request identity, database state, and historical responses. Record elapsed time through acceptance and any reliable agent usage data.

`max_attempts` must be a positive integer, excluding `bool`; invalid values raise `ValueError` before sending a request.
