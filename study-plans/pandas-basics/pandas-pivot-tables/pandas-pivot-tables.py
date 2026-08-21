import pandas as pd

def create_pivot(data, index, columns, values, aggfunc):
    """
    Returns: nested dict {column_value: {index_value: agg_result}}
    """
    df = pd.DataFrame(data)
    return df.groupby([index, columns])[values].agg(aggfunc).unstack().fillna(0).to_dict()