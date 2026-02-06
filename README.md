# 📊 Python Libraries for Data Analysis & Visualization

This repository demonstrates the basics of some of the most widely used Python libraries in data science: **NumPy, Pandas, Matplotlib, and Seaborn.** These libraries help in numerical computation, data manipulation, and visualization.

## 🚀 Libraries Overview

### 🔹 NumPy
**NumPy (Numerical Python)** is used for fast mathematical operations on arrays and matrices.

**Key Features:**
- Multi-dimensional arrays  
- Mathematical functions  
- Linear algebra support  
- High performance  

**Example:**
```python
import numpy as np

arr = np.array([1,2,3,4])
print(arr * 2)

🔹 Pandas

Pandas is used for data handling and analysis. It works like Excel but is much more powerful.

Key Features:

DataFrames for structured data

Read/write CSV & Excel files

Data cleaning

Filtering & grouping

Example:

import pandas as pd

data = pd.DataFrame({
    "Name": ["Ali", "Kaif"],
    "Marks": [85, 90]
})

print(data)

🔹 Matplotlib

Matplotlib is a plotting library used to create charts and graphs.

Key Features:

Line charts

Bar graphs

Histograms

Scatter plots

Example:

import matplotlib.pyplot as plt

x = [1,2,3]
y = [10,20,30]

plt.plot(x,y)
plt.title("Simple Line Graph")
plt.show()

🔹 Seaborn

Seaborn is built on top of Matplotlib and provides more attractive and informative statistical graphics.

Key Features:

Better visual styles

Statistical plots

Heatmaps

Distribution plots

Example:

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.histplot(tips["total_bill"])

plt.show()

📌 Why Learn These Libraries?

These libraries are essential for Data Science, Machine Learning, Artificial Intelligence, Data Visualization, and Research & Analytics. Mastering them helps build a strong foundation for working with real-world data.

⚙️ Installation
pip install numpy pandas matplotlib seaborn

🎯 Conclusion

NumPy, Pandas, Matplotlib, and Seaborn form the core toolkit for anyone starting with data analysis in Python. Learning them will significantly improve your ability to analyze and visualize data effectively.
