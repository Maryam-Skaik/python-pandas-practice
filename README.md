# 🐼 Pandas Fundamentals – Practice Repository

This repository contains my **hands-on practice and notes while learning Pandas** through the following YouTube playlist:

### 🔗 Pandas Tutorial Playlist
https://www.youtube.com/playlist?list=PLUaB-1hjhk8GZOuylZqLz-Qt9RIdZZMBE

All code files were written **step by step while watching the videos**, with added comments, examples, and expected outputs to reinforce understanding.

---

## 🎯 Learning Objectives

- Understand Pandas core data structures (Series & DataFrame)
- Load data from multiple file formats
- Filter, sort, and index data efficiently
- Perform grouping and aggregation
- Merge, join, and concatenate DataFrames
- Visualize data using Pandas + Matplotlib
- Clean messy, real-world datasets
- Perform Exploratory Data Analysis (EDA)

---

## 📂 Repository Structure (All files in root)

Each file corresponds to one topic/video from the playlist:

```pgsql
.
├── 01_read_in_files.py
├── 02_filtering_columns_rows.py
├── 03_indexes_in_pandas.py
├── 04_groupby_aggregate_functions.py
├── 05_merging_dataframes.py
├── 06_visualizations_with_pandas.py
├── 07_data_cleaning_in_pandas.py
├── 08_exploratory_data_analysis.py
└── README.md
```

---

## 📘 File Breakdown

### [01_read_in_files.py](01_read_in_files.py)

**Reading data into Pandas**

Covers:

- Reading CSV files (with/without headers)
- Reading TXT (tab-separated) files
- Reading JSON files
- Reading Excel files and sheets
- Display options (`pd.set_option`)
- Basic data access (`head`, `tail`, `shape`, `info`)
- Column and row access using `loc` and `iloc`

---

### [02_filtering_columns_rows.py](02_filtering_columns_rows.py)

**Filtering, sorting, and conditional selection**

Covers:

- Boolean filtering with conditions
- Filtering using `isin()`
- String-based filtering with `str.contains()`
- Setting columns as index for easier querying
- Using `.filter()` for rows and columns
- Sorting by single and multiple columns
- Mixed ascending/descending sorts

Includes **clear example outputs** for each operation.

---

### [03_indexes_in_pandas.py](03_indexes_in_pandas.py)

**Working with indexes**

Covers:

- Setting an index while reading data
- Resetting indexes
- Permanently vs temporarily setting an index
- Accessing rows using `loc` and `iloc`
- Multi-level (hierarchical) indexes
- Sorting by index
- Accessing data in multi-index DataFrames

---

### [04_groupby_aggregate_functions.py](04_groupby_aggregate_functions.py)

**Grouping and aggregation**

Covers:

- `groupby()` on single and multiple columns
- Aggregation functions: `mean`, `sum`, `min`, `max`, `count`
- Using `agg()` with multiple functions
- Grouping with multiple keys
- Summary statistics using `describe()`

Includes **well-structured example tables** and outputs.

---

### [05_merging_dataframes.py](05_merging_dataframes.py)

**Combining DataFrames**

Covers:

- `merge()` (INNER, LEFT, RIGHT, OUTER joins)
- CROSS join
- Index-based `join()`
- `concat()` (row-wise and column-wise)
- Why `append()` is deprecated

Includes **SQL-style explanations and conceptual tables.**

---

### [06_visualizations_with_pandas.py](06_visualizations_with_pandas.py)

**Data visualization using Pandas**

Covers:

- Line plots (single & multiple columns)
- Subplots
- Bar and stacked bar charts
- Horizontal bar charts
- Scatter plots (size & color customization)
- Histograms
- Boxplots
- Area plots
- Pie charts
- Matplotlib styles

Each plot includes **comments describing the expected chart output.**

---

### [07_data_cleaning_in_pandas.py](07_data_cleaning_in_pandas.py)

**Data cleaning & preprocessing**

Covers:

- Removing duplicate rows
- Dropping unnecessary columns
- Cleaning text data with `str.strip()`
- Normalizing phone numbers
- Handling missing values
- Splitting columns into multiple fields
- Standardizing categorical values (yes/no)
- Removing rows based on conditions
- Resetting index after cleaning

Includes:

- **Before-cleaning table**
- **After-cleaning table**
- **Clear step-by-step transformations**

---

### [08_exploratory_data_analysis.py](08_exploratory_data_analysis.py)

**Exploratory Data Analysis (EDA)**
*(Dataset based on population statistics)*

Covers:

- Dataset overview with `info()`
- Statistical summaries using `describe()`
- Missing value detection
- Cardinality checks with `nunique()`
- Sorting to find top/bottom values
- Correlation analysis
- Heatmaps using Seaborn
- Data transposition
- Trend plots
- Histograms and boxplots for distribution & outliers

**Demonstrates how EDA guides data understanding before modeling.**

---

## 🛠 Tools & Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## ⚠️ Disclaimer

This repository is created **strictly for educational purposes.**
All code reflects **personal practice and understanding** while following the tutorial playlist.
