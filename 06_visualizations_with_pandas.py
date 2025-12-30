import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------
# Example DataFrame for demonstration
# ------------------------------------------------
# Suppose df looks like this:
# +------------+-------+-------+
# | Date       | A     | B     |
# +------------+-------+-------+
# | 2025-01-01 | 10    | 5     |
# | 2025-01-02 | 15    | 7     |
# | 2025-01-03 | 20    | 12    |
# | 2025-01-04 | 25    | 17    |
# +------------+-------+-------+

df = pd.read_csv(r"file_path")
df = df.set_index('Date')


# =================================================
# LINE PLOTS
# =================================================

# Default line plot (all columns)
df.plot()
# Output: A line chart with Date on x-axis and values of columns A and B

# Explicitly set kind = 'line'
df.plot(kind='line')

# Line plot with subplots (each column in separate chart)
df.plot(kind='line', subplots=True)
# Output: Two separate line charts, one for A, one for B

# Add title
df.plot(kind='line', title="Line Chart Example")

# Add title and labels
df.plot(kind='line', title="Line Chart Example", xlabel="Date", ylabel="Values")

# Check available matplotlib styles
print(plt.style.available)
# Output: List of styles like ['bmh', 'classic', 'ggplot', ...]

# Apply a style
plt.style.use('ggplot')  # Example style

# =================================================
# BAR PLOTS
# =================================================

# Basic bar plot
df.plot(kind='bar')
# Output: Vertical bars for each column grouped by Date

# Stacked bar plot
df.plot(kind='bar', stacked=True)
# Output: Columns stacked in a single bar per Date

# Horizontal bar plot
df.plot.barh(stacked=True)
# Output: Stacked horizontal bars

# Single column bar plot
df['A'].plot(kind='bar')
# Output: Only column A values as bars

# =================================================
# SCATTER PLOTS
# =================================================

# Basic scatter plot
df.plot.scatter(x='A', y='B')
# Output: Points plotted with A on x-axis and B on y-axis

# Adjust marker size
df.plot.scatter(x='A', y='B', s=100)
# Output: Larger points

# Adjust marker color
df.plot.scatter(x='A', y='B', s=100, c='red')
# Output: Red colored points

# =================================================
# HISTOGRAM
# =================================================

df.plot.hist(bins=20)
# Output: Histogram of all numeric columns
# Bins = 20, shows distribution of values

# =================================================
# BOX PLOT
# =================================================

df.boxplot()
# Output: Boxplot per column showing median, quartiles, and outliers

# =================================================
# AREA PLOT
# =================================================

df.plot.area(figsize=(10,5))
# Output: Area plot, filled under the line for each column

# =================================================
# PIE CHART
# =================================================

# Example: Pie chart for column 'A'
df.plot.pie(y='A', figsize=(5,5), autopct='%1.1f%%')
# Output: Pie chart showing percentage contribution of each row in column A
