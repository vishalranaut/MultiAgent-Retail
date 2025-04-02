import sqlite3
import pandas as pd

DB_PATH = "database/retail_inventory.db"

def initialize_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Load and execute schema.sql
    with open("database/schema.sql", "r") as schema_file:
        cursor.executescript(schema_file.read())

    # Load CSV files into the database
    demand_data = pd.read_csv("data/demand_forecasting.csv")
    demand_data.to_sql("Demand", conn, if_exists="append", index=False)

    inventory_data = pd.read_csv("data/inventory_monitoring.csv")
    inventory_data.to_sql("Inventory", conn, if_exists="append", index=False)

    pricing_data = pd.read_csv("data/pricing_optimization.csv")
    pricing_data.to_sql("Pricing", conn, if_exists="append", index=False)

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    initialize_database()
