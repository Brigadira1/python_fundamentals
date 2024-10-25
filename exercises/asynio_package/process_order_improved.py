import asyncio
import time


async def process_order():
    print("Before waiting await from Process Order")
    await asyncio.sleep(1)
    for i in range(3):
        time.sleep(1)
        print(f"Waited {i+1} seconds from Process Order")
    print("Process order slept await for 1 second")
    # time.sleep(3)
    # print("Process Order complete!")


async def process_order1():
    print("Before waiting await from Process Order#1")
    await asyncio.sleep(1)
    for i in range(3):
        time.sleep(1)
        print(f"Waited {i+1} seconds from Process Order#1")
    print("Process order#1 slept await for 1 second")
    # time.sleep(1)
    # print("Order complete!")


async def process_order2(i: int):
    print(f"Coroutine#{i} was executed by the event loop...")
    await asyncio.sleep(1)
    time.sleep(2)
    print(f"Coroutine#{i} finished!")


async def main():
    t1 = time.perf_counter()
    await asyncio.gather(process_order2(1), process_order2(2))
    t2 = time.perf_counter()
    print(f"The time is: {t2 - t1}")
    print("Finished processing.")


asyncio.run(main())
