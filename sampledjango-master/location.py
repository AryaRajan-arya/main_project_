import phonenumbers
import opencage
import folium
from urllib.request import urlopen
from myphone import number
from phonenumbers import geocoder
pepnumber=phonenumbers.parse(number)
location=geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import OpenCageGeocode

key='ed2a5807eba74d10a66c09403ae11643'

geocoder=OpenCageGeocode(key)
query = str(location)
results=geocoder.geocode(query)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_starter=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("mylocation.html")