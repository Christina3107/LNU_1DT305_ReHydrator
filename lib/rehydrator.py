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

def calibrate():
    #measure initial distance, get total volume, set initial distance --> first array value? get initial volume
    distance = get_distance()
    initial_volume = get_volume(distance)
    print("ReHydrator calibrated")
    return initial_volume

def get_distance():
    #returns distance between sensor and water surface
    distance = dist.distance_median()
    print('Distance:', abs(distance), 'cm')
    return abs(distance)

def get_volume(distance):
    height = 29.3 - abs(distance)
    print('Height: ', height, 'cm')
    current_volume = round((3.14 * height * 8.4**2), 2)
    print('Current volume: ', current_volume, 'ml')
    return current_volume

def get_tank_status(current_volume):
    #return percentage of total volume
    current_percentage = current_volume / 4433.42 * 100
    print('Current percentage: ', round(current_percentage, 1), '%')
    if current_percentage >= 100:
            return 100
    else:
        return round(current_percentage, 1)

def get_temp_rh():
    th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
    time.sleep(2)
    result = th.read()
    while not result.is_valid():
        time.sleep(5)
        result = th.read()
    print('Temperature: ', result.temperature, '°C')
    print('RH: ', result.humidity, '%')
    return result

def get_water_quantity(initial_volume, current_volume):
    difference = initial_volume - current_volume
    print('Difference: ', difference, 'ml')
    if difference <= 0:
        return 0
    else:
        return difference

def get_RDA_percentage(quantities_sum):
    RDA_percentage = quantities_sum / 2500 * 100
    print('RDA percentage: ', RDA_percentage, '%')
    if RDA_percentage >= 100:
        return 100
    else:
        return RDA_percentage
