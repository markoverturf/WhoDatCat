#!/home/pi/Desktop/aipython/bin/python3.10
# coding: utf-8

from imageai.Detection import ObjectDetection
import os
import cv2
from IPython.display import clear_output
import oracledb 
import datetime
import time

sql = "INSERT INTO CATTRACKING (COUNT) VALUES(1)"

current_directory = os.getcwd()

timestamp = 0

camera = cv2.VideoCapture(0)
#camera.resize(im, (960, 540))

camera.set(3, 640)
camera.set(4, 480)
#camera.set(cv2.CAP_PROP_FPS,5) 

detector = ObjectDetection()

detector.setModelTypeAsYOLOv3()

detector.setModelPath(r"/home/pi/Desktop/yolov3.pt")
detector.loadModel()

aiTimer = 0
detection = False

while True:
    if time.time() - aiTimer >= 5:
        ret, frame = camera.read()
        returned_image, detections = detector.detectObjectsFromImage(
        input_image = (frame),
        output_type = "array")
        for eachObject in detections:
            if eachObject["name"] == "cat":
                detection = True
                if time.time() - timestamp >= 30:
                    connection=oracledb.connect(*****)
                    with connection.cursor() as cursor:                    
                        cursor.execute(sql)
                        connection.commit()
                    connection.close()
                    timestamp = time.time()
                    detection = False
        aiTimer = time.time()
        cv2.imshow('Image Recognition', returned_image)
    else:
        ret, frame = camera.read()
        cv2.imshow('Image Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break