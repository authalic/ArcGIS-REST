import requests
import json
import agol_token


# url = r"https://services.arcgis.com/ZzrwjTRez6FJiOq4/ArcGIS/rest/services/2011_Helo_Tracks_All/FeatureServer/0/query"

url = r"https://rmgsc-haws1.cr.usgs.gov/arcgis/rest/services/geomac_dyn/MapServer/0/query"  # geomac current fires

payload = {
    'where': "Region='SER'" ,
    'objectIds': '',
    'time': '',
    'geometry': '',
    'geometryType': 'esriGeometryEnvelope',
    'inSR': '',
    'outSR': '4326',
    'spatialRel': 'esriSpatialRelIntersects',
    'resultType': 'none',
    'distance': '0.0',
    'units': 'esriSRUnit_Meter',
    'returnGeodetic': 'false',
    'outFields': '*',
    'returnGeometry': 'false',
    'returnIdsOnly': 'false',
    'f': 'pjson',
    'token': agol_token.get_token()
    }

r = requests.post(url, data=payload)

print(r.text)
