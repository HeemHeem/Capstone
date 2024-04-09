#!/usr/bin/env python

import sys
import time
import json
import random
import paho.mqtt.client as paho
from paho import mqtt
	
client = paho.Client("")
mqttBroker = "broker.hivemq.com"
#mqttBroker = "test.mosquitto.org"
client.connect(mqttBroker)

# get json from stdin and load into python dict
intents = sys.stdin.read()
client.publish("Callcare/intent", payload=intents)
time.sleep(0.1)

# convert dict to json and print to stdout
print(intents)
client.disconnect()
