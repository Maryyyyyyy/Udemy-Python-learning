# Check whether user name or password is correct or not
username = "Chunmo Chen"
pwd = "abc"

name = str(raw_input("What is your user name?"))
password = str(raw_input("What is your password?"))

if name == username and password == pwd:
    print("Welcome!")
elif name == username or password == pwd:
    print("Sorry, the username and password is unmatched")
else:
    print("Do not have account. ")