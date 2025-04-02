from utils.db_connector import get_db_connection

def check_inventory(product_id, store_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT StockLevels, ReorderPoint FROM Inventory WHERE ProductID=? AND StoreID=?", (product_id, store_id))
    stock, reorder_point = cursor.fetchone()
    conn.close()
    return "Reorder Needed" if stock < reorder_point else "Stock Sufficient"