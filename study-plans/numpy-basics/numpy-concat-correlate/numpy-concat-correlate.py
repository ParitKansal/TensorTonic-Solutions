import numpy as np
def fun(A):
    X = A - A.mean(axis=0)
    C = X.T @ X / (len(X) - 1)
    std = np.sqrt(np.diag(C))
    std_ = std[:, None]@std[None, :]
    return C/std_
def compare_correlations(a, b):
    """Returns: np.ndarray of shape (3, n, n), stacked correlation matrices"""
    return np.array([
        fun(np.array(a)),
        fun(np.array(b)),
        fun(np.array(a+b))
    ]
    )