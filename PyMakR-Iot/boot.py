# boot.py -- run on boot-up

import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests

#Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = "string here" #Wi-Fi SSID
password = "string here" #Password for your WI-FI
wlan.connect(ssid, password) #Connects to Wi-Fi

#Gets current time from GMT+0
print("\n\n2. Querying the current GMT+0 time:")
r = urequests.get("http://date.jsontest.com") # Server that returns the current GMT+0 time.
print(r.json())




