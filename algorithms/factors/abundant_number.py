n = int(input("Enter a number: "))

fact_sum = 0

for i in range(1, n):
    if n % i == 0:
        fact_sum += i

if fact_sum > n:
    print(f"{n} is an Abundant number")
else:
    print(f"{n} is not an Abundant number")