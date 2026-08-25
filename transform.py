import pandas as pd
from extract import extract

def transform(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out.columns = [c.strip().lower().replace(" ", "_") for c in out.columns]
    out = out.drop_duplicates()
    return out

if __name__ == "__main__":
    df = extract()
    cleaned = transform(df)
    print(cleaned.head())
