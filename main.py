from agents.inventory_agent import check_inventory
from agents.pricing_agent import optimize_pricing
from agents.order_agent import manage_order
from models.demand_forecast_model import predict_demand

print(predict_demand(4277, 48))
print(check_inventory(4277, 48))
print(optimize_pricing(4277, 48))
print(manage_order(4277, 48))