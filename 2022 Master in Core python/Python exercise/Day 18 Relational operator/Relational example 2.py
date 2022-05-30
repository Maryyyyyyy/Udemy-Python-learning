# Get two number from user and display greater number

a = int(raw_input("What is the first number?"))
b = int(raw_input("What is the second number?"))

if a>b:
    print(a)
elif a==b:
    print("Both numbers are equal")
else:
    print(b)