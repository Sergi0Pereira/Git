numbers = []

while True:
    num = input("Please enter an integer number (or press enter to finish): ")
    if num == '':
        break
    numbers.append(int(num))

numbers.sort()

print("The ordered numbers are: ")
for n in numbers:
    print(n)