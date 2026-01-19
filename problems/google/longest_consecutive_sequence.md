# Longest Consecutive Sequence

🔗 **Source**: [LeetCode #128](https://leetcode.com/problems/longest-consecutive-sequence/)  
🏷️ **Companies**: Google  
🔄 **Pattern**: Hash Set / Sequence Detection  

---

## 💡 Why It Matters for Data Scientists

This problem maps to detecting **continuous runs** in data:

- Consecutive days of user activity
- Streak detection in behavioral analytics
- Identifying uninterrupted time-series segments
- Feature engineering for temporal continuity

---

## 🧠 Interview Explanation

- **Approach**:  
  Store all numbers in a hash set.  
  Start counting only from numbers that do **not** have a predecessor (`num - 1`).

- **Key Insight**:  
  Each number is visited at most once → linear time.

- **Time Complexity**:  
  **O(n)**

- **Space Complexity**:  
  **O(n)**

- **Follow-up Discussion**:  
  - How would this change for sorted input?
  - Can this be adapted for timestamps or dates?

---

## 🐍 Solution

See: [`solutions/longest_consecutive_sequence.py`](../../solutions/longest_consecutive_sequence.py)