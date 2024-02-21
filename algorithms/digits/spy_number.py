n = int(input("Enter a number: "))

m = n

sum_digits = 0
mult_digits = 1

while m != 0:
    current_digit = m % 10
    sum_digits += current_digit
    mult_digits *= current_digit
    m = m // 10

if sum_digits == mult_digits:
    print(f"{n} is a Spy number.")
else:
    print(f"{n} is not a Spy number.")