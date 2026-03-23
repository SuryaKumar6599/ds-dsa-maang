# Two Sum

🔗 **Source**: [LeetCode #1](https://leetcode.com/problems/two-sum/)  
🏷️ **Companies**: Amazon, Google, Meta  
🔄 **Pattern**: Hashing  

---

## 💡 Why It Matters for Data Scientists

This problem reflects:

- Matching complementary values
- Pair-based filtering
- Join-like logic in data processing
- Constraint satisfaction in feature engineering

It tests **basic optimization and lookup skills**.

---

## 🧠 Interview Explanation

- **Approach**:  
  Iterate once while storing seen values in a hash map.  
  For each number, check if `target - number` already exists.

- **Key Insight**:  
  Trade space for time to reduce complexity.

- **Time Complexity**:  
  **O(n)**

- **Space Complexity**:  
  **O(n)**

- **Follow-up Discussion**:  
  - What if the array is sorted?
  - How would you return all valid pairs?

---

## 🐍 Solution

See: [`solutions/two_sum.py`](../../solutions/two_sum.py)