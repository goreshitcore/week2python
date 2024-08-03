import numpy as np

# Create a 2x3 two-dimensional array filled with ones
arr = np.ones((2, 3), dtype=int)

# Prompt the user for values for the 2nd row
row2_values = input("Enter values for the second row (comma-separated):\n")
#row2_values = [int(float(val)) for val in row2_values.split(",")]
row2_values = [int(val) if val.isdigit() else float(val) for val in row2_values.split(",")]

print("Two-dimensional array:")
# Populating the array with user-provided values for the 2nd row
arr[1,:] = row2_values

# Displaying the array
print(arr)   
