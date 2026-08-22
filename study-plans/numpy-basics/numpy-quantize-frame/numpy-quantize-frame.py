import numpy as np

def quantize_and_frame(data, decimals, pad_width):
    """Returns: np.ndarray of shape (3, m+2p, n+2p), stacked rounded, floored, ceiled with zero-padding"""
    pass
    data = np.array(data)
    result1 = np.zeros((data.shape[0] + 2 * pad_width, data.shape[1] + 2 * pad_width))
    result1[pad_width: data.shape[0] + pad_width, pad_width: data.shape[1] + pad_width] = np.round(data, decimals)
    result2 = np.zeros((data.shape[0] + 2 * pad_width, data.shape[1] + 2 * pad_width))
    result2[pad_width: data.shape[0] + pad_width, pad_width: data.shape[1] + pad_width] = np.floor(data)
    result3 = np.zeros((data.shape[0] + 2 * pad_width, data.shape[1] + 2 * pad_width))
    result3[pad_width: data.shape[0] + pad_width, pad_width: data.shape[1] + pad_width] = np.ceil(data)
    return np.array(
        [
            result1,
            result2,
            result3
        ]
    )
    