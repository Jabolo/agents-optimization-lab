# Integration contract

Python 3.11+, standard library only. Use a fresh disposable SQLite file for every run; schema migration is out of scope. `python3 smoke.py` exercises an ordinary request. Session catalog, waitlist promotion, and server idempotency retain the behavior in `booking.py`.

`BookingClient(transport).book(session, attendee, request_key, max_attempts=2)` makes one logical reservation. `request_key` is globally unique to the caller's logical request and is sent **unchanged** as the `Idempotency-Key` header on every attempt. `X-Request-ID` identifies an individual attempt and must differ between attempts within one call. The transport passes the idempotency header, not the attempt identifier, to the reservation service. Reusing a key for different request data raises `ValueError` without changing reservations.

The transport raises `TransientTransportError` either before the request reaches the service or after the service commits but before its response arrives. Retry only that exception, at most `max_attempts` total attempts; propagate it when attempts are exhausted. Other errors propagate immediately. A successful retry after a lost response returns the original response and creates one reservation, never an extra waitlist entry. Independent keys remain independent. `FakeTransport.requests` captures sent envelopes for inspection; its failure script accepts `before`, `after`, and `ok`.

`max_attempts` must be a positive integer (a boolean is not accepted); invalid values raise `ValueError` before sending a request.

Your task: investigate `trace.txt`, repair the integration across the client and transport, and write a deterministic regression check that proves both what was sent and the final database state. Run the public smoke check too. Compare elapsed time through acceptance and any reliable agent usage data.
