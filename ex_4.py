import asyncio
import math

async def calculate_factioral(number):
    await asyncio.sleep(0)
    result = math.factioral(number)
    print(f"Factioral of {number} is {result}")
    return result

async def main():
    numbers=[7, 10, 18, 25]
    tasks=[calculate_factioral(num) for num in numbers]
    
    results=await asyncio.gather(*tasks)
    
    print("All factiorals have been calculated")
    print("Results:", results)
    
asyncio.run(main())
    