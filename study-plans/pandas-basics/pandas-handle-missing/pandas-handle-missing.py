import pandas as pd

def handle_missing(data, fill_value):
    """
    Returns: dict with 'null_counts' (dict) and 'cleaned_data' (dict)
    """
    df = pd.DataFrame(data)
    return {
        "null_counts": {col : int(sum(df[col].isna())) for col in df.columns},
        "cleaned_data": df.fillna(fill_value).to_dict(orient="list")
    }
    pass