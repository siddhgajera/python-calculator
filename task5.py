"""Task 5 : Data Analysis on CSV Files
 Objective:  Analyze sales data using Pandas.
 Tools :Python, Pandas, Jupyter Notebook / Colab
 Deliverables: Notebook + charts
 Hints/Mini Guide:
 1.Load CSV using Pandas
 2.Use groupby(), sum(), plot()
 Outcome: :  Basic data insights using Python"""
import pandas as pd
import matplotlib.pyplot as plt

# GENERATE DUMMY DATA (CSV file) 
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03', '2023-01-04'],
    'Product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse', 'Laptop'],
    'Region': ['North', 'South', 'East', 'North', 'West', 'North'],
    'Sales': [1000, 20, 1000, 50, 20, 1200],
    'Quantity': [1, 2, 1, 5, 2, 1]
}

# Save this as a CSV so we can practice loading it
df_raw = pd.DataFrame(data)
df_raw.to_csv('sales_data.csv', index=False)
print("sales_data.csv created successfully!\n")


# In a real scenario,start here
df = pd.read_csv('sales_data.csv')

print("--- First 5 Rows of Data ---")
print(df.head()) 
print("\n")


#ANALYZE DATA (Groupby & Sum)
product_sales = df.groupby('Product')['Sales'].sum()

print("--- Total Sales by Product ---")
print(product_sales)
print("\n")


# VISUALIZE DATA 
# Create a bar chart
plt.figure(figsize=(8, 5))
product_sales.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Total Revenue by Product')
plt.xlabel('Product Name')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=0) # labels horizontal
plt.grid(axis='y', linestyle='--', alpha=0.7)

print("--- Generating Chart... ---")
plt.show()