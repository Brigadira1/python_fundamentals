n = int(input("Enter a number: "))

m = n

while m != 0:
    digit = m % 10
    print(digit)
    m = m // 10
