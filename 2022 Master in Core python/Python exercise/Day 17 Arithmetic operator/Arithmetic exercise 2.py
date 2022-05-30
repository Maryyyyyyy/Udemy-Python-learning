# Write a program to get 4 number from user, subtract frist two, add 2nd two number, then find multiplication of both results

a = int(raw_input("What is the first number?"))
b = int(raw_input("What is the second number?"))
c = int(raw_input("What is the third number?"))
d = int(raw_input("What is the fourth number?"))

first_subtract = a-b 
second_add = c+d
print(first_subtract * second_add)