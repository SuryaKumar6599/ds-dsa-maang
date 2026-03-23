# Random Pick Index

🔗 **Source**: [LeetCode #398](https://leetcode.com/problems/random-pick-index/)  
🏷️ **Companies**: Google  
🔄 **Pattern**: Reservoir Sampling / Probability  

---

## 💡 Why It Matters for Data Scientists

Random sampling is critical when working with:

- Large datasets that cannot fit into memory
- Streaming data pipelines
- Online experimentation and A/B testing
- Fair selection of samples from logs

This problem demonstrates **reservoir sampling**, a core concept in scalable data processing.

---

## 🧠 Interview Explanation

- **Approach**:  
  Use reservoir sampling (k = 1).  
  For every occurrence of the target, replace the previously chosen index with probability `1 / count`.

- **Why It Works**:  
  Ensures **uniform probability** across all valid indices without storing them.

- **Time Complexity**:  
  **O(n)** per `pick()` call

- **Space Complexity**:  
  **O(1)** — no additional storage

- **Follow-up Discussion**:  
  - How would you extend this to sample `k` indices?
  - How does this differ from random sampling with replacement?

---

## 🐍 Solution

See: [`solutions/random_pick_index.py`](../../solutions/random_pick_index.py)