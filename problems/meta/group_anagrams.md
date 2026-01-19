# Group Anagrams

🔗 **Source**: [LeetCode #49](https://leetcode.com/problems/group-anagrams/)  
🏷️ **Companies**: Meta (Facebook), Amazon  
🔄 **Pattern**: Hashing / String Normalization  

---

## 💡 Why It Matters for Data Scientists

This problem maps directly to:

- Text normalization in NLP
- Grouping semantically equivalent records
- Canonicalization of categorical features
- Clustering based on invariant representations

It demonstrates how **normalization enables grouping**.

---

## 🧠 Interview Explanation

- **Approach**:  
  Normalize each word by sorting characters (or using frequency counts).  
  Use the normalized form as a hash key.

- **Key Insight**:  
  Different permutations can map to the same canonical representation.

- **Time Complexity**:  
  **O(n · k log k)** — n words of length k (sorting-based)

- **Space Complexity**:  
  **O(n · k)** — storing grouped words

- **Follow-up Discussion**:  
  - How would you avoid sorting?
  - How does this scale for large vocabularies?

---

## 🐍 Solution

See: [`solutions/group_anagrams.py`](../../solutions/group_anagrams.py)