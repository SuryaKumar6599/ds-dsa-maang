# Top K Frequent Words

🔗 **Source**: [LeetCode #692](https://leetcode.com/problems/top-k-frequent-words/)  
🏷️ **Companies**: Amazon, Google, Apple  
🔄 **Pattern**: Top-K / Heap  

---

## 💡 Why It Matters for Data Scientists

Frequency-based ranking is central to analytics:

- Identifying trending search terms or queries
- Finding most common user actions or events
- Feature selection based on frequency
- Monitoring heavy hitters in logs or streams

This problem mirrors **ranking and aggregation tasks** common in DS workflows.

---

## 🧠 Interview Explanation

- **Approach**:  
  Count word frequencies using a hash map.  
  Use a heap (or sorted list) to extract the top `k` words, ordered by:
  1. Higher frequency  
  2. Lexicographical order (for ties)

- **Time Complexity**:  
  **O(n log k)** using a heap  
  *(or O(n log n) if fully sorted)*

- **Space Complexity**:  
  **O(n)** — frequency map + heap

- **Follow-up Discussion**:  
  - How would you handle streaming input?
  - How would this change for very large vocabularies?

---

## 🐍 Solution

See: [`solutions/top_k_frequent_words.py`](../../solutions/top_k_frequent_words.py)