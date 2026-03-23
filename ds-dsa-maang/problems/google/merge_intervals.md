# Merge Intervals

🔗 **Source**: [LeetCode #56](https://leetcode.com/problems/merge-intervals/)  
🏷️ **Companies**: Google, Apple  
🔄 **Pattern**: Sorting + Linear Scan  

---

## 💡 Why It Matters for Data Scientists

Interval merging is common in:

- Sessionization of user activity
- Log aggregation
- Time-window consolidation
- Scheduling and availability analysis

This problem reflects **real-world timeline data cleanup**.

---

## 🧠 Interview Explanation

- **Approach**:  
  1. Sort intervals by start time  
  2. Iterate and merge overlapping intervals

- **Key Insight**:  
  Sorting reduces the problem to a single linear scan.

- **Time Complexity**:  
  **O(n log n)** — due to sorting

- **Space Complexity**:  
  **O(n)** — output list

- **Follow-up Discussion**:  
  - Can this be done in-place?
  - How would you handle streaming intervals?

---

## 🐍 Solution

See: [`solutions/merge_intervals.py`](../../solutions/merge_intervals.py)