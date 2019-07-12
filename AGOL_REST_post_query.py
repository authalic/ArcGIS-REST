import requests
import json
import agol_token


url = r"https://services.arcgis.com/ZzrwjTRez6FJiOq4/ArcGIS/rest/services/2011_Helo_Tracks_All/FeatureServer/0/query"

payload = {
    'where': '1=1',
    'objectIds': '',
    'time': '',
    'geometry': '',
    'geometryType': 'esriGeometryEnvelope',
    'inSR': '',
    'spatialRel': 'esriSpatialRelIntersects',
    'resultType': 'none',
    'distance': '0.0',
    'units': 'esriSRUnit_Meter',
    'returnGeodetic': 'false',
    'outFields': '*',
    'returnGeometry': 'false',
    'multipatchOption': 'xyFootprint',
    'maxAllowableOffset': '',
    'geometryPrecision': '',
    'outSR': '',
    'datumTransformation': '',
    'applyVCSProjection': 'false',
    'returnIdsOnly': 'false',
    'returnUniqueIdsOnly': 'false',
    'returnCountOnly': 'false',
    'returnExtentOnly': 'false',
    'returnDistinctValues': 'false',
    'orderByFields': '',
    'groupByFieldsForStatistics': '',
    'outStatistics': '',
    'having': '',
    'resultOffset': '',
    'resultRecordCount': '',
    'returnZ': 'false',
    'returnM': 'false',
    'returnExceededLimitFeatures': 'true',
    'quantizationParameters': '',
    'sqlFormat': 'none',
    'f': 'pjson',
    'token': agol_token.get_token()
    }

r = requests.post(url, data=payload)

print(r.text)
