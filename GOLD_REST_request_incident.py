import requests
import json  # needed to prettify the json, but not to convert response to json
import GOLD_token


# URL of REST service
resturl = "https://fbs.utah.gov/fire/s/api/incidents"

# HTTP Headers: required for authorization
headers = {
    'Authorization': GOLD_token.get_token()
}
# URL parameters
payload = {
    'irwinId': "e6340533-cd6b-4ed2-bfa7-2b9962d69464"
    }

# params=payload

# t = 'irwinId': "e6340533-cd6b-4ed2-bfa7-2b9962d69464"

# get the Requests Response object
r = requests.get(resturl, headers=headers, params=payload)
print(r.url)

j = r.json()

# print and prettify the dict using the json.dumps() method
print(json.dumps(j, sort_keys=True, indent=4))
