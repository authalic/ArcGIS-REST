import requests
import json


"""
ArcGIS Online access tokens.
returns 'client id' and 'client secret'
stored as a JSON object in a text file outside of version control
"""

# id and secret from registered AGOL application 
#   see: https://developers.arcgis.com/applications 
#   and: https://developers.arcgis.com/rest/services-reference/generate-token.htm


def get_token(org='dnr'):   # 'dnr' or 'nifc'

    agol_tokens = json.loads(open('tokens.json').read())

    client_id = agol_tokens[org]['id']
    client_secret = agol_tokens[org]['secret']

    # URL of AGOL Token Endpoint OAuth REST service
    authurl = "https://www.arcgis.com/sharing/rest/oauth2/token/"
    
    # parameters of GET request
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    # send request to AGOL Token REST service
    request = requests.get(authurl, params=params)

    # unpack the request response to json
    # extract the access token from the API response
    return request.json()["access_token"]
