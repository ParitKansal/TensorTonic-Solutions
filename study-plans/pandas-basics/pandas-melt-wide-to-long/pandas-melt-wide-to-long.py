import pandas as pd

def melt_dataframe(data, id_vars, value_vars):
    df = pd.DataFrame(data).set_index(id_vars)

    out = pd.concat(
        [df[[v]].rename(columns={v: "value"}) for v in value_vars]
    ).reset_index()

    out["variable"] = [
        v
        for v in value_vars
        for _ in range(len(df))
    ]

    return out[id_vars + ["variable", "value"]].to_dict(orient="list")