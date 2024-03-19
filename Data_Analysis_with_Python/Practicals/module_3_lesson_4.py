
import numpy as np
from scipy import stats

# Generate some sample data
np.random.seed(0)
sample1 = np.random.normal(loc=5, scale=2, size=100)  # Sample 1 with mean 5 and standard deviation 2
sample2 = np.random.normal(loc=4, scale=2, size=100)  # Sample 2 with mean 4 and standard deviation 2

# Conduct a t-test to compare means of two independent samples
t_statistic, p_value = stats.ttest_ind(sample1, sample2)
print("T-statistic:", t_statistic)
print("P-value:", p_value)

# Perform a chi-square test for independence
# Create a contingency table
observed = np.array([[20, 30], [15, 35]])  # Example contingency table
chi2_statistic, p_value, degrees_of_freedom, expected = stats.chi2_contingency(observed)
print("\nChi-square statistic:", chi2_statistic)
print("P-value:", p_value)
print("Degrees of freedom:", degrees_of_freedom)
print("Expected frequencies:\n", expected)

# Conduct a one-way ANOVA test
# Generate some additional sample data
group1 = np.random.normal(loc=10, scale=2, size=50)  # Group 1 with mean 10 and standard deviation 2
group2 = np.random.normal(loc=12, scale=2, size=50)  # Group 2 with mean 12 and standard deviation 2
group3 = np.random.normal(loc=14, scale=2, size=50)  # Group 3 with mean 14 and standard deviation 2
# Combine all groups
all_groups = [group1, group2, group3]
f_statistic, p_value = stats.f_oneway(*all_groups)
print("\nF-statistic:", f_statistic)
print("P-value:", p_value)
