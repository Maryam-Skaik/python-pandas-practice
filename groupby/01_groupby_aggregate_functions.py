import pandas as pd

# ##############################
# 1️⃣ Load data
# ##############################

df = pd.read_csv(r"file_path.csv")

# Example df:
#    Country      Sales  Quantity
# 0  USA          200    5
# 1  USA          150    2
# 2  Jordan       300    8
# 3  Palestine    250    6
# 4  Jordan       100    3

##############################
# 2️⃣ Grouping by a single column
##############################

group_by_country = df.groupby('Country')
# group_by_country is a DataFrameGroupBy object

# Compute mean for numeric columns
group_by_country.mean()
# Example output:
#           Sales  Quantity
# Country
# Jordan      200       5.5
# Palestine   250       6.0
# USA         175       3.5

# Or directly
df.groupby('Country').mean()

##############################
# 3️⃣ Counting rows in each group
##############################

df.groupby('Country').count()
# Example output:
#           Sales  Quantity
# Country
# Jordan       2       2
# Palestine    1       1
# USA          2       2

##############################
# 4️⃣ Other aggregation functions
##############################

df.groupby('Country').min()
df.groupby('Country').max()
df.groupby('Country').sum()

##############################
# 5️⃣ Using agg() for multiple functions
##############################

# Aggregation with multiple functions on numeric columns
df.groupby('Country').agg({
    'Sales': ['mean', 'max', 'count', 'sum'],
    'Quantity': ['mean', 'max', 'count', 'sum']
})
# Example output:
#           Sales                  Quantity
#           mean   max count  sum     mean  max count sum
# Country
# Jordan    200    300  2     400     5.5   8    2   11
# Palestine 250    250  1     250     6.0   6    1   6
# USA       175    200  2     350     3.5   5    2   7

##############################
# 6️⃣ Grouping by multiple columns
##############################

df.groupby(['Country', 'Quantity']).mean()
# Example output:
#                     Sales
# Country   Quantity
# Jordan    3          100
#           8          300
# Palestine 6          250
# USA       2          150
#           5          200

# Aggregation with multiple columns/functions on multi-level groups
df.groupby(['Country', 'Quantity']).agg({
    'Sales': ['mean', 'max', 'count', 'sum']
})

##############################
# 7️⃣ Summary statistics with describe()
##############################

df.groupby('Country').describe()
# Example output:
#          Sales                                           Quantity
#          count   mean   std    min   25%   50%   75%   max    count  mean  std min 25% 50% 75% max
# Country
# Jordan   2      200    141.4 100   150   200   250   300    2     5.5   3.5 3 4 5 7 8
# Palestine1      250    NaN   250   250   250   250   250    1     6.0   NaN 6 6 6 6 6
# USA      2      175    35.3 150   162.5 175   187.5 200    2     3.5   1.5 2 3 4 3 5
