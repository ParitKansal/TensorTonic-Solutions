import pandas as pd

def unstack_to_wide(data, index_col, columns_col, values_col):
    """
    Returns: dict with index_col plus one key per unique value in columns_col
    """
    df = pd.DataFrame(data)
    return df.groupby([index_col, columns_col])[values_col].sum().unstack().reset_index(drop=False).to_dict(orient="list")
    pass