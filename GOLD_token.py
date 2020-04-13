import requests
import json


"""
get Gold Systems access token
"""


def get_token(org='gold'):

    # client id and client secret are from a registered AGOL application in the
    # dnr and nifc AGOL organizations
    #   see: https://developers.arcgis.com/applications
    #   and: https://developers.arcgis.com/rest/services-reference/generate-token.htm

    gold_tokens = json.loads(open('tokens.json').read())

    client_id = gold_tokens[org]['id']
    client_secret = gold_tokens[org]['secret']

    # URL of Gold Systems Endpoint service
    authurl = "https://fbs.utah.gov/fire/s/api/token"

    # parameters of GET request
    params = {
        'username': client_id,
        'password': client_secret
    }

    # send request to AGOL Token REST service
    request = requests.post(authurl, data=params)

    # unpack the request response to json
    # extract and return the access token from the API response
    # note: "access token" is a specific ArcGIS Online JSON response key, and
    # has been removed here
    r = request.json()

    return r['token']


if __name__ == "__main__":
    # test code executes when module is run as script

    j = get_token()

    print(j)
