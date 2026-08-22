import numpy as np

def reshape_array(data, operation):
    """
    Returns: ndarray of float64 with shape determined by the operation
    """
    if operation == "flatten":
        return np.array(data, dtype="float64").flatten()
    if operation == "transpose":
        return np.array(data, dtype="float64").transpose()
    return np.array([data], dtype="float64")
