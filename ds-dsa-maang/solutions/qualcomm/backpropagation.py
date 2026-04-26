# Dense Layer Forward & Backward
def dense_forward(X, W, B):
    out = X @ W + B
    cache = (X, out)
    return out, cache

def dense_backward(d_out, cache):
    X, out = cache
    # dL/dW = X.T @ dL/dY
    dW = X.T @ d_out
    # dL/dB = sum(dL/dY, axis=0)
    dB = np.sum(d_out, axis=0, keepdims=True)
    # dL/dX = dL/dY @ W.T
    dX = d_out @ cache[1].W.T  # Assuming W stored in cache
    return dX, dW, dB

