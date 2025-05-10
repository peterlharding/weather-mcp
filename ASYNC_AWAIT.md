# Invoking Async Functions at the Outer Level in Python

To invoke an async function at the outer (top) level in Python, you have several options:

## Option 1: Using asyncio.run() (Python 3.7+)

```
pythonimport asyncio

async def my_async_function():
    print("Inside async function")
    await asyncio.sleep(1)
    return "Completed"

# Outer level invocation
result = asyncio.run(my_async_function())
print(result)
```

This is the recommended approach for Python 3.7 and later. The asyncio.run() function handles creating and managing the event loop for you.

## Option 2: Using event loop explicitly

```
pythonimport asyncio

async def my_async_function():
    print("Inside async function")
    await asyncio.sleep(1)
    return "Completed"

# Get the event loop and run the coroutine
loop = asyncio.get_event_loop()
result = loop.run_until_complete(my_async_function())
print(result)

## Option 3: Using IPython/Jupyter notebooks

If you're in an IPython or Jupyter environment, you can use:

```
pythonimport asyncio

async def my_async_function():
    print("Inside async function")
    await asyncio.sleep(1)
    return "Completed"

# Use this in Jupyter notebooks
await my_async_function()
```

## Option 4: Using nest_asyncio for nested event loops

In situations where you need to run async code within another async context:

```
pythonimport asyncio
import nest_asyncio

# Apply nest_asyncio patch
nest_asyncio.apply()

async def my_async_function():
    print("Inside async function")
    await asyncio.sleep(1)
    return "Completed"

# Now you can run asyncio.run() inside another async function
asyncio.run(my_async_function())
```


Would you like me to explain any of these approaches in more detail?

