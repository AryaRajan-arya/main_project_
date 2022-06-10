import json
from urllib import response
from urllib.request import urlopen
url='https://ipinfo.io/json/'
response=urlopen(url)
data=json.load(response)
print(data)

