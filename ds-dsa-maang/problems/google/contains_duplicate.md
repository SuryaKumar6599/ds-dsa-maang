# Contains Duplicate

🔗 **Source**: [LeetCode #217](https://leetcode.com/problems/contains-duplicate/)  
🏷️ **Companies**: Google, Amazon  
🔄 **Pattern**: Hashing / Data Validation  

---

## 💡 Why It Matters for Data Scientists

Duplicate detection is a foundational data-quality task:

- Validating primary keys in datasets
- De-duplicating user event logs
- Ensuring uniqueness in A/B test assignments
- Preventing data leakage due to repeated records

This problem mirrors **real-world ETL validation steps**.

---

## 🧠 Interview Explanation

- **Approach**:  
  Traverse the array and store seen values in a hash set.  
  If a value appears again, a duplicate exists.

- **Time Complexity**:  
  **O(n)** — single pass through the data

- **Space Complexity**:  
  **O(n)** — worst case when all elements are unique

- **Follow-up Discussion**:  
  - What if the dataset is too large to fit in memory?  
    → Discuss streaming approaches, Bloom filters, or external sorting.

---

## 🐍 Solution

See: [`solutions/contains_duplicate.py`](../../solutions/contains_duplicate.py)