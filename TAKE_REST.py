
import json
import requests

# URL of feature service query service
url=r'http://----/arcgis/rest/services/----/query/'

recordCount = 101000 # record count: 109,204
batchsize = 1000    # number of records requested per API call (1000 max)
output_filename = 'getresults.json'


# SQL WHERE clause for API request
whereclause = """
    year_of_const LIKE '%1985%' OR
    year_of_const LIKE '%1986%' OR
    year_of_const LIKE '%1987%' OR
    year_of_const LIKE '%1988%' OR
    year_of_const LIKE '%1989%' OR
    year_of_const LIKE '%1990%' OR
    year_of_const LIKE '%1991%' OR
    year_of_const LIKE '%1992%' OR
    year_of_const LIKE '%1993%' OR
    year_of_const LIKE '%1994%' OR
    year_of_const LIKE '%1995%' OR
    year_of_const LIKE '%1996%' OR
    year_of_const LIKE '%1997%'
    """

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
    "outSR": "",
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

# request the total number of records (recordCount)
# in increments of max requests permitted per API call (batchsize)
for offset in range(0, recordCount, batchsize):

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


# write the dictionary of results to a JSON text file
with open(output_filename, 'w') as file:
    file.write(json.dumps(records))

print("done")
