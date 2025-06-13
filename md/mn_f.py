# mn_f.py
import uasyncio as asyncio  # Import asyncio at the top

# IMPORT FROM THE MANUAL
from md.mnsf import mn_signal
# changes for the other house
# _c_1")
# hw_switch_1
# DC CONTROL


def remove_number(s):
    parts = s.rsplit('_', 1)
    if len(parts) == 2 and parts[1].isdigit() and 1 <= len(parts[1]) <= 2:
        return parts[0]
    return s


async def mn_control_motors(gpio, var, btn_val, io_pin, auto_mode):
    hw_button = var.hw_switch_1
    # check hardware button and cloud auto/manual
    if hw_button == "at" and (auto_mode != "on" and auto_mode != "ON"):
        # Remove trailing _number at the end
        split_pin = remove_number(io_pin)
        if btn_val == "open":
            gpio.turn_off_pins(f"{split_pin}_c_1")  # opposite pin off
            gpio.turn_on_pins(io_pin)
            # setattr(var, io_pin, "open")
            print(f"PIN :{io_pin}::open")
        elif btn_val == "close":
            gpio.turn_off_pins(io_pin)
            gpio.turn_on_pins(f"{split_pin}_c_1")  # opposite pin off
            # setattr(var, io_pin, "close")
            print(f"PIN :{split_pin}_c_1::close")
        elif btn_val == "off":
            gpio.turn_off_pins(io_pin)
            gpio.turn_off_pins(f"{split_pin}_c_1")  # opposite pin off
            # setattr(var, io_pin, "off")
            print(f"PIN :{io_pin}::off")
            print(f"PIN :{split_pin}_c_1::off")
    elif hw_button == "mn":
        print(f"HARDWARE BUTTON ::{hw_button}")
        await mn_signal(gpio, var)  # off the all hardware signl
    else:
        print(f"HARDWARE BUTTON::{hw_button}, WEB AUTO/MAN :: {auto_mode}")


async def mn_control_ac(gpio, var, btn_val, io_pin, auto_mode):
    hw_button = var.hw_switch_1
    if hw_button == "at" and (auto_mode != "on" and auto_mode != "ON"):
        if btn_val == "on":
            gpio.turn_on_pins(io_pin)
        elif btn_val == "off":
            gpio.turn_off_pins(io_pin)
    elif hw_button == "mn":
        print(f"Auto mode BTN{hw_button} ")
        await mn_signal(gpio, var)
    else:
        print(f"Auto mode is -------{auto_mode}")
