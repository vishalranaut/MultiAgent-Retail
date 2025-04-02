import numpy as np
from sklearn.linear_model import LinearRegression
from utils.db_connector import get_db_connection

def predict_demand(product_id, store_id):
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM Demand WHERE ProductID=? AND StoreID=?", conn, params=(product_id, store_id))
    conn.close()
    if len(df) > 5:
        X = np.arange(len(df)).reshape(-1, 1)
        y = df["SalesQuantity"].values
        model = LinearRegression()
        model.fit(X, y)
        return model.predict([[len(df) + 1]])[0]
    return "Insufficient data for prediction"