import numpy as np

def vector_norms(v):
    """
    Returns: float64 array of shape (3,) containing [L1, L2, L-inf] norms.
    """
    x = np.array(v)
    return np.array(
        [
            np.sum(np.abs(x)),
            (np.sum(x**2))**0.5,
            np.max(np.abs(x))
        ]
    )