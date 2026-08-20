import pandas as pd

def head_tail(data, n):
    """
    Returns: dict with 'head' and 'tail' (both dicts of column -> list)
    """
    df = pd.DataFrame(data)
    tail = df.tail(n)
    head = df.head(n)
    tail_ = {
        str(x): list(tail[x]) for x in list(tail.columns)
    }
    head_ = {
        str(x): list(head[x]) for x in list(head.columns)
    }
    return {
        "tail": tail_,
        "head": head_
    }