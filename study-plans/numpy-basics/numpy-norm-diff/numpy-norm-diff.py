import numpy as np

def norm_diff(a, b, lo, hi):
    """Returns: np.ndarray of absolute differences after clipping and rescaling to [0, 1]"""
    a_clip = np.maximum(np.minimum(np.array(a, dtype="float64"), hi), lo)
    a_scale = (a_clip - lo)/(hi - lo)
    b_clip = np.maximum(np.minimum(np.array(b, dtype="float64"), hi), lo)
    b_scale = (b_clip - lo)/(hi - lo)
    return np.abs(a_scale-b_scale)
