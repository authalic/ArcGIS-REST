
import json
import requests

# URL of feature service query service
url=r'https://services.arcgis.com/ZzrwjTRez6FJiOq4/arcgis/rest/services/Utah_Earthquake_Hazards/FeatureServer/2/query'

recordCount = 12 # record count: total records
batchsize = 12   # number of records requested per API call (usually 1000 max)
output_filename = 'faults_polyline_x.json'


# SQL WHERE clause for API request
whereclause = """1=1"""

# URL query string key/value pairs
payload = {
    "where": whereclause,
    "text": "",
    "objectIds": "",
    "time": "",
    "geometry": "",
    "geometryType": "esriGeometryEnvelope",
    "inSR": "",
    "spatialRel": "esriSpatialRelIntersects",
    "relationParam": "",
    "outFields": "*",
    "returnGeometry": "true",
    "returnTrueCurves": "false",
    "maxAllowableOffset": "",
    "geometryPrecision": "",
    "outSR": "4326",
    "returnIdsOnly": "false",
    "returnCountOnly": "false",
    "orderByFields": "",
    "groupByFieldsForStatistics": "",
    "outStatistics": "",
    "returnZ": "false",
    "returnM": "false",
    "gdbVersion": "",
    "returnDistinctValues": "false",
    "resultOffset": "",               # starting point of record request
    "resultRecordCount": batchsize,   # number of records requested (1000 max)
    "queryByDistance": "",
    "returnExtentsOnly": "false",
    "datumTransformation": "",
    "parameterValues": "",
    "rangeValues": "",
    "f": "pjson"
}

# dictionary to store the results returned from the requests
records = {}


def getRecordCount():
    recordpayload = payload
    recordpayload["returnCountOnly"] = "true"
    recordpayload["returnGeometry"] = "false"

    r = requests.get(url, params=payload)
    records = json.loads(r.text)

    return records["maxRecordCount"]


# request the total number of records (recordCount)
# in increments of max requests permitted per API call (batchsize)
for offset in range(0, recordCount, batchsize):

    # Note:  This paging loop could also be done with checking "exceededTransferLimit" attribute
    # value of "true" means there are still records avaialable in the next offset

    print(str(offset) + " - " + str(offset + batchsize))

    # set the starting point for the next batch of records requested
    payload["resultOffset"] = offset

    # send the GET request to the REST endpoint
    r = requests.get(url, params=payload)

    if offset == 0:
        # first API request: save complete JSON response as dict
        records = json.loads(r.text)
    else:
        # each subsequent request, append only the records to dict
        j = json.loads(r.text)
        records["features"] += j["features"]

def roundgeom(records, roundlen):
    '''
    Removes extraneous digits from the decimal fraction in GeoJSON (x,y) point coordinates.
      records = JSON object containing any properly formatted GeoJSON geometry.
      roundlen = number of decimal places to which to round the decimal values
    Note: z and m values are not affected
    '''

    # loop through each geometry in each feature
    features = records["features"]  # features is a list of dicts, each dict is a feature


    if records["geometryType"] == "esriGeometryPoint":

        for pt_feat in features:
            pt_feat['geometry']['x'] = round(pt_feat['geometry']['x'], roundlen)
            pt_feat['geometry']['y'] = round(pt_feat['geometry']['y'], roundlen)


    elif records["geometryType"] == "esriGeometryPolyline":

        for ln_feat in features:
            for path in ln_feat["geometry"]["paths"]:
                for segment in path:
                    segment[0] = round(segment[0], roundlen)
                    segment[1] = round(segment[1], roundlen)


    elif records["geometryType"] == "esriGeometryPolygon":

        for pg_feat in features:
            for ring in pg_feat["geometry"]["rings"]:
                for ringpath in ring:
                    ringpath[0] = round(ringpath[0], roundlen)
                    ringpath[1] = round(ringpath[1], roundlen)

    else:
        # geometry type is either esriGeometryMultipoint or esriGeometryEnvelope
        # implement multipoint later, perhaps
        # envelope never happens

        pass


# write the dictionary of results to a JSON text file
with open(output_filename, 'w') as file:
    roundgeom(records, 6)
    file.write(json.dumps(records))

print("done")
