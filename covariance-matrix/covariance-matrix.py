import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    x = np.array(X)
    mu = np.mean(x, axis = 0)
    x_center = x - mu
    if(len(x.shape) <= 1):
        return None
    N = len(X)
    if N <= 1:
        return None
    return np.dot(np.transpose(x_center),x_center)/(N-1)