import requests
import json
import agol_token


url = "https://services.arcgis.com/ZzrwjTRez6FJiOq4/ArcGIS/rest/services/REST_test_point/FeatureServer/0/query"

payload = {
    'f': 'pjson',
    'token': agol_token.get_token(),
    'where': '1=1',
    'outFields': '*',
    'returnGeodetic': 'false',
    'outFields': '*',
    'returnGeometry': 'true'
    }

print("\n" + payload['token'] + "\n")


r = requests.post(url, data=payload)

print(r.text)
