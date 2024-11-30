def counter_gen():
    counter = 0
    while True:
        new_counter = yield counter
        if new_counter:
            counter = new_counter
        else:
            counter += 1


gen = counter_gen()
print(gen.send(None))
print(gen.send(None))
print(gen.send(189))
print(gen.send(None))
print(gen.send(5))
print(next(gen))
print(next(gen))
print(next(gen))
