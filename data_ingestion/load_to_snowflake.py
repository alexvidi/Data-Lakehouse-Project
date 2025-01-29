import snowflake.connector
import pandas as pd
import json
import os

# Load configuration from config.json
config_path = os.path.join(os.path.dirname(__file__), '../config/config.json')
with open(config_path, "r") as file:
    config = json.load(file)

# Snowflake connection details
SNOWFLAKE_CONFIG = config["snowflake"]

def connect_to_snowflake():
    """Establish connection to Snowflake"""
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_CONFIG["user"],
        password=SNOWFLAKE_CONFIG["password"],
        account=SNOWFLAKE_CONFIG["account"],
        database=SNOWFLAKE_CONFIG["database"],
        schema=SNOWFLAKE_CONFIG["schema"],
        warehouse=SNOWFLAKE_CONFIG["warehouse"]
    )
    return conn

def create_table_if_not_exists(conn):
    """Create products table if it does not exist"""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        id INT PRIMARY KEY,
        title STRING,
        price FLOAT,
        category STRING,
        brand STRING,
        stock INT
    )
    """
    cursor = conn.cursor()
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()

def load_data_to_snowflake(conn):
    """Load data from CSV to Snowflake"""
    csv_path = os.path.join(os.path.dirname(__file__), "products.csv")
    
    # Read CSV into a DataFrame
    df = pd.read_csv(csv_path)

    # Insert data into Snowflake
    cursor = conn.cursor()
    for _, row in df.iterrows():
        # Use parameterized query to avoid SQL injection and handle special characters
        insert_query = """
        INSERT INTO products (id, title, price, category, brand, stock)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            int(row['id']),
            str(row['title']).replace("'", "''"),  # Escapar comillas simples
            float(row['price']),
            str(row['category']).replace("'", "''"),
            str(row['brand']).replace("'", "''"),
            int(row['stock'])
        ))
    
    conn.commit()
    cursor.close()
    print("✅ Data successfully loaded into Snowflake.")

if __name__ == "__main__":
    conn = connect_to_snowflake()
    create_table_if_not_exists(conn)
    load_data_to_snowflake(conn)
    conn.close()

