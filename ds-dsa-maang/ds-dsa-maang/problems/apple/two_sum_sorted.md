# Two Sum II – Input Array Is Sorted

🔗 **Source**: [LeetCode #167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)  
🏷️ **Companies**: Apple, Amazon  
🔄 **Pattern**: Two Pointers  

---

## 💡 Why It Matters for Data Scientists

This problem highlights:

- Leveraging sorted data for efficiency
- Constraint-based pair selection
- Memory-efficient scanning
- Query optimization on ordered datasets

It is common when working with **pre-sorted metrics or time-series**.

---

## 🧠 Interview Explanation

- **Approach**:  
  Use two pointers at both ends of the array.  
  Move pointers inward based on the sum relative to the target.

- **Key Insight**:  
  Sorted order eliminates the need for extra memory.

- **Time Complexity**:  
  **O(n)**

- **Space Complexity**:  
  **O(1)**

- **Follow-up Discussion**:  
  - How would you return all valid pairs?
  - What if the array is streamed but sorted?

---

## 🐍 Solution

See: [`solutions/two_sum_sorted.py`](../../solutions/two_sum_sorted.py)