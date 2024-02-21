n = 4
a = 1
sum = 0

for i in range(0, n):
    if i % 2 == 0:
        sum = sum + a
    else:
        sum = sum - a

    a = a + 1

print(sum)
