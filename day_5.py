import matplotlib.pyplot as plt
import pandas as pd

# ==============================
# 1. LINE PLOT
# ==============================

x = [1,2,3,4,5]
y = [4,5,3,7,8]

plt.figure(figsize=(6,4))
plt.plot(x, y, color='red', linestyle='--', marker='o')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line Plot')
plt.grid(True)
plt.show()


# ==============================
# 2. MULTIPLE PLOTS (SUBPLOTS)
# ==============================

y2=[1,2,3,4,5]

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.plot(x,y)
plt.title('Plot 1')

plt.subplot(2,2,2)
plt.plot(x,y2)
plt.title('Plot 2')

plt.subplot(2,2,3)
plt.plot(y,y2)
plt.title('Plot 3')

plt.subplot(2,2,4)
plt.plot(x,y,color='orange')
plt.title('Plot 4')

plt.tight_layout()
plt.show()


# ==============================
# 3. BAR PLOT
# ==============================

category=['A','B','C','D','E']
values=[5,6,7,8,9]

plt.figure(figsize=(6,4))
plt.bar(category, values, color='green')
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.show()


# ==============================
# 4. HISTOGRAM
# ==============================

data=[1,2,3,4,5,5,5,6,7,8,6,5,7]

plt.figure(figsize=(6,4))
plt.hist(data, bins='auto', color='yellow', edgecolor='black')
plt.title('Histogram')
plt.show()


# ==============================
# 5. SCATTER PLOT
# ==============================

x=[1,2,3,4,5]
y=[6,7,8,9,10]

plt.figure(figsize=(6,4))
plt.scatter(x,y,color='blue')
plt.title('Scatter Plot')
plt.show()


# ==============================
# 6. PIE CHART
# ==============================

labels=['A','B','C','D','E']
sizes=[10,20,30,40,50]
explode=(0.2,0,0,0,0)

plt.figure(figsize=(6,6))
plt.pie(
    sizes,
    explode=explode,
    labels=labels,
    autopct='%1.1f%%',
    shadow=True
)
plt.title('Pie Chart')
plt.show()


# ==============================
# 7. REAL DATASET EXAMPLE
# ==============================

student_data_df = pd.read_csv(r'F:\Downloads\student_dataset_large.csv')

print(student_data_df.head())
print(student_data_df.info())


# ✅ Count students by gender (Correct way)
gender_count = student_data_df['Gender'].value_counts()

plt.figure(figsize=(6,4))
gender_count.plot(kind='bar', color='gold')
plt.xlabel('Gender')
plt.ylabel('Number of Students')
plt.title('Total Students by Gender')
plt.show()


# ✅ Top 10 student name occurrences
student_count = student_data_df['Name'].value_counts().head(10)

plt.figure(figsize=(8,4))
student_count.plot(kind='bar')
plt.title('Top 10 Student Occurrences')
plt.show()