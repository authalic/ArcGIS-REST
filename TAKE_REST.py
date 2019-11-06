
import json
import requests
from urllib.parse import urljoin


# TODO
# 1 Date fields from ArcGIS REST Services are in the ESRI format and should be converted to ANSI or text
# 2 Vertex coordinates contain a crazy amount of digits beyond the decimal point


# URL of feature service (path must NOT end with '/')
featserv_url = r'https://services.arcgis.com/ZzrwjTRez6FJiOq4/arcgis/rest/services/Utah_Urban_Tree_Inventory_Public_View/FeatureServer/0'
output_filename = 'getresults.json'

queryurl = urljoin(featserv_url, "query")


# SQL WHERE clause for API request

whereclause = '1=1'

# more complex example:
# whereclause = """
#     year_of_const LIKE '%1985%' OR
#     year_of_const LIKE '%1986%' OR
#     """


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
    "resultRecordCount": "",          # max number of records per API request (usually 1000)
    "queryByDistance": "",
    "returnExtentsOnly": "false",
    "datumTransformation": "",
    "parameterValues": "",
    "rangeValues": "",
    "f": "pjson"
}


def getRecordCount():
    url = urljoin(featserve_url, r'/query')
    payload = {
        'where': '1=1',
        'returnCountOnly': 'true',
        'f': 'pjson'
    }
    r = requests.get(url, params=payload)
    records = json.loads(r.text)

    return records["count"]


def getMaxRecordCount():
    services_url = urljoin(featserv_url, r'?f=pjson')
    r = requests.get(services_url)
    records = json.loads(r.text)

    return records["maxRecordCount"]


def getRecords():
    # request the total number of records (recordCount)
    # in increments of max requests permitted per API call (batchsize)
    
    recordCount = getRecordCount # total record count in feature service
    batchsize = getMaxRecordCount    # number of records requested per API call (usually 1000 max, but may be more)
    payload["resultRecordCount"] = batchsize
    

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
    
    return records


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


def writeRecords(records):
    # write the dictionary of results to a JSON text file
    with open(output_filename, 'w') as file:
        roundgeom(records, 6) # round to 6 decimal places
        file.write(json.dumps(records))  

records = getRecords()
writeRecords(records) 

print("done")
