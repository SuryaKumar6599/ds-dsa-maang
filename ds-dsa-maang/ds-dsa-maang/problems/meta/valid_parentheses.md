# Valid Parentheses

🔗 **Source**: [LeetCode #20](https://leetcode.com/problems/valid-parentheses/)  
🏷️ **Companies**: Meta (Facebook), Google  
🔄 **Pattern**: Stack  

---

## 💡 Why It Matters for Data Scientists

This problem reflects **structured validation tasks** such as:

- Validating mathematical or logical expressions
- Parsing queries, JSON, or configuration files
- Ensuring syntactic correctness in rule-based systems
- Preprocessing inputs before downstream analysis

It tests your ability to **model nested structure validation**.

---

## 🧠 Interview Explanation

- **Approach**:  
  Use a stack to track opening brackets.  
  For each closing bracket, ensure it matches the most recent opening bracket.

- **Key Insight**:  
  Stack naturally represents nested structures (LIFO).

- **Time Complexity**:  
  **O(n)** — single pass through the string

- **Space Complexity**:  
  **O(n)** — stack in worst case

- **Follow-up Discussion**:  
  - How would you validate HTML/XML tags?
  - What if brackets are streamed one by one?

---

## 🐍 Solution

See: [`solutions/valid_parentheses.py`](../../solutions/valid_parentheses.py)