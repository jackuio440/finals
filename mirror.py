import cv2
import buildface,findface,sound
import os,glob
import numpy as np
from time import sleep
import time,threading,finger
import time as t
import newsFind
from gtts import gTTS
import mp3,youtube
import pyttsx3


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_alt2.xml")
compare=''
text=''
def openvideo():
    
    k=0
    
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ti1=t.localtime()
        sTime=str(ti1.tm_mon)+"/"+str(ti1.tm_mday)+" "+str(ti1.tm_hour)+":"+str(ti1.tm_min)+":"+str(ti1.tm_sec)+" week"+str(ti1.tm_wday+1)
        ret, frame= cap.read()
        
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,3)
        
        cv2.putText(frame,sTime,(100, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255), 1)
        cv2.imshow('live', frame)
        try:
            cv2.imwrite("media/hand.jpg",frame)
        except:
            cv2.imwrite("media/hand.jpg","media/hand.jpg")
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
                threading.Thread(target=model_2).start() 
                print("hello")
                
                k+=1 
                print(k)
            else: 
                k=0  
        if cv2.waitKey(1) == ord('q'):
            break
            cap.release()
            cv2.destroyAllWindows()

def model_1():
    global snm
    snm='0'
    while True:
        snm=sound.sound()
        print(snm)
def model_2():
    global snm
    while True:
        text=finger.hand_check()
        snum=snm
        ti1=t.localtime()
        sTime=str(ti1.tm_mon)+"月"+str(ti1.tm_mday)+"日"+str(ti1.tm_hour)+"點"+str(ti1.tm_min)+"分"+str(ti1.tm_sec)+"秒 星期"+str(ti1.tm_wday+1)
        print(text)
        print(snum)
        with open('news.txt', 'r') as f:
            z = f.read()
        if(text=="1" or snum=='1'):
            if z !="1":
                f = open('num.txt','w')
                f.write("1")
                f.close()
                newsFind.newsFind()
                newsFind.newsRead()
        elif(text=="2" or snum=='2'):
            if z !="2":
                f = open('num.txt','w')
                f.write("2")
                f.close()
                newsFind.newsFind()
                newsFind.newsRead_en()
        elif(text=="3"or snum=='3'):
            if z !="3":
                f = open('num.txt','w')
                f.write("3")
                f.close()
                mp3.playmusic()
        elif(text=="4"or snum=='4'):
            if z !="4":
                f = open('num.txt','w')
                f.write("4")
                f.close()
                youtube.news()
            
        elif(text=="5" or snum=='5'):
            f = open('num.txt','w')
            f.write("5")
            f.close()
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 0.9)
            engine.say("嗨 現在時間是"+sTime+"今天過得好嗎")
            engine.runAndWait()

     
threading.Thread(target=openvideo).start() 
    


   


   

    