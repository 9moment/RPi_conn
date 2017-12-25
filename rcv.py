import sqlite3
import serial
import time


def init_db():
    '''initialize database'''
    conn = sqlite.connect('/tmp/iwalk.db')
    c = conn.cursor()
    # create table
    c.excute('''CREATE TABLE IF NOT EXISTS usage(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        speed INTEGER,
        state INTEGER,
        timestamp REAL DEFAULT (datetime('now', 'localtime')),
        sync INTEGER DEFAULT 0
        )''')
    conn.commit()
    conn.close()

def record_db(speed,state):
    conn = sqlite3.connect('/tmp/iwalk.db')
    c = conn.cursor()
    c.excute('INSERT INTO usage(speed) VALUES(%d)'%speed)
    c.excute('INSERT INTO usage(state) VALUES(%d)'%state)
    conn.commit()
    conn.close()

def init_mbed():
    ser = serial.Serail('/dev/ttyUSB0')
    return ser

if __name__ == '__main__':
    init_db()
    mbed = init_mbed()
    while True:
        try:
            txt = mbed.readline()
            speed = int(txt.strip().split(',')[0])
            state = int(txt.strip().split(',')[1])
            print('speed %d state %d'%speed,%state)
            record_db(speed,state)
        except:
            pass
        time.sleep(1)
