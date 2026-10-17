import pandas as pd
from faker import Faker
import random
from pathlib import Path


fake = Faker()

Faker.seed(42)
random.seed(42)


categories = [
    "Electronics",
    "Clothing",
    "Home & Kitchen",
    "Books",
    "Beauty"
]


def generate_orders(row_count=10000):
    data = []

    duplicate_order_ids = [
        f"ORD-{i:06d}"
        for i in range(1, 2001)
    ]

    for i in range(row_count):

   
        if random.random() < 0.05:
            order_id = random.choice(duplicate_order_ids)
        else:
            order_id = f"ORD-{i + 2001:06d}"

        if random.random() < 0.2:
            customer_name = f"  {fake.name()}  "
        else:
            customer_name = fake.name()

    
        category = random.choice(categories)

    
        price_val = round(random.uniform(10, 1000), 2)

    
        if random.random() < 0.3:
            price = f"${price_val}"
        else:
            price = str(price_val)

    
        if random.random() < 0.02:
            quantity = random.choice([-1, 0])
        else:
            quantity = random.randint(1, 5)

    
        order_date = fake.date_between(
            start_date="-180d",
            end_date="today"
        )

        data.append([
            order_id,
            customer_name,
            category,
            price,
            quantity,
            order_date
        ])


    return pd.DataFrame(
        data,
        columns=[
            "order_id",
            "customer_name",
            "product_category",
            "price",
            "quantity",
            "order_date"
        ]
    )


def main():
    base_dir = Path(__file__).resolve().parent
    output_file = base_dir / "data" / "raw" / "orders.csv"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    df_raw = generate_orders()
    df_raw.to_csv(output_file, index=False)

    print(f"File: {output_file}")
    print(f"Số dòng: {len(df_raw)}")
    print(f"Số cột: {len(df_raw.columns)}")


if __name__ == "__main__":
    main()