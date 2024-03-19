# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Step 2: Load your dataset
# For this example, let's use a sample dataset
# Replace 'your_dataset.csv' with the path to your dataset
df = pd.read_csv('module_1_lesson_4_sampledata.csv')

# Step 3: Preprocess your data if necessary

# Step 4: Create visualizations using different libraries
# Plotly scatter plot
fig1 = px.scatter(df, x='feature1', y='feature2', color='target', title='Plotly Scatter Plot')

# Matplotlib histogram
plt.figure(figsize=(8, 6))
plt.hist(df['numerical_feature'], bins=30, color='skyblue', edgecolor='black')
plt.title('Matplotlib Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Seaborn pairplot
plt.figure(figsize=(8, 6))
sns.pairplot(df, hue='target')
plt.suptitle('Seaborn Pairplot')

# Step 5: Show the visualizations
# Plotly scatter plot
fig1.show()

# Matplotlib histogram
plt.show()

# Seaborn pairplot doesn't need explicit show as it automatically shows the plot

# Step 6: Combine the visualizations into a single dashboard (optional)
# You can combine them using HTML layout or use specific dashboard frameworks like Dash for Plotly

# Step 7: Save the dashboard or display it in a web application (optional)
# You can save the dashboard as HTML or display it using a web framework like Flask or Django

# For more interactivity and customization, consider using Dash framework for Plotly
