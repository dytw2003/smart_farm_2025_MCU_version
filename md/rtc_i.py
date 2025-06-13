


import urequests  # Ensure you have a library like urequests for HTTP requests


async def get_current_time_from_cloud(var):
    """
    Fetch the current time from your server and print the hour, minute, and second.

    Args:
        var (object): An object to store the fetched time variables.

    Returns:
        None
    """
    # Replace with your PHP API endpoint
    cloud_time_url = "http://www.adas.today/sf/time_api/time_api.php"
    try:
        print("-----------------------------------------------------------------------------Fetching current time from the cloud...")
        response = urequests.get(cloud_time_url)
        if response.status_code == 200:
            data = response.json()
            print(f"Current Time from Cloud: {data}")

            # Extract hour, minute, and second from the response
            current_hour = int(data.get("hour", 0))
            current_min = int(data.get("minute", 0))
            current_sec = int(data.get("second", 0))

            # Set the attribute to indicate the time has been fetched
            setattr(var, "cld_rtc_lcl", True)

            # Set attributes on the passed `var` object
            setattr(var, "cld_hour", f"{current_hour:02d}")
            setattr(var, "cld_min", f"{current_min:02d}")
            setattr(var, "cld_sec", f"{current_sec:02d}")

            print(
                f"Server Time -> Hour: {current_hour:02d}, Minute: {current_min:02d}, Second: {current_sec:02d}")
        else:
            print(
                f"Failed to fetch time. HTTP status code: {response.status_code}")
        response.close()
    except Exception as e:
        print(f"-------------------------------------------------------------------------------------Error fetching time from the cloud: {e}")
