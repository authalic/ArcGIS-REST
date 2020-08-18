import requests
import json

"""
get Timmons access token
"""


def get_token(org='timmons'):

    gold_tokens = json.loads(open('tokens.json').read())

    client_id = gold_tokens[org]['id']
    client_secret = gold_tokens[org]['secret']

    # Login URL
    authurl = "https://maps3.timmons.com/arcgis/rest/login"

    # parameters of GET request
    params = {
        'username': client_id,
        'password': client_secret
    }

    # send request to Token REST service
    request = requests.post(authurl, data=params)

    # unpack the request response to json
    # extract and return the access token from the API response
    r = request.json()

    return r['token']


if __name__ == "__main__":
    # test code executes when module is run as script

    j = get_token()

    print(j)
