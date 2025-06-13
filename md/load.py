

###---------------------------------------------------------------------- FROM THE FLASH MEMORY OF THE MCU


import uasyncio as asyncio
import os

# Define the CSV file path
CSV_FILE_PATH = 'var.csv'

# Function to load CSV data into the var module


async def load_csv(var, file_path=CSV_FILE_PATH):
    # Check if the file exists and is not empty using os.stat
    if not var.ld_flg:
        try:

            file_info = os.stat(file_path)
            # File size (in bytes) is non-zero
            if file_info[6] > 0:
                with open(file_path, 'r') as file:
                    for line in file:
                        row = line.strip().split(',')
                        if len(row) == 2:
                            key, value = row
                            # Convert the value to the appropriate type
                            value = convert_value(value)

                            # Update the attribute in var
                            if hasattr(var, key):
                                setattr(var, key, value)
                                print(f"Loaded {key} = {value} into var.")
                            else:
                                print(f"Warning:{key}is not an attribute of var.")
                # Set the load flag to True after loading
                setattr(var, "ld_flg", True)
            else:
                print(f"Skipping CSV loading --- {file_path} is empty.")
        except OSError as e:
            print(f"Error reading file {file_path}: {e}")

    else:
        print(f"Skipping CSV loading ------Flag:: {var.ld_flg} -------------.")

# Helper function to convert string values to appropriate types


def convert_value(value):
    if value.lower() == 'true':
        return True
    elif value.lower() == 'false':
        return False
    elif value.isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        return value

# Periodic loader using uasyncio.sleep for MicroPython compatibility


async def load_csv_to_var(var):
    while True:
        await load_csv(var, file_path=CSV_FILE_PATH)
        await asyncio.sleep(60)  # Delay between loads
