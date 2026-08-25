import pandas as pd
from extract import extract
from transform import transform

def validate(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("Dataset is empty.")
    duplicate_rows = int(df.duplicated().sum())
    missing = df.isna().sum().sort_values(ascending=False)
    print(f"Duplicate rows: {duplicate_rows}")
    print("Missing values by column:")
    print(missing[missing > 0])

if __name__ == "__main__":
    validate(transform(extract()))
