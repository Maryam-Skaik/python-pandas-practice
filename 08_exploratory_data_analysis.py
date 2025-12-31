import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ============================================================
# Example Dataset (Population Data) – BEFORE EDA
# ============================================================
# Country        | Year | Population | Growth_Rate | Area_km2
# -------------- | ---- | ---------- | ----------- | ---------
# Palestine      | 2020 | 5101414    | 2.5         | 6220
# Jordan         | 2020 | 10203134   | 1.0         | 89342
# Egypt          | 2020 | 102334404  | 1.9         | 1002450
# Lebanon        | 2020 | 6825442    | 0.3         | 10452
# Syria          | 2020 | NaN        | 2.8         | 185180

# ============================================================
# Read CSV file
# ============================================================

df = pd.read_csv(r"path")

# ============================================================
# Format float numbers for readability
# ============================================================

pd.set_option('display.float_format', lambda x: f"{x:.2f}")

# ============================================================
# Basic overview of the dataset
# ============================================================

df.info()

# Expected output:
# - Column names
# - Non-null counts
# - Data types (int, float, object)
# - Memory usage

# ============================================================
# Statistical summary of numerical columns
# ============================================================

df.describe()

# Expected output (for numeric columns):
# count, mean, std, min, 25%, 50%, 75%, max
# Useful for understanding population ranges and spread

# ============================================================
# Check for missing values
# ============================================================

df.isnull().sum()

# Example output:
# Country         0
# Year            0
# Population      1   ← missing value
# Growth_Rate     0
# Area_km2        0

# ============================================================
# Number of unique values per column
# ============================================================

df.nunique()

# Helps identify:
# - Categorical columns
# - Columns with low/high cardinality

# ============================================================
# Sorting data (Top / Bottom values)
# ============================================================

# Countries with lowest population
df.sort_values(by="Population").head()

# Countries with highest population
df.sort_values(by="Population", ascending=False).head()

# ============================================================
# Value counts (useful for categorical columns)
# ============================================================

df["Country"].value_counts()

# ============================================================
# Correlation Analysis
# ============================================================

df.corr(numeric_only=True)

# Explanation:
# - Correlation measures the linear relationship between numeric variables
# - Values range from -1 to +1
#   +1  → strong positive relationship
#   -1  → strong negative relationship
#   0   → no relationship

# ============================================================
# Correlation Heatmap
# ============================================================

plt.figure(figsize=(12, 6))
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)
plt.title("Correlation Heatmap of Population Dataset")
plt.show()

# Expected result:
# - Clear visual relationships between Population, Growth_Rate, Area

# ============================================================
# Transpose the DataFrame
# Useful for comparing features instead of rows
# ============================================================

df_transposed = df.transpose()

df_transposed.head()

# ============================================================
# Plot numeric trends
# ============================================================

df.select_dtypes(include="number").plot(
    figsize=(14, 6),
    title="Numeric Feature Trends"
)

plt.show()

# ============================================================
# Distribution of population values
# ============================================================

df["Population"].plot(
    kind="hist",
    bins=20,
    title="Population Distribution"
)

plt.xlabel("Population")
plt.ylabel("Frequency")
plt.show()

# ============================================================
# Boxplot for detecting outliers
# ============================================================

df.select_dtypes(include="number").boxplot(figsize=(14, 6))
plt.title("Outlier Detection using Boxplot")
plt.show()

# ============================================================
# Final Notes:
# ============================================================
# - EDA helps understand data quality and structure
# - Detect missing values, outliers, and relationships
# - Guides decisions for data cleaning and modeling
