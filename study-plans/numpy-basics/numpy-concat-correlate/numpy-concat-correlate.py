import numpy as np

def compare_correlations(a, b):
    """Returns: np.ndarray of shape (3, n, n), stacked correlation matrices"""
    return np.array([
        np.corrcoef(np.array(a).T),
        np.corrcoef(np.array(b).T),
        np.corrcoef(np.array(a+b).T)
    ]
    )