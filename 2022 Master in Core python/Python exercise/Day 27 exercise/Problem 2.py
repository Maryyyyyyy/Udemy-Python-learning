# Get age of user and convert into seconds

age = float(raw_input("What is the user age?"))
age_into= age *365*24*60*60
print("You are born for "+ str(age_into)+" seconds.")