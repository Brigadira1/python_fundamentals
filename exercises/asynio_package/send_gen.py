def generate_numbers():
    i = 0
    while i < 10:
        i += 1
        print(f"IN GENERATOR: {i=}")
        from_send = yield i
        print(f"GENERATOR: This was sent to me from the main() function: {from_send}")


gen = generate_numbers()
for num in gen:
    print(f"\nMAIN: Number {num} received from the generator in main()")
    gen.send(f"SEND_FROM_MAIN: {num}")
