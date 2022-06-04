# Generate odd number from 1 to 20 and generate even number from 20 to 1. Then add both result to each other

sum1 = 0
sum2 = 0

for i in range(1, 21):
    if i % 2 == 1:
        sum1 +=i 
        i += 1
    else:
        i += 1

for n in range(20,1, -1):
    if n % 2 == 0:
        sum2 += n
        n -= 1
    else:
        n -= 1
print(sum1)
print(sum2)



