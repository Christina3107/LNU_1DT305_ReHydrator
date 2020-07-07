import time
import pycom
import send_data as ubidots
import rehydrator

print("Welcome to ReHydrator")

water_volumes = []
water_quantities = []

def collect_sensor_data():
    #Loop running 12 times (once every "active hour") once the program is started

    for i in range(12):
        print("Collecting sensor data")
        print("Measurement" , i+1, "of 12.")
        pycom.heartbeat(False)
        pycom.rgbled(0x00FF00)
        #Assigning variables by calling rehydrator-functions
        th = rehydrator.get_temp_rh()
        temp = th.temperature
        RH = th.humidity
        distance = rehydrator.get_distance()
        current_volume = rehydrator.get_volume(distance)
        water_volumes.append(current_volume) #Tank volumes are collected in an array in order to be able to calculate the difference between measurements
        tank_status = rehydrator.get_tank_status(current_volume)
        #print(water_volumes, water_volumes[i])
        initial_volume = water_volumes[i] #initial volume = volume from the previous measurement
        water_quantity = rehydrator.get_water_quantity(initial_volume, current_volume)
        water_quantities.append(water_quantity)
        #print(water_quantities)
        quantities_sum = sum(water_quantities)
        #print(quantities_sum)
        RDA_percentage = rehydrator.get_RDA_percentage(quantities_sum)
        if water_quantity < 170:
            dehydration_warning = 0
        else:
            dehydration_warning = 1
        if temp > 25 or (temp >= 20 and RH >=70):
            temp_warning = 1
        else:
            temp_warning = 0
        #print(temp, RH, tank_status, round(RDA_percentage, 2), water_quantity, dehydration_warning, temp_warning)
        #Variables are sent to Ubidots via HTTP-post request
        ubidots.post_var("ReHydrator",  temp, RH, tank_status, RDA_percentage, water_quantity, dehydration_warning, temp_warning)
        pycom.heartbeat(True)
        #Time to next measurement (60 minutes)
        time.sleep(3600)


initial_volume = rehydrator.calibrate()
water_volumes.append(initial_volume)
time.sleep(60)
collect_sensor_data()
