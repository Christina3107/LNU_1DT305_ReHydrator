#Library for the HC-SR04 ultrasonic distance sensor
import utime
import time
import pycom
import machine
from machine import Pin

# initialise Ultrasonic Sensor pins
echo = Pin('P20', mode=Pin.IN)
trigger = Pin('P21', mode=Pin.OUT)
trigger(0)

# Ultrasonic distance measurment
def distance_measure():
    # trigger pulse LOW for 2us (just in case)
    trigger(0)
    utime.sleep_us(2)
    # trigger HIGH for a 10us pulse
    trigger(1)
    utime.sleep_us(10)
    trigger(0)

    # wait for the rising edge of the echo then start timer
    while echo() == 0:
        pass
    start = utime.ticks_us()

    # wait for end of echo pulse then stop timer
    while echo() == 1:
        pass
    finish = utime.ticks_us()

    # pause for 20ms to prevent overlapping echos
    utime.sleep_ms(20)

    # calculate distance by using time difference between start and stop
    # speed of sound 340m/s or .034cm/us. Time * .034cm/us = Distance sound travelled there and back
    # divide by two for distance to object detected.
    distance = ((utime.ticks_diff(start, finish)) * .034)/2

    return distance


# to reduce errors we take thirty readings and use the median
def distance_median():

    # initialise the list
    distance_samples = []
    # take 30 samples and append them into the list
    for count in range(30):
        distance_samples.append(distance_measure())
    # sort the list
    distance_samples = sorted(distance_samples)
    # take the center list row value (median average)
    distance_median = distance_samples[int(len(distance_samples)/2)]
    # apply the function to scale to volts

    return distance_median
