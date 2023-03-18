import math as m


n = int(input("Enter n = "))
x = int(input("Enter x = "))

a = 5
k = 1
l = 2

sum = 0

for i in range(0, n):

    sum += ((x * a) ** 2) / (k + m.factorial(l))
    a = a * 5
    k = k + 1
    l = l + 1

print(sum)