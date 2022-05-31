# Get short name of week and display full name of week.Mon/mon --> Monday

name = str(raw_input("Enter the week: "))

if name == "mon" or name == "Mon":
    print("Monday")
elif name == "tue" or name == "Tue":
    print("Tuesday")
elif name == "wed" or name == "Wed":
    print("Wednesday")
elif name == "thur" or name == "Thur":
    print("Thursday")
elif name == "fri" or name == "Fri":
    print("Friday")
elif name == "sat" or name == "Sat":
    print("Saturday")
elif name == "sun" or name == "Sun":
    print("Sunday")
else: 
    print("Not match. ")