#!/usr/bin/env python3
# coding:utf-8
from geopy.geocoders import Nominatim

# 48.609431111111114, 0.9004377777777778
# 43.1558975, -77.60493666666666
# 43.063899166666666, -79.04972305555556
lat = 43.1558975
lon = -77.60493666666666



geolocator = Nominatim(user_agent="OpenMapQuest")
location = geolocator.reverse("{}, {}".format(lat, lon))

print(location.address)

# from pygeocoder import Geocoder 

# results = Geocoder.reverse_geocode(lat, lon)

# print(results.city)

fullAdress = (location.address.split(','))

print(len(fullAdress))
print((fullAdress[6]).lstrip(),(fullAdress[5]).lstrip(),(fullAdress[4]).lstrip(),(fullAdress[3]).lstrip())
print("{}_{}_{}_{}".format((fullAdress[6]).lstrip(),(fullAdress[5]).lstrip(),(fullAdress[4]).lstrip(),(fullAdress[3]).lstrip()))

print((fullAdress[(len(fullAdress)) - 1].lstrip()))
print((fullAdress[(len(fullAdress)) - 5].lstrip()))
print((fullAdress[(len(fullAdress)) - 7].lstrip()))