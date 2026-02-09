"""
Reading Data from Different Sources using Pandas
Sources Covered:
1. JSON String
2. CSV File
3. HTML Tables (Website)
"""

import pandas as pd
from io import StringIO


# =====================================
# 1️⃣ Reading Data from JSON String
# =====================================

json_data = '''
{
    "employee_name": "Kaif",
    "email": "kaifc@gmail.com",
    "job_profile": [
        {"title1": "Team Lead", "title2": "Sr. Developer"}
    ]
}
'''

df_json = pd.read_json(StringIO(json_data))

print("JSON Data:")
print(df_json)

print("\nJSON -> Index Format")
print(df_json.to_json(orient='index'))

print("\nJSON -> Records Format")
print(df_json.to_json(orient='records'))


# =====================================
# 2️⃣ Reading Data from CSV File
# =====================================

csv_path = r'F:\Downloads\student_dataset_large.csv'

df_csv = pd.read_csv(csv_path)

print("\nCSV Data (First 5 Rows):")
print(df_csv.head())


# =====================================
# 3️⃣ Reading Tables from Website (HTML)
# =====================================

url = "https://en.wikipedia.org/wiki/Mobile_Country_code"

tables = pd.read_html(url, match="Country", header=0)

print("\nFirst Table from Website:")
print(tables[0])   # because read_html returns a list
