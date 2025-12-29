import pandas as pd

# to read a .csv file
df = pd.read_csv(r"path of the file", header=None, name=['first_name', 'second_name'])
# df is data frame,
# index added automatically 


##############

# import .txt files 
# we can import it with read_csv also, but data will returned without separator 
# to add separator, we can use sep
df = pd.read_csv(r"path of the file", sep="\t")

# or we can use read_table
df = pd.read_table(r"path of the file")


# note: also read_table can used to read csv files, but same we must add separator.

#################

# reading json files
df = pd.read_json(r"path of the file")

#################

# reading excel files
df = pd.reas_excel(r"path of the file")
# will read the first sheet only.

df = pd.reas_excel(r"path of the file", sheet_name="sheet_1")

#####################
# all previous data frames, just return first and last 5 rows

pd.set_option("display.max.rows", 235)

#####################

# to got information about data frame, or the shape 
df.info()
df.shape # (230, 4)


########

# to got first five rows
df.head()

# also we can specify 
df.head(10)

# same for last
df.tail()
df.tail()

########
df['column name']
df.loc[row number]

df.iloc[row number]
