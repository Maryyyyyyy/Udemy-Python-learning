#get two number fomr the user, whether they are same objects or not.

a = int(raw_input("What is the first number?"))
b = int(raw_input("What is the second number?"))

if a is b:
    print("Both numbers are the same")
else:
    print("Not same number")

print(id(a))
print(id(b))