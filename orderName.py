# solution

# take input from user
num = int(input("Enter the number of names to insert: "))

# create an empty list
name_list = []

# iterate num times
for i in range(num):
    # take name as input
    name = input("Enter the name: ")
    # append to the list
    name_list.append(name)

# sort list in alphabetical order
name_list.sort()

# print the list
print("The ordered names are:")
for name in name_list:
    print(name)