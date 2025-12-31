import pandas as pd

# ============================================================
# Example dataset (BEFORE CLEANING)
# ============================================================
# index | first_name | last_name    | phone_number        | address                     | do_not_contact
# ----- | ---------- | ------------ | ------------------- | --------------------------- | ---------------
# 0     | Ali        | /Ali__       | 059-123-4567        | Main St, CA, 90001          | n
# 1     | Sara       | 123.Sara/    | (059) 987 6543      | Second St, NY, 10001        | y
# 2     | Omar       | ...Omar      | NaN                 | Third St, TX, 73301         | n
# 3     | Lina       | Lina_        | 059.111.2222        | Fourth St, FL, 33101        | n
# 4     | Lina       | Lina_        | 059.111.2222        | Fourth St, FL, 33101        | n  ← duplicate

# ============================================================
# Read CSV file
# ============================================================

df = pd.read_csv(r"path")

# ============================================================
# 1️⃣ Remove duplicate rows
# ============================================================

df = df.drop_duplicates()

# Expected result:
# - Row index 4 is removed (duplicate of index 3)

# ============================================================
# 2️⃣ Remove unnecessary column
# ============================================================

df = df.drop(columns="col_name")

# ============================================================
# 3️⃣ Clean last_name column
#    Remove numbers and symbols from beginning/end
# ============================================================

# BEFORE:
# /Ali__ , 123.Sara/ , ...Omar , Lina_

df["last_name"] = df["last_name"].str.strip("123._/")

# AFTER:
# Ali , Sara , Omar , Lina

# ============================================================
# 4️⃣ Clean and format phone numbers
# ============================================================

# Convert to string first (important!)
df["phone_number"] = df["phone_number"].astype(str)

# Remove all non-numeric characters
df["phone_number"] = df["phone_number"].str.replace(
    r"[^0-9]", "", regex=True
)

# Format phone numbers as XXX-XXX-XXXX
df["phone_number"] = df["phone_number"].apply(
    lambda x: f"{x[0:3]}-{x[3:6]}-{x[6:10]}" if len(x) == 10 else ""
)

# Expected result:
# 059-123-4567
# 059-987-6543
# ""   ← for NaN or invalid numbers

# ============================================================
# 5️⃣ Split address into multiple columns
# ============================================================

df[["street_address", "state", "zip_code"]] = (
    df["address"].str.split(",", n=2, expand=True)
)

# Example:
# "Main St, CA, 90001"
# →
# street_address = Main St
# state = CA
# zip_code = 90001

# ============================================================
# 6️⃣ Standardize Yes / No values
# ============================================================

# Convert everything to lowercase first
df["do_not_contact"] = df["do_not_contact"].str.lower()

# Replace full words
df["do_not_contact"] = df["do_not_contact"].str.replace("yes", "y")
df["do_not_contact"] = df["do_not_contact"].str.replace("no", "n")

# ============================================================
# 7️⃣ Remove people who do NOT want to be contacted
# ============================================================

df.drop(df[df["do_not_contact"] == "y"].index, inplace=True)

# Sara is removed

# ============================================================
# 8️⃣ Remove rows without phone numbers
# ============================================================

df.drop(df[df["phone_number"] == ""].index, inplace=True)

# Omar is removed (missing phone number)

# ============================================================
# 9️⃣ Reset index after cleaning
# ============================================================

df.reset_index(drop=True, inplace=True)

# ============================================================
# Final cleaned dataset (AFTER CLEANING)
# ============================================================
# index | first_name | last_name | phone_number  | street_address | state | zip_code
# ----- | ---------- | --------- | ------------- | -------------- | ----- | --------
# 0     | Ali        | Ali       | 059-123-4567  | Main St        | CA    | 90001
# 1     | Lina       | Lina      | 059-111-2222  | Fourth St      | FL    | 33101
