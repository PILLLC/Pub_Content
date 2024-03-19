
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5,6])

# Print the array
print("Original array:")
print(arr)

# Reshape the array to a 2x3 matrix
reshaped_arr = arr.reshape(2, 3)

# Print the reshaped array
print("\nReshaped array:")
print(reshaped_arr)

# Indexing: Accessing elements of the array
print("\nAccessing elements of the array:")
print("Element at index 0:", arr[0])  # Accessing the first element
print("Element at index 2:", arr[2])  # Accessing the third element

# Slicing: Accessing a subset of the array
print("\nAccessing a subset of the array:")
print("Elements from index 1 to 3:", arr[1:4])  # Accessing elements from index 1 to 3