# Find occurrence of specific color from a list

color = ["red", "orange", "blue", "white"]

colorinput = str(raw_input("What is the color? "))

if colorinput in color:
    print("The color is in the list")
else:
    print("Does not have the color. ")