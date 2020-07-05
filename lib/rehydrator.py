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
    #Function measuring the initial distance from sensor to water surface and returning the initial water quantity of the tank
    distance = get_distance()
    initial_volume = get_volume(distance)
    print("ReHydrator calibrated")
    return initial_volume

def get_distance():
    #Returns distance between sensor and water surface
    distance = dist.distance_median()
    print('Distance:', abs(distance), 'cm')
    return abs(distance)

def get_volume(distance):
    #Returns current water volume
    height = 29.3 - abs(distance) #must be adjusted if different tank is used
    print('Height: ', height, 'cm')
    current_volume = round((3.14 * height * 8.4**2), 2)
    print('Current volume: ', current_volume, 'ml')
    return current_volume

def get_tank_status(current_volume):
    #Returns percentage of total volume, if the percentage (due to minor measurement errors) is greater than 100, 100 is returned
    current_percentage = current_volume / 4433.42 * 100 #must be adjusted if different tank is used
    print('Current percentage: ', round(current_percentage, 1), '%')
    if current_percentage >= 100:
            return 100
    else:
        return round(current_percentage, 1)

def get_temp_rh():
    #Gets values from the DHT-11 sensor and returns the result
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
    #Returns the current water quantity
    difference = initial_volume - current_volume
    print('Difference: ', difference, 'ml')
    if difference <= 0:
        return 0
    else:
        return difference

def get_RDA_percentage(quantities_sum):
    #Returns the percentage of the recommended daily amount of water (here: 2.5 liters, this might have to be adjusted to individual values) that has been consumed
    RDA_percentage = quantities_sum / 2500 * 100
    print('RDA percentage: ', RDA_percentage, '%')
    if RDA_percentage >= 100:
        return 100
    else:
        return RDA_percentage
