# Fruit Into Baskets

🔗 **Source**: [LeetCode #904](https://leetcode.com/problems/fruit-into-baskets/)  
🏷️ **Companies**: Amazon, Apple  
🔄 **Pattern**: Sliding Window (At Most K Distinct)  

---

## 💡 Why It Matters for Data Scientists

This pattern applies to:

- Longest period with limited categories
- Session segmentation
- Constraint-based subarray analysis
- Streaming analytics with category limits

It generalizes to **"at most K distinct"** problems.

---

## 🧠 Interview Explanation

- **Approach**:  
  Use a sliding window with two pointers and a frequency map.  
  Expand window until more than 2 distinct values appear, then shrink.

- **Key Insight**:  
  Window expands and contracts dynamically while maintaining constraints.

- **Time Complexity**:  
  **O(n)**

- **Space Complexity**:  
  **O(1)** — map size bounded by K (=2)

- **Follow-up Discussion**:  
  - How would this generalize to K baskets?
  - How does this work for streaming input?

---

## 🐍 Solution

See: [`solutions/fruit_into_baskets.py`](../../solutions/fruit_into_baskets.py)