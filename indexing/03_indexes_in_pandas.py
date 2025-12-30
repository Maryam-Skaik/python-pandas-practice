import pandas as pd

# ##############################
# 1️⃣ Load the data with custom index
# ##############################

# Read CSV file and set 'Country' as index
df = pd.read_csv(r"file_path.csv", index_col="Country")

df.head()
# Example output:
#                   first_name second_name  col_name
# Country
# Palestine          Maryam     Skaik       15
# USA                John       Doe         8
# Jordan             Ali        Khan        20
# United Kingdom     Jane       Smith       12

##############################
# 2️⃣ Resetting index
##############################

# Reset index to default integer index
df.reset_index(inplace=True)
df.head()
# Example output:
#    Country         first_name second_name  col_name
# 0  Palestine      Maryam       Skaik       15
# 1  USA            John         Doe         8
# 2  Jordan         Ali          Khan        20
# 3  United Kingdom Jane         Smith       12

##############################
# 3️⃣ Setting a new index
##############################

# Set 'Country' as index again (does not modify df permanently)
df.set_index('Country', inplace=False).head()

# Save the new index permanently
df.set_index('Country', inplace=True)
df.head()

##############################
# 4️⃣ Accessing rows by index
##############################

# Using loc with index label
df.loc['Palestine']
# Example output:
# first_name    Maryam
# second_name   Skaik
# col_name      15
# Name: Palestine, dtype: object

# Using iloc with integer position (Palestine is now at position 0)
df.iloc[0]
# Example output: same as above

##############################
# 5️⃣ Multi-level (Hierarchical) index
##############################

# Reset index first
df.reset_index(inplace=True)

# Set multi-index using 'first_name' and 'second_name'
df.set_index(['first_name', 'second_name'], inplace=True)
df.head()
# Example output:
#                           Country  col_name
# first_name second_name
# Maryam     Skaik          Palestine   15
# John       Doe            USA         8
# Ali        Khan           Jordan      20
# Jane       Smith          United Kingdom 12

##############################
# 6️⃣ Sorting by index
##############################

# Sort by index (ascending)
df.sort_index(ascending=True).head()

# Sort by index (descending)
df.sort_index(ascending=False).head()

# Sort by multi-index with mixed order
df.sort_index(ascending=[True, False]).head()

##############################
# 7️⃣ Accessing rows with multi-index
##############################

# Access all rows with first_name = 'Maryam'
df.loc['Maryam']
# Example output:
#             Country    col_name
# second_name
# Skaik       Palestine 15

# Access a specific row with both levels of index
df.loc[('Maryam', 'Skaik')]
# Example output:
# Country     Palestine
# col_name           15
# Name: (Maryam, Skaik), dtype: object

# Using iloc for integer-based selection
df.iloc[0]
# Example output: same as above
