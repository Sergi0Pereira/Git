n = int(input("How many numbers do you want to order? "))
nums = list(map(int, input("Enter the numbers: ").split()))
nums.sort()
print("The ordered numbers are: ", *nums)