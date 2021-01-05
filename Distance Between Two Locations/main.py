from functools import partial
from geopy import distance
from geopy.geocoders import Nominatim


def findCoords(location):
    ''' Finds the coordinates for the entered location. Location must be valid (cityname, street address, lat and lng coordinates, etc.)'''
    try:
        geolocator = Nominatim(user_agent='main.py')
        location = (geolocator.geocode(location))
        lat = location.latitude
        lng = location.longitude
        return (lat, lng)
    except:
        return "Location not found!"


def calculateDistance(location1, location2):
    ''' Calculates the distance between two locations.'''
    distanceBetweenTwoInKm = round(distance.distance(
        findCoords(location1), findCoords(location2)).km, 2)
    distanceBetweenTwoInMiles = round(distance.distance(
        findCoords(location1), findCoords(location2)).miles, 2)
    return f"The distance between '{location1}' and '{location2}' is {distanceBetweenTwoInKm} kilometers ({distanceBetweenTwoInMiles} miles)."


print(findCoords('Miami'))
print(findCoords('New York'))
print(calculateDistance('Miami', 'New York'))
