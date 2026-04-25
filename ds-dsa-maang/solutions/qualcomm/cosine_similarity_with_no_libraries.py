import numpy as np

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    
    # Edge case: Zero vector returns 0.0 (or NaN handling based on spec)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)

# 🚀 Follow-up: Batch Cosine Similarity
def batch_cosine_similarity(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    # A: (N, D), B: (M, D) -> Result: (N, M)
    dot_products = np.dot(A, B.T)
    norm_A = np.linalg.norm(A, axis=1, keepdims=True)  # (N, 1)
    norm_B = np.linalg.norm(B, axis=1, keepdims=True).T  # (1, M)
    
    # Broadcasting division
    norms = norm_A * norm_B
    # Avoid division by zero
    norms[norms == 0] = 1e-9
    return dot_products / norms