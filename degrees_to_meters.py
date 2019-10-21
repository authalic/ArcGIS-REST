# convert WGS 84 lat/lon degrees to Web Mercator meters
# source: https://community.esri.com/thread/89445


def geographic_to_web_mercator(x_lon, y_lat):
    if abs(x_lon) <= 180 and abs(y_lat) < 90:
        num = x_lon * 0.017453292519943295
        x = 6378137.0 * num
        a = y_lat * 0.017453292519943295
        x_mercator = x
        y_mercator = 3189068.5 * math.log((1.0 + math.sin(a)) / (1.0 - math.sin(a)))
        return x_mercator, y_mercator
    else:
        print('Invalid coordinate values for conversion')


# another method
# src: https://gis.stackexchange.com/questions/15269/how-to-convert-lat-long-to-meters-using-mercator-projection-in-c

def projLatLonToWorldMercator(lat,lon,isDeg=False):
    """
    LatLonToWorldMercator

     Converts a latitude/longitude pair to x and y coordinates in the
     World Mercator projection.

     Inputs:
       lat   - Latitude of the point.
       lon   - Longitude of the point.
       isDeg - Whether the given latitude and longitude are in degrees. If False 
               (default) it is assumed they are in radians.

     Returns:
       x,y - A 2-element tuple with the World Mercator x and y values.

    """     
    lon0 = 0
    if isDeg:
        lat = projDegToRad(lat)
        lon = projDegToRad(lon)

    x = sm_a*(lon-lon0)
    y = sm_a*math.log((math.sin(lat)+1)/math.cos(lat))

    return  x,y 


def projDegToRad(deg):
    return (deg / 180.0 * pi)

def projRadToDeg (rad):
    return (rad / pi * 180.0)