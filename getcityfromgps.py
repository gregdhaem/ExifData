from geopy.geocoders import Nominatim

lat = 48.841895272996695
lon = 2.3213744523790147

geolocator = Nominatim(user_agent="OpenMapQuest")
location = geolocator.reverse("{}, {}".format(lat, lon))

print(location.address)
print(location.address)

# from pygeocoder import Geocoder 

# results = Geocoder.reverse_geocode(lat, lon)

# print(results.city)