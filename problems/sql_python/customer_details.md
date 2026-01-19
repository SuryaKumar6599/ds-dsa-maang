# Customer Details

🔗 **Source**: [StrataScratch #9891](https://platform.stratascratch.com/coding/9891-customer-details)  
🏷️ **Companies**: Amazon  
🔄 **Pattern**: Left Join + Sorting  

---

## 💡 Why It Matters for Data Scientists

This task reflects **classic data integration problems**:

- Joining customer and transaction data
- Preserving records with missing relationships
- Preparing data for reporting or dashboards
- Handling sparse or incomplete datasets

---

## 🧠 Interview Explanation

- **Approach**:
  1. Perform a left join between customers and orders
  2. Ensure customers without orders are retained
  3. Sort results by relevant fields

- **Time Complexity**:
  **O(n log n)** — join + sorting

- **Space Complexity**:
  **O(n)**

- **Follow-up Discussion**:
  - How would you optimize for very large tables?
  - What if there are duplicate orders?

---

## 🐍 Solution

See: [`solutions/customer_details.py`](../../solutions/customer_details.py)