import cv2
import buildface,findface,sound
import os,glob
import numpy as np
from time import sleep
import time,threading

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_alt2.xml")

def openvideo():
    k=0
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame= cap.read()
        
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,3)
        cv2.imshow('live', frame)
        if(len(faces)>0 and k<=0):
            cv2.imwrite("media/tem.jpg",frame)
            compare=findface.fface()
            if compare==1:
                print("something wrong")
            elif compare==0:
                print("not needcode")
            else:
                threading.Thread(target=model_1()).start() 
                k+=1 
            
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def model_1():    
    print(205)  
    
    sound.sound()

threading.Thread(target=openvideo()).start()     

    