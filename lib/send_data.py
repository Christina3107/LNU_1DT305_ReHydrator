from network import WLAN
import urequests as requests
import machine
import time
import keys

# Builds the json to send the request
def build_json(variable1, value1, variable2, value2, variable3, value3, variable4, value4, variable5, value5, variable6, value6, variable7, value7):
    try:
        data = {variable1: {"value": value1},
                variable2: {"value": value2},
                variable3: {"value": value3},
                variable4: {"value": value4},
                variable5: {"value": value5},
                variable6: {"value": value6},
                variable7: {"value": value7}}
        return data
    except:
        return None

# Sends the request. REST API reference https://ubidots.com/docs/api/
def post_var(device, value1, value2, value3, value4, value5, value6, value7):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": keys.TOKEN, "Content-Type": "application/json"}
        data = build_json("temperature", value1, "humidity", value2, "tank_status", value3, "RDA_percentage", value4, "water_quantity", value5, "dehydration_warning", value6, "temp_warning", value7)
        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            print("An error occurred trying to transmit data to Ubidots")
    except:
        print("An error occurred trying to transmit data to Ubidots")
