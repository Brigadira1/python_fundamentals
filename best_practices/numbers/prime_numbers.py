a = int(input("Enter a number: "))

def is_prime(a):

    if a == 1:
        return False
    for number in range(2, a):
        if(a%number == 0):
            return False

    return True

if is_prime(a):
    print(f"{a} is a prime number")
else:
    print(f"{a} is not prime number")