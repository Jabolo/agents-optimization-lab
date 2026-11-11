# Reviewer report — Retry after promotion

Another reviewer reports a blocker:

“Ada reserved the only seat, then Lin joined the waitlist with key `lin-1`. Canceling Ada promoted Lin. A retry with `lin-1` still returns `waitlisted`, while the catalog says one seat is reserved. This mismatch proves the response-snapshot patch is wrong. Change retries to return the current reservation status.”

Assess the report under the published contract. What do you decide, and what evidence supports that decision?
