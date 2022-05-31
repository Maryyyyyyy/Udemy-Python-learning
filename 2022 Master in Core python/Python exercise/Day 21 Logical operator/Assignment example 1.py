# Check valid user name and password
username = "Chunmo Chen"
pwd = "abc"

name = str(raw_input("What is your user name?"))
password = str(raw_input("What is your password?"))

if name == username and password == pwd:
    print("Welcome!")
else:
    print("Sorry, the username is unmatched")