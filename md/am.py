# am.py
from md.api import device_status_ac
from machine import Pin
import uasyncio as asyncio
pin_A1 = Pin('A1', Pin.IN)
# NEED TO CHANGE
# _1
from md.api import send_status_to_server_db, device_status_ac

async def am_status(var):
    
    while True:
        # selector switch status on variable
        slt_switch = pin_A1.value()
        if slt_switch == 0:
            setattr(var, "hw_switch_1", "at")
            setattr(var, "mnsig_flag_1", False)
            print(f"SELECTOR SWITCH Auto-----: {getattr(var, "hw_switch_1")}")           
        else:
            setattr(var, "hw_switch_1", "mn")
            print(
                f"_SELECTOR SWITCH Manual----: {getattr(var, "hw_switch_1")}")
         

        await asyncio.sleep(1)


async def am_status_sent_db(var):
    hw_auto = False
    hw_manual = False
    mcu_rst = False

    while True:
        print(f"===================running function")

        if not mcu_rst:
            print(f"===================if -----------1")
            await send_status_to_server_db(device_status_ac("MCU_reset_1", "MCU_RESET", "현장제어"))
            mcu_rst = True
            print(f"====================MCU Reset-----:  flags: Auto:{hw_auto}   ----Manual: {hw_manual}")
        elif getattr(var, "hw_switch_1") == "at" and not hw_auto:
            print(f"=================== elif ----- auto------1")
            await send_status_to_server_db(device_status_ac("hw_switch_1", "AUTO", "현장제어"))
            print(f"==============SELECTOR SWITCH Auto-----: {getattr(var, 'hw_switch_1')}   -- Flag:{hw_auto}")
            hw_auto = True
            hw_manual = False
        elif getattr(var, "hw_switch_1") == "mn" and not hw_manual:
            print(f"=================== elif -------manual----1")
            await send_status_to_server_db(device_status_ac("hw_switch_1", "MANUAL", "현장제어"))
            print(f"===============SELECTOR SWITCH Manual----: {getattr(var, 'hw_switch_1')}-- Flag:{hw_manual}")
            hw_manual = True
            hw_auto = False

        await asyncio.sleep(5)

