
Write a Python class for a thread-safe LRU cache (ML model cache use case)
Use OrderedDict + threading.Lock. Override __getitem__, __setitem__. Handle eviction on capacity breach.