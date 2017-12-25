import serial
import sqlite3

if __name__ == '__main__':
	ser = serial.serial('/dev/ttyACM0')
	conn = sqlite3.connect('example.db')
	c = conn.cursor()

	#create table
	c.execute('''CREATE TABLE device IF NOT EXISTS
			(id INTRGER, timestamp TEXT, update INTEGER)''')
	c.execute("INSERT INTO devive VALUE (10, '2016-09-26 11:45',0)")
	conn.comit()
	conn.close()

