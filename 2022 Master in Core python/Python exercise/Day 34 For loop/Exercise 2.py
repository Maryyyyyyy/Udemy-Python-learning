# Write a python program to generate number from 50 to 1, only odd number and find their sums:

list = [] 

for i in range(49, 0, -2):
    list.append(i)
    sum_list = sum(list)

print(list)
print(sum_list)