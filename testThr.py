#!/usr/bin/env python
import time
import threading


def printMe():
	while True:
		time.sleep(3)
		print "Me"

def printYou():
	while True:	
		time.sleep(5)
		print "You"

if __name__ == '__main__':
	t1 = threading.Thread(target=printMe)
	t2 = threading.Thread(target=printYou)
	t1.start()
	t2.start()
	while True:
		print "Hello world"
		time.sleep(10)
