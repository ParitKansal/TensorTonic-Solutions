import pandas as pd

def replace_values(data, column, old_val, new_val):
    """
    Returns: dict with 'data' (dict) and 'count' (int)
    """
    temp = data[column]
    count = sum(x == old_val for x in temp)
    temp = [new_val if x == old_val else x for x in temp]
    data[column] = temp
    return {
        "data": data,
        "count": count
    }