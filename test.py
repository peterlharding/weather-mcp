#!/usr/bin/env python

import asyncio

async def my_async_function():
    print("Inside async function")
    await asyncio.sleep(1)
    return "Completed"

# Outer level invocation
result = asyncio.run(my_async_function())
print(result)
