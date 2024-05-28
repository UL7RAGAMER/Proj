import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # Simulate an I/O-bound task
    print("World")

async def main():
    print("Starting...")
    await say_hello()  # Pause here until say_hello() completes
    print("Finished")

# Run the main coroutine
asyncio.run(main())
