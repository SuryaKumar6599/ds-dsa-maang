# User Feature Completion

🔗 **Source**: [StrataScratch #9792](https://platform.stratascratch.com/coding/9792-user-feature-completion)  
🏷️ **Companies**: Meta  
🔄 **Pattern**: Join + GroupBy  

---

## 💡 Why It Matters for Data Scientists

This problem mirrors **real analytics workflows**:

- Measuring feature adoption and completion rates
- User funnel analysis
- Product analytics and growth metrics
- Experiment analysis (drop-off at each step)

It closely resembles **SQL + Pandas interview tasks** for DS roles.

---

## 🧠 Interview Explanation

- **Approach**:
  1. Identify the maximum step completed by each user per feature
  2. Join with the feature table to get total steps
  3. Compute completion percentage
  4. Aggregate results per feature

- **Time Complexity**:
  **O(n)** — grouping and joins

- **Space Complexity**:
  **O(n)** — intermediate tables

- **Follow-up Discussion**:
  - How would you handle missing steps?
  - How would you compute completion over time?

---

## 🐍 Solution

See: [`solutions/user_feature_completion.py`](../../solutions/user_feature_completion.py)