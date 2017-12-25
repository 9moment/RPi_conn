import serial

data = "Hello B1"

ser = serial.Serial('/dev/ttyUSB0')

output = ser.write(data)
print('Data sent')

print('Wait Data input')
input = ser.readline()
print(input)
