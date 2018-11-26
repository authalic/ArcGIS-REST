import requests
import json

# URL of AGOL Token Endpoint OAuth REST service
authurl = "https://www.arcgis.com/sharing/rest/oauth2/token/"

# id and secret from registered AGOL application (see https://developers.arcgis.com/applications)
j = json.loads(open("tokens.json").read())

client_id = j["client_id"]
client_secret = j["client_secret"]


def get_token():

    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': "client_credentials"
    }

    request = requests.get(authurl, params=params)

    # unpack the request response to json
    JSONresponse = request.json()

    token = JSONresponse["access_token"]
    return token


url = r"https://services.arcgis.com/ZzrwjTRez6FJiOq4/ArcGIS/rest/services/2011_Helo_Tracks_All/FeatureServer/0/query"

payload = {
    'where': " 'Region' LIKE '%SER' " ,
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
    'returnIdsOnly': 'false',
    'f': 'pjson',
    'token': ''
    }

r = requests.post(url, data=payload)

print(r.text)
