from functools import wraps
import os
import pickle
import time

def cache_func(cache_file, ttl_seconds=None):
    """
    A decorator to memoize function results, persist the cache to a file, and support cache expiration.

    :param cache_file: Path to the file where the cache will be stored.
    :param ttl: Time-to-live for each cache entry in seconds. If None, cache never expires.
    """
    def decorator(func):
        # Load the existing cache if it exists
        if os.path.exists(cache_file):
            with open(cache_file, 'rb') as f:
                cache = pickle.load(f)
        else:
            cache = {}

        @wraps(func)
        def wrapper(*args):
            current_time = time.time()

            # Check if the result is cached and not expired
            if args in cache:
                result, timestamp = cache[args]
                if ttl_seconds is None or current_time - timestamp < ttl_seconds:
                    #print(f"Cache is {current_time - timestamp} seconds, ttl is {ttl_seconds}")
                    return result
                else:
                    # If the cache entry is expired, remove it
                    del cache[args]

            # Compute the result and cache it with the current timestamp
            result = func(*args)
            cache[args] = (result, current_time)

            # Persist the cache to the file
            with open(cache_file, 'wb') as f:
                pickle.dump(cache, f)

            return result

        return wrapper

    return decorator
