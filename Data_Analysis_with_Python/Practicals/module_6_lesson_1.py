import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Step 1: Load the Time Series Data
# Assuming 'date' is the index and 'value' is the time series data
df = pd.read_csv('module_6_lesson_1_sampledata.csv', parse_dates=['date'], index_col='date')

# Step 2: Visualize the Time Series
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['value'], label='Original Time Series')
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# Step 3: Decompose the Time Series
decomposition = seasonal_decompose(df['value'], model='additive')

# Step 4: Visualize Trend and Seasonality
plt.figure(figsize=(10, 6))
plt.plot(df.index, decomposition.trend, label='Trend')
plt.title('Trend Component of Time Series')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df.index, decomposition.seasonal, label='Seasonality')
plt.title('Seasonality Component of Time Series')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# Step 5: Visualize Residuals (Noise)
plt.figure(figsize=(10, 6))
plt.plot(df.index, decomposition.resid, label='Residuals (Noise)')
plt.title('Residual Component of Time Series')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()