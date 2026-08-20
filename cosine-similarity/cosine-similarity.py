import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    a_ = (np.sum(a**2))**0.5
    b_ = (np.sum(b**2))**0.5
    if a_ == 0:
        return 0
    if b_ == 0:
        return 0
    return float(np.sum(a*b)/(a_*b_))