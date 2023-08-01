# This Python script uses the requests library to get the sunset time from the sunrise-sunset.org API, calculates the time 2 hours before sunset, and displays it
# The script assumes that the computer's local time is set correctly.
# The script requires the requests and pytz libraries. To install them, use 'pip install requests pytz'

import requests
from datetime import datetime, timedelta
import pytz

def get_sunset_time(lat, lng):
    response = requests.get(f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&formatted=0")
    sunset_utc = datetime.fromisoformat(response.json()['results']['sunset'].replace('Z', '+00:00'))
    return sunset_utc

def convert_to_local(sunset_utc):
    local_tz = datetime.now().astimezone().tzinfo
    sunset_local = sunset_utc.astimezone(local_tz)
    return sunset_local

def display_time_before_sunset(sunset_local, hours_before=2):
    time_before_sunset = sunset_local - timedelta(hours=hours_before)
    print(f"The time 2 hours before sunset is: {time_before_sunset.time()}")

if __name__ == "__main__":
    lat, lng = 41.026531, -73.628548
    sunset_utc = get_sunset_time(lat, lng)
    sunset_local = convert_to_local(sunset_utc)
    display_time_before_sunset(sunset_local)
