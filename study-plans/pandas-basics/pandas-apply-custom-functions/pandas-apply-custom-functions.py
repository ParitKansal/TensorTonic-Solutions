import pandas as pd

def apply_transform(data, column, operation):
    """
    Returns: dict with original columns plus val_transformed
    """
    df = pd.DataFrame(data)

    if operation == "normalize":
        df[f"{column}_transformed"] = (
            (df[column] - df[column].min()) /
            (df[column].max() - df[column].min())
        ).round(4)

    elif operation == "rank":
        df[f"{column}_transformed"] = df[column].rank()

    elif operation == "cumsum":
        df[f"{column}_transformed"] = df[column].cumsum()

    elif operation == "double":
        df[f"{column}_transformed"] = df[column] * 2

    return df.to_dict(orient="list")