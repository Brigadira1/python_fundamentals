memo = {}

def fib(n):
    if n == 0 or n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = fib(n - 1) + fib(n - 2)
        memo[n] = result
        return result


print(fib(100))

