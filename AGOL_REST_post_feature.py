import requests
import json
from datetime import datetime as dt
import agol_token


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
    'token': agol_token.get_token()
}


r = requests.post(url, data=payload)

print(r.text)
