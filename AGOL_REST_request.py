import requests
import json  # needed to prettify the json, but not to convert response to json

# address to geocode using ESRI geocode server
geocode = '336 West 300 South, Salt Lake City, UT'

# URL of REST service
resturl = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates"


# URL parameters
payload = {
    'f' : 'json',
    'singleLine': geocode,
    'outSR': '4326',
    'outFields' : 'Match_addr,Addr_type'
    }

# get the Requests Response object
r = requests.get(resturl, params=payload)

j = r.json()

# print and prettify the dict using the json.dumps() method
print(json.dumps(j, sort_keys=True, indent=4))
