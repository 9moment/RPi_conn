import serial
import sqlite3

if __name__ == '__main__':
	ser serial.Serial('/dev/ttyACM0')
	conn = sqlite3.connect('example.db')
	c = conn.cursor(0

	# Create table
	c.execute('''CREATE TABLE device IF NOT EXISTS
			(id INTEGER, timestamp TEXT, update INTEGER)''') 
	c.execute("INSERT INTO device VALUE (10, '2016-09-26 11:45',0)")
	conn.commit()
	conn.close()
