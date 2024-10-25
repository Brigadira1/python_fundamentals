import asyncio
import time


async def process_order():
    await asyncio.sleep(1)
    print("Order complete!")


async def main():
    t1 = time.perf_counter()
    await process_order()
    await process_order()
    t2 = time.perf_counter()
    print(f"The time is: {t2 - t1}")
    print("Finished processing.")


asyncio.run(main())
