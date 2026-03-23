# Kth Largest Element in an Array

🔗 **Source**: [LeetCode #215](https://leetcode.com/problems/kth-largest-element-in-an-array/)  
🏷️ **Companies**: Amazon, Netflix  
🔄 **Pattern**: Heap / Selection  

---

## 💡 Why It Matters for Data Scientists

This problem is closely related to:

- Percentile computation
- Threshold selection
- Outlier detection
- Ranking metrics in large datasets

It teaches **efficient selection without full sorting**.

---

## 🧠 Interview Explanation

- **Approach**:  
  Maintain a min-heap of size `k`.  
  Push elements into the heap and pop when size exceeds `k`.

- **Key Insight**:  
  The heap root always contains the k-th largest element.

- **Time Complexity**:  
  **O(n log k)**

- **Space Complexity**:  
  **O(k)**

- **Follow-up Discussion**:  
  - How does QuickSelect compare?
  - How would you compute multiple percentiles efficiently?

---

## 🐍 Solution

See: [`solutions/kth_largest_element.py`](../../solutions/kth_largest_element.py)