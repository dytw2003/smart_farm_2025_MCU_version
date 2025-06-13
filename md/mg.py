#mg.py
# read from the Gateway /Master (raspberry pi)
import uasyncio as asyncio
import json
# change for the other house , take from uart only reset, if the network and mqtt has issues to reset the board
# _1"
#  rst_1
async def read_master(var, uart_hmi):
    if uart_hmi.any():
        try:
            data = uart_hmi.readline().decode('utf-8').strip()
            json_data = json.loads(data)

            for name, state in json_data.items():             
                
                if name=="rst_1":
                    setattr(var, name, state)
                    print(f"UART-- VALUES -- ||:({name} : {state})")
                    #await send_data_to_hmi(uart_hmi, json_data)
                    # UPDATE THE DATA TO THE var.csv
                    #await update_csv(name,state) 
                
                else:
                    print(f"Key '{name}' does not match the required ID pattern.")
                    
        except ValueError as e:  # Catch JSON decode errors with ValueError
            print("Failed to decode JSON:", e)
        except Exception as e:
            print("An error occurred:", e)
    else:
        print("No UART data available.---------------from MASTER")

# async def send_data_to_hmi(uart_hmi, data):
#     try:
#         json_data = json.dumps(data)
#         uart_hmi.write(json_data.encode('utf-8'))
#         print(f"Data sent to HMI: {json_data}")
#     except Exception as e:
#         print("Failed to send data to HMI:", e)