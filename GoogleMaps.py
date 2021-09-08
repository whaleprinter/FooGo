#https://stackoverflow.com/questions/58053077/get-distance-from-google-cloud-maps-directions-api
# Maps that we used: https://www.nap.edu/resource/25334/interstate/img/i-map.jpg, https://www.thoughtco.com/thmb/KaGqO8m2w9kfc1cDIwCvzTpWEEE=/2047x1464/filters:fill(auto,1)/GettyImages-153677569-d929e5f7b9384c72a7d43d0b9f526c62.jpg, https://www.nationsonline.org/bilder/Map_US_Airports.gif
# Import libraries

import googlemaps
from datetime import datetime
def routeMapper(coords_0, coords_1, transitMode):
    # Init client


    gmaps = googlemaps.Client(key=)
    # Request directions
    now = datetime.now()

    # Travel modes: walking, driving, transit
    # Calls the Google Maps directions function, which calculates the actual travel distance based off of the cloud maps
    directions_result = gmaps.directions(coords_0, coords_1, mode=transitMode, departure_time=now, avoid='tolls')

    # Get distance
    distance = 0
    # This conditional statement determines whether a point has been selected in water and, if so, will restart the Calculator.py program in order to get the user to select new points
    if len(directions_result) == 0:
        exec(open("Calculator.py").read())
    else:
        legs = directions_result[0].get("legs")
        for leg in legs:
            distance = distance + leg.get("distance").get("value")
    return distance

