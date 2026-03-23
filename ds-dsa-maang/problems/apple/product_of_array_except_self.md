# Product of Array Except Self

🔗 **Source**: [LeetCode #238](https://leetcode.com/problems/product-of-array-except-self/)  
🏷️ **Companies**: Apple, Google  
🔄 **Pattern**: Prefix / Suffix  

---

## 💡 Why It Matters for Data Scientists

This problem illustrates:

- Feature contribution analysis
- Efficient aggregation without division
- Prefix/suffix transformations in arrays
- Memory-efficient computation patterns

It is a classic example of **avoiding redundant computation**.

---

## 🧠 Interview Explanation

- **Approach**:  
  Build prefix products in a forward pass.  
  Multiply with suffix products in a backward pass.

- **Key Insight**:  
  Each element’s result = product of everything before × after.

- **Time Complexity**:  
  **O(n)**

- **Space Complexity**:  
  **O(1)** extra (excluding output array)

- **Follow-up Discussion**:  
  - How do zeros affect the result?
  - Can this be parallelized?

---

## 🐍 Solution

See: [`solutions/product_of_array_except_self.py`](../../solutions/product_of_array_except_self.py)