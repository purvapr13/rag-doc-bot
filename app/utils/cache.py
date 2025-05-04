from cachetools import LRUCache
from cachetools.keys import hashkey
import threading

# Thread-safe LRU cache (max 100 items by default)
_cache = LRUCache(maxsize=100)
_lock = threading.Lock()


def get_cached_answer(question: str) -> str | None:
    key = hashkey(question)
    with _lock:
        return _cache.get(key)


def store_answer_in_cache(question: str, answer: str):
    key = hashkey(question)
    with _lock:
        _cache[key] = answer
