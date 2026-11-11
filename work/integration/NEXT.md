# Support report — A timeout, then another visit

Capacity was 1. The first booking for Ada used caller key `visit-a` and only one allowed attempt. Its response was lost after commit, so the client reported a transport error. Later, the application created a new service/client instance against the same database and submitted the same logical request with `visit-a` again.

Support asks whether the current implementation handles this report under the published contract. What do you decide, and what evidence supports that decision?
