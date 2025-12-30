import pandas as pd

#######################
# 1️⃣ Reading CSV files
#######################

# Read a CSV file without headers
# Provide your column names using 'names' argument
df = pd.read_csv(r"path/to/file.csv", header=None, names=['first_name', 'second_name'])
# df is a DataFrame
# Index is automatically added

# Preview first 5 rows
df.head()  # e.g., returns first 5 rows

# Preview last 5 rows
df.tail()  # e.g., returns last 5 rows

# Shape of DataFrame
df.shape   # e.g., (230, 2)

# Info about DataFrame
df.info()

#######################
# 2️⃣ Reading TXT files
#######################

# If the file is tab-separated, provide 'sep' argument
df_txt = pd.read_csv(r"path/to/file.txt", sep="\t")

# Or use read_table (equivalent)
df_txt2 = pd.read_table(r"path/to/file.txt", sep="\t")

#######################
# 3️⃣ Reading JSON files
#######################

df_json = pd.read_json(r"path/to/file.json")

#######################
# 4️⃣ Reading Excel files
#######################

# Read the first sheet by default
df_excel = pd.read_excel(r"path/to/file.xlsx")

# Specify a sheet
df_excel_sheet1 = pd.read_excel(r"path/to/file.xlsx", sheet_name="sheet_1")

#######################
# 5️⃣ Display Options
#######################

# Increase number of rows displayed
pd.set_option("display.max.rows", 235)

#######################
# 6️⃣ Accessing data
#######################

# Access a single column
df['first_name']  # returns Series

# Access rows by label/index
df.loc[0]         # first row by index label

# Access rows by integer position
df.iloc[0]        # first row by integer position
