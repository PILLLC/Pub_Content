import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv('module_3_lesson_1_sampledata.csv')

# Step 2: Inspect the dataset
print("First few rows of the dataset:")
print(df.head())

print("\nDataset information:")
print(df.info())

# Step 3: Descriptive statistics
print("\nDescriptive statistics:")
print(df.describe())

# Step 4: Visualize distributions
# Histograms for numerical variables
df.hist(figsize=(10, 8))
plt.suptitle("Histograms of Numerical Variables")
plt.show()

# Box plots for numerical variables
plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.title("Box Plot of Numerical Variables")
plt.show()

# Bar plot for categorical variables
plt.figure(figsize=(8, 6))
sns.countplot(x='category', data=df)
plt.title("Count of Observations by Category")
plt.show()

# Step 5: Explore relationships
# Pair plot for numerical variables
sns.pairplot(df)
plt.title("Pair Plot of Numerical Variables")
plt.show()

# Heatmap of correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# Step 6: Identify outliers
# Box plot of numerical variables
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['numeric_column1', 'numeric_column2']])
plt.title("Box Plot of Numerical Variables")
plt.show()

# Step 7: Feature engineering (if necessary)

# Further analysis based on insights gained

# Save or display visualizations