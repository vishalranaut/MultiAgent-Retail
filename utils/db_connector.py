import sqlite3
DB_PATH = "database/retail_inventory.db"
def get_db_connection():
    return sqlite3.connect(DB_PATH)