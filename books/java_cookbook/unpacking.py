data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, share, price, date = data

print(name)
print(share)
print(price)
print(date)

_, share, price, _ = data
print(share)
print(price)

name, *_, (*_, year) = data
print("Prints only the name of the company and the year!")
print(name)
print(year)

n, s, p, (year, mon, day) = data
print(year)
print(mon)
print(day)

s = 'Hello'
a, b, c, d, e = s
print(a)
print(b)
print(c)
print(d)
print(e)

record = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for a, b, c in record:
    print(a)
    print(b)
    print(c)

for tuple in record:
    print(tuple)