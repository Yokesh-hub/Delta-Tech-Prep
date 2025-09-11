# array_manipulation.py

# Step 1: Initialize the array 
print("Starting Array Manipulation Program ")

# Create a list of integers
numbers = [25, 10, 50, 5, 45, 15, 30]

# Print the original array to show the initial state
print("Original array:", numbers)
print("-" * 30)


# Step 2: Find the maximum value 
max_value = numbers[0]

# Iterate through the array to find the largest number
for number in numbers:
    if number > max_value:
        max_value = number

# Print the result
print("Problem 1: Find the maximum value")
print("The maximum value is:", max_value)
print("-" * 30)


# Step 3: Add a new element 
# This shows how to modify the array's size
new_number = 99
numbers.append(new_number)

# Print the updated array
print("Problem 2: Add a new number (99) to the array")
print("Array after addition:", numbers)
print("-" * 30)


# Step 4: Sort the array 
# This shows how to reorder elements in the array
numbers.sort()

# Print the sorted array
print("Problem 3: Sort the array in ascending order")
print("Array after sorting:", numbers)
print("-" * 30)


print("--- Program Finished ---")