# Get start and end number from user to generate a sequence of number

first = int(raw_input("Enter first number: "))
second = int(raw_input("Enter end number: "))

list = []

if first < second: 
    for i in range(first, second+1):
        list.append(i)
        i += 1
else: 
    print("First number should be smaller than last number")

print(list)