import json
import requests
from urllib.parse import urljoin


# TODO
# 1 Date fields from ArcGIS REST Services are in the ESRI format and should be converted to ANSI or text

# URL of feature service
featserv_url = r'https://services.arcgis.com/ZzrwjTRez6FJiOq4/arcgis/rest/services/Uintah_Co_Fires/FeatureServer/0'
output_filename = 'getresults.json'


# SQL WHERE clause for API request
whereclause = '1=1'

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
    "returnGeometry": "false",
    "returnTrueCurves": "false",
    "maxAllowableOffset": "",
    "geometryPrecision": "6",  # number of decimal places in the x/y coordinates
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
    "resultRecordCount": "",          # max number of records per API request (usually 1000)
    "queryByDistance": "",
    "returnExtentsOnly": "false",
    "datumTransformation": "",
    "parameterValues": "",
    "rangeValues": "",
    "f": "pjson"
}


def getRecordCount(featserv_url):
    query_url = featserv_url.strip('/') + r'/query'

    payload = {
        'where': '1=1',
        'returnCountOnly': 'true',
        'f': 'pjson'
    }
    r = requests.get(query_url, params=payload)
    records = json.loads(r.text)

    return int(records["count"])


def getMaxRecordCount(featserv_url):
    services_url = featserv_url.strip('/') + r'?f=pjson'

    r = requests.get(services_url)
    records = json.loads(r.text)

    return int(records["maxRecordCount"])


def getRecords(featserv_url, payload):
    # request the total number of records (recordCount)
    # in increments of max requests permitted per API call (batchsize)

    query_url = featserv_url.strip('/') + r'/query'
    
    recordcount = getRecordCount(featserv_url)  # total record count in feature service
    batchsize = getMaxRecordCount(featserv_url) # number of records requested per API call (usually 1000 max)
    payload["resultRecordCount"] = batchsize

    print(recordcount, "total records")
    
    for offset in range(0, recordcount, batchsize):

        if offset + batchsize <= recordcount:
            print(str(offset) + " - " + str(offset + batchsize))
        else:
            print(str(offset) + " - " + str(recordcount))


        # set the starting point for the next batch of records requested
        payload["resultOffset"] = offset

        # send the GET request to the REST endpoint
        r = requests.get(query_url, params=payload)  # SHOULD BE QUERY URL

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
    Performs the same task as the "geometryPrecision" value in the request payload
    (most of the time)  geometryPrecision doesn't appear to work with geoprocessing services

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
        # round off the geometry values to specified number of decimal places
        # this seems to be unnecessary, with feature services
        # use "geometryPrecision" key in the requests payload
        # this function may be ncessary when using other services, i.e. geocoding

        # if payload["returnGeometry"].lower() == 'true':
        #     # if geometry was requested, round the x/y coordinates to specified
        #     # number of decimal places
        #     roundgeom(records, 6) 
    
        file.write(json.dumps(records))  


records = getRecords(featserv_url, payload)
writeRecords(records) 

print("done")
