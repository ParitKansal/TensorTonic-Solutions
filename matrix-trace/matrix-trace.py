import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    x = np.array(A)
    temp = 0
    for i in range(x.shape[0]):
        temp += x[i][i]
    return float(temp)
