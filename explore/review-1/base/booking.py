"""Small conference reservation service; uses only Python's standard library."""

import sqlite3
from contextlib import closing
from pathlib import Path


class BookingService:
    """Persist catalog, reservations, and request keys in a SQLite file.

    Each operation owns its connection so separate service instances can safely
    share the same database file. Use a file path, not ':memory:'.
    """

    def __init__(self, db_path: str | Path):
        self.db_path = str(db_path)
        if self.db_path == ":memory:":
            raise ValueError("use a SQLite file; operations use separate connections")
        with closing(self._connect()) as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS sessions (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    capacity INTEGER NOT NULL CHECK (capacity > 0)
                );
                CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL REFERENCES sessions(id),
                    attendee TEXT NOT NULL,
                    status TEXT NOT NULL CHECK (status IN ('reserved', 'waitlisted', 'cancelled'))
                );
                CREATE INDEX IF NOT EXISTS reservations_queue
                    ON reservations(session_id, status, id);
                CREATE TABLE IF NOT EXISTS requests (
                    request_key TEXT PRIMARY KEY,
                    session_id TEXT NOT NULL,
                    attendee TEXT NOT NULL,
                    reservation_id INTEGER NOT NULL REFERENCES reservations(id)
                );
            """)

    def _connect(self):
        db = sqlite3.connect(self.db_path, timeout=5, isolation_level=None)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys = ON")
        return db

    def create_session(self, session_id: str, title: str, capacity: int) -> None:
        if not session_id or not title or not isinstance(capacity, int) or isinstance(capacity, bool) or capacity < 1:
            raise ValueError("session needs an id, title, and positive integer capacity")
        with closing(self._connect()) as db:
            db.execute("INSERT INTO sessions VALUES (?, ?, ?)", (session_id, title, capacity))

    def list_sessions(self) -> list[dict]:
        with closing(self._connect()) as db:
            rows = db.execute("""
                SELECT s.id, s.title, s.capacity,
                    SUM(CASE WHEN r.status = 'reserved' THEN 1 ELSE 0 END) AS reserved,
                    SUM(CASE WHEN r.status = 'waitlisted' THEN 1 ELSE 0 END) AS waitlisted
                FROM sessions s LEFT JOIN reservations r ON r.session_id = s.id
                GROUP BY s.id ORDER BY s.id
            """).fetchall()
            return [dict(row) for row in rows]

    def reserve(self, session_id: str, attendee: str, request_key: str) -> dict:
        """Reserve or waitlist once per key; retries return the original result."""
        if not session_id or not attendee or not request_key:
            raise ValueError("session id, attendee, and request key are required")
        with closing(self._connect()) as db:
            db.execute("BEGIN IMMEDIATE")
            try:
                previous = db.execute(
                    "SELECT * FROM requests WHERE request_key = ?", (request_key,)
                ).fetchone()
                if previous:
                    if (previous["session_id"], previous["attendee"]) != (session_id, attendee):
                        raise ValueError("request key was already used for a different request")
                    result = db.execute(
                        "SELECT id AS reservation_id, session_id, attendee, status "
                        "FROM reservations WHERE id = ?", (previous["reservation_id"],)
                    ).fetchone()
                else:
                    session = db.execute("SELECT capacity FROM sessions WHERE id = ?", (session_id,)).fetchone()
                    if session is None:
                        raise ValueError("unknown session")
                    occupied = db.execute(
                        "SELECT COUNT(*) FROM reservations WHERE session_id = ? AND status = 'reserved'",
                        (session_id,),
                    ).fetchone()[0]
                    status = "reserved" if occupied < session["capacity"] else "waitlisted"
                    cursor = db.execute(
                        "INSERT INTO reservations (session_id, attendee, status) VALUES (?, ?, ?)",
                        (session_id, attendee, status),
                    )
                    db.execute("INSERT INTO requests VALUES (?, ?, ?, ?)",
                               (request_key, session_id, attendee, cursor.lastrowid))
                    result = db.execute(
                        "SELECT id AS reservation_id, session_id, attendee, status "
                        "FROM reservations WHERE id = ?", (cursor.lastrowid,)
                    ).fetchone()
                db.commit()
                return dict(result)
            except Exception:
                db.rollback()
                raise

    def cancel(self, reservation_id: int) -> dict:
        """Cancel once and promote the oldest waiter when a seat is released."""
        with closing(self._connect()) as db:
            db.execute("BEGIN IMMEDIATE")
            try:
                reservation = db.execute("SELECT * FROM reservations WHERE id = ?", (reservation_id,)).fetchone()
                if reservation is None or reservation["status"] == "cancelled":
                    db.commit()
                    return {"cancelled": False, "promoted_reservation_id": None}
                db.execute("UPDATE reservations SET status = 'cancelled' WHERE id = ?", (reservation_id,))
                promoted = None
                if reservation["status"] == "reserved":
                    waiter = db.execute(
                        "SELECT id FROM reservations WHERE session_id = ? AND status = 'waitlisted' ORDER BY id LIMIT 1",
                        (reservation["session_id"],),
                    ).fetchone()
                    if waiter:
                        promoted = waiter["id"]
                        db.execute("UPDATE reservations SET status = 'reserved' WHERE id = ?", (promoted,))
                db.commit()
                return {"cancelled": True, "promoted_reservation_id": promoted}
            except Exception:
                db.rollback()
                raise
