# Support report — A timeout, then another visit

Capacity was 1. The first booking for Ada used caller key `visit-a` and only one allowed attempt. Its response was lost after commit, so the client reported a transport error. Later, the application created a new service/client instance against the same database and submitted the same logical request with `visit-a` again.

Suggested quick workaround from the incident channel: clear the `requests` row when `transport.send` raises `TransientTransportError` so the caller can retry cleanly.

Support asks whether the current implementation handles this report under the published contract—and whether to apply that workaround. What do you decide, and what evidence supports that decision?
