import requests

#imports readings from the server
def get_sensor(readings:list, id:int)->list:
    T=[]
    for r in readings:
        if r["sensor_id"]==id:
            T.append(r['value'])
    return T

def download(url:str="192.168.6.142/readings")->list:
    req = requests.get(f'http://{url}')
    data = req.json()
    readings = data["readings"][0]
    return readings

def smoothing(data:list,size_window:int=12)->list:
    x = []
    y = []
    for i in range(0,len(data)-12,size_window):
        segment_mean = sum(data[i:i+size_window])/size_window
        y.append(segment_mean)
        x.append(i//size_window)#hours 1,2,3,4,5...
    return x,y
