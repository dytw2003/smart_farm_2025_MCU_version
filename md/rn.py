
from machine import Pin
import uasyncio as asyncio
pin_A2 = Pin('A7', Pin.IN)
## NEED TO CHANGE FOR OTHER HOUSE
     #_1

async def read_rain_status(var):    
    while True:
    # store rain status on variable
        rain = pin_A2.value()
        if rain == 0:
            var.rain_status_1 = 1
            print("___________________rain is true")
        else:
            var.rain_status_1 = 0
            print("___________________rain false")
        await asyncio.sleep(1)
