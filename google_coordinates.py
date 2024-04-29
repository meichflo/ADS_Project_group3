import googlemaps

# API keys from gitignored file
from keys import keyFlorian

def get_google_coordinates(address):
    """Takes an address as an argument.
    Returns latitude and longitude as tuple.
    Make sure to have a valid Google API key in the keys.py file.
    """
    print("Getting coordinates for: ", address)
    try:
        gmaps = googlemaps.Client(key=keyFlorian)
    except Exception as e:
        print("Error: ", e)
    # Geocoding an address
    geocode_result = gmaps.geocode(address)
    if geocode_result:
        latitude = geocode_result[0]['geometry']['location']['lat']
        longitude = geocode_result[0]['geometry']['location']['lng']
    else:
        latitude = None
        longitude = None
    return latitude, longitude