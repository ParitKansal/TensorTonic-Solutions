import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    dfs_ = [pd.DataFrame(df) for df in dfs]
    df = pd.concat(dfs_).reset_index(drop=True)
    return [
        list(df.shape),
        df.to_dict(orient = "list")
    ]
    pass