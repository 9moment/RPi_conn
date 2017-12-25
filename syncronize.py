import urllib2
import sqlite3

if __name__ == '__main__':
	conn = sqlite3.connect('examle.db')
	c = conn.cursor()

	c.excute("SELRCT * FROM device")
	print c.fetchone()

