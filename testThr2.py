#!/usr/bin/env python
import time
import threading
import sqlite3

class myDb:
	def __init__(self):
		conn = sqlite3.connect('my.db')
		c = conn.cursor()
		c.execute('CREATE TABLE IF NOT EXISTS data(t REAL, reported INTEGER)')
		conn.commit()
		conn.close()

	def record(self, t):
		conn = sqlite3.connect('my.db')
		c = conn.cursor()
		c.execute('INSERT INTO data VALUES(?,0)', (t,))
		conn.commit()
		conn.close()

	def query(self):
		conn = sqlite3.connect('my.db')
		c = conn.cursor()
		c.execute('SELECT t FROM data WHERE reported = 0')
		print c.fetchall()
		c.execute('UPDATE data SET reported = 1 WHERE reported = 0')
		conn.commit()
		conn.close()
	

def acquireData():
	dbase = myDb()
	while True:
		t = time.time()
		dbase.record(t)
		time.sleep(2)

def reportData():
	dbase = myDb()
	while True:
		dbase.query()
		time.sleep(5)

if __name__ == "__main__":
	t1 = threading.Thread(target=acquireData)
	t2 = threading.Thread(target=reportData)
	t1.start()
	t2.start()
