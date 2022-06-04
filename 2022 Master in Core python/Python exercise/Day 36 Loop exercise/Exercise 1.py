# Get a number from user to display table of that number using while loop
num = int(raw_input("Enter the number: "))
i = 1
list = []
while i <= 10:
    print(str(num) + "*" + str(i) + "=" + str(num*i))
    i +=1
