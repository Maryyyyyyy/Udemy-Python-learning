# list is mutable
list = [2,3,4,5]
#update list the third number into ten
list[2] = 10
print(list)

# Tuple is the immutable
tuple= (2,3,4,5)
#cannot update tuple
tuple[0] = 10
# only give me error code: 'tuple' object does not support item assignment
print(tuple)