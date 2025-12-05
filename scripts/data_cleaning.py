"""
Blinkit Analysis Dashboard - Data Cleaning Script
Cleans and preprocesses raw data for Power BI dashboard
"""

import pandas as pd
import numpy as np
from datetime import datetime

print("="*70)
print("BLINKIT ANALYSIS DASHBOARD - DATA CLEANING")
print("="*70)

# ============================================================================
# LOAD RAW DATA
# ============================================================================

print("\n[1/5] Loading raw data files...")

try:
    df_customers = pd.read_csv('data/raw/customer_data.csv')
    df_products = pd.read_csv('data/raw/product_data.csv')
    df_sales = pd.read_csv('data/raw/sales_data.csv')
    df_deliveries = pd.read_csv('data/raw/delivery_data.csv')
    print("✓ All data files loaded successfully")
except FileNotFoundError as e:
    print(f"❌ Error: {e}")
    print("Please run data_generation.py first to generate sample data")
    exit(1)

# ============================================================================
# CLEAN CUSTOMER DATA
# ============================================================================

print("\n[2/5] Cleaning customer data...")

# Convert dates
df_customers['RegistrationDate'] = pd.to_datetime(df_customers['RegistrationDate'])

# Remove duplicates
initial_count = len(df_customers)
df_customers = df_customers.drop_duplicates(subset=['CustomerID'])
print(f"  - Removed {initial_count - len(df_customers)} duplicate customers")

# Handle missing values
df_customers['Email'].fillna('unknown@email.com', inplace=True)
df_customers['Phone'].fillna('0000000000', inplace=True)

# Standardize city names
df_customers['City'] = df_customers['City'].str.title()

print(f"✓ Cleaned {len(df_customers)} customer records")

# ============================================================================
# CLEAN PRODUCT DATA
# ============================================================================

print("\n[3/5] Cleaning product data...")

# Remove duplicates
initial_count = len(df_products)
df_products = df_products.drop_duplicates(subset=['ProductID'])
print(f"  - Removed {initial_count - len(df_products)} duplicate products")

# Ensure positive prices
df_products = df_products[df_products['Price'] > 0]
df_products = df_products[df_products['CostPrice'] > 0]

# Recalculate profit margin
df_products['ProfitMargin'] = round(
    ((df_products['Price'] - df_products['CostPrice']) / df_products['Price']) * 100, 
    2
)

# Handle stock quantities
df_products['StockQuantity'] = df_products['StockQuantity'].fillna(0).astype(int)
df_products['MinStockLevel'] = df_products['MinStockLevel'].fillna(20).astype(int)

# Add stock status
df_products['StockStatus'] = df_products.apply(
    lambda x: 'Out of Stock' if x['StockQuantity'] == 0 
    else 'Low Stock' if x['StockQuantity'] < x['MinStockLevel']
    else 'In Stock',
    axis=1
)

print(f"✓ Cleaned {len(df_products)} product records")

# ============================================================================
# CLEAN SALES DATA
# ============================================================================

print("\n[4/5] Cleaning sales data...")

# Convert datetime columns
df_sales['OrderDateTime'] = pd.to_datetime(df_sales['OrderDateTime'])
df_sales['OrderDate'] = pd.to_datetime(df_sales['OrderDate'])

# Remove duplicates
initial_count = len(df_sales)
df_sales = df_sales.drop_duplicates(subset=['OrderID'])
print(f"  - Removed {initial_count - len(df_sales)} duplicate orders")

# Remove invalid orders (negative amounts)
df_sales = df_sales[df_sales['TotalAmount'] > 0]

# Add calculated columns
df_sales['Year'] = df_sales['OrderDateTime'].dt.year
df_sales['Month'] = df_sales['OrderDateTime'].dt.month
df_sales['MonthName'] = df_sales['OrderDateTime'].dt.strftime('%B')
df_sales['Quarter'] = df_sales['OrderDateTime'].dt.quarter
df_sales['WeekOfYear'] = df_sales['OrderDateTime'].dt.isocalendar().week

# Add time-based segments
df_sales['TimeSegment'] = df_sales['OrderHour'].apply(
    lambda x: 'Morning' if 6 <= x < 12
    else 'Afternoon' if 12 <= x < 17
    else 'Evening' if 17 <= x < 21
    else 'Night'
)

# Calculate order value segments
df_sales['OrderValueSegment'] = pd.cut(
    df_sales['TotalAmount'],
    bins=[0, 200, 500, 1000, float('inf')],
    labels=['Small', 'Medium', 'Large', 'Extra Large']
)

print(f"✓ Cleaned {len(df_sales)} sales records")

# ============================================================================
# CLEAN DELIVERY DATA
# ============================================================================

print("\n[5/5] Cleaning delivery data...")

