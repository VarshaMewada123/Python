import asyncio  # Required for async event loop and async tasks

# This is a coroutine function (an async function)
async def download_file(file_name, delay):
    print(f"Started downloading {file_name}...")
    await asyncio.sleep(delay)  # Simulate time delay (non-blocking)
    print(f"Finished downloading {file_name} in {delay} seconds.")

# This is the main coroutine where we run all downloads together
async def main():
#await ka use sirf async def ke andar hi hota hai.
#Agar main() me await likhna hai (jaise await asyncio.gather(...)), 
# toh usse async def main(): banana zaroori ha
    # Create 3 coroutine tasks (they are not running yet)
    task1 = download_file("File1.txt", 3)
    task2 = download_file("File2.txt", 2)
    task3 = download_file("File3.txt", 1)

    # Run all tasks concurrently (at the same time)
    await asyncio.gather(task1, task2, task3)

# This is how we run the main coroutine in a normal Python script
asyncio.run(main())
