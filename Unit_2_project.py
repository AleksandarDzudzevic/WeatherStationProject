import json
import Adafruit_DHT
import statistics
from datetime import datetime
import requests
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import time
sensor_1_pin=17
sensor_2_pin=4
sensor_3_pin=22
sensor_4_pin=27

sensor1tempid=35
sensor2tempid=397
sensor3tempid=399
sensor4tempid=401

sensor1humidityid=33
sensor2humidityid=398
sensor3humidityid=400
sensor4humidityid=402


def token():
    user = {"username":"Aleks","password":"October19"}
    req=requests.post('http://192.168.6.142/login',json=user)
    access_token = req.json()["access_token"]
    return(access_token)

access_token=token()

auth = {"Authorization": f"Bearer {access_token}"}
list = [sensor_1_pin,sensor_2_pin,sensor_3_pin,sensor_4_pin]
#check if the sensor is connected
for i in range(4):
    if Adafruit_DHT.read_retry(11,list[i]) is not None:
        print(f"Sensor {i+1} is connected")
    else:
        print(f" Sensor {i+1} is Not Working")
        exit(f"Sensor {i+1} is not working")

def senddata(value, sensor_id):
    new_record ={"datetime":str(datetime.isoformat(datetime.now())),"sensor_id":sensor_id, "value":value}
    r = requests.post('http://192.168.6.142/reading/new', json=new_record, headers=auth)

def get_readings():
    humidity1, temperature1 = Adafruit_DHT.read_retry(11, sensor_1_pin)
    senddata(temperature1, sensor1tempid)
    senddata(humidity1, sensor1humidityid)
    humidity2, temperature2 = Adafruit_DHT.read_retry(11, sensor_2_pin)
    senddata(temperature2, sensor2tempid)
    senddata(humidity2, sensor2humidityid)
    humidity3, temperature3 = Adafruit_DHT.read_retry(11, sensor_3_pin)
    senddata(temperature3, sensor3tempid)
    senddata(humidity3, sensor3humidityid)
    humidity4, temperature4 = Adafruit_DHT.read_retry(11, sensor_4_pin)
    senddata(temperature4, sensor4tempid)
    senddata(humidity4, sensor4humidityid)


    median_temp = statistics.median([temperature1, temperature2, temperature3, temperature4])
    median_humidity = statistics.median([humidity1, humidity2, humidity3, humidity4])
    reading =(f"{temperature1},{humidity1},{temperature2},{humidity2},{temperature3},{humidity3},{temperature4},{humidity4},{datetime.isoformat(datetime.now())},{median_temp},{median_humidity}")
    return (reading)

#with open("log.log", "r") as file:
#        log_data = file.readlines()
reading=get_readings()
with open("/home/dev/readings.csv","a") as f:
    f.write(f"{reading} \n")
print(f"It worked {datetime.now()} \n")



