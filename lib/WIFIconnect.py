#Module for estabishing a WiFi connection
from network import WLAN
import keys
import machine

def connect_to_WIFI():
    wlan = WLAN(mode=WLAN.STA)
    wlan.antenna(WLAN.INT_ANT)

    wlan.connect(keys.SSID, auth=(WLAN.WPA2, keys.WIFIkey), timeout=5000)

    while not wlan.isconnected ():
        machine.idle()
    print("Connected to Wifi\n")
    #add green led!!!
