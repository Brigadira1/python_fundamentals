n = 5

# Pattern 0
for i in range(n):
    for j in range (n):
        print("*", end=" ")
    print()

print()


# Pattern 1
for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

print()

# Pattern 3
for i in range(n):
    for j in range(i, n):
        print("*", end=" ")
    print()


# print("\n")
# # Pattern 2
#
# for i in range(0, n):
#     for j in range(0, n):
#         print("*", end="")
#     print("")
#
# print("\n")
# # Pattern 3
#
# for i in range(0, n):
#     for j in range(n-1-i, -1, -1):
#         print("*", end="")
#     print("")
#
# print("\n")
#
# # Pattern 4
#
# for i in range(0, n):
#     for col in range(0, i+1):
#         print(f"{col + 1} ", end="")
#     print("")
#
# print("\n")
#
# # Pattern 5
#
# for row in range(0, 2*n):
#     col = 0
#     if row < n:
#         col = row + 1
#     else:
#         col = 2*n - 1 - row
#     for j in range(0, col):
#         print("*", end="")
#     print("\n", end="")
#
# print("\n")
#
# # Pattern 6


