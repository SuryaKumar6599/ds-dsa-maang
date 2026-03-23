# Find Median from Data Stream

🔗 **Source**: [LeetCode #295](https://leetcode.com/problems/find-median-from-data-stream/)  
🏷️ **Companies**: Amazon, Google  
🔄 **Pattern**: Two Heaps / Streaming  

---

## 💡 Why It Matters for Data Scientists

Running medians are widely used in:

- Real-time KPI monitoring
- Robust statistics (median vs mean)
- Outlier-resistant analytics
- Streaming dashboards and alerts

This problem models **online aggregation** over a data stream.

---

## 🧠 Interview Explanation

- **Approach**:  
  Maintain two heaps:
  - Max-heap for the lower half
  - Min-heap for the upper half  
  Balance the heaps so their sizes differ by at most one.

- **Key Insight**:  
  Median is always at the top of one or both heaps.

- **Time Complexity**:  
  **O(log n)** per insertion

- **Space Complexity**:  
  **O(n)** — stores all elements

- **Follow-up Discussion**:  
  - How would you compute rolling medians?
  - How does this compare to batch computation?

---

## 🐍 Solution

See: [`solutions/find_median_from_data_stream.py`](../../solutions/find_median_from_data_stream.py)