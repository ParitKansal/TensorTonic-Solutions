import numpy as np

def linear_regression(X, y, lr, epochs):
    """
    Returns: tuple (weights, bias)
    """
    X = np.array(X)
    X = np.hstack((np.ones((X.shape[0], 1)), X))
    Y = np.array(y)[:, None]
    W = np.zeros((X.shape[1], 1), dtype = "float64")
    for epoch in range(epochs):
        W = W - (lr/X.shape[0])*(-2*X.T@Y+2*X.T@X@W)
    return (np.round(np.reshape(W[1:], shape=(-1)), 4), np.round(W[0][0], 4))