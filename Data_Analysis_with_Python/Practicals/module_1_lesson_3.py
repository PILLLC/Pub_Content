# Step 1: Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Step 2: Generate some sample data
# For this example, let's generate 1000 random numbers from a normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)

# Step 3: Create the Matplotlib histogram plot
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')

# Step 4: Customize the plot (optional)
plt.title('Distribution of a Numerical Variable')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Step 5: Show the plot
plt.show()
