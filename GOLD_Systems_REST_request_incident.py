import requests
import json  # needed to prettify the json, but not to convert response to json
import GOLD_Systems_token


# FBS API Documentation
# https://ut.firebilling.org/fire/s/api

# URL of REST service
resturl = "https://ut.firebilling.org/fire/s/api/incidents"

# Acceptance URL
# resturl = "https://testut.firebilling.org/fire/s/api/incidents"


# HTTP Headers: required for authorization
headers = {
    'Authorization': GOLD_Systems_token.get_token()
}
# URL parameters
# Options and examples
    # 'irwinId': '57c08414-6cac-43b9-bc33-611af128f22d'  # Pahvant WMA
    # 'irwinId': 'd59ee23f-17b6-4153-bf6f-629161315654'  # West Tridell (acreages available)
    # 'irwinId': '1bfd3a06-0959-4fdf-a7d9-72b7b1bb78a3'  # Green Ravine
    # 'year': 2019
    # 'incidentNumber: 'UTSWS-000029'
    # 'modifiedFrom': '2020-04-01T07:00:00.000Z',
    # 'modifiedTo':   '2020-04-15T06:59:59.000Z'

payload = {
    'modifiedFrom': '2020-07-15T07:00:00.000Z',
    'modifiedTo':   '2020-07-22T05:59:59.000Z'
    }


# get the Requests Response object
r = requests.get(resturl, headers=headers, params=payload)

# extract response as JSON
if r:
    j = r.json()

    # print and prettify the dict using the json.dumps() method
    print(json.dumps(j, sort_keys=True, indent=4))
