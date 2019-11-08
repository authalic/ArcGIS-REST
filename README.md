# ArcGIS-REST
Python scripts using Requests module and ArcGIS REST services.

## Using Authentication
* employing tokens
* to be fleshed-out later
## Request Payload
Python dict consisting of key/value pairs which are submitted to the API as the HTTP query string.  Most can use empty strings as their value, but some are required to have explicit values in order to return any results from the API.  The `get()` method of the `requests` module takes this dict, along with the url string, to submit a GET request and store the `response` object.
See [ESRI Feature Service Documentation](https://developers.arcgis.com/rest/services-reference/query-feature-service-.htm)
### `where` clause
* **Must** be a SQL `where` clause that evaluates to True
* formatted as a Python string
* no URL encoding is required
* supported operators
  * `( '<=' | '>=' | '<' | '>' | '=' | '!=' | '<>' | LIKE )`
  * `(AND | OR)`
  * `(IS | IS_NOT)`
  * `(IN | NOT_IN) ( expr )`
  * `COLUMN_NAME BETWEEN LITERAL_VALUE AND LITERAL_VALUE`  
* examples:
  * `"where": "1=1",`
  * `'where': 'OBJECTID > 0',`
  * `"where": "year = 1998",`
  * `"where": """year_of_const LIKE '%1985%' OR year_of_const LIKE '%1986%'""",`
  * `"where": "CITY_NAME = 'Barrington'",`
    * note: string literals must be single-quoted
  * see more examples in the REST API [where documentation](https://developers.arcgis.com/rest/services-reference/query-feature-service-layer-.htm)
### `outFields`
* List of fields to be returned from the API query
* formatted as a Python string, with a comma-delimited (no space) list of fieldnames
* use an asterisk (quoted) to return all fields
* examples:
  * `'outFields': '*',`
  * `"outFields": "Match_addr,Addr_type",`
### `returnGeometry`
* when set to `true` the GeoJSON representation of the feature geometry is included in the response
* when set to `false` the geometry is not included
  * use this option when you need to get attribute field values and have no need for the geometry, which can be very large
### `outSR`
* spatial reference of the returned geometry features
* can be an empty string, in which case, according to ESRI documentation, the SRID returned is "the same as the map"
  * typically `SRID: 3857 - WGS 84 Web (pseudo) Mercator`
* can be specified as a WKID number (in a string format)
  * `'outSR': '4326',  # 4326 = WGS 84 lat/lon decimal degrees`
  * `'outSR': '32612', # 32612 = WGS 84 UTM zone 12`
  * `"outSR": "3395",  # 3395 = WGS 84 compliant World Mercator, units: meters`
### `returnCountOnly`
* when `true` the number of features that match the `where` clause is returned
* no additional attributes or features are returned
* useful when you need to know the total number features you need to request
* divide this value by the `maxRecordCount` attribute of the feature service to determine the number of API requests required to obtain all of the features in a feature service
### `resultRecordCount` and `resultOffset`
* specifies the number of records to return in the API request and the starting point
* use both to obtain records in batches when the Max Record Count property exceeds the total number of records that are needed from the feature service
* example scenario:
1. the `maxRecordCount` attribute limits requests to 1000 records per API call
2. the `returnCountOnly` request indicates that there are 14,523 total records available in the feature service
3. to obtain all records, 15 individual API calls will be required
  * 1st request: `'resultOffset': 0` and `'resultRecordCount': 1000`
  * 2nd request: `'resultOffset': 1000` and `'resultRecordCount': 1000`
  * 3rd request: `'resultOffset': 2000` and `'resultRecordCount': 1000` ...
  * 15th request:`'resultOffset': 14000` and `'resultRecordCount': 1000`
### `geometryPrecision`
* allows for specifying the number of decimal places in coordinates in the feature geometry returned from feature service
  * doesn't seem to work when tested on the ArcGIS Online geocoding service, but that service might not be returning a Geometry GeoJSON object
### `f`
* specifies the format of the response
* valid options are:
  * `html` and `json`
* use `json` for spatial data
  * output can be imported directly into GIS software

## SQL Statistics (needs more work)
* see documentation: ArcGIS REST API Services Reference [Query](https://developers.arcgis.com/rest/services-reference/query-feature-service-layer-.htm)

