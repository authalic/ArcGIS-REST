import requests
import json
import agol_token


url = r"https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/West_US_GACC_Areas/FeatureServer/0/query"

payload = {
    'where': '1=1' ,
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
    'token': agol_token.get_token('nifc')
    }

r = requests.post(url, data=payload)

print(r.text)
