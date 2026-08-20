import pandas as pd

def data_types_overview(data):
    """
    Returns: dict with 'dtypes', 'type_counts', 'num_columns'
    """
    df = pd.DataFrame(data)
    result =  {
        "dtypes": {
            x: str(y) for x, y in zip(list(df.columns), list(df.dtypes))
        },
        "num_columns": len(df.columns),
    }
    temp = {}
    list(df.dtypes)
    for x in list(df.dtypes):
        temp[str(x)] = temp.get(str(x), 0) + 1
    result['type_counts'] = temp
    return result