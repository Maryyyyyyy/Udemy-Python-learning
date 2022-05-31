# Get age and mark from user. Select user have greater or equal to 18 age and marks should be greater than 90 and less than 100

age = int(raw_input("Enter the age: "))
mark = int(raw_input("Enter the mark: "))

if age >= 18:
    if mark > 90 and mark < 100:
        print("You are selected!")