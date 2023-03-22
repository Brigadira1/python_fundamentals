n = int(input("Enter n: "))

for i in range(0, n):
    for j in range(i + 1):
        print(" ", end= " ")

    for k in range(i, n - 1):
        print("*", end=" ")

    for l in range(i, n):
        print("*", end=" ")


    print()

