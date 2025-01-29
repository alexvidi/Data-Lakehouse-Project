import requests
import pandas as pd
import json
import os

# Load configuration from config.json
config_path = os.path.join(os.path.dirname(__file__), '../config/config.json')
with open(config_path, "r") as file:
    config = json.load(file)

# API URL from DummyJSON
API_URL = config["api_url"]

def fetch_products():
    """Fetch product data from DummyJSON API"""
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        data = response.json()["products"]
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

if __name__ == "__main__":
    # Fetch data and save to CSV
    df_products = fetch_products()
    
    if df_products is not None:
        output_path = os.path.join(os.path.dirname(__file__), "products.csv")
        df_products.to_csv(output_path, index=False)
        print(f"✅ Data saved to: {output_path}")
    else:
        print("❌ Failed to fetch data.")
