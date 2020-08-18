
from datetime import datetime


### BUG in PYTHON?
### the following doesn't work

timestamp = 'Tue, 11 Aug 2020 09:33:09 PDT'
dtstr = r'%a, %d %b %Y %H:%M:%S %Z'

d = datetime.strptime(timestamp, dtstr)

# the datetime.striptime() method doesn't like that time zone portion at the end
# the 'PDT' doesn't fit in the %Z
