"""Proposed ordering for a conference agenda export."""


def order_sessions(sessions):
    """Return sessions in the order used by the exported agenda."""
    return sorted(sessions, key=lambda session: (session["starts_at"], session["id"]))
