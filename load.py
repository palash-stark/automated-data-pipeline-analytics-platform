from pathlib import Path
from extract import extract
from transform import transform
from validate import validate

OUTPUT_PATH = Path("data/processed/output.parquet")

def load():
    df = transform(extract())
    validate(df)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(OUTPUT_PATH, index=False)
    print(f"Saved processed data to {OUTPUT_PATH}")

if __name__ == "__main__":
    load()
