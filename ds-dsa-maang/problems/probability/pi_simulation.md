# Monte Carlo π Estimation

🔗 **Source**: [Monte Carlo Method – Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)  
🏷️ **Companies**: Google, Netflix  
🔄 **Pattern**: Monte Carlo Simulation  

---

## 💡 Why It Matters for Data Scientists

Monte Carlo methods are widely used for:

- Probability estimation
- Risk modeling
- A/B test simulations
- Approximating solutions where analytical methods are hard

This problem demonstrates **random sampling for estimation**.

---

## 🧠 Interview Explanation

- **Approach**:
  1. Randomly sample points in a unit square
  2. Count points inside the quarter-circle
  3. Estimate π using the ratio

- **Time Complexity**:
  **O(n)** — number of simulations

- **Space Complexity**:
  **O(1)**

- **Follow-up Discussion**:
  - How does accuracy scale with n?
  - Where is Monte Carlo used in ML systems?

---

## 🐍 Solution

See: [`solutions/pi_simulation.py`](../../solutions/pi_simulation.py)