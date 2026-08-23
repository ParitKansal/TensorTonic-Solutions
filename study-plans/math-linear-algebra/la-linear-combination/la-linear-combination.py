import numpy as np

def linear_combination(vectors, coefficients):
    """
    Returns: float64 array, the weighted sum of vectors.
    """
    vectors = np.array(vectors)
    
    result = np.zeros(vectors[0].shape)
    for c, v in zip(coefficients, vectors):
        result += c*v
    return result