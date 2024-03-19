import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the dataset
data = pd.read_csv('module_3_lesson_2_sampledata.csv')

# Prepare the data
X = data[['feature1', 'feature2']]  # Independent variables
y = data['target']  # Dependent variable

# Add a constant term to the independent variables (intercept term)
X = sm.add_constant(X)

# Fit the linear regression model
model = sm.OLS(y, X).fit()

# Print the summary statistics
print(model.summary())

# Perform hypothesis testing
# For example, test the significance of the coefficients
print("Hypothesis Testing:")
print("Test for feature1 coefficient:")
print("Null Hypothesis: Coefficient for feature1 is zero")
print("Alternative Hypothesis: Coefficient for feature1 is not zero")
print("p-value:", model.pvalues['feature1'])
print("Conclusion: Reject the null hypothesis if p-value < significance level (e.g., 0.05)")