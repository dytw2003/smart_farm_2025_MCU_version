import machine
import uasyncio as asyncio

# change for the other house
# _1

# UART configuration
uart = machine.UART(7, baudrate=9600, bits=8, parity=None)

# Lists to store the high and low nibbles
high_nibbles = []
low_nibbles = []

# Function to split bytes into high and low nibbles and store them


def split_and_store_nibbles(raw_data):
    global high_nibbles, low_nibbles

    # Clear previous values
    high_nibbles.clear()
    low_nibbles.clear()

    # Iterate over each byte and split into high and low nibbles
    for i, byte in enumerate(raw_data):
        high_nibble = (byte & 0xF0) >> 4  # Extract the high 4 bits
        low_nibble = byte & 0x0F          # Extract the low 4 bits

        # Store the nibbles in separate lists
        high_nibbles.append(high_nibble)
        low_nibbles.append(low_nibble)

        # Print the nibbles
        print(
            f"Byte {i + 1:02d}: {byte:02X} -> High: {high_nibble:X}, Low: {low_nibble:X}")


# Function to parse temperature from high and low nibbles

def combine_nibbles(*nibbles):
    """
    Combine a variable number of nibbles (4-bit values) into an integer.
    Each nibble contributes 4 bits to the final number.
    """
    combined = 0
    for nibble in nibbles:
        # Shift left by 4 bits and add the current nibble
        combined = (combined << 4) | nibble
    return combined


def parse_sensor_data_from_nibbles(var):
    global high_nibbles, low_nibbles

    # Example data parsing
    
    # if not high_nibbles or not low_nibbles:  # Check if high_nibbles and low_nibbles
    wind_direction_raw = (combine_nibbles(high_nibbles[2], low_nibbles[2]))
    temperature_raw = (combine_nibbles(
        low_nibbles[3], high_nibbles[4], low_nibbles[4])-400)/10
    humidity_raw = combine_nibbles(high_nibbles[5], low_nibbles[5])
    wind_speed_raw = (combine_nibbles(high_nibbles[6], low_nibbles[6]))/8*1.2
    gust_speed_raw = combine_nibbles(high_nibbles[7], low_nibbles[7])*1.2
    rain_raw = combine_nibbles(
        high_nibbles[8], low_nibbles[8], high_nibbles[9], low_nibbles[9])
    uv_raw = combine_nibbles(
        high_nibbles[10], low_nibbles[10], high_nibbles[11], low_nibbles[11])
    solar_raw = combine_nibbles(
        high_nibbles[13], low_nibbles[13],
        high_nibbles[14], low_nibbles[14],
        high_nibbles[15], low_nibbles[15]
    )

    if wind_direction_raw:
        var.envout_wd_1 = wind_direction_raw
    else:
        print("wind direction data unexpected")

    if temperature_raw:
        var.envout_temp_1 = temperature_raw
    else:
        print("Temperature data unexpected")

    if humidity_raw:
        var.envout_humi_1 = humidity_raw
    else:
        print("Humidity data unexpected")

    if wind_speed_raw:
        var.envout_ws_1 = wind_speed_raw
    else:
        print("Wind speed data unexpected")
    if gust_speed_raw:
        var.gust_speed_1 = gust_speed_raw
    else:
        print("Gust speed data unexpected")

    if uv_raw:
        var.uv_1 = uv_raw
    else:
        print("UV data unexpected")

    if solar_raw:
        var.envout_light_intensity_1 = solar_raw//10000
    else:
        print("Solar light data unexpected")

    # Print parsed values for debugging
    print(f"Wind Direction---raw: {wind_direction_raw} °")
    print(f"Temperature---raw: {temperature_raw} °C")
    print(f"Humidity---raw: {humidity_raw} %")
    print(f"Wind Speed---raw: {wind_speed_raw} : m/s")
    print(f"Gust Speed---raw: {gust_speed_raw}: m/s")
    # print(f"Rain: {rain_raw}")
    print(f"UV---raw: {uv_raw}")
    print(f"Solar---raw: {solar_raw}  :lux")

    # Print parsed values for debugging
    print(f"Wind Direction---var: {var.envout_wd_1} °")
    print(f"Temperature---var: {var.envout_temp_1} °C")
    print(f"Humidity---var: {var.envout_humi_1} %")
    print(f"Wind Speed---var: {var.envout_ws_1} : m/s")
    print(f"Gust Speed---var: {var.gust_speed_1}: m/s")
    # print(f"Rain: {rain_raw}")
    print(f"UV---var: {var.uv_1}")
    print(f"Solar---var: {var.envout_light_intensity_1}  :lux")
    # else:
    #     print("No data to parse")


# Async task to read data from UART and process it
async def read_uart_envout(var):

    while True:
        if uart.any():  # Check if data is available
            raw_data = uart.read()  # Read all available data
            if raw_data:
                # Print the raw data first
                print("\nRaw data received (hex):", " ".join(
                    f"{byte:02X}" for byte in raw_data))

                # Split the bytes into nibbles and store them
                split_and_store_nibbles(raw_data)

                # Parse and print sensor data
                parse_sensor_data_from_nibbles(var)
            else:
                print("No data received")
        await asyncio.sleep(0.1)  # Yield to allow other tasks to run
