import numpy as np

def row_extremes(data):
    """Returns: np.ndarray of shape (4, m), rows are max_val, max_col, min_val, min_col"""
    temp1 = np.array(data, dtype="float64")
    max_ = np.argmax(temp1, axis=1)
    min_ = np.argmin(temp1, axis=1)
    max_values = [y[x] for x, y in zip(max_, temp1)]
    min_values = [y[x] for x, y in zip(min_, temp1)]
    return np.array(
        [
            max_values,
            max_,
            min_values,
            min_
        ]
    )
    