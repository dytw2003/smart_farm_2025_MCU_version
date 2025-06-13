import uasyncio as asyncio
from machine import RTC

async def current_rtc(var):   
    rtc = RTC()  # Create the RTC object outside the loop
    while True:
        print("RTC synchronization task is running...")

        if not var.rtc_init:
            # Initialize the RTC if cloud-provided hour, minute, and second are available
            if var.cld_hour is not None and var.cld_min is not None and var.cld_sec is not None:
                try:
                    # Set the RTC with cloud-provided time
                    # (year, month, day, weekday, hour, minute, second, subseconds)
                    rtc.datetime((2024, 11, 22, 4, int(var.cld_hour), int(var.cld_min), int(var.cld_sec), 0))
                    setattr(var, "rtc_init", True)  # Mark RTC as initialized
                    print(f"RTC initialized with Cloud Time -> Hour: {var.cld_hour}, Minute: {var.cld_min}, Second: {var.cld_sec}")
                except Exception as e:
                    print(f"Error initializing RTC: {e}")
            else:
                print("Cloud-provided time (hour, minute, and second) is unavailable. RTC initialization skipped.")
        else:
            # Once initialized, retrieve the current RTC time
            try:
                year, month, day, week, hour, minute, second, *_ = rtc.datetime()

                # Update the variable object with the current RTC values
                var.c_hour_1 = hour
                var.c_min_1 = minute

                # Debug print
                print(f"Current RTC Time -> Hour: {hour}, Minute: {minute}")
            except Exception as e:
                print(f"Error reading RTC time: {e}")

        # Sleep for 1 second before the next iteration
        await asyncio.sleep(10)
