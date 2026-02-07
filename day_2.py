"""
PANDAS – SERIES AND DATAFRAME
Pandas is a powerful Python library used for data analysis,
data manipulation, and data cleaning.
"""

import pandas as pd


# =======================
# 1️⃣ PANDAS SERIES
# =======================

# Create Series from list
data = [1, 2, 3, 4, 5]
series = pd.Series(data)

print("Series from list:\n", series)
print("Type:", type(series))


# Create Series from dictionary
data_dict = {'a': 1, 'b': 2, 'c': 3}
series_dict = pd.Series(data_dict)

print("\nSeries from dictionary:\n", series_dict)


# Custom index
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']

custom_series = pd.Series(data, index=index)
print("\nSeries with custom index:\n", custom_series)



# =======================
# 2️⃣ PANDAS DATAFRAME
# =======================

# Create DataFrame from dictionary of lists
data = {
    'name': ["kaif", "danish", "taleeb", "anna"],
    'age': [21, 23, 43, 21],
    'city': ["sikar", "jaipur", "bangalore", "udaipur"],
    'field': ['ai&ml', 'ai&ml', 'ai&ds', 'ai&ml']
}

df = pd.DataFrame(data)

print("\nDataFrame:\n", df)
print("Type:", type(df))


# Create DataFrame from list of dictionaries
data_list = [
    {'name': "kaif", 'age': 34, 'city': 'bangalore'},
    {'name': "danish", 'age': 30, 'city': 'bangalore'},
    {'name': "taleeb", 'age': 34, 'city': 'bangalore'},
    {'name': "anna", 'age': 24, 'city': 'bangalore'}
]

df2 = pd.DataFrame(data_list)
print("\nDataFrame from list of dictionaries:\n", df2)



# =======================
# 3️⃣ ACCESSING DATA
# =======================

# Access single column
print("\nName Column:\n", df['name'])
print("Column Type:", type(df['name']))  # Series


# Access row using loc (label based)
print("\nRow using loc:\n", df.loc[0])

# Access row using iloc (index based)
print("\nRow using iloc:\n", df.iloc[0])


# Access specific element
print("\nUsing at:", df.at[2, 'city'])
print("Using iat:", df.iat[2, 2])



# =======================
# 4️⃣ DATA MANIPULATION
# =======================

# Add new column
df['salary'] = [23000, 34000, 64000, 23000]
print("\nAfter adding salary column:\n", df)


# Remove column
df.drop('salary', axis=1, inplace=True)
print("\nAfter removing salary column:\n", df)


# Update column values
df['age'] = df['age'] + 1
print("\nAfter incrementing age:\n", df)


# Drop a row
df = df.drop(3)
print("\nAfter dropping row index 3:\n", df)



# =======================
# 5️⃣ DATA INFORMATION
# =======================

# Data types
print("\nData Types:\n", df.dtypes)

# Statistical summary
print("\nStatistical Summary:\n", df.describe())
