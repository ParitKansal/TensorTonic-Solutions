import pandas as pd

def cross_tab(data, row_col, col_col):
    """
    Returns: nested dict {col_value: {row_value: frequency}}
    """
    df = pd.DataFrame(data)
    return df.groupby(row_col)[col_col].value_counts().unstack().fillna(0).to_dict()