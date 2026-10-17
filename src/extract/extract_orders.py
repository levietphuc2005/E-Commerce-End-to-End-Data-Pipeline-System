from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
RAW_FILE = BASE_DIR / "data" / "raw" / "orders.csv"


def extract_orders(file_path=RAW_FILE):
	"""Read raw orders from the source CSV without changing their values."""
	if not file_path.exists():
		raise FileNotFoundError(f"Raw orders file not found: {file_path}")

	return pd.read_csv(file_path)


if __name__ == "__main__":
	raw_orders = extract_orders()
	print(f"File: {RAW_FILE}")
	print(f"Số dòng: {len(raw_orders)}")
	print(f"Số cột: {len(raw_orders.columns)}")
