import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
data = serial.readline()
print(data)
