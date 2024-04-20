# Libraries
import os
import json
import urllib
import requests
import pandas as pd
from math import radians, cos, sin, sqrt, atan2


def get_distance_to_station(Latitude, Longitude):
    """
    This function determines the closesd trainstation based on the input coordinates and returns the distance between the given Point and the nearest station in km.
    NOTICE: Assumes that the input Points are in WGS84 projection (lat/lon).
    """
    # Get the town of the given coordinates
    if Latitude is None or Longitude is None:
        return None
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        'format': 'json',
        'lat': Latitude,
        'lon': Longitude,
        'zoom': 18,
        'addressdetails': 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    if 'address' in data and 'town' in data['address']:
        Town = data['address']['town']
    elif 'address' in data and 'city' in data['address']:
        Town = data['address']['city']
    else:
        return None
    url = "http://transport.opendata.ch/v1/locations"
    params = {
        'type': 'station',
        'query': Town
    }

    # Get the coordinates of the nearest station with exception handling
    try:
        data = requests.get(url, params=params).json()
        station_lat = data["stations"][0]["coordinate"]["x"]
        station_lon = data["stations"][0]["coordinate"]["y"]
    except (IndexError, KeyError):
        return None
    # If no station is found, return "No station found"
    if station_lat is None or station_lon is None: 
        return None

    # Convert latitude and longitude to radians
    lat1, lon1, lat2, lon2 = map(radians, [Latitude, Longitude, station_lat, station_lon])
    
    # Calculate the distance between the two points with pythagoras
    # Can not apply pythagoras directly, because the earth is not flat - therefore: Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    radius_of_earth_km = 6371.0
    distance = radius_of_earth_km * c
    return distance