"""Client-side retry orchestration for the local reservation transport."""
from transport import TransientTransportError


class BookingClient:
    def __init__(self, transport):
        self.transport = transport

    def book(self, session, attendee, request_key, max_attempts=2):
        if not request_key or not isinstance(max_attempts, int) or isinstance(max_attempts, bool) or max_attempts < 1:
            raise ValueError("request key and positive max_attempts are required")
        for attempt in range(1, max_attempts + 1):
            envelope = {
                "headers": {
                    "Idempotency-Key": f"{request_key}:{attempt}",
                    "X-Request-ID": f"{request_key}:{attempt}",
                },
                "body": {"session_id": session, "attendee": attendee},
            }
            try:
                return self.transport.send(envelope)
            except TransientTransportError:
                if attempt == max_attempts:
                    raise
