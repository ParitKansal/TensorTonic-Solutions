import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)
    filtered_data = df[df[column] > threshold]
    filtered_data_ = {
        col: list(filtered_data[col]) for col in filtered_data.columns
    }
    return {
        "filtered_data" : filtered_data_,
        "count": len(filtered_data)
    }