import sys

f = open(sys.argv[1], mode='rt', encoding='utf-8')
i = 0
for line in f:
    print(line)
    i += 1

print(f"The files has {i} lines total")
f.close()


