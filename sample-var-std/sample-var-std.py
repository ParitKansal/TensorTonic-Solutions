import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.array(x)
    mean = np.mean(x)
    n = np.shape(x)[0]
    var = np.sum(((x-mean)**2))/(n-1)
    return (var, var**0.5)