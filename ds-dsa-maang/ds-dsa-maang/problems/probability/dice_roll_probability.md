# Dice Roll Probability

🔗 **Source**: [Dice Probability – Wikipedia](https://en.wikipedia.org/wiki/Dice#Probability)  
🏷️ **Companies**: Facebook, Amazon  
🔄 **Pattern**: Simulation / Discrete Probability  

---

## 💡 Why It Matters for Data Scientists

This problem models:

- Discrete probability distributions
- Simulation vs analytical solutions
- Validation of theoretical assumptions
- Experiment outcome modeling

It directly relates to **A/B testing and probabilistic reasoning**.

---

## 🧠 Interview Explanation

- **Approach**:
  Simulate dice rolls multiple times and compute the frequency of outcomes  
  (or derive probabilities analytically)

- **Time Complexity**:
  **O(n)** — number of simulations

- **Space Complexity**:
  **O(1)**

- **Follow-up Discussion**:
  - How would you generalize to biased dice?
  - When is simulation preferred over closed-form solutions?

---

## 🐍 Solution

See: [`solutions/dice_roll_probability.py`](../../solutions/dice_roll_probability.py)