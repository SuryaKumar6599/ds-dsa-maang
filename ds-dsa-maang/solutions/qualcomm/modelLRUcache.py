import threading
from collections import OrderedDict

class model_LRU_cache:
    def __init__(self, capacity: int):
        if capacity <=0:
            raise ValueError("Capacity must be greater than 0")
        self.cache  = OrderedDict()
        self.lock = threading.Lock()
        self.capacity = capacity
        
    def __getitem__(self, key):
        with self.lock:
            if key in self.cache:
                # Move the key to the end (most recently used)
                self.cache.move_to_end(key)
                return self.cache[key]
            raise KeyError(key)
        
    def __setitem__(self, key, value):
        with self.lock:
            if key in self.cache:
                # Update the value and move to end
                self.cache[key] = value
                self.cache.move_to_end(key)
            else:
                if len(self.cache) >= self.capacity:
                    # Remove the least recently used item
                    self.cache.popitem(last=False)
                self.cache[key] = value
                
#example usage
example_cache = model_LRU_cache(2)
example_cache['a'] = 1
example_cache['b'] = 2
print(example_cache['a'])  # Output: 1          
example_cache['c'] = 3  # Evicts 'b'
try:
    print(example_cache['b'])  # Should raise KeyError
except KeyError:
    print("Key 'b' not found in cache")  # Output: Key 'b' not found in cache  