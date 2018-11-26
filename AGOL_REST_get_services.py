import requests

# URL of REST service
resturl = "https://services.arcgis.com/ZzrwjTRez6FJiOq4/ArcGIS/rest/services/24kQuadIndex/FeatureServer"

# request the response in json format
payload = {'f': 'json'}

# get the Requests Response object
r = requests.get(resturl, params=payload)

# convert the response to a dictionary
j = r.json()


print(j["capabilities"])
print(j["serviceDescription"])
print(j["spatialReference"]["wkid"])
