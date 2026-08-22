import numpy as np

def norm_gate(X, W, threshold):
    """Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed"""
    temp = np.array(X)@np.array(W)
    temp1 = (np.sum(temp**2, axis=1)[:, None])**0.5 >= threshold
    return temp*temp1