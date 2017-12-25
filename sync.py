import urllib2
import sqlite3
from datetime import datetime
import time
import json

def compute_data():
    while True:
        c = conn.cursor()
        for row in c.execute ("SELECT * FROM usage WHERE sync = '0' ORDER BY timetsmp DESC LIMIT 1")
        

def sync_data():
    receive data from above fx adn explane data
    url = 'http://abc.com/update?api_key=abc&speed=%d&time=%d'
    resp = urllib2.urlopen(url%(speed,time))
    reply = json.load(resp)

if __name__ == '__main__':
    conn = sqlite3.connect('iwalk.db')
    while True:
        c = conn.cursor()

        for row in c.execute ("SELECT * FROM usage WHERE sync = '0' ORDER BY timestamp DESC LIMIT 1"):

            d = datetime.strptime(row[0],"%d-%m-%y %H:%M:%S")
            t = time.mktime(d.timetuple())
            status = row[1]
            print d
            print status
            if status=='0':
                val = 0
            elif status=='1':
                val = 1
            url = 'http://api.thingspeak.com/update?api_key=EGGASSTT9JZ8J0K9&field1=%d&field2=%d'
            print url
            print val
            resp = urllib2.urlopen(url%(val,id))
            reply = json.load(resp)
            c.execute ("UPDATE usage SET sync = '1' ")
        conn.commit()
        time.sleep(2)
    conn.close
