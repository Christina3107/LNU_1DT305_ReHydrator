print("Hello main")
## get_volume
## get_temperature
## get_humidity
## if temp > ...
##
# my first project ..
import time
from machine import Pin
import _thread
from dht import DHT


th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
time.sleep(10)


def send_env_data():
    while True:
        result = th.read()
        while not result.is_valid():
            time.sleep(5)
            result = th.read()
        print('Temp:', result.temperature)
        print('RH:', result.humidity)


        time.sleep(10)


send_env_data()
