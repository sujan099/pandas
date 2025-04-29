import numpy as np

def percentile_scaling(data):
    """
    Scales numeric data based on percentile rank (0 to 100).

    Args:
        data (list or np.array): List or array of numeric data.

    Returns:
        list: Percentile rank scaled values.
    """
    data = np.array(data)
    min_val = np.min(data)
    max_val = np.max(data)
    if max_val == min_val:
        raise ValueError("Cannot scale data with identical values.")

    scaled = 100 * (data - min_val) / (max_val - min_val)
    return scaled.tolist()
