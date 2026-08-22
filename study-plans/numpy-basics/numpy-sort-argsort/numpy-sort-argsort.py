import numpy as np

def sort_with_indices(data, axis):
    """Returns: np.ndarray of shape (2, m, n), stacked sorted values and sort indices"""
    return np.array(
        [
            np.sort(np.array(data), axis=axis),
            np.argsort(np.array(data), axis=axis)
        ]
    )