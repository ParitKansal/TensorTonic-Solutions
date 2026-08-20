import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """

    try:
        x = np.array(matrix, dtype=float)
        if x.ndim != 2:
            return None

        if norm_type == "l2":
            norm = np.sqrt(np.sum(x**2, axis=axis, keepdims=True))
        elif norm_type == "l1":
            norm = np.sum(np.abs(x), axis=axis, keepdims=True)
        elif norm_type == "max":
            norm = np.max(np.abs(x), axis=axis, keepdims=True)
        else:
            return None
        norm = np.where(norm == 0, 1, norm)

        return x / norm

    except:
        return None