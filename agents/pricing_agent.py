from utils.db_connector import get_db_connection

def optimize_pricing(product_id, store_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Price, CompetitorPrices FROM Pricing WHERE ProductID=? AND StoreID=?", (product_id, store_id))
    price, competitor_price = cursor.fetchone()
    conn.close()
    return f"Consider reducing price by {0.1 * price}" if price > competitor_price else "Price is optimal"