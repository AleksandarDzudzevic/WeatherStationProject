import statistics

import requests
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

plt.style.use('ggplot')


def get_sensor(readings: list, id: int) -> list:
    T = []
    for r in readings:
        if r["sensor_id"] == id and r["id"] > 31847 and r[
            "id"] < 44980:  # This is the id range for the 48hour period that we chose
            T.append(r['value'])
    return T


def download(url: str = "192.168.6.142/readings") -> list:
    req = requests.get(f'http://{url}')
    data = req.json()
    readings = data["readings"][0]
    return readings


def smoothing(data: list, size_window: int = 12) -> list:
    x = []
    y = []
    for i in range(0, len(data) - 12, size_window):
        segment_mean = sum(data[i:i + size_window]) / size_window
        y.append(segment_mean)
        x.append(i // size_window)  # hours 1,2,3,4,5...
    return x, y


mean_per_hour_temp = []
mean_per_hour_hum = []
sensor1tempid = 35
sensor2tempid = 397
sensor3tempid = 399
sensor4tempid = 401

sensor1humidityid = 33
sensor2humidityid = 398
sensor3humidityid = 400
sensor4humidityid = 402

readings = download()
sensors_temp = [sensor1tempid, sensor2tempid, sensor3tempid, sensor4tempid]
sensors_humidity = [sensor1humidityid, sensor2humidityid, sensor3humidityid, sensor4humidityid]
outside_humidity_id = 4
outside_temp_id = 5

humidity_readings_out = get_sensor(readings, outside_humidity_id)
temperature_readings_out = get_sensor(readings, outside_temp_id)
x = []
mean_per_hour = []
for i in range(576):
    x.append(i/12)
avarage_temp = []
avarage_hum = []
data1temp = get_sensor(readings, sensor1tempid)
data2temp = get_sensor(readings, sensor2tempid)
data3temp = get_sensor(readings, sensor3tempid)
data4temp = get_sensor(readings, sensor4tempid)

data1hum = get_sensor(readings, sensor1humidityid)
data2hum = get_sensor(readings, sensor2humidityid)
data3hum = get_sensor(readings, sensor3humidityid)
data4hum = get_sensor(readings, sensor4humidityid)
# Raw data graph comparison
plt.subplot(2,1,1)
plt.plot(x,humidity_readings_out,color="blue")
plt.xlabel("Hours")
plt.ylabel("Humidity (%)")
plt.title("Humidity recorded outside during the 48 hour period")
plt.subplot(2,1,2)
plt.plot(x,temperature_readings_out,color="red")
plt.xlabel("Hours")
plt.ylabel("Temperature (Celsius)")
plt.title("Temperature recorded outside during the 48 hour period")

plt.show()



for i in range(576):
    x.append(i/12)
temp_max = []
hum_max = []
temp_min = []
hum_min = []
temp_dif = []
counter_for_good_temp=0

# Pie chart showing the percentage of recordings of temperatrue which were in the optimal tempertaure range
for i in range(576):
    avarage_temp.append((data1temp[i] + data2temp[i] + data3temp[i] + data4temp[i]) / 4)
    avarage_hum.append((data1hum[i] + data2hum[i] + data3hum[i] + data4hum[i]) / 4)
    temp_max.append(max(data1temp[i] ,data2temp[i] , data3temp[i] , data4temp[i]))
    temp_min.append(min(data1temp[i] ,data2temp[i] , data3temp[i] , data4temp[i]))
    hum_max.append(max(data1hum[i],data2hum[i],data3hum[i],data4hum[i]))
    hum_min.append(min(data1hum[i],data2hum[i],data3hum[i],data4hum[i]))
    temp_dif.append(temp_max[i]-temp_min[i])
if (avarage_temp[i]>=20 and avarage_temp[i]<=22 ):
    counter_for_good_temp+=1
temperature_good_bad=[counter_for_good_temp,576]
percentage= str(int(counter_for_good_temp/576 *100))+"%"
mylabels=["Recorded optimal temperature in the room[ 20-22 Celsius ]","Recorded unoptimal temperature in the rooms"]
mycolors=["#109010","red"]
myexplode=[0.3,0]

plt.pie(temperature_good_bad,labels = mylabels,colors=mycolors,explode=myexplode,shadow=True,startangle = 90)
plt.legend()
plt.text(x=-0.45,y=0.8,s=percentage)
plt.show()


y_third = []
x,avarage_temp=smoothing(avarage_temp)
x,temp_dif=smoothing(temp_dif)
p= np.polyfit(x,avarage_temp, 3)  # 2 means power of 2
for i in x:
    y_third.append(p[0]* (i**3) + p[1] * (i ** 2) + p[2] * i + p[3])
plt.errorbar(x,y_third,temp_dif,color='#771299')
plt.title(f"Mean temperature with standard deviation recived during that recording from 13:05 10.12.2022 - 01:05 11.12.2022")
plt.xlabel("Hours")
plt.ylabel("Temperature (Celsius)")
plt.show()





# Predicting the weather for the next 12 hours with 4.5% error margin after calculating the difference in the outside weather from the 2 days before compared to today
sensor_data = []
for s in sensors_temp:
    data = get_sensor(readings, s)
    x, data_smth = smoothing(data)
    sensor_data.append((data_smth))

for i in range(len(sensor_data[0])):
    d = [sensor_data[x][i] for x in range(len(sensors_temp))]
    mean_per_hour_temp.append(sum(d) / len(sensors_temp))


prediction_hum_12h_higher = []
prediction_hum_12h_lower = []
x_pred = []

for i in range(144):  # 576 readings for 48 hours-> 144 for 12h
    prediction_hum_12h_higher.append(avarage_hum[
                                         i + 144] * 1.2)  # +144 because the data from 24th to 36th hour of recording is most aplicable for the prediction
    prediction_hum_12h_lower.append(avarage_hum[i + 144] * 0.8)
    x_pred.append(i / 12)
y_quad = []
p0, p1, p2 = np.polyfit(x_pred, avarage_hum[288:(288 + len(x_pred))], 2)  # 2 means power of 2
for i in x_pred:
    y_quad.append(p0 * (i ** 2) + p1 * i + p2)
plt.plot(x_pred, y_quad, color="red")
plt.errorbar(x_pred,y_quad,1.5,color='blue')
plt.title(f"Prediction of the Humidity for the subsequent 12 hours from 13:05 10.12.2022 - 01:05 11.12.2022")
plt.xlabel("Hours")
plt.ylabel("Humidity (%)")

plt.show()

# predicting the weather for subseqyent 12 hours
prediction_temp_12h_higher = []
prediction_temp_12h_lower = []
x_pred = []
# Predicting the weather for the next 12 hours with 4.5% error margin after calculating the difference in the outside weather from the 2 days before compared to today

for i in range(144):  # 576 readings for 48 hours-> 144 for 12h
    prediction_temp_12h_higher.append(avarage_temp[
                                          i + 144] * 1.045)  # +144 because the data from 24th to 36th hour of recording is most aplicable for the prediction
    prediction_temp_12h_lower.append(avarage_temp[i + 144] * 0.955)
    x_pred.append(i / 12)
plt.fill_between(x_pred, prediction_temp_12h_lower, prediction_temp_12h_higher, alpha=.5, linewidth=0)
plt.plot(x_pred, avarage_temp[144:288], linewidth=2)
plt.title(f"Prediction of the temperature for the subsequent 12 hours from 13:05 10.12.2022 - 01:05 11.12.2022")
plt.xlabel("Hours")
plt.ylabel("Temp (Celsius)")
plt.show()


# Shows the Mean temperature and individual recordings of temperatures during the period 13:05 8.12.2022 - 13:05 10.12.2022
fig = plt.figure(figsize=(10,8))
# from matplot.lib.gridspec import GridSpec
grid = GridSpec(4,4,figure=fig)
#create the big plot
box1= fig.add_subplot(grid[0:4,0:3])
plt.stem(x,mean_per_hour_temp)
plt.title(f"Temperature of local sensor inside 13:05 8.12.2022 - 13:05 10.12.2022")
plt.xlabel("Hours")
plt.ylabel("Temp (Celsius)")
plt.ylim([10,28])
my_colors = ["#7fffcc", "#34ff45","#44ffff","#ff3344"]
for i in range(len(sensors_temp)):
    box2 = fig.add_subplot(grid[i,3])
    plt.plot(x,sensor_data[i],color = my_colors[i])
    plt.title(f"Sensor #{sensors_temp[i]}")
    plt.ylim([10,28]) # shows Y axis from _ to _ (helps with visibility)
plt .show()

# Shows the Mean humidity and individual recordings of humidity during the period 13:05 8.12.2022 - 13:05 10.12.2022
sensor_data = []
for s in sensors_humidity:
    data = get_sensor(readings, s)
    x2,data_smth = smoothing(data)
    sensor_data.append((data_smth))

for i in range (len(sensor_data[0])) :
    d = [sensor_data[x][i] for x in range (len(sensors_humidity))]
    mean_per_hour_hum.append(sum(d)/len(sensors_humidity))

fig = plt.figure(figsize=(10,8))
# from matplot.lib.gridspec import GridSpec
grid = GridSpec(4,4,figure=fig)
#create the big plot
box1= fig.add_subplot(grid[0:4,0:3])
plt.bar(x2,mean_per_hour_hum,color='#102099')
plt.ylim([15,30])# shows Y axis from _ to _ (helps with visibility)
plt.title(f"Humidity of local sensor inside 13:05 8.12.2022 - 13:05 10.12.2022")
plt.xlabel("Hours")
plt.ylabel("Humidity (%)")


my_colors = ["#7fffcc", "#34ff45","#44ffff","#ff3344"]
for i in range(len(sensors_humidity)):
    box2 = fig.add_subplot(grid[i,3])
    plt.plot(x2,sensor_data[i],color = my_colors[i])
    plt.title(f"Sensor #{sensors_humidity[i]}")
    plt.ylim([15,55])# shows Y axis from _ to _ (helps with visibility)


# Relationship between inside and outside weather
x3=[]
plt.subplot(2,1,1)
for i in range(144):
    x3.append(i/12)
y_quad=[]
y_quad4=[]
print(len(temperature_readings_out[0:144]))
print(len(avarage_temp[0:144]))
p0,p1,p2 = np.polyfit(x3,temperature_readings_out[0:144],2)#2 means power of 2
q0,q1,q2 = np.polyfit(x3,avarage_temp[0:144],2)#2 means power of 2
for i in x3:
    y_quad.append(p0*(i**2)+p1*i+p2)
    y_quad4.append(q0*(i**2)+q1*i+q2)

plt.plot(x3,y_quad,color="blue")
plt.title(f"Comparison:mean outside temp(BLUE) vs mean inside temp(RED)13:05 8.12.2022 - 13:05 10.12.2022")
plt.xlabel("Hours")
plt.ylabel("Temp (Celsius)")
plt.plot(x3,y_quad4,color='red')

plt.subplot(2,1,2)
x4,mean_hum_out=smoothing(humidity_readings_out)
y_quad2=[]
y_quad3=[]
p0,p1,p2 = np.polyfit(x3,humidity_readings_out[0:144],2)#2 means power of 2
q0,q1,q2 = np.polyfit(x3,avarage_hum[0:144],2)#2 means power of 2

for i in x3:
    y_quad2.append(p0*(i**2)+p1*i+p2)
    y_quad3.append(q0*(i**2)+q1*i+q2)

plt.plot(x3,y_quad2,color="blue")
plt.plot(x3,y_quad3,color='red')
plt.title(f"Comparison:mean outside humidity(BLUE) vs mean inside humidity(RED)13:05 8.12.2022 - 13:05 10.12.2022")
plt.xlabel("Hours")
plt.ylabel("Humidity (%)")
plt.show()
