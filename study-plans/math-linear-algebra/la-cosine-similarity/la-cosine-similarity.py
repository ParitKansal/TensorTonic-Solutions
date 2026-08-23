import numpy as np

def cosine_similarity(a, b):
    """
    Returns: float in [-1, 1], cosine similarity between a and b.
    """
    x = np.array(a)
    y = np.array(b)
    dot_ = np.dot(x, y)
    if dot_ == 0:
        return 0;
    return dot_/(((np.sum(x**2))**0.5)*((np.sum(y**2))**0.5))