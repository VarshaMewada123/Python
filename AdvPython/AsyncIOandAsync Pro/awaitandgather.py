import asyncio
import time

# Async function to simulate a task with delay
async def task(name, delay):
    print(f"{name} started...")
    await asyncio.sleep(delay)
    print(f"{name} finished after {delay} seconds.")

# Sequential version: runs tasks one by one
async def run_sequential():
    print("\n--- Running tasks sequentially ---")
    start = time.time()
    await task("Task 1", 2)
    await task("Task 2", 2)
    await task("Task 3", 2)
    end = time.time()
    print(f"Sequential total time: {end - start:.2f} seconds\n")

# Concurrent version: runs all tasks together
async def run_concurrent():
    print("\n--- Running tasks concurrently with gather() ---")
    start = time.time()
    await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 2),
        task("Task 3", 2)
    )
    end = time.time()
    print(f"Concurrent total time: {end - start:.2f} seconds\n")

# Main function to call both
async def main():
    await run_sequential()
    await run_concurrent()

# Run the main coroutine
asyncio.run(main())
