"""
Blinkit Analysis Dashboard - Sample Data Generator
Generates realistic sample data for sales, customers, products, and deliveries
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from faker import Faker
import random
import os

# Initialize Faker
fake = Faker('en_IN')
Faker.seed(42)
np.random.seed(42)
random.seed(42)

# Configuration
NUM_CUSTOMERS = 5000
NUM_PRODUCTS = 200
NUM_ORDERS = 20000
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2024, 12, 31)

print("="*70)
print("BLINKIT ANALYSIS DASHBOARD - DATA GENERATOR")
print("="*70)

# ============================================================================
# 1. GENERATE CUSTOMER DATA
# ============================================================================

def generate_customers(num_customers):
    """Generate customer data"""
    print(f"\n[1/4] Generating {num_customers} customers...")
    
    cities = ['Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Pune', 'Chennai', 
              'Kolkata', 'Ahmedabad', 'Jaipur', 'Lucknow']
    
    customer_segments = ['Premium', 'Regular', 'Occasional', 'New']
    
    customers = []
    for i in range(num_customers):
        customer = {
            'CustomerID': f'CUST{i+1:05d}',
            'Name': fake.name(),
            'Email': fake.email(),
            'Phone': fake.phone_number(),
            'City': random.choice(cities),
            'Area': fake.city_suffix(),
            'Pincode': fake.postcode(),
            'RegistrationDate': fake.date_between(start_date=START_DATE, end_date=END_DATE),
            'CustomerSegment': random.choice(customer_segments),
            'PreferredPaymentMethod': random.choice(['UPI', 'Card', 'Wallet', 'Cash']),
            'IsActive': random.choice([True, True, True, False])  # 75% active
        }
        customers.append(customer)
    
    df_customers = pd.DataFrame(customers)
    print(f"✓ Generated {len(df_customers)} customers")
    return df_customers

# ============================================================================
# 2. GENERATE PRODUCT DATA
# ============================================================================

def generate_products(num_products):
    """Generate product catalog"""
    print(f"\n[2/4] Generating {num_products} products...")
    
    categories = {
        'Dairy & Breakfast': ['Milk', 'Bread', 'Butter', 'Cheese', 'Eggs', 'Yogurt'],
        'Fruits & Vegetables': ['Apple', 'Banana', 'Tomato', 'Onion', 'Potato', 'Carrot'],
        'Snacks & Beverages': ['Chips', 'Biscuits', 'Soft Drink', 'Juice', 'Coffee', 'Tea'],
        'Personal Care': ['Shampoo', 'Soap', 'Toothpaste', 'Face Wash', 'Lotion'],
        'Household': ['Detergent', 'Cleaner', 'Tissue', 'Garbage Bags', 'Dishwash'],
        'Packaged Food': ['Rice', 'Atta', 'Dal', 'Oil', 'Spices', 'Noodles']
    }
    
    products = []
    product_id = 1
    
    for category, items in categories.items():
        for _ in range(num_products // len(categories)):
            base_item = random.choice(items)
            brand = fake.company().split()[0]
            
            # Price based on category
            if category == 'Personal Care':
                price = round(random.uniform(50, 500), 2)
                margin = random.uniform(0.25, 0.40)
            elif category == 'Dairy & Breakfast':
                price = round(random.uniform(20, 200), 2)
                margin = random.uniform(0.15, 0.25)
            else:
                price = round(random.uniform(30, 300), 2)
                margin = random.uniform(0.20, 0.35)
            
            product = {
                'ProductID': f'PROD{product_id:04d}',
                'ProductName': f'{brand} {base_item}',
                'Category': category,
                'SubCategory': base_item,
                'Brand': brand,
                'Price': price,
                'CostPrice': round(price * (1 - margin), 2),
                'ProfitMargin': round(margin * 100, 2),
                'StockQuantity': random.randint(50, 1000),
                'MinStockLevel': random.randint(20, 100),
                'IsActive': random.choice([True, True, True, True, False])  # 80% active
            }
            products.append(product)
            product_id += 1
    
    df_products = pd.DataFrame(products)
    print(f"✓ Generated {len(df_products)} products across {len(categories)} categories")
    return df_products

# ============================================================================
# 3. GENERATE SALES DATA
# ============================================================================

def generate_sales(num_orders, df_customers, df_products):
    """Generate sales transactions"""
    print(f"\n[3/4] Generating {num_orders} sales transactions...")
    
    orders = []
    
    # Peak hours: 7-9 AM, 12-2 PM, 7-10 PM
    peak_hours = [7, 8, 12, 13, 19, 20, 21]
    
    for i in range(num_orders):
        # Random date with higher probability on weekends
        order_date = fake.date_time_between(start_date=START_DATE, end_date=END_DATE)
        
        # Increase weekend orders
        if order_date.weekday() >= 5:  # Saturday or Sunday
            if random.random() < 0.3:  # Skip 30% to balance
                continue
        
        # Peak hour probability
        hour = random.choice(peak_hours) if random.random() < 0.6 else random.randint(6, 23)
        order_datetime = order_date.replace(hour=hour, minute=random.randint(0, 59))
        
        # Select customer
        customer = df_customers.sample(1).iloc[0]
        
        # Number of items (1-8 items per order)
        num_items = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8], 
                                     p=[0.3, 0.25, 0.2, 0.12, 0.08, 0.03, 0.01, 0.01])
        
        # Select products
        products = df_products.sample(num_items)
        
        # Calculate order details
        subtotal = sum(products['Price'] * np.random.randint(1, 4, size=len(products)))
        delivery_fee = 0 if subtotal > 200 else 20
        discount = round(subtotal * random.choice([0, 0, 0.05, 0.10, 0.15]), 2)
        total_amount = round(subtotal + delivery_fee - discount, 2)
        
        order = {
            'OrderID': f'ORD{i+1:06d}',
            'CustomerID': customer['CustomerID'],
            'OrderDateTime': order_datetime,
            'OrderDate': order_datetime.date(),
            'OrderTime': order_datetime.time(),
            'OrderHour': hour,
            'DayOfWeek': order_datetime.strftime('%A'),
            'IsWeekend': order_datetime.weekday() >= 5,
            'NumItems': num_items,
            'Subtotal': round(subtotal, 2),
            'DeliveryFee': delivery_fee,
            'Discount': discount,
            'TotalAmount': total_amount,
            'PaymentMethod': customer['PreferredPaymentMethod'],
            'OrderStatus': random.choice(['Completed', 'Completed', 'Completed', 'Cancelled']),
            'City': customer['City'],
            'Area': customer['Area']
        }
        orders.append(order)
    
    df_sales = pd.DataFrame(orders)
    
    # Add repeat customer flag
    customer_order_counts = df_sales.groupby('CustomerID').size()
    df_sales['IsRepeatCustomer'] = df_sales['CustomerID'].map(
        lambda x: customer_order_counts[x] > 1
    )
    
    print(f"✓ Generated {len(df_sales)} sales transactions")
    print(f"  - Average order value: ₹{df_sales['TotalAmount'].mean():.2f}")
    print(f"  - Total revenue: ₹{df_sales['TotalAmount'].sum():,.2f}")
    return df_sales

# ============================================================================
# 4. GENERATE DELIVERY DATA
# ============================================================================

def generate_deliveries(df_sales):
    """Generate delivery data"""
    print(f"\n[4/4] Generating delivery data...")
    
    deliveries = []
    
    for _, order in df_sales.iterrows():
        if order['OrderStatus'] == 'Completed':
            # Delivery time: 8-25 minutes
            delivery_minutes = np.random.choice(
                range(8, 26),
                p=[0.05, 0.08, 0.12, 0.15, 0.18, 0.15, 0.12, 0.08, 0.04, 0.02, 
                   0.01, 0, 0, 0, 0, 0, 0, 0]
            )
            
            delivery_datetime = order['OrderDateTime'] + timedelta(minutes=delivery_minutes)
            
            # On-time if delivered within 15 minutes
            is_on_time = delivery_minutes <= 15
            
            delivery = {
                'DeliveryID': f'DEL{order["OrderID"][3:]}',
                'OrderID': order['OrderID'],
                'CustomerID': order['CustomerID'],
                'OrderDateTime': order['OrderDateTime'],
                'DeliveryDateTime': delivery_datetime,
                'DeliveryTimeMinutes': delivery_minutes,
                'IsOnTime': is_on_time,
                'DeliveryPartnerID': f'DP{random.randint(1, 50):03d}',
                'DeliveryRating': random.choice([4, 4, 5, 5, 5, 3]) if is_on_time else random.choice([2, 3, 3, 4]),
                'City': order['City'],
                'Area': order['Area'],
                'DeliveryStatus': 'Delivered'
            }
            deliveries.append(delivery)
    
    df_deliveries = pd.DataFrame(deliveries)
    print(f"✓ Generated {len(df_deliveries)} delivery records")
    print(f"  - Average delivery time: {df_deliveries['DeliveryTimeMinutes'].mean():.1f} minutes")
    print(f"  - On-time delivery rate: {(df_deliveries['IsOnTime'].sum() / len(df_deliveries) * 100):.1f}%")
    return df_deliveries

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function"""
    
    # Create directories
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    
    # Generate data
    df_customers = generate_customers(NUM_CUSTOMERS)
    df_products = generate_products(NUM_PRODUCTS)
    df_sales = generate_sales(NUM_ORDERS, df_customers, df_products)
    df_deliveries = generate_deliveries(df_sales)
    
    # Save raw data
    print("\n" + "="*70)
    print("SAVING DATA FILES")
    print("="*70)
    
    df_customers.to_csv('data/raw/customer_data.csv', index=False)
    print("✓ Saved: data/raw/customer_data.csv")
    
    df_products.to_csv('data/raw/product_data.csv', index=False)
    print("✓ Saved: data/raw/product_data.csv")
    
    df_sales.to_csv('data/raw/sales_data.csv', index=False)
    print("✓ Saved: data/raw/sales_data.csv")
    
    df_deliveries.to_csv('data/raw/delivery_data.csv', index=False)
    print("✓ Saved: data/raw/delivery_data.csv")
    
    # Create consolidated dataset
    df_consolidated = df_sales.merge(df_deliveries, on='OrderID', how='left', suffixes=('', '_delivery'))
    df_consolidated.to_csv('data/processed/blinkit_consolidated.csv', index=False)
    print("✓ Saved: data/processed/blinkit_consolidated.csv")
    
    # Summary statistics
    print("\n" + "="*70)
    print("DATA GENERATION SUMMARY")
    print("="*70)
    print(f"Customers:     {len(df_customers):,}")
    print(f"Products:      {len(df_products):,}")
    print(f"Orders:        {len(df_sales):,}")
    print(f"Deliveries:    {len(df_deliveries):,}")
    print(f"Total Revenue: ₹{df_sales['TotalAmount'].sum():,.2f}")
    print(f"Date Range:    {df_sales['OrderDate'].min()} to {df_sales['OrderDate'].max()}")
    print("="*70)
    print("\n✅ Data generation complete! Files saved in data/ directory")
    print("\nNext steps:")
    print("1. Open Power BI Desktop")
    print("2. Import the CSV files from data/raw/")
    print("3. Create relationships and build visualizations")

if __name__ == "__main__":
    main()