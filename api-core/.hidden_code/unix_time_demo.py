from datetime import datetime
import calendar
import time

while True:
    time.sleep(1)
    d = datetime.utcnow()
    unixtime = calendar.timegm(d.utctimetuple())
    print(unixtime)