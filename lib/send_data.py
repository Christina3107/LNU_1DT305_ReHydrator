from network import WLAN
import urequests as requests
import machine
import time
import keys

# Builds the json to send the request
def build_json(variable1, value1, variable2, value2, variable3, value3):
    try:
        data = {variable1: {"value": value1},
                variable2: {"value": value2},
                variable3: {"value": value3}}
        return data
    except:
        return None

# Sends the request. REST API reference https://ubidots.com/docs/api/
def post_var(device, value1, value2, value3):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": keys.TOKEN, "Content-Type": "application/json"}
        data = build_json("temperature", value1, "humidity", value2, "distance", value3)
        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            pass
    except:
        pass

#
#while True:
#    fuel = 123 # Data values
#    speed = 234 # Data values
#    post_var("ReHydrator", fuel, 1, speed)
#    time.sleep(DELAY)