# Convert datetime columns
df_deliveries['OrderDateTime'] = pd.to_datetime(df_deliveries['OrderDateTime'])
df_deliveries['DeliveryDateTime'] = pd.to_datetime(df_deliveries['DeliveryDateTime'])

# Remove duplicates
initial_count = len(df_deliveries)
df_deliveries = df_deliveries.drop_duplicates(subset=['DeliveryID'])
print(f"  - Removed {initial_count - len(df_deliveries)} duplicate deliveries")

# Ensure delivery time is positive
df_deliveries = df_deliveries[df_deliveries['DeliveryTimeMinutes'] > 0]

# Add delivery time segments
df_deliveries['DeliveryTimeSegment'] = pd.cut(
    df_deliveries['DeliveryTimeMinutes'],
    bins=[0, 10, 15, 20, float('inf')],
    labels=['Very Fast', 'Fast', 'Normal', 'Slow']
)

# Add rating categories
df_deliveries['RatingCategory'] = pd.cut(
    df_deliveries['DeliveryRating'],
    bins=[0, 2, 3, 4, 5],
    labels=['Poor', 'Average', 'Good', 'Excellent']
)

print(f"✓ Cleaned {len(df_deliveries)} delivery records")

# ============================================================================
# SAVE CLEANED DATA
# ============================================================================

print("\n" + "="*70)
print("SAVING CLEANED DATA")
print("="*70)

# Save individual cleaned files
df_customers.to_csv('data/processed/customers_clean.csv', index=False)
print("✓ Saved: data/processed/customers_clean.csv")

df_products.to_csv('data/processed/products_clean.csv', index=False)
print("✓ Saved: data/processed/products_clean.csv")

df_sales.to_csv('data/processed/sales_clean.csv', index=False)
print("✓ Saved: data/processed/sales_clean.csv")

df_deliveries.to_csv('data/processed/deliveries_clean.csv', index=False)
print("✓ Saved: data/processed/deliveries_clean.csv")

# Create master dataset
df_master = df_sales.merge(
    df_deliveries[['OrderID', 'DeliveryTimeMinutes', 'IsOnTime', 'DeliveryRating', 
                   'DeliveryPartnerID', 'DeliveryTimeSegment', 'RatingCategory']],
    on='OrderID',
    how='left'
)

df_master = df_master.merge(
    df_customers[['CustomerID', 'Name', 'City', 'CustomerSegment', 'RegistrationDate']],
    on='CustomerID',
    how='left',
    suffixes=('', '_customer')
)

df_master.to_csv('data/processed/master_dataset.csv', index=False)
print("✓ Saved: data/processed/master_dataset.csv")

# ============================================================================
# DATA QUALITY REPORT
# ============================================================================

print("\n" + "="*70)
print("DATA QUALITY REPORT")
print("="*70)

print(f"\nCustomers:")
print(f"  - Total records: {len(df_customers):,}")
print(f"  - Active customers: {df_customers['IsActive'].sum():,}")
print(f"  - Unique cities: {df_customers['City'].nunique()}")

print(f"\nProducts:")
print(f"  - Total products: {len(df_products):,}")
print(f"  - Active products: {df_products['IsActive'].sum():,}")
print(f"  - Categories: {df_products['Category'].nunique()}")
print(f"  - Out of stock: {(df_products['StockStatus'] == 'Out of Stock').sum()}")

print(f"\nSales:")
print(f"  - Total orders: {len(df_sales):,}")
print(f"  - Completed orders: {(df_sales['OrderStatus'] == 'Completed').sum():,}")
print(f"  - Total revenue: ₹{df_sales['TotalAmount'].sum():,.2f}")
print(f"  - Average order value: ₹{df_sales['TotalAmount'].mean():.2f}")
print(f"  - Date range: {df_sales['OrderDate'].min()} to {df_sales['OrderDate'].max()}")

print(f"\nDeliveries:")
print(f"  - Total deliveries: {len(df_deliveries):,}")
print(f"  - On-time deliveries: {df_deliveries['IsOnTime'].sum():,} ({df_deliveries['IsOnTime'].mean()*100:.1f}%)")
print(f"  - Average delivery time: {df_deliveries['DeliveryTimeMinutes'].mean():.1f} minutes")
print(f"  - Average rating: {df_deliveries['DeliveryRating'].mean():.2f}/5")

print("\n" + "="*70)
print("✅ Data cleaning complete!")
print("\nCleaned files are ready for Power BI import:")
print("  - data/processed/master_dataset.csv (recommended)")
print("  - data/processed/customers_clean.csv")
print("  - data/processed/products_clean.csv")
print("  - data/processed/sales_clean.csv")
print("  - data/processed/deliveries_clean.csv")
print("="*70)