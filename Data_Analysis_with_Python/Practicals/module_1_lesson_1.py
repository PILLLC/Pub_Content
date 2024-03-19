import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv('module_1_lesson_1_sampledata.csv')

# Create the Plotly visualization
fig = px.line(df, x='date_column', y='value_column', title='Trends Over Time')

# Customize the visualization
fig.update_layout(xaxis_title='Date', yaxis_title='Value')

# Show the visualization
fig.show()