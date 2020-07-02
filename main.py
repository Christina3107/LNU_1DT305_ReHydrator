print("Welcome to ReHydrator")
## get_volume
## get_temperature
## get_humidity
## if temp > ...
##
import time
from machine import Pin
from dht import DHT
import HCSR04 as dist
import send_data as ubidots


th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
time.sleep(10)

dist_array = []

def collect_sensor_data():
    while True:
        result = th.read()
        temp = result.temperature
        RH = result.humidity
        while not result.is_valid():
            time.sleep(5)
            result = th.read()
        print('Temp:', temp)
        print('RH:', RH)
        distance = dist.distance_median()
        dist_array.append(distance)
        print(dist_array)
        print('Distance:', abs(distance), 'cm')
        #ubidots.post_var("ReHydrator",  temp, RH, abs(distance))


        time.sleep(30)


collect_sensor_data()
