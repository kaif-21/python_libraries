# ==============================
# Data Manipulation & Analysis with Pandas
# ==============================

import pandas as pd

# ==============================
# 1. Load Dataset
# ==============================
df = pd.read_csv(r'C:\Users\mohammed kaif\PycharmProjects\PythonProject3\Student_Mental_health.csv')

# ==============================
# 2. View Data
# ==============================
print("FIRST 5 ROWS:")
print(df.head())

print("\nLAST 5 ROWS:")
print(df.tail())

# ==============================
# 3. Data Summary
# ==============================
print("\nSTATISTICAL SUMMARY:")
print(df.describe())

print("\nDATATYPES:")
print(df.dtypes)

# ==============================
# 4. Handle Missing Values
# ==============================

print("\nMISSING VALUES:")
print(df.isnull().sum())

# Fill numeric columns with mean
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Fill categorical columns with mode
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values handled!")

# ==============================
# 5. Rename Column
# ==============================
if 'Timestamp' in df.columns:
    df = df.rename(columns={'Timestamp': 'date'})

# ==============================
# 6. Change Datatype
# ==============================
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

# ==============================
# 7. Grouping & Aggregation
# ==============================

# Example: count records by date
if 'date' in df.columns:
    grouped = df.groupby('date').size()
    print("\nGROUPED DATA:")
    print(grouped.head())

# ==============================
# 8. Merging DataFrames Example
# ==============================

df1 = pd.DataFrame({
    'key': ['a', 'b', 'c'],
    'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'key': ['a', 'b', 'd'],
    'value2': [4, 5, 6]
})

print("\nOUTER MERGE:")
print(pd.merge(df1, df2, on='key', how='outer'))

print("\nLEFT MERGE:")
print(pd.merge(df1, df2, on='key', how='left'))

print("\nRIGHT MERGE:")
print(pd.merge(df1, df2, on='key', how='right'))

print("\n✅ Data Manipulation Completed Successfully!")
