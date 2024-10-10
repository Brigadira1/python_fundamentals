a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")
a, b, c = (3, 4, 5)
print(f"a={a}, b={b}, c={c}")
beginning, *middle, end = "My Python Experiments Continue"
print(f"beginning={beginning}, middle={middle}, end={end}")

a, [b, c, *rem], *d = [6, [7, 8, 15, 16, 17, 18, 19], 9, 10, 11]
print(f"a={a}, b={b}, c={c}, rem={rem}, d={d}")

# a, [b, [c, d, *rem, e]], f = [1, [2, [3, 4, 5, 6, 7, 8, 9]]], 10
# print(f"a={a}, b={b}, c={c}, d={d}, rem={rem}, e={e}, f={f}")
