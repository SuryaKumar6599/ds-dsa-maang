# Scaled Dot-Product Attention

The core formula for Scaled Dot-Product Attention is the engine inside every Transformer and LLM. Here it is:
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

## Breaking it down step-by-step

   1. $QK^T$ (The Matchmaking): You multiply the Query matrix by the transpose of the Key matrix. This calculates a "similarity score" for every word against every other word. It answers: "How much should word A pay attention to word B?"
   2. $\sqrt{d_k}$ (The Scaling): We divide by the square root of the dimension of the keys ($d_k$). As dimensions get larger, dot products grow very big, which can "explode" the math. This keeps the numbers manageable and the gradients stable during training.
   3. $\text{softmax}$ (The Importance Filter): This turns those raw scores into probabilities between 0 and 1 that sum up to 1. If "it" has a 0.9 score for "animal" and 0.05 for "street," the model knows where to focus.
   4. $V$ (The Output): Finally, you multiply those probabilities by the Value matrix. This ensures the output of the formula is a weighted sum of the information you actually want to keep.

To turn a raw word into Q, K, and V, the model uses three separate "learned" weight matrices: $W^Q$, $W^K$, and $W^V$.
Think of these matrices as filters. Every word in your sentence passes through these three filters to get its specific role.

## 1. The Transformation

When a word enters the model, it is first represented as a vector (a list of numbers) called an Embedding ($x$). To get our Q, K, and V, we do simple matrix multiplication:

* $Q = x \cdot W^Q$
* $K = x \cdot W^K$
* $V = x \cdot W^V$

## 2. Why do we need the Weights ($W$)?

If we didn't have these $W$ matrices, the Query and Key for a word would be identical. That doesn't work because:

* The Query needs to represent what the word is looking for.
* The Key needs to represent what the word is.

By having separate weight matrices ($W^Q, W^K, W^V$), the model can "learn" during training how to transform the same word into three different functional versions of itself.

## 3. Training the "Knobs"

During training, the values inside $W^Q$, $W^K$, and $W^V$ are the actual "knobs" the AI adjusts.

* If the model fails to realize "it" refers to "animal," it tweaks the numbers in $W^Q$ and $W^K$ via Backpropagation.
* It keeps adjusting until the $Q$ for "it" and the $K$ for "animal" result in a high dot-product score.

In summary: The Weights are the intelligence of the model. They are the fixed rules that tell the model: "When you see an embedding like this, extract this specific info to be the Query, and that info to be the Key."
Would you like to know how Multi-Head Attention uses multiple sets of these weights at the same time?

In the context of Transformers and Large Language Models (LLMs), there are three primary "flavours" of attention you need to know. They all use the $Q, K, V$ formula, but they change where those vectors come from.

## 1. Self-Attention (The internal map)

This is what we have been discussing. Here, the Queries, Keys, and Values all come from the same sequence.

* Purpose: To understand how words within a single sentence relate to each other.
* Example: In "The cat sat on the mat," self-attention helps the word "sat" link to "cat" (who did it) and "mat" (where it happened).

## 2. Causal / Masked Self-Attention (The "No-Cheating" mode)

This is the specific type used by GPT models for text generation.

* How it works: It is exactly like self-attention, but it uses a mask to hide future words.
* Purpose: When the model is predicting the next word, it shouldn't be allowed to "look ahead" at the answer. Each word can only attend to itself and the words before it.

## 3. Cross-Attention (The bridge)

This is used in models that translate or connect two different things (like English to French or Text-to-Image). [10, 11]

* How it works: The Queries come from one sequence (e.g., the sentence being generated), but the Keys and Values come from a different sequence (e.g., the original input sentence).
* Purpose: To help one sequence "pull" information from another.
* Example: When a translation model is writing the French word "chat," it uses Cross-Attention to look back at the English word "cat" in the original text. [1, 3, 10, 12]

## Other technical variations

* Multi-Head Attention: Running several attention mechanisms in parallel so the model can focus on different aspects (like grammar and sentiment) at the same time.
* Soft vs. Hard Attention: Soft attention (most common) assigns fractional weights to everything; Hard attention picks exactly one thing to focus on and ignores the rest.
* Global vs. Local Attention: Global attention looks at the entire sequence; Local attention only looks at a small "window" of nearby words to save computational power. [7, 13, 14, 15, 16]
  