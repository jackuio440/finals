import cv2,os,glob
import numpy as np
from time import sleep
def bface():
    def saveImg(image,index):
        filename="images/"+name+"/face{:03d}.jpg".format(index)
        cv2.imwrite(filename,image)
        
    index=1
    total = 100

    name = input("輸入姓名(英文):")
    if os.path.isdir("images/"+name):
        print("此姓名已存在!")
    else:
        os.mkdir("images/"+name)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_alt2.xml")
        cap = cv2.VideoCapture(0)
        while index>0:
            ret,frame = cap.read()
            frame = cv2.flip(frame,1)
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,1.1,3)
            for(x,y,w,h) in faces:
                frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
                image = cv2.resize(gray[y:y + h,x: x+w],(400,400))
                saveImg(image,index)
                sleep(0.1)
                index+=1
                if index > total:
                    print("done!")

                    index = -1
                    break
                
                
            cv2.imshow('video',frame)
            cv2.waitKey(1)
        cv2.destroyWindow('video')
    images=[]
    labels=[]
    labelstr=[]
    count=0
    dirs = os.listdir('images')
    for d in dirs:
        if os.path.isdir('images/'+d):
            files = glob.glob("images/"+d+"/*.jpg")
            for filename in files:
                img = cv2.imread(filename,cv2.COLOR_BGR2GRAY)
                images.append(img)
                labels.append(count)
            labelstr.append(d)
            count += 1
            
    f = open('member.txt','w')
    f.write(','.join(labelstr))
    f.close()

    print("start create...")
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(np.asarray(images),np.asarray(labels))
    model.save('faces_LBPH.yml')
    print("create done!")