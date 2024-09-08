# pymethodecache

Simple caching/memoization mechanism for Python

With some ChatGPT help, a common dependency to a bunch of my quick experiments.

## Usage

```
from cache import cache_func

@cache_func('data/somethingexpensive.pkl')
def somethingexpensive():
    return wget(...)

@cache_func('cache/something_updated_every_week.pkl', ttl_seconds=60*60*24*7)
def something_updated_every_week():
    return wget(...)
```

