import pandas as pd

def groupby_basics(data, group_col, value_col):
    """
    Returns: dict with 'sum', 'mean', 'count' (each a dict)
    """
    df = pd.DataFrame(data)
    return {
        "sum": df.groupby(group_col)[value_col].sum().to_dict(),
        "mean": df.groupby(group_col)[value_col].mean().to_dict(),
        "count": df.groupby(group_col)[value_col].count().to_dict()

    }