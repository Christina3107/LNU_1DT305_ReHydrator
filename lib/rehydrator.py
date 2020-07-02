#Tankinfo
#diameter = 16,8cm
#radius = 8,4cm
#max waterlevel (= height) = 20cm
#max volume = 4433,42cm3
#sensorheight (from tank bottom)= 29,3cm
import time
from machine import Pin
from dht import DHT
import HCSR04 as dist

dist_array = []

def calibrate():
    #measure initial distance, get total volume, set initial distance --> first array value? get initial volume
    distance = dist.distance_median()
    dist_array.append(distance)
    print(dist_array)
    print('Distance:', abs(distance), 'cm')
    return distance

def get_volume(distance):
    height = 29.3 - abs(distance)
    print(height)
    current_volume = round((3.14 * height * 8.4**2), 2)
    return current_volume

def get_tank_status(current_volume):
    #return percentage of total volume
    current_percentage = current_volume / 4433.42 * 100
    print(round(current_percentage, 1))
    if current_percentage >= 100:
            return 100
    else:
        return round(current_percentage, 1)

def get_temperature():
    pass

def get_humidity():
    pass

def get_distance():
    #returns distance from sensor to water surface
    pass

def get_water_amount(initial_volume, current_volume):
    #returns amount of water that has been consumed since last measurement
    #if distance2 < distance1 --> return 0, sätt utgångsvärde till distance 2
    pass

distance = calibrate()
get_tank_status(distance)
