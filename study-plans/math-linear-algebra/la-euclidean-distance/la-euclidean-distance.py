import numpy as np

def euclidean_distance(x, y):
    """
    Returns: float, the Euclidean distance between x and y.
    """
    return (np.sum((np.array(x)-np.array(y))**2))**0.5