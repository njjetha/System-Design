# import time 
import asyncio

async def hello():
    print("HHHHHHHHHHEEEEEEELLLLLLLLLOOOOOOOOOO")
    await asyncio.sleep(1)
    print("Hello World!")

async def func1():
    print("func1")

async def main():
    await asyncio.gather(hello(), func1()) 
    # func1()

asyncio.run(main())