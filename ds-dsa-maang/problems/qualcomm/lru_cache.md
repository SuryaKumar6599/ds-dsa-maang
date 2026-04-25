An LRU (Least Recently Used) Cache is a caching algorithm that removes the item that hasn’t been accessed for the longest time when the cache reaches its maximum capacity. It operates on the principle that data recently accessed is likely to be accessed again soon. [1, 2, 3]  
It is designed for high performance, aiming to provide $O(1)$ time complexity for both retrieving () and inserting/updating () items. [4, 5, 6, 7]  
Key Concepts 

• Fixed Capacity: The cache has a predefined size. 
• Eviction Policy: When full, the "oldest" item (not accessed recently) is kicked out. 
• Most Recently Used (MRU): Any time an item is read or updated, it is moved to the "newest" position. [1, 8, 9, 10, 11]  

How it Works (Example) 
Imagine a cache with a capacity of 3. 

1. Cache:  (C is most recent, A is least recent) 
2. Access B: Cache becomes  (B moved to the end because it was just used) 
3. Add D (Cache full): A is evicted. Cache becomes  [12, 13, 14, 15, 16]  

Technical Implementation 
To achieve $O(1)$ performance for all operations, an LRU cache is typically implemented using two data structures combined: 

1. Hash Map (Dictionary): Provides fast $O(1)$ lookup for items. It maps keys to nodes in the linked list. 
2. Doubly Linked List: Maintains the order of usage. 

	• Head: Most recently used (MRU) item. 
	• Tail: Least recently used (LRU) item. [2, 19, 20, 21, 22]  

Use Cases 

• Web Browsers: Storing recently visited pages. 
• Operating Systems: Managing page replacement in memory (paging). 
• Databases: Caching frequently accessed query results. 
• CDNs (Content Delivery Networks): Caching popular content close to users. [23, 24, 25, 26, 27]  

Advantages & Disadvantages 

| Feature [1, 2, 28, 29, 30] | Description  |
| --- | --- |
| Fast Access | Both get/put are $O(1)$ on average.  |
| Efficient | Removes only the least likely-to-be-needed data.  |
| Memory Usage | Higher than simpler caches because it needs to store order tracking pointers (doubly linked list).  |
| Complexity | More complex to implement than FIFO (First-In, First-Out).  |
