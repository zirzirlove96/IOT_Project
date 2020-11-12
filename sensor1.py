import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
import os
import sys

channel=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

sensor_topic = "sensor"
broker_url = "test.mosquitto.org"


#사운드를 감지하여 안드로이드로 mqtt 메시징이 갈 수 있도록 한다. 
    
def mqtt_client_connect():
    client = mqtt.Client("client_name")
    print("connect to:", broker_url)
    client.connect(broker_url,1883)
    client.publish(sensor_topic, "sound!!!!")
    client.loop_start()
    


def callback(channel): 
    if GPIO.input(channel):
        print("Sound Detected")
        print("Connect Android")
        mqtt_client_connect()


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=5000)
GPIO.add_event_callback(channel, callback)



while True:
    time.sleep(1)
    #os.system("python sendfile.py")
    
    
    


