# Get six subjects from user to display total, average and percentage of that mark

mark = list(raw_input("Enter the numbers: "))

grade = [i for i in mark if i != ","]
grade = [int(i) for i in grade]
total = sum(grade)
average = total / len(grade)

print("Total is "+str(total))
print("Average is "+ str(average))
