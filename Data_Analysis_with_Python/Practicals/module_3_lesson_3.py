
import pandas as pd
import pingouin as pg

# Load the dataset
data = pd.read_csv('module_3_lesson_3_sampledata.csv')

# Correlation Analysis
# Pearson correlation coefficient and p-value
pearson_corr = pg.corr(data['variable1'], data['variable2'], method='pearson')
print("Pearson correlation coefficient:")
print(pearson_corr)

# Spearman correlation coefficient and p-value
spearman_corr = pg.corr(data['variable1'], data['variable2'], method='spearman')
print("\nSpearman correlation coefficient:")
print(spearman_corr)

# Kendall correlation coefficient and p-value
kendall_corr = pg.corr(data['variable1'], data['variable2'], method='kendall')
print("\nKendall correlation coefficient:")
print(kendall_corr)

# Non-parametric tests
# Wilcoxon signed-rank test
wilcoxon_test = pg.wilcoxon(data['variable1'], data['variable2'])
print("\nWilcoxon signed-rank test:")
print(wilcoxon_test)

# Mann-Whitney U test
mannwhitneyu_test = pg.mwu(data['variable1'], data['variable2'])
print("\nMann-Whitney U test:")
print(mannwhitneyu_test)