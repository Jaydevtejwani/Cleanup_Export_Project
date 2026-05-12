import pandas as pd

def load_excel(path):
    df = pd.read_excel(path, dtype=str)
    df.columns = df.columns.str.strip()
    df = df.fillna("")
    return df