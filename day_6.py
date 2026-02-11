"""
DATA VISUALIZATION WITH SEABORN
Seaborn is a Python visualization library based on matplotlib.
It provides a high-level interface for drawing attractive
and informative statistical graphics.
"""

# ==================================
# Import Libraries
# ==================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ==================================
# Load Dataset
# ==================================

sales_df = pd.read_csv(r'F:\Downloads\student_dataset_large.csv')

print("First 5 Rows:\n")
print(sales_df.head())

print("\nColumn Names:\n")
print(sales_df.columns)


# ======================================================
# IMPORTANT:
# Replace 'product' and 'total_sales'
# with EXACT column names from your dataset
# ======================================================


# ==================================
# Bar Plot (Total Sales by Product)
# ==================================

sales_grouped = sales_df.groupby('product')['total_sales'].sum().reset_index()

plt.figure(figsize=(10,6))
sns.barplot(x='product', y='total_sales', data=sales_grouped)

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.show()


# ==================================
# Scatter Plot
# ==================================

plt.figure(figsize=(8,5))
sns.scatterplot(x='total_sales', y='profit', data=sales_df)

plt.title("Sales vs Profit")

plt.show()


# ==================================
# Line Plot
# ==================================

plt.figure(figsize=(8,5))
sns.lineplot(x='product', y='total_sales', data=sales_grouped)

plt.title("Sales Trend")

plt.show()


# ==================================
# Box Plot
# ==================================

plt.figure(figsize=(8,5))
sns.boxplot(x='product', y='total_sales', data=sales_df)

plt.title("Sales Distribution")

plt.show()


# ==================================
# Histogram
# ==================================

plt.figure(figsize=(8,5))
sns.histplot(sales_df['total_sales'], bins=20, kde=True)

plt.title("Sales Frequency")

plt.show()


# ==================================
# KDE Plot
# ==================================

plt.figure(figsize=(8,5))
sns.kdeplot(sales_df['total_sales'], fill=True)

plt.title("Sales Density Curve")

plt.show()


# ==================================
# Correlation Heatmap
# ==================================

plt.figure(figsize=(8,6))

numeric_df = sales_df.select_dtypes(include=['number'])
corr = numeric_df.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.title("Correlation Heatmap")

plt.show()


# ==================================
# Pairplot (Can be slow on large data)
# ==================================

sns.pairplot(numeric_df)

plt.show()
