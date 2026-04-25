from collections import OrderedDict
from threading import Lock
import time


class ThreadSafeLRUCache:
    """
    Thread-safe LRU cache.
    - get(key) / __getitem__: returns value or raises KeyError
    - put(key, value) / __setitem__: inserts/updates and evicts if needed
    - Optional TTL (seconds): if set, entries expire lazily on access
    """

    def __init__(self, capacity: int, ttl: float | None = None):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")

        self.capacity = capacity
        self.ttl = ttl  # seconds; None = no TTL
        self._store = OrderedDict()  # key -> (value, timestamp)
        self._lock = Lock()

    # ---------- Internal helpers ----------

    def _is_expired(self, ts: float) -> bool:
        return self.ttl is not None and (time.time() - ts) > self.ttl

    def _evict_if_needed(self):
        # Evict until within capacity (handles burst inserts safely)
        while len(self._store) > self.capacity:
            # popitem(last=False) pops LRU (front)
            self._store.popitem(last=False)

    def _touch(self, key):
        # Mark as recently used
        self._store.move_to_end(key, last=True)

    # ---------- Public API ----------

    def get(self, key):
        with self._lock:
            if key not in self._store:
                raise KeyError(key)

            value, ts = self._store[key]

            # Lazy TTL eviction
            if self._is_expired(ts):
                del self._store[key]
                raise KeyError(key)

            # Update recency
            self._touch(key)
            return value

    def put(self, key, value):
        with self._lock:
            now = time.time()
            if key in self._store:
                # Update + move to MRU
                self._store[key] = (value, now)
                self._touch(key)
            else:
                self._store[key] = (value, now)
                self._touch(key)

            self._evict_if_needed()

    # Pythonic sugar
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __contains__(self, key):
        with self._lock:
            if key not in self._store:
                return False
            _, ts = self._store[key]
            if self._is_expired(ts):
                # Clean up lazily
                del self._store[key]
                return False
            return True

    def __len__(self):
        with self._lock:
            # Optional: clean expired entries on len()
            if self.ttl is not None:
                keys_to_delete = [k for k, (_, ts) in self._store.items() if self._is_expired(ts)]
                for k in keys_to_delete:
                    del self._store[k]
            return len(self._store)

    def clear(self):
        with self._lock:
            self._store.clear()

    def items(self):
        """Snapshot of items (safe copy)."""
        with self._lock:
            return [(k, v_ts[0]) for k, v_ts in self._store.items()]

