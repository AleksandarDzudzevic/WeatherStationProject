![weather.png](https://github.com/AleksandarDzudzevic/Project_unit_2/blob/main/weatherpic.jpeg)

# Unit 2: A Distributed Weather Station for ISAK

# Criteria A: Planning

## Problem definition
The health center is in urgent need to solve a fast-growing problem at ISAK. Due to unoptimal humidity and temperature of the student rooms, ISAK students have been visiting nurses a lot more frequently with the issues related to soar throat. The nurses believe that the reasoning behind students sore throats is because of the humidity and temperature levels inside of student rooms. The nurses want a remote server that they can access online to check the different humidity and temperature levels in the student doorms at different times throughout the day, and compare it to the optimal levels, as well as temperature and humidity levels outside. The data can vary depending on the part of the room so nurses need the data to be collected from different parts of the room in order to get the most accurate representation of the humidity and temperature levels.

## Success Criteria

1. The solution provides a visual representation of the Humidity and Temperature values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours. 
1. The local variables will be measure using a set of 4 sensors around the dormitory.
2. The solution provides a mathematical modelling for the Humidity and Temperature levels for each Local and Remote locations. (both lineal and non-lineal model)
3. The solution provides a comparative analysis for the Humidity and Temperature levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median.
4. The Local samples are stored in a csv file and posted to the remote server.
5. Create a prediction the subsequent 12 hours for both temperature and humidity.
6. A poster summarizing the visual representations, model and analysis is created and communicated.

## Design Statement 
Our team will create a device and program that will calculate both humiditiy and temperature in a room of a residential house on campus. To do this, we will use a Raspberry Pi 4 and four DHT_11 sensors to collect the humidity and temperature. The program will upload the collected data onto a server in real-time to reinforce the reliability and validity of our calculated data. We will use the device to record the humidity and temperature inside of a room for 48 hours, and the nurses on campus will be able to access the data through an online server anytime using a granted access token. Further, the nurses can use the data collected to compare to their information on optimal humidity and temperature. This project will take approximately 4 weeks and will be evaluated according to the criteria set above.


## Rationale for Proposed Solution
Considering the client requirements an adequate solution includes a low cost sensing device for humidity and temperature and a custom data script that process and anaysis the samples acquired. For a low cost sensing device an adequate alternative is the DHT11 sensor[1] which is offered online for less than 5 USD and provides adequare precision and range for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20 or the AM2301B [2] have higher specifications, however the DHT11 uses a simple serial communication (SPI) rather than more eleborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy required in this applicaiton the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Arduino UNO microcontroller [3]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[4]. In additon to the low cost of the Arduino (< 6USD), this devide is programable and expandable[1]. Other alternatives include diffeerent versions of the original Arduino but their size and price make them a less adequate solution.

Considering the budgetary constrains of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python is open source, it is mature and supported in mutiple platforms (platform-independent) including macOS, Windows, Linux and can also be used to program the Arduino microprocessor[5][6]. In comparison to the alternative C or C++, which share similar features, Python is a High level programming language (HLL) with high abstraction [7]. For example, memory management is automatic in Python whereas it is responsability of the C/C++ developer to allocate and free up memory [7], this could result in faster applications but also memory problems. In addition a HLL language will allow me and future developers extend the solution or solve issues proptly.

# Criteria B: Design

![](sysdim_hl.png)

**Fig.2** shows the system diagram for the proposed solution (**HL**). The indoor variables will be measured using a Raspberry PI and four DHT11 sensors located inside a room. Four sensors are used to determine more precisely the physical values and include measurement uncertainty. The outdoor variables will be requested to the remote server using a GET request to the API of the server at ```192.168.6.147/readings```. The local values are stored in a CSV database locally and POST to the server using the API and TOKEN authentication. A laptop computer is used for remotely controlling the local Rasberry Pi using a Dekptop sharing application (VNC Viewer). (Optional) Data from the local raspberry is downloaded to the laptop for analysis and processing.

### List of materials:

1 x Rasberry Pi model 4

4 x DHT-11 sensor

1x Breadboard

6 x Long Wires

8 x Small Connectors

A Remote desktop

1 x Usb cable to connect the rasberry pi to a power source

## Test Plan

| Test Type | Target | Procedure | Expected Outcome |
|-----------|--------|-----------|------------------|
| Functional: Integrational testing | User Sign Up  | 1. Enter the desired username and password 2. Try to sign up with the same username | The first time the username and password is set, the program should not return any error message and exit as normal. When the same username is used to attempt and create a new account, the program will return and error message, as the username is already taken. |
| Functional: Integrational testing | Login: Access Token | 1. Use the function (token). 2. Have the set credentials (username and password) in the function. | If the username and passwords match with the credentials from the remote server, the code will return an access token, which will allow the user to access the remote server that includes all the collected data (readings). If the username and password entered does not match any of the existing crendentials, the access token will not be granted to the user. |
| Functional: Integrational testing | Sensor connectivity | 1. Connect all sensors to breadboard 2. Run get_readings function | The program should return readings for all sensors connected, and if there is an error within any of the sensors, an error message should appear. |
| Non-functional: Load testing | Testing if the program has little lag or glitches due to the amount of time the program is ran for (48 hours). Additionally, see if continously added data (readings) influence the proccessing of the program. | 1. Run the program. 2. Continously check up on the code, every 2-3 hours. | All data is up to date, and the program is still continously running and recoridng data wihtout any glitches or lag. |
| Non-functional: Response time | Testing if the sensor responds quickly to the running program and see how long it takes for the sensor to register and print out the current temperature and humidity| 1. Run the basic program that aims to print the current temperature and humidity the sensor collects.| The program returns the swiftly returns the current temperature and humidity the sensor collects without any lag or delay. |
| Non-functional：Code review | Reviewing if the code has adequate comments, function name, and variable name.As this reviews the quality of the code, there are no inputs. | The procedure included a review of the code from a external developer who is not familiar with techniques used in it. The developer then gave feedback on which parts are not understandable and names of which variables are not logical when looking at the purpose of the variable.|The code will include comments explaining what is occuring within the code. Furthermore, the names of variables are simple and it is easy to understand what is their usage in the program |


## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
|1| Brainstorm and write the problem definition | A clear problem definition on Github   | 15 minutes         | Nov 22    | A
|2| Write the list of  materials  |  Have a full list of materials    |  5 minutes | Nov 24   | B |
|3| Brainstorm and write the design statement | A clear design statement that suits the need of the client | 20 minutes  |  Nov 29  | A |
|4| Write the Rationale for proposed solution | A clear justification that suits the client and developer.  | 10 minutes  |  Nov 29  | A |
|5|   Construct the device used to collect temperature and humidity data  |  A working device that accurately collects temperature and humidity data | 45 minutes  |  Nov 30  | B |
|6|   Create the code needed to accurately display data collected from the device  | The program continously collects data and stores it in a log over time.  | 20 minutes  |  Nov 30  | B |
|7| Create a code for signing up on the server |  Allows the user to create a username and password for the server | 30 minutes  |  Dec 2  | B |
|8|   Create a code for logging in on the server  | Allows the user to log into their account they had created  | 30 miinutes  |  Dec 2  | B |
|9| Create 8 seperate servers, 4 for both humidity and temperature levels. | Setup 8 servers to which the data will be automatically sent every 5 minutes for 48 hours | 15 min| Dec 4| B|
|10| Make a code for collecting the data and sending it to the server | Establish a connection to the server and send the obtained data|25min |Dec 6 | B | 
|11| Make a code for getting the data in the refined format and send it to the .csv file, and start with data collecting | Start data collecting by making the code for CSV file data input |40min| Dec 7| B|
|12| Implement better coding practices in the code| Have a more efficent code by using loops instead of multiple if statements, thus making the program faster and more organized|20min|Dec 9| B |
|13| Draw and describe the flow diagrams | Flow diagrams for different parts of the solution along with a brief explanation | 45 minutes | Dec 9 | B |
|14| Write the test plan (3 functional and 3 non-functional) | Procedures in which one should take to test the program and descriptions of the expected outcome of each test is on Github | 45 minutes | Dec 9 | B |
|15| Work on the development part in criteria C related to the criteria number 5|explained CT and process behind the data recording in a .csv file and posting it on the server| 20 min| Dec 10| C|
|16|Extract the reading from the remote server outside during the 48 hours when the recording inside the studentroom took place| Have apropriate range of data from the outside sensor (done by checking if the id of the reading is a part of the certain range compatable with id-s during the 48 hours when we collected recordings inside)|35 min|Dec 10| B |
|17| Work on the development part in criteria C related to the criteria number 2|Show the rasberry pi and the 4 sensors we used as well as the different locations inside the room from which the temperature and humidity were measured| 10 min| Dec 10| C|
|18|Code the program that plots graphs containg mean temp and humidity, and individual recordings from all the sensors|Program will produce the graphs that will be used on the poster and in section C|60min|Dec 10 |B|
|19|Code the program that plots graphs comparison of the outside and inside the room humidity and temperature during the 48hour recording|By using quadratic equations, plot a graph which is both visually pleasing and practical in the way that the client can see he relation between the outside and inside temperature and humidity|30 min| Dec 11|B|
|20|Work on the development part in criteria C related to the criteria number 1|Have a visual represntation  with an explanation of the data which fulfills the criteria 1 stated by the client|20 min|Dec 11|C|
|21|Code the program that plots graph predicting the temperature of the room during subsequent 12 hours|Have a program that will create a graph that clearly indicates predicted numbers for the temperature during subsequent 12 hours after 48hour recording period using the formula and CT that is given in criteria C #6 criteria|40min|Dec 11|B|
|22|Work on the development part in criteria C related to the criteria number 6| Have clear visual represntation with an explanation and CT behind the prediction of the data in the subsequent 12 hours|30 min|Dec 11|C|
|23|Code the program that plots graph predicting t humidity of the room during subsequent 12 hours|Have a program that will create a graph that clearly indicates predicted numbers for the humidity during subsequent 12 hours after 48hour recording period using the formula and CT that is given in criteria C #6 criteria|20min|Dec 11|B|

## Flow Diagrams

![](unit2flowchart1.jpg)

Fig 3. In this flow diagram above, it shows the function that checks if the sensor is connected and working. It checks if each sensor is collecting data, and if it does, it will print a message that tells the user that sensor is connected. However, if the sensor is not connected, it will print an error message displaying that the sensor is not working. It works by using a for loop and if-statement. The if-statement runs 4 times to check if all 4 sensors are connected.

![](unit2flowchart2.jpg)

Fig 4. In this flow diagram above, it shows the function that allows the user to gain an access token through the remote server using a username and password. It sends a request to the remote server, and inputs the credentials, and if the account exists and the crendtials are accurate within the database of the server, it returns an access token to the user which will allow them gain access to the data (readings) collected.

![](flowchart3.jpg)

Fig 5. In this flow diagram above, it shows the function that extracts the data from the sensors with an id within the appropriate range. The range of the sensor_ids that were used while collecting temperature and humidity data during the 48 hour procedure of data collecting inside the room. By using this function only the relavant data during that time will be used and later on presented, preventing any mistakes in the data corelation between the readings inside and outside the room.

## Data storing
#### Data consisting of the humidity and temperature levels during the 48-hour period when the recording was done was both recorded in a csv file and posted on the server. The example of the readings stored in a .csv file is given in the figure below.
![We used a .csv file to store 48hours worth of data measured every 5 min. Each row has a time when data was recorded, tempratures and humidity from all 4 sensors, median temperature and humidity](https://github.com/AleksandarDzudzevic/Project_unit_2/blob/main/crietria-c-proof5.1.png)

```.py
def get_readings(): #Intentionally not done in a for loop because this way we could see if there is an error with data sending we knowwhich sensor is the problem
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

    average_temp = (temperature1 + temperature2 + temperature3 + temperature4) / 4
    average_humidity = (humidity1 + humidity2 + humidity3 + humidity4) / 4
    median_temp = statistics.median([temperature1, temperature2, temperature3, temperature4])
    median_humidity = statistics.median([humidity1, humidity2, humidity3, humidity4])
    reading =(f"{temperature1},{humidity1},{temperature2},{humidity2},{temperature3},{humidity3},{temperature4},{humidity4},{datetime.isoformat(datetime.now())},{median_temp},{median_humidity}")
    return (reading)

reading=get_readings()
with open("/home/dev/readings.csv","a") as f:
    f.write(f"{reading} \n")
print(f"It worked {datetime.now()} \n")
```
# Criteria C: Development

## List of techniques used
Functions

Lists

For loops

While loops

PIN connection validation

File reading

Writing in a csv file

Loging to the Api servers 

Sending data to Api servers

Reading data from the Api server

Plotting graphs


## Development


### 1. The client wants The solution that provides a visual representation of the Humidity and Temperature values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours.
> By using matplot.lib we have visually presented mean temperature and humidity inside the room during the 48 hours as well as readings from all the sensors individually. For the mean readings of temperature and humidity inside(fig 1.1 and 1.2) we used plt.bar and plt.stem so that the data will be presented in the way which makes it easier to visually understand the change in the temperature and humidity througout the day.

>   Outside readings will be visually compared with the mean of the readings inside the dorm. We presented the data through using  quadratic equation, as the lines that way are much more visible and the client can clearly see the behaviour of the data changing due to the time of the day. This way we also allowed the client to easily see how the outside weather affects the humidity and temperature inside the room. With all these features we have presented a reliable solution to the request stated in criteria number 1 of the client.

We fulfilled criteria 1 by first using Decomposing part of CT and divided graph plotting into separate parts of the code. The Code 1.1  and 1.2 plots the representation of humidity and temperature readings during the 48h period. They consists of pattern recognition for calculating and storing mean value of the data from all 4 sensors,for smoothing data making the graphs visibility better, and for plotting of separate graphs for sensors individualy.

The outside data was presented using the comparison graph (Figure 1.3) The code for this (Code 1.3) was developed by first decomposing data into humidity and temperature segment. To get the data we developed an algorithm (Code 1.4) which checks if the id of the reading is in the certain range which represents the time period when 48hours of recording happend.
#### Code 1.1 Shows code used for plotting graphs for humidity data recorded during 48 hours.
```.py
# Graph for humidity
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
 ```
#### Code 1.2 Shows code used for plotting graphs for temperature data recorded during 48 hours.
```.py
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
```
#### Code 1.3 Shows the part of the program used to plot comparison graphs, allowing client to visually understand the relationship between the outside and inside data
```.py
plt.subplot(2,1,1)
x3,mean_temp_out=smoothing(temperature_readings_out)
y_quad=[]
y_quad4=[]
p0,p1,p2 = np.polyfit(x3,mean_temp_out,2)#2 means power of 2
q0,q1,q2 = np.polyfit(x3,mean_per_hour_temp,2)#2 means power of 2

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
p0,p1,p2 = np.polyfit(x3,mean_hum_out,2)#2 means power of 2
q0,q1,q2 = np.polyfit(x3,mean_per_hour_hum,2)#2 means power of 2

for i in x4:
    y_quad2.append(p0*(i**2)+p1*i+p2)
    y_quad3.append(q0*(i**2)+q1*i+q2)

plt.plot(x4,y_quad2,color="blue")
plt.plot(x4,y_quad3,color='red')
plt.title(f"Comparison:mean outside humidity(BLUE) vs mean inside humidity(RED)13:05 8.12.2022 - 13:05 10.12.2022")
plt.xlabel("Hours")
plt.ylabel("Humidity (%)")
plt.show()
```
#### Code 1.4 Shows the algorithm used to only acquire the data apropriate for the needed time period.
```.py def get_sensor(readings: list, id: int) -> list:
    T = []
    for r in readings:
        if r["sensor_id"] == id and r["id"] > 31847 and r[
            "id"] < 44980:  # This is the id range for the 48hour period that we chose
            T.append(r['value'])
    return T
  ```
#### Figure 1.1 shows mean humidity in the dorm and the humidity readings from all sensors individually.
![](https://github.com/AleksandarDzudzevic/Project_unit_2/blob/main/humidity_all_sensors_mean.png)
#### Figure 1.2 shows mean temperature in the dorm and the temperature readings from all sensors individually.
![](https://github.com/AleksandarDzudzevic/Project_unit_2/blob/main/temp_allsensors_mean.png)
#### Figure 1.3 shows the relation between humidity and temperature inside the room and outside 
![](https://github.com/AleksandarDzudzevic/Project_unit_2/blob/main/comparison_graphs_outside_inside.png)

 

### 2. The client requested that the local variables will be measured using a set of 4 sensors around the dormitory.
> We used rasberry pi 4 and 4 DHT 11 sensors to collect the data. By collecting it from multiple locations the diversity in data was achieved, allowing better representation of the humidity and temperature in thhe rooms was possible. The locations were changed during the 48 hour period, with location 1 being the main one where the majority of data was recorded. This is because it is distanced further from the window than location 1 but closer than location 3, so the data gives us what is closest to an avarage of the whole room. By doing this we fulfilled client's request for criteria 2.
> In adition to this, to make sure the data is being emasured every 5 minutes without any mistakes, we implemented a procedure in the code which checks if all the sensors are properly connected and working, allowing us to interven in the shortest period of tim e if neccesery. The code to this is given under the figure 2.2. 

We first developed code that would check if all the sensors are connected and working. Instead of using 4 if statements, we used the pattern recognition part of CT making the for loop that will execute the procedure more eficiently and making the code more visually pleasing.

#### Figure 2.1 shows Rsberry Pi connected to 4 DHT 11 sensors which recorded the data that client requested.
![](https://github.com/AleksandarDzudzevic/Project_unit_2/blob/main/rasberrypipic.jpg)
#### Figure 2.2 shows the location inside the room where the data gathering took place.
![](https://github.com/AleksandarDzudzevic/Project_unit_2/blob/main/locationsrasberrypi.jpg)
#### Figure 2.1 shows the part of the program that was used to monitor if the sensors are working during the 48hour period.
#### Code 2.1 
```.py
access_token=token()

auth = {"Authorization": f"Bearer {access_token}"}
list = [sensor_1_pin,sensor_2_pin,sensor_3_pin,sensor_4_pin]
for i in range(4):
    if Adafruit_DHT.read_retry(11,list[i]) is not None:
        print(f"Sensor {i+1} is connected")
    else:
        print(f" Sensor {i+1} is Not Working")
        exit(f"Sensor {i+1} is not working")
   ```
 
*Screenshot of for sensors used,picture of the model, picture of the rasberry pi and where it was moved during recordings

### 3. The client requested that the solution provides a mathematical modelling for the Humidity and Temperature levels for each Local and Remote locations. (both lineal and non-lineal model)
> We fulfilled this request for the following: comparison of the humidity and temperature levels inside and outside the student room (Figure 3.1), prediction of humidity level during the subsequent 12 hour period after the recordings took place. This is shown in the Figure 3.2. We have decided to use mathematical modelling when providing the visual representation for these examples due to the advantage of having data clearly separated and the relations between outside and inside clearly visible and easy to understand. For the humidity prediction we used this because unlike the temperature prediction, humidity varied a lot more with a bigger marginal error so the quadratic equation allowed us to present the expected trend of the humidity during this time period which was the main goal of that graph. With this criteria number 3 was fulfilled.

The development of the part of the program that fulfilled this criteria was first decomposed into 2 parts. Showing relations using mathematical modeling, and showing predictions using mathematical modeling. The code for the relations between data (Code 1.3) was developed by decomposing it into two subplots showing the relation between humidities and temperatures separately. Quadratic formula was aquired using np.polyfit and then put into an algorithm which would collect it into the list allowing the cretion of non-linear graphs.

#### Figure 3.1 shows the relation between humidity and temperature inside the room and outside using quadratic formlua
![](https://github.com/AleksandarDzudzevic/Project_unit_2/blob/main/comparison_graphs_outside_inside.png)
#### Figure 3.2 shows the linear graphing for the prediction of the humidity in the subsequent 12 hours after the measuring took place.
![](https://github.com/AleksandarDzudzevic/Project_unit_2/blob/main/humidity_prediciton_fot_next12h.png)
*Quadratic function graph for both remote and local

### 4. The solution provides a comparative analysis for the Humidity and Temperature levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median.

*Screenshots of the graphs

### 5. The client wanted the Local samples stored in a .csv file and posted to the remote server. We did this by uploading recordings to the server using the following code

> We used the following function to send the data to the server y using /reading/new endpoint on the server API. It allowed us to create a record for a sensor in the server. The user logged in is the owner of the record. 

The procedure behind this is that we needed to decompose problem into the following:
1) Sending data to the server (Code 5.1)
2) Putting the data into a .csv file (Code 5.2)

#### Code 5.1 Abstracting part of CT- defining a function used to post the recordings.

```.py
def senddata(value, sensor_id):
    new_record ={"datetime":str(datetime.isoformat(datetime.now())),"sensor_id":sensor_id, "value":value}
    r = requests.post('http://192.168.6.142/reading/new', json=new_record, headers=auth)
```

> The client also wanted us to store the data into a csv file which we did, using the code below. We used get_readings function in the way which allowed us to first send data from all the sensors to the server, and then store the data in the variable which would get returned in the endo of the function allowing us to store it in the .csv file using poen f and f.write features.

#### Code 5.2 Getting the readings from all sensors  and putting them into a .csv file(The recognition of the pattern  was present but it was not done, explained in the commemnt)
```.py
def get_readings(): #Intentionally not done in a for loop because this way we could see if there is an error with data sending we know which sensor is the problem
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

    average_temp = (temperature1 + temperature2 + temperature3 + temperature4) / 4
    average_humidity = (humidity1 + humidity2 + humidity3 + humidity4) / 4
    median_temp = statistics.median([temperature1, temperature2, temperature3, temperature4])
    median_humidity = statistics.median([humidity1, humidity2, humidity3, humidity4])
    reading =(f"{temperature1},{humidity1},{temperature2},{humidity2},{temperature3},{humidity3},{temperature4},{humidity4},{datetime.isoformat(datetime.now())},{median_temp},{median_humidity}")
    return (reading)

reading=get_readings()
with open("/home/dev/readings.csv","a") as f:
    f.write(f"{reading} \n")
print(f"It worked {datetime.now()} \n")
```
#### Figure 5.1 shows the recorded data stored in the .csv file. The data was measured everyb5 minutes for 48 hours for a totl of 576 data units.
![We used a .csv file to store 48hours worth of data measured every 5 min. Each row has a time when data was recorded, tempratures and humidity from all 4 sensors, median temperature and humidity](https://github.com/AleksandarDzudzevic/Project_unit_2/blob/main/crietria-c-proof5.1.png)


### 6. The client wanted a prediction the subsequent 12 hours for both temperature and humidity.
> We made a prediction  for the temperature and humidity for the next 12 hours which is shown in the graphs bellow (pictures 6.1 & 6.2), using the data from 24th to 36th hour of recording is most aplicable for the prediction, with a 4.5% margin error which was calculated by comparing the predicted temperature outside from these time periods and a +1.5% or 1.5% humidity range for the margin error for humidity prediction whcih was calculated based on how much data varied throughout recordings. We used plt.fillinbetween and plt.errorbar becuase it was the best way to represnt the margin error and allow the client to visually understand what range of temperature to expect for the following 12 hours. With this criteria 6 was fulfilled.

We developed a program that fulfilled client's criteria by calculating the coefficents of quadratic equations for the graph using np.polyfit, and then an algorithm which stored the data which was then plotted. The margin error was calculating by dividing the difference in data at that time period during the two days.
#### Code 6.1
```.py
plt.subplot(2,1,1)
x3,mean_temp_out=smoothing(temperature_readings_out)
y_quad=[]
y_quad4=[]
p0,p1,p2 = np.polyfit(x3,mean_temp_out,2)#2 means power of 2
q0,q1,q2 = np.polyfit(x3,mean_per_hour_temp,2)#2 means power of 2

for i in x3:
    y_quad.append(p0*(i**2)+p1*i+p2)
    y_quad4.append(q0*(i**2)+q1*i+q2)

plt.plot(x3,y_quad,color="blue")
plt.title(f"Comparison:mean outside temp(BLUE) vs mean inside temp(RED)13:05 8.12.2022 - 13:05 10.12.2022")
plt.xlabel("Hours")
plt.ylabel("Temp (Celsius)")
plt.plot(x3,y_quad4,color='red')

```
#### Code 6.2
```.py
plt.subplot(2,1,2)
x4,mean_hum_out=smoothing(humidity_readings_out)
y_quad2=[]
y_quad3=[]
p0,p1,p2 = np.polyfit(x3,mean_hum_out,2)#2 means power of 2
q0,q1,q2 = np.polyfit(x3,mean_per_hour_hum,2)#2 means power of 2

for i in x4:
    y_quad2.append(p0*(i**2)+p1*i+p2)
    y_quad3.append(q0*(i**2)+q1*i+q2)

plt.plot(x4,y_quad2,color="blue")
plt.plot(x4,y_quad3,color='red')
plt.title(f"Comparison:mean outside humidity(BLUE) vs mean inside humidity(RED)13:05 8.12.2022 - 13:05 10.12.2022")
plt.xlabel("Hours")
plt.ylabel("Humidity (%)")
```

#### Figure 6.1 shows the prediction of the temperature in the room for the subsequent 12 hours after the measuring took place.
![](https://github.com/AleksandarDzudzevic/Project_unit_2/blob/main/temperature_prediction_for_next_12h.png)
#### Figure 6.2 shows the prediction of the humidity in the room for the subsequent 12 hours after the measuring took place with the apropriate margin error.
![](https://github.com/AleksandarDzudzevic/Project_unit_2/blob/main/humidity_prediciton_fot_next12h.png)
*Will use the same part of the day from the second 24h period because it is more relatable and use the diff in the early afternoon readings as a prediction for the error bar

### 7. A poster summarizing the visual representations, model and analysis is created and communicated. 

*Will be uploaded here as proof

# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration

# Citations
1. Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
2. Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
3. “How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
4. Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  
5. Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
6. Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
7. Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 
8. BCR, Chris @. “Setting up a Cron Job on the Raspberry Pi.” BC Robotics, 5 Feb. 2022, https://bc-robotics.com/tutorials/setting-cron-job-raspberry-pi/. 
