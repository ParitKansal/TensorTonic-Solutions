import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    data = np.array(data, dtype="float64")
    return np.array([np.array(data>threshold, dtype = "float64"),
                     [x if np.any(x > threshold) else np.zeros(x.shape) for x in data],
                     [x if np.all(x > threshold) else np.zeros(x.shape) for x in data]
                    ]) 