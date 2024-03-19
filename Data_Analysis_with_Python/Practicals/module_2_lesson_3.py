import time
import pandas as pd
import numpy as np
import polars as pl

# Data loading
start_time = time.time()
# Pandas
pandas_df = pd.read_csv('module_2_lesson_3_sampledata.csv')
pandas_loading_time = time.time() - start_time

start_time = time.time()
# NumPy
numpy_arr = np.genfromtxt('module_2_lesson_3_sampledata.csv', delimiter=',', names=True, dtype=None, encoding=None)
numpy_loading_time = time.time() - start_time

start_time = time.time()
# Polars
polars_df = pl.read_csv('module_2_lesson_3_sampledata.csv')
polars_loading_time = time.time() - start_time

# Data filtering
# Assuming we want to filter rows where a column 'value' is greater than 100
start_time = time.time()
# Pandas
pandas_filtered_df = pandas_df[pandas_df['value'] > 100]
pandas_filtering_time = time.time() - start_time

start_time = time.time()
# NumPy
numpy_filtered_arr = numpy_arr[numpy_arr['value'] > 100]
numpy_filtering_time = time.time() - start_time

start_time = time.time()
# Polars
polars_filtered_df = polars_df.filter(pl.col('value') > 100)
polars_filtering_time = time.time() - start_time

# Data aggregation
# Assuming we want to group by 'category' and sum the 'value' column
start_time = time.time()
# Pandas
pandas_aggregated_df = pandas_df.groupby('category')['value'].sum()
pandas_aggregation_time = time.time() - start_time

start_time = time.time()
# NumPy
numpy_aggregated_arr = np.sum(numpy_arr['value'][numpy_arr['category'] == b'category'])
numpy_aggregation_time = time.time() - start_time

start_time = time.time()
# Polars
polars_aggregated_df = polars_df.groupby('category').agg(pl.sum('value'))
polars_aggregation_time = time.time() - start_time

# Print loading, filtering, and aggregation times
print("Loading time (Pandas):", pandas_loading_time)
print("Loading time (NumPy):", numpy_loading_time)
print("Loading time (Polars):", polars_loading_time)

print("\nFiltering time (Pandas):", pandas_filtering_time)
print("Filtering time (NumPy):", numpy_filtering_time)
print("Filtering time (Polars):", polars_filtering_time)

print("\nAggregation time (Pandas):", pandas_aggregation_time)
print("Aggregation time (NumPy):", numpy_aggregation_time)
print("Aggregation time (Polars):", polars_aggregation_time)
