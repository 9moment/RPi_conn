import urllib2
import sqlite3
from datetime import datetime
import time
import json

if __name__ == '__main__':
    conn = sqlite3.connect('info.db')
    while True:
        c = conn.cursor()
        for row in c.execute ("SELECT * FROM two ORDER BY timestamp DESC LIMIT 1"):
            d = datetime.strptime(row[0],"%d-%m-%y %H:%M:%S")
            t = time.mktime(d.timetuple())
            id = 15
            status = row[1]
            print d
            print status
            if status=='on':
               val = 1
            elif status=='off':
               val=0
            url = 'https://api.thingspeak.com/update?api_key=EGGA5STT9JZ8J0K9&field1=%d&field2=%d'
            print url
            print val
            resp = urllib2.urlopen(url%(val,id))
            reply = json.load(resp)
        conn.commit()
        time.sleep(2)
    conn.close
