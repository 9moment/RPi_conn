from threading import Thread, Timer, Lock, Event
import time
import serial
import urllib2
import sqlite3


def accept_callback(run_flag, dev_db):
    ''' Callback for accept thread '''
    ser = serial.Serial('/dev/ttyACM1')
    print('Accept thread starts')
    while True:
        conn = sqlite3.connet("mantour.db")
        c = conn.cursor()
        c.execute(''''CREATE TABLE IF NOT EXISTS non(id INTEGER, status INTEGER, timestamp TEXT)''')
        try:
            b = ser.readline()
            bs = b.split(",")
            d = datetime.now()
            txt = d.strftime("%d-%m-%Y %H:%M")
            bs1 = int(bs[0])
            bs2 = int(bs[1])
            c.execute("INSERT INTO non VALUES (%d,%d, '%s' )"%(bs1, bs2, txt))
            print bs1
            print bs2
            print txt
        except:
            pass
        if run_flag.is_set():
            print 'Thread'

        else:
            break
    print('Accept thread stops')


def sync_callback(accept_thread, dev_db):
    ''' Callback for synchronize thread '''
    print('Synchronize timer starts')

    if accept_thread.is_alive():
        print 'Timer'
        Timer(2, sync_callback, [accept_thread, dev_db]).start()
    else:
        print('Synchronize timer terminates')


class DatabaseWrapper():
    ''' Utility class to wrap database '''
    def __init__(self, dbfile):
        self.db = sqlite3.connect(dbfile)
        c = self.db.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS device
                     (_id INTEGER PRIMARY KEY AUTOINCREMENT, ID INTEGER, timestamp TEXT, updated INTEGER)''')
        self.db.commit()
        self.lock = Lock()

    def access(self):
        self.lock.acquire()
        return self.db

    def release(self):
        self.lock.release()


if __name__ == '__main__':
    ''' Execute threads to accept and synchronize '''
    dev_db = DatabaseWrapper('test.db')
    run_flag = Event()
    run_flag.set()
    accept_thread = Thread(target=accept_callback, args=(run_flag, dev_db,))
    accept_thread.start()
    Timer(2, sync_callback, args=[accept_thread, dev_db]).start()
    try:
        while True:
            time.sleep(0.1)
    except:
        run_flag.clear()
    accept_thread.join()
    print 'Program ended'
