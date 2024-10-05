#CREATING AN ACCOUNT
from datetime import datetime

import requests

user = {"username":"Aleks","password":"October19"}
req=requests.post('http://192.168.6.142/register',json =user)
print(req.json())
#CREATING THE LOGIN
req=requests.post('http://192.168.6.142/login',json=user)
access_token = req.json()["access_token"]
print(access_token)
# SENSOR
auth={"Authorization":f"Bearer {access_token}"}

new_sensor = {"type":"Temperature","location":"R2-10B","name":"sensor_alex_bern_1","unit":"C"}

r = requests.post('http://192.168.6.142/sensor/new', json=new_sensor,headers=auth)
print(r.json())
# POSTING A NEW RECORDING
auth = {"Authorization":f"Bearer {access_token}"}

new_record= {"datetime":datetime.isoformat(datetime.now()),"sensor_id":26,"value":90.0}

r=requests.post('http://192.168.6.142/reading/new',json=new_record,headers=auth)
print(r.json())
