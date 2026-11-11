# Agenda export contract

`agenda.order_sessions(sessions)` receives a list of session dictionaries and returns a new list containing the same dictionaries. Each session has a unique string `id`, a `title`, and `starts_at`. The latter has the exact form `YYYY-MM-DDTHH:MM:SS±HH:MM`, with a valid Gregorian date and time (no leap seconds), year 2000–2099, and an explicit numeric UTC offset of less than 24 hours in magnitude (for example, `2026-10-24T09:00:00+02:00`). Inputs are valid. Extra fields, if present, must be retained.

The exported agenda orders sessions by their actual start instant, earliest first. When two sessions start at the same instant, order them by ascending `id` (Python string ordering). An empty input returns an empty list. The input list and its dictionaries must not be modified.

The module uses Python 3.11+ and the standard library. The proposed implementation and a synthetic dataset are included. `python3 smoke.py` runs a small example check.
