from functools import lru_cache

@lru_cache(maxsize=3)
def get_data(data_id):
    print(f"Fetching {data_id}...")
    return f"Data {data_id}"

# Accessing data
get_data(1) # Fetches
get_data(2) # Fetches
get_data(1) # Returns from cache (1 is now MRU)
get_data(3) # Fetches
get_data(4) # Fetches (2 was least recently used, so it is evicted)
