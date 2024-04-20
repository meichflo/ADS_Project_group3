import requests
from datetime import date, timedelta
import math
import time as time

# Dates setup
today = date.today()
one_year_ago = today - timedelta(days=365)

def get_sunshine_duration(latitude, longitude):
    """Get the average sunshine duration for the past year.
    Return in seconds."""
    print("Getting sunshine duration data for", latitude, longitude)

    time.sleep(0.2)

    # Check if latitude and longitude are valid
    if latitude is None or longitude is None or math.isnan(latitude) or math.isnan(longitude):
        return None
    # Request setup
    url = "https://archive-api.open-meteo.com/v1/archive" 
    params = {
        "latitude": latitude,  # Assuming latitude is defined earlier in your code
        "longitude": longitude,  # Assuming longitude is defined earlier in your code
        "start_date": one_year_ago,
        "end_date": today,
        "daily": "sunshine_duration", #	The number of seconds of sunshine per day is determined by calculating direct normalized irradiance exceeding 120 W/m², following the WMO definition. Sunshine duration will consistently be less than daylight duration due to dawn and dusk.
        "timezone": "Europe/Berlin"
    }
    # Fetch data
    response = requests.get(url, params=params).json()

    if 'daily' in response and 'sunshine_duration' in response['daily']:
        sunshine_duration = [x for x in response["daily"]["sunshine_duration"] if x is not None]
        # Calculate and print average if there is any sunshine duration data
        if sunshine_duration:
            average = sum(sunshine_duration) / len(sunshine_duration)
            return average
        else:
            return None
    else:
        # Print/log error or handle the missing key scenario
        print("Error: 'daily' or 'sunshine_duration' key is missing in the response.")
        return None
    
    #sunshine_duration = [x for x in response["daily"]["sunshine_duration"] if x is not None]

    # Calculate and print average
    #average = sum(sunshine_duration) / len(sunshine_duration)
    #return average