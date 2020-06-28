print("Welcome to ReHydrator")
## get_volume
## get_temperature
## get_humidity
## if temp > ...
##
# my first project ..
import time
from machine import Pin
from dht import DHT
import HCSR04 as dist


th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
time.sleep(10)


def get_data():
    while True:
        result = th.read()
        while not result.is_valid():
            time.sleep(5)
            result = th.read()
        print('Temp:', result.temperature)
        print('RH:', result.humidity)
        distance = dist.distance_median()
        print('Distance:', abs(distance), 'cm')


        time.sleep(10)


get_data()
