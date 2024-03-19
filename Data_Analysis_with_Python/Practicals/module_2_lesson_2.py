
import pandas as pd

# Step 1: Load the dataset
# Let's assume we have a CSV file named 'sales_data.csv' containing sales data
# Replace 'sales_data.csv' with the actual path to your dataset
df = pd.read_csv('module_2_lesson_2_sampledata.csv')    

# Step 2: Display the first few rows of the dataset to understand its structure
print("First few rows of the dataset:")
print(df.head())

# Step 3: Data cleaning (if necessary)
# For example, handling missing values or converting data types

# Step 4: Data filtering
# Let's filter the dataset to include only sales data from a specific region
region_filter = df['Region'] == 'North'
sales_data_north = df[region_filter]

# Step 5: Data aggregation
# Let's calculate the total sales amount for each product category in the North region
sales_by_category = sales_data_north.groupby('Product Category')['Sales Amount'].sum()

# Step 6: Display the aggregated data
print("\nTotal sales amount by product category in the North region:")
print(sales_by_category)