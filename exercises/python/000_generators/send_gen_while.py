import random


def generate_numbers():
    i = 0
    while i < 10:
        i += 1
        from_send = yield i
        print(f"GENERATOR: This was sent to me from the main() function: {from_send}")


gen = generate_numbers()
while True:
    try:
        num = next(gen)  # Start the generator
        print(f"\nMAIN: Number {num} received from the generator in main()")
        value = gen.send(f"SEND_FROM_MAIN: {random.randint(1000, 2000)}")
        print(f"Value right after the send function is: {value}")
        # missing_value = gen.send(f"SEND_FROM_MAIN: {num}")
        # print(f"The missing value is: {missing_value}")
    except StopIteration:
        break
