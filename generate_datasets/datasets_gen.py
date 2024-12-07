"""Generate synthetic data"""
import pandas as pd
import numpy as np
from faker import Faker
import random, datetime
import json

fake = Faker()

# ------------------------ Helper Functions ------------------------

# Generate Customers
def generate_customers(n):
    data = []
    for _ in range(n):
        data.append({
            "customer_id": fake.uuid4(),
            "name": fake.name(),
            "email": fake.email() if np.random.random() > 0.1 else None,  # 10% missing
            "phone": fake.phone_number(),
            "loyalty_points": np.random.randint(0, 1000),
            "join_date": fake.date_between(start_date="-5y", end_date="today")
        })
    return pd.DataFrame(data)

# Generate Products
def generate_products(n):
    categories = ['Electronics', 'Clothing', 'Groceries', 'Furniture']
    data = []
    for _ in range(n):
        data.append({
            "product_id": fake.uuid4(),
            "name": fake.word(),
            "category": np.random.choice(categories),
            "price": round(np.random.uniform(5, 500), 2),
            "stock_level": np.random.randint(0, 1000)
        })
    return pd.DataFrame(data)

# Generate Stores
def generate_stores(n):
    regions = ['North', 'South', 'East', 'West']
    data = []
    for _ in range(n):
        data.append({
            "store_id": fake.uuid4(),
            "name": fake.company(),
            "location": fake.city(),
            "region": np.random.choice(regions)
        })
    return pd.DataFrame(data)

# Generate Sales Transactions
def generate_sales_transactions(n, customers, products, stores):
    data = []
    for _ in range(n):
        customer = customers.sample(1).iloc[0]
        product = products.sample(1).iloc[0]
        store = stores.sample(1).iloc[0]
        quantity = np.random.randint(1, 10)
        price = product["price"]
        discount = round(price * 0.1, 2) if np.random.random() > 0.8 else 0  # 20% chance of discount
        total_amount = round(quantity * price - discount, 2)

        data.append({
            "transaction_id": fake.uuid4(),
            "customer_id": customer["customer_id"],
            "product_id": product["product_id"],
            "store_id": store["store_id"],
            "sale_date": fake.date_this_year(),
            "quantity": quantity,
            "total_amount": total_amount,
            "discount": discount,
            "return_status": np.random.choice([True, False])
        })
    return pd.DataFrame(data)

# Generate Inventory Movements
def generate_inventory_movements(n, products, stores):
    data = []
    for _ in range(n):
        product = products.sample(1).iloc[0]
        store = stores.sample(1).iloc[0]
        movement_type = np.random.choice(['IN', 'OUT'])
        quantity = np.random.randint(1, 50)
        movement_date = fake.date_this_year()

        data.append({
            "movement_id": fake.uuid4(),
            "product_id": product["product_id"],
            "store_id": store["store_id"],
            "movement_date": movement_date,
            "movement_type": movement_type,
            "quantity": quantity
        })
    return pd.DataFrame(data)

# Generate Suppliers
def generate_suppliers(n):
    data = []
    for _ in range(n):
        data.append({
            "supplier_id": fake.uuid4(),
            "name": fake.company(),
            "contact_info": fake.phone_number()
        })
    return pd.DataFrame(data)

# Generate Supply Chain Deliveries
def generate_supply_chain_deliveries(n, suppliers, products):
    data = []
    for _ in range(n):
        supplier = suppliers.sample(1).iloc[0]
        product = products.sample(1).iloc[0]
        delivery_quantity = np.random.randint(1, 100)
        delivery_date = fake.date_this_year()
        status = np.random.choice(['Delivered', 'Pending', 'Delayed'])

        data.append({
            "delivery_id": fake.uuid4(),
            "supplier_id": supplier["supplier_id"],
            "product_id": product["product_id"],
            "delivery_date": delivery_date,
            "quantity": delivery_quantity,
            "status": status
        })
    return pd.DataFrame(data)

# ------------------------ Document DB Data Generation ------------------------

# Generate Product Metadata (Document DB)
def generate_product_metadata(products):
    data = []
    for _, product in products.iterrows():
        data.append({
            "product_id": product["product_id"],
            "description": fake.text(),
            "specifications": fake.text(),
            "images": fake.image_url()
        })
    return data

# Generate Marketing Campaigns (Document DB)
def generate_marketing_campaigns(n):
    data = []
    for _ in range(n):
        data.append({
            "campaign_id": fake.uuid4(),
            "campaign_name": fake.company(),
            "channels": np.random.choice(['Email', 'Social Media', 'SMS']),
            "start_date": fake.date_this_year(),
            "end_date": fake.date_this_year(),
            "performance_metrics": {
                "click_through_rate": round(np.random.uniform(0, 1), 2),
                "conversion_rate": round(np.random.uniform(0, 1), 2),
                "roi": np.random.randint(1000, 50000)
            }
        })
    return data

# Generate Customer Preferences (Document DB)
def generate_customer_preferences(customers):
    data = []
    for _, customer in customers.iterrows():
        data.append({
            "customer_id": customer["customer_id"],
            "preferred_categories": np.random.choice(['Electronics', 'Clothing', 'Groceries', 'Furniture']),
            "spending_patterns": fake.text()
        })
    return data

# ------------------------ Data Generation ------------------------
main_path = "/Users/Oamen/OneDrive/Documents/DATA PROJECTS/RetailXpress_data_warehouse/datasets"

def json_serializer(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


# # Generate Data
products = generate_products(10000)  # 10 thousand products
products.to_csv(f'{main_path}/products.csv', index=False)
print('Done with first csv')

product_metadata = generate_product_metadata(products)
# Export Document DB data to JSON
with open(f'{main_path}/product_metadata.json', 'w') as f:
    json.dump(product_metadata, f)

marketing_campaigns = generate_marketing_campaigns(100)  # 100 campaigns
with open(f'{main_path}/marketing_campaigns.json', 'w') as f:
    json.dump(marketing_campaigns, f, default=json_serializer)

suppliers = generate_suppliers(500)  # 500 suppliers
suppliers.to_csv(f'{main_path}/suppliers.csv', index=False)

stores = generate_stores(500)  # 500 stores
stores.to_csv(f'{main_path}/stores.csv', index=False)

customers = generate_customers(1000000)  # 1 million customers
customers.to_csv(f'{main_path}/customers.csv', index=False)

customer_preferences = generate_customer_preferences(customers)
with open(f'{main_path}/customer_preferences.json', 'w') as f:
    json.dump(customer_preferences, f)

inventory_movements = generate_inventory_movements(1000000, products, stores)  # 1 million inventory movements
inventory_movements.to_csv(f'{main_path}/inventory_movements.csv', index=False)

deliveries = generate_supply_chain_deliveries(1000000, suppliers, products)  # 1 million deliveries
deliveries.to_csv(f'{main_path}/supply_chain_deliveries.csv', index=False)

transactions = generate_sales_transactions(5000000, customers, products, stores)  # 5 million sales transactions
transactions.to_csv(f'{main_path}/sales_transactions.csv', index=False)



# Document DB Data


