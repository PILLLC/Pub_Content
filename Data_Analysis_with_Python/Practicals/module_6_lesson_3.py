
from kats.consts import TimeSeriesData
from kats.detectors.trend_mk import MKDetector
from kats.detectors.outlier import OutlierDetector
from kats.detectors.seasonal_decomposition import TimeSeriesDecompositionDetector
import matplotlib.pyplot as plt

# Step 2: Load the Time Series Data
# Assuming 'date' is the index and 'value' is the time series data
# Replace 'your_time_series_data.csv' with the path to your dataset
# Load data into a Kats TimeSeriesData object
ts_data = TimeSeriesData.load_csv('module_6_lesson_3_sampledata.csv')

# Step 3: Perform Time Series Decomposition
# Use seasonal decomposition to decompose the time series into trend, seasonality, and residual components
decomposition_detector = TimeSeriesDecompositionDetector(ts_data)
decomposition_result = decomposition_detector.run()

# Step 4: Detect Anomalies
# Use an anomaly detection algorithm, such as the Mann-Kendall trend change detector
mk_detector = MKDetector(ts_data)
mk_outliers = mk_detector.detector()

# Alternatively, you can use other outlier detection algorithms provided by Kats
# For example, you can use an outlier detector based on z-score
# outlier_detector = OutlierDetector(ts_data)
# zscore_outliers = outlier_detector.detector()

# Step 5: Visualize Results
# Plot the original time series, its decomposition components, and detected anomalies
plt.figure(figsize=(12, 8))

# Plot original time series
plt.subplot(3, 1, 1)
plt.plot(ts_data.time, ts_data.value)
plt.title('Original Time Series')

# Plot decomposed components
plt.subplot(3, 1, 2)
plt.plot(ts_data.time, decomposition_result.trend)
plt.plot(ts_data.time, decomposition_result.seasonal)
plt.plot(ts_data.time, decomposition_result.residue)
plt.title('Decomposed Components')

# Plot detected anomalies
plt.subplot(3, 1, 3)
plt.plot(ts_data.time, ts_data.value)
plt.scatter(mk_outliers['time'], mk_outliers['value'], color='red', label='Anomalies')
plt.title('Anomaly Detection')
plt.legend()

plt.tight_layout()
plt.show()