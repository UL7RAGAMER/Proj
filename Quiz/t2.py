import asyncio

async def wait_until(condition):
    while not condition():
        await asyncio.sleep(1)  # Wait for 1 second before checking the condition again

async def main():
    # Define a condition function
    def check_condition():
        return input("Enter 'y' to proceed: ").lower() == 'y'
    
    # Wait until the condition is met
    print("Waiting for condition to be met...")
    await wait_until(check_condition)
    
    # Condition met, proceed to next iteration
    print("Condition met! Proceeding to next iteration.")

# Run the main coroutine
asyncio.run(main())
