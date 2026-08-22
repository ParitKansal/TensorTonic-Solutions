import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    data = np.array(data, dtype = "float64")
    return np.array(
        [
            data[row_idx],
            np.minimum(np.maximum(data[row_idx], lo), hi)
        ]
    )