# Retail Inventory Optimization - Multi-Agent System

## Overview
This project is a multi-agent AI system designed to optimize inventory management in retail. It helps predict demand, monitor stock levels, automate restocking, and optimize pricing to prevent stockouts and reduce holding costs.

## Features
- **Demand Forecasting**: Predicts future demand using machine learning.
- **Inventory Monitoring**: Tracks stock levels and identifies reorder needs.
- **Automated Restocking**: Places orders when stock levels are low.
- **Pricing Optimization**: Adjusts prices dynamically based on demand and competition.
- **Ollama AI Integration**: Uses an LLM for intelligent insights and automation.
- **Flask API**: Provides real-time interaction with the system.

## Installation & Setup
### Prerequisites
- Python 3.8+
- Virtual environment (recommended)
- Required Python packages (see `requirements.txt`)

### Steps to Install
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd RetailInventoryOptimization
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Initialize the database:
   ```bash
   python database/init_db.py
   ```
5. Run the Flask API:
   ```bash
   python api/app.py
   ```
6. Access the API at `http://127.0.0.1:5000/`

## Usage
### API Endpoints
- **Predict Demand**:
  ```
  GET /predict_demand?product_id=123&store_id=1
  ```
- **Check Inventory**:
  ```
  GET /inventory_status?product_id=123&store_id=1
  ```
- **Optimize Pricing**:
  ```
  GET /optimize_price?product_id=123&store_id=1
  ```
- **Manage Orders**:
  ```
  GET /order?product_id=123&store_id=1
  ```

## Technologies Used
- **Python** (Flask, Pandas, SQLite, Scikit-learn, Ollama)
- **Machine Learning** (Linear Regression for demand forecasting)
- **SQLite** (Database management)
- **Flask** (API for real-time interaction)
- **Ollama LLM** (AI-powered insights)

---

🚀 **Retail Inventory Optimization** ensures seamless inventory management, reducing costs and improving efficiency! Let us know if you have any questions or need enhancements!
