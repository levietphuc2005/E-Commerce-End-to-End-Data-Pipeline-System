import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
raw_file = BASE_DIR / "data" / "raw" / "orders.csv"
processed_file = BASE_DIR / "data" / "processed" / "orders_clean.csv"

df = pd.read_csv(raw_file)

df["customer_name"] = (
    df["customer_name"]
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
    .str.title()
)
df["product_category"] = df["product_category"].str.strip().str.title()
df["price"] = pd.to_numeric(
    df["price"].astype(str).str.replace("$", "", regex=False).str.strip(),
    errors="coerce",
)
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

df = df.drop_duplicates(subset=["order_id"])
df = df.dropna(subset=["order_id", "customer_name", "price", "quantity", "order_date"])


processed_file.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(processed_file, index=False)


