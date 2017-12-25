import serial
import sqlite3
from datetime import datetime
import time

if __name__=='__main__':
    ser = serial.Serial('/dev/ttyACM0')
    while True:
        conn = sqlite3.connect ('info.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS two (timestamp TEXT,status TEXT,id TEXT)''')
        try:
           val = ser.readline()
           d = datetime.now()
           txt = d.strftime("%d-%m-%y %H:%M:%S")
           s = val.split(",")
           c.execute("INSERT INTO two VALUES('%s','%s','%s')"%(txt,s[0],s[1]))
           print txt
           print s[0]
           print s[1]
        except:
           print 'fail'
        conn.commit()
    conn.close()
