# Find occurrence of specific student name from a tuple
tuple = ("Mark","Well","Josh","Adam","Ashley","Emily")

student = str(raw_input("What is the student name?"))

if student in tuple:
    print("We have that student.")
else:
    print("Does not have that student")