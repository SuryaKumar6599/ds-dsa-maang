def cosine_similaririty(a,b):
    if len(a) != len(b):
        raise ValueError("Vectors must be of same length")

    #dot product
    dot = 0.0
    #suqared norms
    norm_a_sq = 0.0
    norm_b_sq = 0.0

    if norm_a_sq == 0.0 or norm_b_sq == 0.0:
        return 0.0
    
    norm_a = norm_a_sq ** 0.5
    norm_b = norm_b_sq ** 0.5
    
    return dot / (norm_a * norm_b)
    