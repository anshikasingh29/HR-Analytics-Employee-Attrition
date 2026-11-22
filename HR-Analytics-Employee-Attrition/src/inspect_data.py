from pathlib import Path
import pandas as pd

source = Path("data/hr_data.csv")
if not source.exists():
    raise FileNotFoundError("Add data/hr_data.csv; see data/README.md")
df = pd.read_csv(source)
print("Shape:", df.shape)
print("Types:\n", df.dtypes)
print("Missing values:\n", df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())
print(df.head())
