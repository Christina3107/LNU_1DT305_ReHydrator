import time
from machine import Pin
from dht import DHT
import HCSR04 as dist
import send_data as ubidots
import rehydrator


#th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
#time.sleep(2)
print("Welcome to ReHydrator")

water_volumes = []
water_quantities = []

def collect_sensor_data():
    for i in range(12):
        th = rehydrator.get_temp_rh()
        temp = th.temperature
        RH = th.humidity
        distance = rehydrator.get_distance()
        current_volume = rehydrator.get_current_volume(distance)
        water_volumes.append(current_volume)
        tank_status = rehydrator.get_tank_status(current_volume)
        #if i = 0:
        #    initial_volume = current_volume
        #else:
        print(water_volumes, water_volumes[i-1])
        initial_volume = water_volumes[i-1]
        water_quantity = rehydrator.get_water_quantity(initial_volume, current_volume)
        water_quantities.append(water_quantity)
        print(water_quantities)
        quantities_sum = sum(water_quantities)
        print(quantities_sum)
        RDA_percentage = rehydrator.get_RDA_percentage(quantities_sum)
        if water_quantity < 170:
            dehydration_warning = True
        else:
            dehydration_warning = False
        if temp >= 25:
            temp_warning = True
        else:
            temp_warning = False
        print(temp, RH, tank_status, RDA_percentage, water_quantity, dehydration_warning, temp_warning)
        #ubidots.post_var("ReHydrator",  temp, RH, tank_status, RDA_percentage, water_quantity, dehydration_warning, temp_warning)
        time.sleep(60)



#def collect_sensor_data():
#    while True:
#        result = th.read()
#        temp = result.temperature
#        RH = result.humidity
#        while not result.is_valid():
#            time.sleep(5)
#            result = th.read()
#        print('Temp:', temp)
#        print('RH:', RH)
#        distance = dist.distance_median()
#        dist_array.append(distance)
#        print(dist_array)
#        print('Distance:', abs(distance), 'cm')
        #ubidots.post_var("ReHydrator",  temp, RH, abs(distance))


        #time.sleep(30)

rehydrator.calibrate()
collect_sensor_data()
