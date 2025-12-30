import pandas as pd

# --------------------------------------------------
# Example input DataFrames (conceptual)
# --------------------------------------------------
# df1
# +----+----------+-------+
# | id | name     | score |
# +----+----------+-------+
# | 1  | Alice    | 80    |
# | 2  | Bob      | 90    |
# | 3  | Charlie  | 85    |
# +----+----------+-------+

# df2
# +----+----------+---------+
# | id | country  | age     |
# +----+----------+---------+
# | 2  | Jordan   | 22      |
# | 3  | Palestine| 21      |
# | 4  | Egypt    | 23      |
# +----+----------+---------+

df1 = pd.read_csv(r"path_file")
df2 = pd.read_csv(r"another_path_file")


# ==================================================
# MERGE (SQL-style joins)
# ==================================================

# INNER JOIN (default)
df1.merge(df2, on='id')

# Output:
# +----+----------+-------+----------+-----+
# | id | name     | score | country  | age |
# +----+----------+-------+----------+-----+
# | 2  | Bob      | 90    | Jordan   | 22  |
# | 3  | Charlie  | 85    | Palestine| 21  |
# +----+----------+-------+----------+-----+
#
# Explanation:
# - Keeps only matching ids in both DataFrames


# --------------------------------------------------
# OUTER JOIN
# --------------------------------------------------

df1.merge(df2, how='outer', on='id')

# Output:
# +----+----------+-------+----------+-----+
# | id | name     | score | country  | age |
# +----+----------+-------+----------+-----+
# | 1  | Alice    | 80    | NaN      | NaN |
# | 2  | Bob      | 90    | Jordan   | 22  |
# | 3  | Charlie  | 85    | Palestine| 21  |
# | 4  | NaN      | NaN   | Egypt    | 23  |
# +----+----------+-------+----------+-----+
#
# Explanation:
# - Keeps ALL rows from both DataFrames
# - Missing values filled with NaN


# --------------------------------------------------
# LEFT JOIN
# --------------------------------------------------

df1.merge(df2, how='left', on='id')

# Output:
# +----+----------+-------+----------+-----+
# | id | name     | score | country  | age |
# +----+----------+-------+----------+-----+
# | 1  | Alice    | 80    | NaN      | NaN |
# | 2  | Bob      | 90    | Jordan   | 22  |
# | 3  | Charlie  | 85    | Palestine| 21  |
# +----+----------+-------+----------+-----+
#
# Explanation:
# - Keeps ALL rows from df1
# - Adds matching data from df2 only


# --------------------------------------------------
# RIGHT JOIN
# --------------------------------------------------

df1.merge(df2, how='right', on='id')

# Output:
# +----+----------+-------+----------+-----+
# | id | name     | score | country  | age |
# +----+----------+-------+----------+-----+
# | 2  | Bob      | 90    | Jordan   | 22  |
# | 3  | Charlie  | 85    | Palestine| 21  |
# | 4  | NaN      | NaN   | Egypt    | 23  |
# +----+----------+-------+----------+-----+


# --------------------------------------------------
# CROSS JOIN
# --------------------------------------------------

df1.merge(df2, how='cross')

# Output:
# Every row in df1 paired with every row in df2
# Total rows = len(df1) * len(df2)
#
# Example:
# (Alice, Jordan), (Alice, Palestine), (Alice, Egypt),
# (Bob, Jordan), ...


# ==================================================
# JOIN (Index-based)
# ==================================================

df1_idx = df1.set_index('id')
df2_idx = df2.set_index('id')

df1_idx.join(df2_idx, lsuffix='_left', rsuffix='_right')

# Output:
# +----+----------+-------+----------+-----+
# | id | name     | score | country  | age |
# +----+----------+-------+----------+-----+
# | 1  | Alice    | 80    | NaN      | NaN |
# | 2  | Bob      | 90    | Jordan   | 22  |
# | 3  | Charlie  | 85    | Palestine| 21  |
# +----+----------+-------+----------+-----+
#
# Explanation:
# - join() aligns on index
# - Default join type is LEFT


# ==================================================
# CONCATENATION
# ==================================================

pd.concat([df1, df2])

# Output:
# Rows stacked vertically
# Columns not shared become NaN


pd.concat([df1, df2], axis=1)

# Output:
# DataFrames combined side-by-side
# Index alignment is used


# ==================================================
# APPEND (Deprecated)
# ==================================================

# df1.append(df2)  ❌ Deprecated

pd.concat([df1, df2])
# ✅ Recommended replacement
