import requests
import json
import agol_token



# NIFC Event Points
url = 'https://utility.arcgis.com/usrsvcs/servers/56fa25d190754487820a7da9db05d409/rest/services/GISS/Event_CollectorView/FeatureServer/1'


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
