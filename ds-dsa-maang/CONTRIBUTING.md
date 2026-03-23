# Contributing to ds-dsa-maang

Thank you for your interest in contributing to **ds-dsa-maang** 🎉  
This repository exists to help **Data Scientists crack MAANG / product-company interviews** with high-quality, practical DSA problems and solutions.

We welcome thoughtful contributions that **maintain quality, clarity, and relevance**.

---

## 🧭 Contribution Philosophy

This is **not** a generic DSA repository.

Please contribute only if the problem or improvement:
- Is **relevant to Data Scientist interviews**
- Reflects **real-world data problems**
- Avoids unnecessary algorithmic complexity
- Can be explained clearly in a DS interview context

---

## 📁 Repository Structure (Must Follow)

```
ds-dsa-maang/
├── problems/{company}/{problem}.md
├── solutions/{problem}.py
├── patterns/{pattern}.md
```

---

## 🧾 How to Add a New Problem

### 1️⃣ Choose the Right Problem

Ensure the problem:
- Appears in DS interviews (screening / mid-round)
- Uses patterns like hashing, sliding window, heap, simulation, SQL-style logic
- Is **NOT** advanced graph theory or complex DP

---

### 2️⃣ Add the Problem Markdown

Create a file at:

```
problems/{company}/{problem_name}.md
```

Use the standard template:

```markdown
# Problem Title

🔗 **Source**: [Platform + Problem Link]  
🏷️ **Companies**: Google, Amazon, Meta  
🔄 **Pattern**: Sliding Window / Hashing / Heap  

## 💡 Why It Matters for Data Scientists
Explain real-world relevance (data cleaning, streaming, aggregation, etc.)

## 🧠 Interview Explanation
- **Approach**
- **Time Complexity**
- **Space Complexity**
- **Follow-up discussion**

## 🐍 Solution
See: [`solutions/problem_name.py`](../../solutions/problem_name.py)
```

---

### 3️⃣ Add the Python Solution

Create a file at:

```
solutions/problem_name.py
```

#### ✅ Solution Standards
- Python **only**
- Use **type hints**
- Clear **docstring**
- No LeetCode boilerplate
- Include simple `assert` tests or example usage

Example:

```python
from typing import List

def example_function(nums: List[int]) -> int:
    ...
```

---

## 🧠 Adding Pattern Documentation

If introducing a **new pattern**, add a markdown file under:

```
patterns/{pattern_name}.md
```

Explain:
- When to use the pattern
- Core idea
- Time/space trade-offs
- Common DS use cases

---

## ❌ What Not to Add

Please **do not** add:
- Hard dynamic programming problems
- Graph traversal problems (DFS/BFS-heavy)
- Competitive programming tricks
- Copy-pasted LeetCode editorial text
- Low-effort or unexplained code

---

## 🔍 Review Process

All contributions are reviewed for:
- Correctness
- Clarity
- Data Science relevance
- Code quality

Maintainers may request changes before merging.

---

## 🤝 Community Guidelines

- Be respectful and professional
- Give constructive feedback
- Follow the Code of Conduct
- Help others learn

---

## 🙌 Thank You

Your contributions help make **ds-dsa-maang** a **high-signal resource for Data Scientists worldwide**.

Happy contributing 🚀