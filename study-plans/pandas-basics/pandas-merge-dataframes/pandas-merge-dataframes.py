import pandas as pd

def merge_dataframes(left, right, on, how):
    """
    Returns: dict of column to value lists
    """
    df1 = pd.DataFrame(left)
    df2 = pd.DataFrame(right)
    return df1.merge(df2, on = on , how = how).to_dict(orient = "list")