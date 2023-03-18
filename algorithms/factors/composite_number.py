n = int(input("Enter a number: "))

count = 0

for i in range(2, n):
    if n % i == 0:
        count += 1

if count >= 2:
    print(f"{n} is a composite number")
else:
    print(f"{n} is not a composite number")