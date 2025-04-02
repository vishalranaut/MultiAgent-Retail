import pandas as pd
from utils.db_connector import get_db_connection

def load_datasets():
    df_demand = pd.read_csv("data/demand_forecasting.csv")
    df_inventory = pd.read_csv("data/inventory_monitoring.csv")
    df_pricing = pd.read_csv("data/pricing_optimization.csv")
    return df_demand, df_inventory, df_pricing