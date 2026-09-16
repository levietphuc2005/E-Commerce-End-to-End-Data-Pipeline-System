# E-Commerce End-to-End Data Pipeline System

## 1. Project Overview
This project builds an end-to-end data pipeline for e-commerce sales data. It simulates a real-world ETL process where raw order data is extracted, cleaned, validated, transformed, and loaded into a MySQL data warehouse for downstream analytics.

The project is designed to demonstrate core data engineering concepts such as:
- raw data ingestion
- data quality checks
- transformation logic
- staging and warehouse modeling
- SQL-based analytical database design

## 2. Architecture

```text
E-Commerce End-to-End Data Pipeline System/
├── data/
│   ├── raw/
│   │   └── orders.csv
│   └── processed/
│       └── orders_clean.csv
├── src/
│   ├── config/
│   │   └── database.py
│   ├── extract/
│   │   └── extract_orders.csv
│   ├── load/
│   │   └── load_to_mysql.py
│   └── tranform/
│       ├── clean_orders.py
│       ├── tranform_orders.py
│       └── vadiate_orders.py
├── sql/
│   ├── staging/
│   │   └── creating_staging_orders.sql
│   └── warehouse/
│       ├── create_dim_customers.sql
│       ├── create_dim_date.sql
│       ├── create_dim_product.sql
│       └── create_fact_orders.sql
├── tests/
│   └── test_orders.py
├── logs/
├── etl_pipeline.py
├── requirement.txt
├── README.md
└── .gitignore
```

## 3. Technologies
- Python
- Pandas
- NumPy
- Faker
- SQLAlchemy
- PyMySQL
- MySQL
- SQL scripts for staging and warehouse layers

## 4. Data Source
The raw data is generated from synthetic e-commerce order records. The dataset includes fields such as:
- order_id
- customer_name
- product_category
- price
- quantity
- order_date

This raw dataset is stored in the data/raw folder and is used as the starting point for the ETL process.

## 5. Pipeline Workflow

```text
Raw CSV (orders.csv)
        ↓
Extract data
        ↓
Load to staging table
        ↓
Clean invalid records
        ↓
Validate data quality
        ↓
Transform into dimensional model
        ↓
Load into MySQL warehouse tables
        ↓
fact_orders
 dim_customers
 dim_product
 dim_date
```

The pipeline is designed to process transactional order data into a star schema for analytical reporting.

## 6. Project Structure
- data/raw: contains source CSV files
- data/processed: contains cleaned/processed datasets
- src/extract: ingestion logic
- src/tranform: cleaning, validation, and transformation scripts
- src/load: loading to MySQL
- src/config: database configuration
- sql/staging: staging table definitions
- sql/warehouse: fact and dimension table definitions
- tests: validation and quality checks
- logs: pipeline execution logs

## 7. Database Schema
The warehouse layer follows a dimensional model with the following main tables:
- fact_orders: stores transactional order facts
- dim_customers: stores customer dimension
- dim_product: stores product dimension
- dim_date: stores date dimension

The staging layer is used to temporarily hold raw or partially processed data before loading to the warehouse.

## 8. Data Quality Issues
This project is intended to handle several common data quality problems, including:
- duplicate order IDs
- missing or extra spaces in customer names
- inconsistent price formats such as currency strings and numeric strings
- invalid or negative quantities
- malformed or uncleaned data values in source files

These issues are cleaned and validated before the data is transformed and loaded.

## 9. How to Run
1. Create a virtual environment.
2. Install dependencies:
   pip install -r requirement.txt
3. Configure your MySQL connection in the database configuration file.
4. Run the ETL pipeline:
   python etl_pipeline.py
5. Check the generated data and warehouse tables in MySQL.

## 10. Example Output
The pipeline produces cleaned and transformed order data that can be used for analytics, such as:
- total sales by product category
- total orders by customer
- monthly sales trend
- order volume by date

## 11. Future Improvements
- add automated scheduling with Airflow
- improve logging and alerting
- add data validation dashboards
- support real database ingestion from cloud storage or APIs
- integrate CI/CD for ETL automation
- add more robust tests for edge cases and pipeline failures
