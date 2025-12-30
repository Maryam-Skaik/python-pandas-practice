import pandas as pd

# ##############################
# 1️⃣ Load the data
# ##############################

# Read a CSV file into a DataFrame
df = pd.read_csv(r"path/to/file.csv")

# Preview first 5 rows
df.head()
# Example output:
#    first_name second_name     Country  col_name
# 0       Maryam       Skaik    Palestine       15
# 1         John       Doe       USA           8
# 2         Ali        Khan     Jordan        20
# 3         Jane       Smith    United Kingdom 12

##############################
# 2️⃣ Filtering columns/rows by condition
##############################

# Filter rows where 'col_name' > 10
df_filtered = df[df['col_name'] > 10]
df_filtered
# Returns rows where col_name > 10
# Example output:
#    first_name second_name     Country  col_name
# 0       Maryam       Skaik    Palestine       15
# 2         Ali        Khan     Jordan        20
# 3         Jane       Smith    United Kingdom 12

##############################
# 3️⃣ Filtering using isin()
##############################

specific_countries = ['Palestine', 'Jordan']
df_filtered = df[df['Country'].isin(specific_countries)]
df_filtered
# Returns rows where Country is either Palestine or Jordan
# Example output:
#    first_name second_name   Country  col_name
# 0       Maryam       Skaik  Palestine       15
# 2         Ali        Khan   Jordan        20

##############################
# 4️⃣ Filtering using str.contains()
##############################

df_filtered = df[df['Country'].str.contains('United')]
df_filtered
# Returns rows where 'Country' contains 'United'
# Example output:
#    first_name second_name         Country  col_name
# 3         Jane       Smith  United Kingdom       12

##############################
# 5️⃣ Setting index for easier filtering
##############################

# Set 'Country' column as index
df2 = df.set_index('Country')
df2.head()
# Example output:
#                   first_name second_name  col_name
# Country
# Palestine           Maryam       Skaik       15
# USA                  John        Doe         8
# Jordan               Ali         Khan       20
# United Kingdom       Jane        Smith      12

##############################
# 6️⃣ Filtering using .filter()
##############################

# Filter rows by index labels (axis=0)
df2.filter(items=['Palestine', 'Jordan'], axis=0)
# Example output:
#           first_name second_name  col_name
# Country
# Palestine   Maryam       Skaik       15
# Jordan        Ali        Khan       20

# Filter columns (axis=1)
df2.filter(items=['first_name', 'second_name'], axis=1)
# Example output:
#                   first_name second_name
# Country
# Palestine           Maryam       Skaik
# USA                  John        Doe
# Jordan               Ali         Khan
# United Kingdom       Jane        Smith

# Filter columns by pattern
df2.filter(like='first', axis=1)
# Example output:
#                   first_name
# Country
# Palestine           Maryam
# USA                  John
# Jordan               Ali
# United Kingdom       Jane

##############################
# 7️⃣ Accessing rows by index
##############################

# Using loc with index label
df2.loc['United Kingdom']
# Example output:
# first_name    Jane
# second_name   Smith
# col_name       12
# Name: United Kingdom, dtype: object

# Using iloc with integer position
df2.iloc[3]
# Example output: same as above

##############################
# 8️⃣ Sorting filtered data
##############################

# Sort filtered DataFrame by one column
df[df['col_name'] > 10].sort_values(by='col_name', ascending=True)
# Example output:
#    first_name second_name         Country  col_name
# 3         Jane       Smith  United Kingdom       12
# 0       Maryam       Skaik        Palestine       15
# 2         Ali        Khan           Jordan       20

# Sort by multiple columns
df[df['col_name'] > 10].sort_values(by=['col_name', 'first_name'], ascending=True)
# Example output:
#    first_name second_name         Country  col_name
# 3         Jane       Smith  United Kingdom       12
# 0       Maryam       Skaik        Palestine       15
# 2         Ali        Khan           Jordan       20

# Mixed ascending/descending
df[df['col_name'] > 10].sort_values(by=['col_name', 'first_name'], ascending=[False, True])
# Example output:
#    first_name second_name         Country  col_name
# 2         Ali        Khan           Jordan       20
# 0       Maryam       Skaik        Palestine       15
# 3         Jane       Smith  United Kingdom       12
