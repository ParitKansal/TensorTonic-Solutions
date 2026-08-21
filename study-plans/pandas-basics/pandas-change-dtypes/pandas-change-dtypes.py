import pandas as pd

def change_dtype(data, column, target_type):
    """
    Returns: list [dtypes_before, dtypes_after] (both dicts)
    """
    df = pd.DataFrame(data)
    df_copy = df.copy()
    df_copy[column] = df_copy[column].astype(target_type)
    return [
        {
            col: str(df[col].dtype) for col in df.columns
        },
        {
            col: str(df_copy[col].dtype) for col in df_copy.columns
        }
        
    ]