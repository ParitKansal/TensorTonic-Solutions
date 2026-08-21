import pandas as pd

def select_columns(data, columns):
    """
    Returns: dict mapping selected column names to value lists
    """
    df = pd.DataFrame(data)
    df = df[columns]
    return {
        col:list(df[col]) for col in df.columns
    }