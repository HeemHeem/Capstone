#!/usr/bin/env python

import paho.mqtt.client as paho
from paho import mqtt
import json
import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Globals
piper_command = "./piper/piper --model ./voice_models/ryan/en_US-ryan-high.onnx --output_file "

# function to launch CallCare
def start_call():
    # Open Browser
    options = webdriver.ChromeOptions()
    service = Service('usr/bin/chromedriver')
    #options.set_preference("permissions.default.microphone", 1)
    #options.set_preference("permissions.default.camera", 1)

    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://capstone-video-calling.web.app/')
    # Allow access to camera
    cam_micro_btn = driver.find_element_by_id('cameraBtn')
    cam_micro_btn.click()
    # Create Room

    return

def on_subscribe(client, userdata, mid, granted_qos, properties= None):
	print("Subscribed: " + str(mid) + " " + str(granted_qos))
	
def on_message(client, userdata, msg):
    intent_parse(msg.payload)
	
def setup():
    client = paho.Client(paho.CallbackAPIVersion.VERSION1, "")
    mqttBroker = "broker.hivemq.com"
    #mqttBroker = "test.mosquitto.org"
    client.connect(mqttBroker)
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.loop_start()
    client.subscribe("Callcare/intent", qos=2)
    
def intent_parse(in_json):
    global piper_command
    json_dict = json.loads(in_json)
    intent = json_dict["intent"]["name"]
    if intent == "StartCall":
        contact = json_dict["slots"]["name"]
        if contact in ["Primary Contact", "Contact"]:
            if not os.path.isfile("./audio_files/confirm_call.wav"):
                shell_com = "echo 'calling " + contact + "' | " + piper_command + "./audio_files/confirm_call.wav"
                os.system(shell_com)
            os.system("aplay -D hw:2,0 ./audio_files/confirm_call.wav")
            start_call()
     

setup()
	
while True:
	pass
