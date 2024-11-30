import asyncio
import time


async def main():
    print("Entering the main() coroutine...")
    task = asyncio.create_task(coroutine())
    await asyncio.sleep(0.5)
    print(f"Is task cancelled the firts time: {task.cancel()}")
    await asyncio.sleep(0.1)
    is_cancelled = task.cancelled()
    print(f"Is the task cancelled second time: {is_cancelled}")


async def coroutine():
    t1 = time.perf_counter()
    print("Executing coroutine...")
    await asyncio.sleep(1)
    print(f"Time for sleeping of the coroutine is {time.perf_counter() - t1}")


if __name__ == "__main__":
    asyncio.run(main())
