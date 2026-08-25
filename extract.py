from pathlib import Path
import pandas as pd

INPUT_PATH = Path("data/sample_input.csv")

def extract(path=INPUT_PATH):
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    df = pd.read_csv(path)
    print(f"Extracted {len(df):,} rows and {len(df.columns)} columns")
    return df

if __name__ == "__main__":
    extract()
