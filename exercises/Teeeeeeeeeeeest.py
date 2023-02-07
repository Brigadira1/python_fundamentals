


a = input("Enter a string: ")
b = input("Enter another string: ")

count = 0


for i in range(len(a) - 1):
    if (b == a[i: i + len(b)]):
        count += 1

print(count)
