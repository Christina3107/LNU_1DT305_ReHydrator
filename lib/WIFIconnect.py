#Module for estabishing a WiFi connection
from network import WLAN
import time
import pycom
import keys
import machine

def connect_to_WIFI():
    print("Establishing Wifi connection")
    pycom.heartbeat(False)
    pycom.rgbled(0xFF0000)
    wlan = WLAN(mode=WLAN.STA)
    wlan.antenna(WLAN.INT_ANT)

    wlan.connect(keys.SSID, auth=(WLAN.WPA2, keys.WIFIkey), timeout=5000)

    while not wlan.isconnected ():
        machine.idle()
    pycom.rgbled(0x00FF00)
    print("Connected to Wifi\n")
    time.sleep(3)
    pycom.heartbeat(True)
