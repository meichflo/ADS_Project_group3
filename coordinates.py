# Libraries
import os
import json
import urllib
import requests
import pandas as pd
from math import radians, cos, sin, sqrt, atan2

def get_coordinates(address):
    """Takes an address as an argument.
    Returns the latitude and longitude of the address.
    Returns a tuple of floats in the mentioned order."""
    base_url= "https://api3.geo.admin.ch/rest/services/api/SearchServer?"
    parameters = {"searchText": address,
                "origins": "address",
                "type": "locations",
                }
    r = requests.get(f"{base_url}{urllib.parse.urlencode(parameters)}")
    try:
        data = json.loads(r.content)
        Latitude = data['results'][0]['attrs']['lat']
        Longitude = data['results'][0]['attrs']['lon']
    except (IndexError, KeyError):
        Latitude, Longitude = None, None
    return Latitude, Longitude  # return a tuple
