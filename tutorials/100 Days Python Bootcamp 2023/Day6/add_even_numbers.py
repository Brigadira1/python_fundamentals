sum_even = 0
for num in range(2, 101, 2):
    if num % 2 == 0:
        sum_even += num
        print(f"Adding {num} to the sum as it is an even number. The sum of all even number now becomes equal to {sum_even}")

print(f"The sum of all even numbers between 2 and 100 is {sum_even}")
