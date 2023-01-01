import cv2
import time
import buildface

def ffaece():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_alt2.xml")
    cap = cv2.VideoCapture(0)
    model = cv2.face.LBPHFaceRecognizer_create()
    try:
        model.read('faces_LBPH.yml')
        f = open('member.txt',"r")
        
        names= f.readline().split((','))
    except:
        buildface.bface()
    timenow = time.time()
    
def fface():
    check=-1
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_alt2.xml")
    img = cv2.imread("media/tem.jpg")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,3)
    model = cv2.face.LBPHFaceRecognizer_create()
    try:
        model.read('faces_LBPH.yml')
    except:
        return 1
        buildface.bface()
        

    for(x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        face_img = cv2.resize(gray[y:y + h,x: x+w],(400,400))
        
        try:
            val = model.predict(face_img)
            if val[1]<70:
                return 2
            else:
                return 0
        except:
            return 1