from machine import UART
import machine
import os
import WIFIconnect as conn

uart = UART(0, baudrate=115200)
os.dupterm(uart)

conn.connect_to_WIFI()
machine.main('main.py')
