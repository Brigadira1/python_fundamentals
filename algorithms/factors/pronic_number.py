n = int(input("Enter a number: "))


for i in range(2, n):
    is_pronic = False
    if n % i == 0:
        if i * (i + 1) == n:
            print(f"{n} is a Pronic number!")
            is_pronic = True
            break

if not is_pronic:
    print(f"{n} is not a Pronic number")