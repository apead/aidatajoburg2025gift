import sys
import os
import mip
import urequests
from utime import sleep
from random import randint
from machine import Pin, I2C
import dht
from picozero import pico_led

import network

exterrnalled = Pin(15, Pin.OUT)   

ssid = '<SSID>'
password = '<WIFIPASSORD>'

def connectWifi():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        if rp2.bootsel_button() == 1:
            sys.exit()
        print('Waiting for connection...')
        pico_led.on()
        sleep(0.5)
        pico_led.off()
        sleep(0.5)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    pico_led.on()
    return ip

connectWifi()

# Use forked version of umqtt that supports cert which was removed.   This should not be necessary in future as functionality has returned.
mip.install("umqtt.simple", index="https://pjgpetecodes.github.io/micropython-lib/mip/add-back-ssl-params")

print("Downloading der file from repo")

filename = "cert.der"
url = "https://cptmsdug.dev/communitycontent/cert.der"

def file_exists(filename):
    try:
        os.stat(filename)
        return True
    except OSError:
        return False

if not file_exists(filename):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = urequests.get(url, headers=headers)
    print(f"HTTP GET request to {url} returned status code {response.status_code}")
    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)
        print("File downloaded successfully")
    else:
        print("Failed to download file")
        print(response.status_code)
        print("Response content:", response.content)
        time.sleep(5)
        machine.reset()
    response.close()
else:
    print("File already exists")

try:
    import iotc
except:
    import mip
    mip.install('github:Azure/iot-central-micropython-client/package.json')
    import iotc
    
from iotc import IoTCClient,IoTCConnectType,IoTCLogLevel,IoTCEvents


scope_id='<SCOPEID>'
device_id='<DEVICEID>'
key='<PRIMARYKEY>'


conn_type=IoTCConnectType.DEVICE_KEY

client=IoTCClient(scope_id,device_id,conn_type,key)
client.set_log_level(IoTCLogLevel.ALL)

def on_properties(name, value):
    print('Received property {} with value {}'.format(name, value))
    return value


def on_commands(command, ack):
    print('Command {}.'.format(command.name))
    ack(command, command.payload)

def on_enqueued(command):
    print('Enqueued Command {}.'.format(command.name))

exterrnalled.value(1)
client.on(IoTCEvents.PROPERTIES, on_properties)
client.on(IoTCEvents.COMMANDS, on_commands)
client.connect()
exterrnalled.value(0)
#client.send_property({'readOnlyProp':40})

while client.is_connected():
    exterrnalled.value(1) 
    client.listen()
    print('Sending telemetry')
    pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
    sensor = dht.DHT11(pin)
    sensor.measure()
    t  = (sensor.temperature())
    h = (sensor.humidity())
    print("Temperature: {}".format(t))
    print("Humidity: {}".format(h))
    client.send_telemetry({'Temperature':t,'Humidity':h})
    exterrnalled.value(0) 
    sleep(30)