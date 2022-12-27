import cv2
import buildface,findface,sound
import os,glob
import numpy as np
from time import sleep
import time,threading,finger
import time as t

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_alt2.xml")
compare=''

def openvideo():
    
    k=0
    text= ''
    if not cap.isOpened():
        
        print("Cannot open camera")
        exit()
    while True:
        ti1=t.localtime()
        sTime=str(ti1.tm_mon)+"/"+str(ti1.tm_mday)+" "+str(ti1.tm_hour)+":"+str(ti1.tm_min)+":"+str(ti1.tm_sec)
        ret, frame= cap.read()
        
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,3)
        cv2.imwrite("media/hand.jpg",frame)
        cv2.putText(frame,sTime,(100, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255), 1)
        cv2.imshow('live', frame)
        if(len(faces)>0 and k<1):
            cv2.imwrite("media/tem.jpg",frame)
            compare=findface.fface()
            print(compare)
            if compare==1:
                print("something wrong")

            elif compare==0:
                print("not pass")
            elif compare==2:
                threading.Thread(target=model_1).start() 
                (hint)
                
                k+=1 
                print(k)
            else: 
                k=0

        finger.hand_check(text)
        
        print(text)

        if(k>1):
            if(text==1):
                news
            elif(text==2):
                youtube
            elif(text==3):
                mp3
            
             
        if cv2.waitKey(1) == ord('q'):
            break
            cap.release()
            cv2.destroyAllWindows()

def model_1():    
    threading.Thread(target= sound.sound).start() 
  
        
threading.Thread(target=openvideo).start() 
    


   


   

    