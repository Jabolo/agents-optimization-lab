"""Deterministic local stand-in for an unreliable reservation transport."""
from copy import deepcopy


class TransientTransportError(Exception):
    pass


class FakeTransport:
    """Failure script entries are 'before', 'after', or 'ok'; then default to ok."""
    def __init__(self, service, failures=()):
        self.service = service
        self.failures = list(failures)
        self.requests = []

    def send(self, envelope):
        self.requests.append(deepcopy(envelope))
        failure = self.failures.pop(0) if self.failures else "ok"
        if failure not in ("before", "after", "ok"):
            raise ValueError("unknown transport failure")
        if failure == "before":
            raise TransientTransportError("request lost before reaching server")
        headers = envelope["headers"]
        body = envelope["body"]
        result = self.service.reserve(body["session_id"], body["attendee"], headers["X-Request-ID"])
        if failure == "after":
            raise TransientTransportError("response lost after server commit")
        return result
