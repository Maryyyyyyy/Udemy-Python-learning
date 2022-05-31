# Get age and name of student and display age and number of the user. If age is greater than 19, otherwise a error message

age = int(raw_input("Enter the age: "))
name = str(raw_input("Enter the name: "))

if age >= 18:
    print("Welcome, "+ str(name)+", age of "+str(age)+ "!")
else:
    print("Error ...")