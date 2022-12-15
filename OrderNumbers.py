# This program orders the numbers that a user inputs

# Take input from the user
nums = input("Enter a list of numbers, separated by spaces: ")

# Split the input string into a list of numbers
nums = nums.split()

# Convert the items in the list to floats
nums = [float(x) for x in nums]

# Sort the list
nums.sort()

# Print the sorted list
print(nums)