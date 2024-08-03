import numpy as np

# Creating a 2x3 two-dimensional array
array_2d = np.zeros((2, 3), dtype=int)

# Prompting the user to populate the array
for i in range(2):
    row_values = input(f"\nEnter values for row {i+1} (comma-separated): ")
    row_values = [int(x) for x in row_values.split(',')]
    array_2d[i] = row_values

# Accessing the element at row 1 column 1
accessed_element = array_2d[1, 1]

# Printing the value of the accessed element
print(f"\nValue at row 2, column 2: {accessed_element}")
