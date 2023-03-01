# Upon creation time set() removes the duplicates
a = {1, 2, 3, 4, 5, 5, 5, 7, 38, 21, 2, 1}
set1 = set(a)
print(set1)

# How to add el in the set
a.add(999)
print(a)

# Adding an already existing el, preserves the set and doesn't add the el
a.add(999)
print(a)

# Removing an el from the set
a.remove(999)
print(a)

# Removing a non-existing el throws KeyError exception
try:

    a.remove(999)
    print(a)

except KeyError:
    print("There is no such el in the set: 999")

# We can remove an el from the set without getting an error using the discard() method
a.discard(6758678)
print(a)

# Removing an arbitrary el from the list
element = a.pop()
print(element)
print(a)

# Updates a set with the elements of an iterable
b = {1, 2}
c = (3, 4)
d = [5, 6]

b.update(c, d)
print(b)

# Iterating over the elements of the set
for el in a:
    print(el)

for index, value in enumerate(a):
    print(f"Index: {index}, Value: {value}")  # Showing the index of each el and its value

a = {1, 2, 3, 6}
b = {1, 2, 3, 4, 5, 6}
c = (6, 7, 8, 9, 10)
d = {1, 2, 3, 4}

print(f"Intersection of two sets (all their common elements: {a.intersection(b)}")

# Intersection can be done when more than one set is passed as argument
print(f"Intersection can be done among  more than two iterables: {a.intersection(b, c)}")
# Intersection can be done with shorthand operator
print(f"Using the shorthand operator for making intersection between sets: {a & b}")

# Difference between two sets shows only the elements available in the first set
print(f"Difference between b and a is: {b.difference(a)}")
# Shorthand operator can be used for showing the difference as well
print(f"Difference between b and a is: {b - a}")

# We can check whether a set is subset of another set
print(f"Set {d} is subset of set {b}: {d.issubset(b)}")

# Symmetric difference shows only the elements that are not part of two sets intersection.
print(f"Symmetric difference between {a} and {d} is: {a.symmetric_difference(d)}")

# There is a shorthand operator for symmetric difference as well
print(f"Symmetric difference between {a} and {d} is: {a ^ d}")







