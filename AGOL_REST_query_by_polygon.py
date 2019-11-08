import requests
import json
import agol_token


# NIFC Event Points
url = r'https://services.arcgis.com/ZzrwjTRez6FJiOq4/arcgis/rest/services/Utah_Earthquake_Hazards_Working/FeatureServer/0/query'

utah_bdy = "{'rings': [[[-114.2,42.2],[-110.8,42.2],[-110.8,41.2],[-108.8,41.2],[-108.8,36.8],[-114.2,36.8],[-114.2,42.2]]]}"

payload = {
    'where': '1=1' ,
    'objectIds': '',
    'time': '',
    'geometry': utah_bdy,
    'geometryType': 'esriGeometryPolygon ',
    'spatialRel': 'esriSpatialRelIntersects',
    'distance': '',
    'units': 'esriSRUnit_Meter',
    'inSR': '4326',
    'outSR': '4326',
    'resultType': 'none',
    'returnGeodetic': 'false',
    'outFields': '*',
    'returnGeometry': 'false',
    'returnIdsOnly': 'false',
    'returnCountOnly': 'true',
    'f': 'pjson',
    'token': ''                    #agol_token.get_token('nifc')
    }

r = requests.get(url, params=payload)
records = json.loads(r.text)

output_filename = r"spatialfilter.json"

# with open(output_filename, 'w') as file:
#     file.write(json.dumps(records))


print(json.dumps(records))