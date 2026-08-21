import pandas as pd

def rename_columns(data, rename_map):
    """
    Returns: dict mapping renamed column names to value lists
    """
    df = pd.DataFrame(data)
    return df.rename(columns=rename_map).to_dict(orient="list")
    pass