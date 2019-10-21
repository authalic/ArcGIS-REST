import requests
import json


"""
get ArcGIS Online access token

Note:  ArcGIS Online registered application 'client id' and 'client secret'
       stored as a JSON object in a text file outside of version control.
"""


def get_token(org='dnr'):   # 'dnr' or 'nifc'

    # client id and client secret are from a registered AGOL application in the
    # dnr and nifc AGOL organizations
    #   see: https://developers.arcgis.com/applications
    #   and: https://developers.arcgis.com/rest/services-reference/generate-token.htm

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
    # extract and return the access token from the API response
    return request.json()["access_token"]
