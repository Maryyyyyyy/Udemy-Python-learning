# check list item in a list, to display those item which are same object

list = [1,2,3,4,5]
input = int(raw_input("What is the input number?"))

if input is list[0]:
    print("Is the same as the first number.")
elif input is list[1]:
    print("Is the same as the second number.")
elif input is list[2]:
    print("Is the same as the third number.")
elif input is list[3]:
    print("Is the same as the fourth number")
elif input is list[4]:
    print("Is the same as the fifth number.")
else:
    print("Item not in the list")