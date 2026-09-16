import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
raw_file = BASE_DIR / "data" / "raw" / "orders.csv"
processed_file = BASE_DIR / "data" / "processed" / "orders_clean.csv"


df = pd.read_csv(raw_file)
df = df[(df["price"] >= 0) & (df["quantity"] > 0)]
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

df["order_id"].notna()

processed_file.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(processed_file, index=False)

