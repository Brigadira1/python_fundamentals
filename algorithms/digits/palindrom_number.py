n = int(input("Enter a number: "))

m = n
reverse_n = 0

while m != 0:
    current_digit = m % 10
    reverse_n = reverse_n * 10 + current_digit
    m = m // 10

if n == reverse_n:
    print(f"{n} is a Palindrome number")
else:
    print(f"{n} is not a Palindrome number")