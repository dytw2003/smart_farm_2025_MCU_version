
import uasyncio as asyncio
import json
import os
from md.api import send_settings_to_server_db

# CHANGE FOR THE OTHER HOUSE
# _1"

# Helper function to check if a file exists


def file_exists(filename):
    try:
        os.stat(filename)
        return True
    except OSError:
        return False


# Buffer to store updates and reduce frequent file I/O
update_buffer = []


async def store_var(var, name, state, client,  filename='var.csv'):
    """Store variable and queue updates for asynchronous CSV file storage."""

    MQTT_TOPIC_MANUAL = b"dytw_1/manual"
    # MQTT_TOPIC_AUTO = b"dytw_1/auto"

    # Check if state is empty and handle it
    if not state:
        print(f"[DEBUG] State for '{name}' is empty; setting to 0.")
        state = 0  # Default state to 0 if empty
    

    
    # Update the variable's attribute
    if name.endswith("_1"):
        if hasattr(var, name):  # Check if the variable exists
            setattr(var, name, state)
            print(f"[DEBUG] Updated variable '{name}' to '{state}'.")

            if state=="on" or state=="off" or state=="open" or state=="close":           
                    # Publish updates via MQTT
                    client.publish(MQTT_TOPIC_MANUAL, json.dumps({str(name): state}))
                    print(f"Published MQTT message: {MQTT_TOPIC_MANUAL} -> {name}: {state}")

            # Check state type (numeric or string)
            if isinstance(state, (int, float)) or state.isdigit():  # If numeric       
                
                if name.endswith("_1"):# and name != "envout_ws_1":  #name not in {"envout_ws_1"}:
                    # send to the server            
                
                    # Skip specific manual mode variables
                    update_buffer.append((name, state))
                    print("Queued Numeric Update -- ||:(", name, ":", state, ")")
                    await send_settings_to_server_db({str(name): state})
            elif state in {"ON","OFF","on","off"}:  # If "ON"/"OFF"
                # Exclude certain names and log debug message
                # state = state.lower()
                # print(f"[after LOWER] State for '{name}' is 'ON'/'OFF'; converted to '{state}'.")
            
                if (name.endswith("btn_1") or name.endswith("hd_1") or name.endswith("vpd_1") or name.endswith("lgt_1") or name.endswith("nd_1")) or name.endswith("_li_1"):
                    update_buffer.append((name, state))
                    print("Queued String Update -- ||:(", name, ":", state, ")")
                    await send_settings_to_server_db({str(name): state})
                else:
                    print("Skipping storage for manual mode")
                
            else:
                print(f"[DEBUG] Unhandled state type for '{name}': {state}")
        else:
            print(f"[DEBUG] Variable '{name}' does not exist in the object; no update performed.")
    else:
        print(f"[DEBUG] Variable '{name}' does not end with '_1'; no update performed.")



async def update_csv_file_periodically(filename='var.csv'):
    """Update the CSV file periodically with buffered changes."""
    while True:
        if update_buffer:
            # Read existing data once
            lines = []
            if file_exists(filename):
                with open(filename, 'r') as f:
                    lines = f.readlines()

            # Create a dictionary of current data in file
            data_dict = {line.split(',')[0]: line.split(',')[
                1].strip() for line in lines}

            # Apply buffered updates to data_dict
            while update_buffer:
                name, state = update_buffer.pop(0)
                data_dict[name] = state  # Update or add new

            # Write updated data back to the file
            with open(filename, 'w') as f:
                for name, state in data_dict.items():
                    f.write(f"{name},{state}\n")
            print(
                "------CSV file updated with buffered data.")

        # Only check for new data after a delay if buffer is empty
        await asyncio.sleep(60)  # Adjust this delay as needed
