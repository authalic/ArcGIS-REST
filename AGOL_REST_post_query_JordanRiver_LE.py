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


# Jordan River LE Site Collect feature service URL
url = r"https://services.arcgis.com/ZzrwjTRez6FJiOq4/arcgis/rest/services/survey123_b492e85bb3bc4d359078d12c23ef1076/FeatureServer/0/query"

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
    'token': ''
    }

r = requests.post(url, data=payload)

print(r.text)
