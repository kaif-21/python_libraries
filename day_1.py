import numpy as np

# =========================================
# 1️⃣ Creating NumPy Arrays
# =========================================

# 1D Array
arr = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr)
print("Type:", type(arr))
print("Shape:", arr.shape)

# Reshape (1 row, 5 columns)
arr1 = arr.reshape(1, 5)
print("Reshaped Array:\n", arr1)

# 2D Array
arr_2d = np.array([[1,2,3,4,5],
                   [1,2,3,4,5]])
print("\n2D Array:\n", arr_2d)
print("Shape:", arr_2d.shape)

# 3D Array
arr_3d = np.array([[[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [3,4,5]]])
print("\n3D Array:\n", arr_3d)
print("Shape:", arr_3d.shape)


# =========================================
# 2️⃣ Special NumPy Arrays
# =========================================

print("\nArange:", np.arange(0,10,5))
print("\nOnes Matrix:\n", np.ones((5,5)))
print("\nIdentity Matrix:\n", np.eye(3))


# =========================================
# 3️⃣ Attributes of NumPy Array
# =========================================

ar = np.array([[1,2,3],
               [4,6,7]])

print("\nArray:\n", ar)
print("Shape:", ar.shape)
print("Number of dimensions:", ar.ndim)
print("Size (total elements):", ar.size)
print("Data type:", ar.dtype)
print("Item size (bytes):", ar.itemsize)


# =========================================
# 4️⃣ Vectorized Operations
# =========================================

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([10,20,30,40,50])

print("\nAddition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)


# =========================================
# 5️⃣ Universal Functions (ufunc)
# =========================================

arr = np.array([1,2,3,4,5,6])

print("\nSquare Root:", np.sqrt(arr))
print("Exponential:", np.exp(arr))
print("Sine:", np.sin(arr))
print("Natural Log:", np.log(arr))


# =========================================
# 6️⃣ Array Indexing & Slicing
# =========================================

arr = np.array([[1,2,3,4],
                [45,56,67,76],
                [23,43,21,12]])

print("\nArray:\n", arr)

# Access elements
print("First element:", arr[0,0])
print("Second element:", arr[0,1])
print("Third element:", arr[0,2])

# Slicing
print("\nRows 1 onward & Columns 2 onward:\n", arr[1:,2:])
print("\nFirst 2 rows & Columns 2 onward:\n", arr[0:2,2:])
print("\nRows 1 onward & Columns 1-2:\n", arr[1:,1:3])


# =========================================
# 7️⃣ Modify Array Elements
# =========================================

arr[0,0] = 100
print("\nAfter modifying one element:\n", arr)

arr[1:] = 100
print("\nAfter modifying rows:\n", arr)


# =========================================
# 8️⃣ Statistical Operations
# =========================================

data = np.array([1,2,3,4,5])

mean = np.mean(data)
std_dev = np.std(data)

normalized_data = (data - mean) / std_dev
print("\nNormalized Data:", normalized_data)


data = np.array([1,2,3,4,5,7,8,9])

print("\nMean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))


# =========================================
# 9️⃣ Logical Operations
# =========================================

data = np.array([1,2,3,4,5,6,7,8,9])

print("\nElements < 5:", data < 5)
print("Elements between 5 and 6:", data[(data >= 5) & (data <= 6)])
