doubles = [num * 2 for num in range(50)]
print(f"Result: {doubles}")

strings = ["intro", "to", "list", "comprehensions"]
upper = [i.upper() for i in strings]
print(f"Upper is: {upper}")

numbers = list(range(100))
conditions = [i * 3.5 if i % 2 else i for i in numbers if i > 20 and i < 50]
print(f"Result: {conditions}")

nested = [[x * y for y in range(1, 6)] for x in range(1, 11)]
print(f"Result: {nested}")

# The nested example from above is equivalent to the following 'traditional' implementation
result = []
for x in range(1, 11):
    construct_element = []
    for y in range(1, 6):
        construct_element.append(x * y)
    result.append(construct_element)

print(result)
