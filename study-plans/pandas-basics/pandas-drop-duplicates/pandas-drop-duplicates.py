import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    df = pd.DataFrame(data)
    temp = df.drop_duplicates()
    return [
        len(df),
        len(temp),
        temp.to_dict(orient="list")
    ]
    pass