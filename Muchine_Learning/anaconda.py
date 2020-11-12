import os, re, glob
import cv2
import numpy as np
import shutil
from numpy import argmax
from keras.models import load_model
import paho.mqtt.client as mqtt
 
categories = ["sad","sleep","smile"]

#anaconda.py는 머신러닝을 구동하여 정확성을 구하는 단계 
def Dataization(img_path):
    image_w = 28
    image_h = 28
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
    return (img/256)
 
src = []
name = []
test = []
image_dir = "D:/project/object-detection-deep-learning/"
for file in os.listdir(image_dir):
    if (file.find('.jpg') is not -1):       
        src.append(image_dir + file)
        name.append(file)
        test.append(Dataization(image_dir + file))
 
 
test = np.array(test)
model = load_model('D:/project/object-detection-deep-learning/Gersang.h5')
predict = model.predict_classes(test)
 
for i in range(len(test)):
    print(name[i] + " : , Predict : "+ str(categories[predict[i]]))
    mqttc = mqtt.Client("python_pub")
    mqttc.connect("broker.hivemqt.com", 1883)
    mqttc.publish("emotion",str(categories[predict[i]]))
    mqttc.loop(2);
