# Generate number from 10 to 50 and add all the generated number

i = 10
list = []
while i >= 10 and i <= 50:
    list.append(i)
    i += 1

sum_list = sum(list)
print(list)
print(sum_list)