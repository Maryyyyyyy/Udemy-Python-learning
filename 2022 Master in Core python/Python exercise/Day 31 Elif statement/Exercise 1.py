# Get a number from user to check whether it is positive, negative or equal to zero

num = int(raw_input("Enter the number: "))

if num > 0:
    print(str(num)+" is a positive number.")
elif num < 0:
    print(str(num)+" is a negative number.")
elif num == 0:
    print("You are entering 0.")