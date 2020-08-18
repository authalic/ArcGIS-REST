import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import pytz


# Hosted Feature Services status RSS feed
AGOL = r'https://status.arcgis.com/rss/ago_fs.rss'

r = requests.get(AGOL)


root = ET.fromstring(r.content)

channel = root[0]
print(channel.find('updated').text)





for t in channel.iter('item'):
    print(t.find('title').text)
