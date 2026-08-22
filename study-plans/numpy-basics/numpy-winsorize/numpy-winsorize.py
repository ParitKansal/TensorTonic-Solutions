import numpy as np

def winsorize(data, lo_q, hi_q):
    """Returns: np.ndarray of shape (3, m, n), stacked clipped values, lo_mask, hi_mask"""
    temp1 = np.array(data)
    lower_ = np.quantile(temp1, lo_q/100, axis = 0)
    upper_ = np.quantile(temp1, hi_q/100, axis = 0)

    result1 = np.clip(
            temp1,
            lower_,
            upper_
        )
    result2 = np.array(temp1 < lower_, dtype="float64")
    result3 = np.array(temp1 > upper_, dtype="float64")
    return np.array(
        [
            result1,
            result2,
            result3
        ]
    )