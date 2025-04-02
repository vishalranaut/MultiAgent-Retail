from agents.inventory_agent import check_inventory

def manage_order(product_id, store_id):
    return f"Placing order for Product {product_id} at Store {store_id}" if check_inventory(product_id, store_id) == "Reorder Needed" else "No order needed"
