from threading import Thread, Timer, Lock
import time
#import serial
import urllib2
import sqlite3


def accept_callback(dev_db):
    ''' Callback for accept thread '''
    print('Accept thread starts')
    while True:
        print 'Thread'
        time.sleep(5)
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
    accept_thread = Thread(target=accept_callback, args=(dev_db,))
    accept_thread.start()
    Timer(2, sync_callback, args=[accept_thread, dev_db]).start()
    accept_thread.join()
