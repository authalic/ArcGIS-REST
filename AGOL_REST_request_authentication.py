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


url = "https://services.arcgis.com/ZzrwjTRez6FJiOq4/ArcGIS/rest/services/REST_test_point/FeatureServer/0/query"

payload = {
    'f': 'pjson',
    'token': get_token(),
    'where': '1=1',
    'outFields': '*',
    'returnGeodetic': 'false',
    'outFields': '*',
    'returnGeometry': 'true'
    }

print("\n" + get_token() + "\n")


r = requests.post(url, data=payload)

print(r.text)
