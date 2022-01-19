import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import  opencage
import folium

mobileNo = input("Enter You Phone Number With Country Code")
mobileNo=phonenumbers.parse(mobileNo)
print(geocoder.description_for_number(mobileNo, "en"))

print(timezone.time_zones_for_number(mobileNo))
print(carrier.name_for_number(mobileNo, "en"))

print(geocoder.description_for_number(mobileNo, "en"))
loc = geocoder.description_for_number(mobileNo, "en")
print("Valid Number?", phonenumbers.is_valid_number(mobileNo))

print("Checking possibility of Number:" , phonenumbers.is_possible_number(mobileNo))

from opencage.geocoder import  OpenCageGeocode
key = 'c45d49b23b8549929e4004375a607d6e'
geocoder = OpenCageGeocode(key)
query = str(loc)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

myMap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=loc).add_to(myMap)

myMap.save("mylocation.html")