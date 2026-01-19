# Longest Substring Without Repeating Characters

🔗 **Source**: [LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  
🏷️ **Companies**: Google, Amazon, Microsoft  
🔄 **Pattern**: Sliding Window  

---

## 💡 Why It Matters for Data Scientists

This pattern is widely applicable in:

- Streaming text analytics
- Session-level uniqueness constraints
- NLP preprocessing
- Sliding-window feature extraction

It demonstrates how to **optimize subarray problems** efficiently.

---

## 🧠 Interview Explanation

- **Approach**:  
  Use a sliding window with two pointers and a set/map to track seen characters.

- **Key Insight**:  
  Each character enters and exits the window once → linear time.

- **Time Complexity**:  
  **O(n)**

- **Space Complexity**:  
  **O(k)** where k is the character set size

- **Follow-up Discussion**:  
  - What if the input is a stream?
  - How does this change for Unicode characters?

---

## 🐍 Solution

See: [`solutions/longest_substring_without_repeating_characters.py`](../../solutions/longest_substring_without_repeating_characters.py)