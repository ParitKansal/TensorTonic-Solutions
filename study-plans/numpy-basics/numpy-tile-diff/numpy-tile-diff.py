import numpy as np

def tile_diff(data, reps):
    """Returns: np.ndarray of shape (2, m*reps, n), stacked tiled array and padded differences"""
    temp1 = np.array([x for x in data]*reps)
    temp2 = np.array([temp1[i] - temp1[i-1] for i in range(1, len(temp1))])
    temp3 = [x for x in temp2] + [np.zeros(temp2[0].shape)]
    return np.array(
        [temp1, temp3]
    )