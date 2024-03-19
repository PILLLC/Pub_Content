from darts import TimeSeries
from darts.models import ExponentialSmoothing
from darts.metrics import mape
import matplotlib.pyplot as plt

# Step 2: Load the Time Series Data
# Assuming 'date' is the index and 'value' is the time series data
# Replace 'your_time_series_data.csv' with the path to your dataset
series = TimeSeries.from_csv('module_6_lesson_2_sampledata.csv', parse_dates=True, index_col='date')

# Step 3: Split the Data
train, val = series.split_before(pd.Timestamp('2022-01-01'))

# Step 4: Choose a Forecasting Model and Fit the Model
model = ExponentialSmoothing()
model.fit(train)

# Step 6: Make Forecasts
forecast = model.predict(len(val))

# Step 7: Evaluate Performance
mape_error = mape(val, forecast)
print(f"MAPE: {mape_error:.2f}%")

# Step 8: Visualize Forecasts
plt.figure(figsize=(10, 6))
series.plot(label='Actual')
forecast.plot(label='Forecast', lw=2)
plt.title('Forecasting with Exponential Smoothing')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()