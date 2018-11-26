import requests
import json
from datetime import datetime as dt

# URL of AGOL Token Endpoint OAuth REST service
authurl = "https://www.arcgis.com/sharing/rest/oauth2/token/"

# id and secret from registered AGOL application (see https://developers.arcgis.com/applications)
j = json.loads(open("tokens.json").read())

client_id = j["client_id"]
client_secret = j["client_secret"]


# note on dates:
# ESRI timestamps are in miliseconds from July 1, 1970
# POSIX timestamps are in seconds from July 1, 1970
# Multiply datetime.datetime.timestamp() by 1000 to get ESRI timestamp


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


url = r'https://services.arcgis.com/ZzrwjTRez6FJiOq4/ArcGIS/rest/services/REST_test_point/FeatureServer/0/addFeatures'

feats = [{
            'attributes': {
                'id': 900,
                'POINTNAME': 'Point 1 of 2',
                'FAKEDATE': dt.timestamp(dt.now()) * 1000,
                'POINTVAL': 2
            },
            'geometry': {
                'x': -12645109,
                'y': 4921110
            }
        }, 
        {
            'attributes': {
                'id': 901,
                'POINTNAME': 'Point 2 of 2',
                'FAKEDATE': dt.timestamp(dt.now()) * 1000,
                'POINTVAL': 1
            },
            'geometry': {
                'x': -12645159,
                'y': 4921110
            }
        }]


payload = {
    'features': json.dumps(feats),
    'rollbackOnFailure': 'false',
    'f': 'json',
    'token': get_token()
}

r = requests.post(url, data=payload)

print(r.text)
