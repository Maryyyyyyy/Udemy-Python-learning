# Get name from user and display the name. The name should contain 5 character and less than 10. Name should start from "a" character

name = str(raw_input("Enter the username: "))

if len(name) > 5 and len(name) < 10:
    if name[0] =="a": # name.startwith("a")
        print("Welcome, "+ name+ "!")