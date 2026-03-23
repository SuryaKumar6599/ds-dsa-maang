# Valid Anagram

🔗 **Source**: [LeetCode #242](https://leetcode.com/problems/valid-anagram/)  
🏷️ **Companies**: Meta (Facebook), Amazon  
🔄 **Pattern**: Frequency Count  

---

## 💡 Why It Matters for Data Scientists

This problem is relevant to:

- Text preprocessing and NLP pipelines
- Data consistency checks
- Feature validation for categorical text data
- Duplicate detection with permutation tolerance

It emphasizes **frequency-based comparison**.

---

## 🧠 Interview Explanation

- **Approach**:  
  Count character frequencies for both strings and compare.

- **Key Insight**:  
  Anagrams share identical frequency distributions.

- **Time Complexity**:  
  **O(n)**

- **Space Complexity**:  
  **O(1)** for fixed alphabet (or O(n) otherwise)

- **Follow-up Discussion**:  
  - How would this change for Unicode?
  - Can this be optimized for streaming input?

---

## 🐍 Solution

See: [`solutions/valid_anagram.py`](../../solutions/valid_anagram.py)