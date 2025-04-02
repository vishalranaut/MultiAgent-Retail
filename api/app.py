from flask import Flask, request, jsonify
from agents.inventory_agent import check_inventory
from agents.pricing_agent import optimize_pricing
from agents.order_agent import manage_order
from models.demand_forecast_model import predict_demand

app = Flask(__name__)

@app.route("/predict_demand", methods=["GET"])
def demand():
    product_id = int(request.args.get("product_id"))
    store_id = int(request.args.get("store_id"))
    return jsonify({"prediction": predict_demand(product_id, store_id)})

@app.route("/inventory_status", methods=["GET"])
def inventory():
    product_id = int(request.args.get("product_id"))
    store_id = int(request.args.get("store_id"))
    return jsonify({"status": check_inventory(product_id, store_id)})

@app.route("/optimize_price", methods=["GET"])
def pricing():
    product_id = int(request.args.get("product_id"))
    store_id = int(request.args.get("store_id"))
    return jsonify({"recommendation": optimize_pricing(product_id, store_id)})

@app.route("/order", methods=["GET"])
def order():
    product_id = int(request.args.get("product_id"))
    store_id = int(request.args.get("store_id"))
    return jsonify({"order_status": manage_order(product_id, store_id)})

if __name__ == "__main__":
    app.run(debug=True)