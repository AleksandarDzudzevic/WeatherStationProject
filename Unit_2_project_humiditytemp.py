import serial
import time
import matplotlib.pyplot as plt
import numpy as np

arduino = serial.Serial(port='/dev/cu.usbserial-10', baudrate=9600, timeout=.1)

def read():
   data = ""
   while len(data)<1:
       data = arduino.readline()
   return data
i = 1

humiditylst = []
templist = []
readingslist = []
while 0<i<30:
   time.sleep(0.1)
   value = read() #wait until data is in the port
   msg = value.decode('utf-8')
   if i==1:
       i += 1
       print(msg)
   else:
       humiditylst.append(msg[9:13])
       templist.append(msg[28:32])
       readingslist.append(i-1)
       print(msg)
       i += 1
newhumidlst = [item.replace("'","") for item in humiditylst]
newhumidlst.sort()
print(templist)
print(newhumidlst)
print(readingslist)
fig = plt.figure(figsize=(10,4))

plt.title("Humidity on campus November 15th 2022")
plt.subplot(1,2,1)#row, col, position
plt.scatter(readingslist,newhumidlst)
plt.ylabel("Humidity")
plt.xlabel("Readings")

plt.subplot(1,2,2)
plt.title("Humidity on campus November 15th 2022")
plt.scatter(readingslist,templist)
plt.ylabel("Temperature")
plt.xlabel("Readings")


plt.show()
