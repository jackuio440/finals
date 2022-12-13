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
    while(cap.isOpened()):
        count=3 - int(time.time() - timenow)
        ret, img = cap.read()
        if ret == True:
            imgcopy = img.copy()
            cv2.putText(imgcopy,str(count),(200,400),cv2.FONT_HERSHEY_SIMPLEX,15, (0,0,255),35)
            k= cv2.waitKey(100)
            if(k == ord('z') or k== ord("Z") or count == 0):
                cv2.imwrite("media/tem.jpg",img)
                break
def fface():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_alt2.xml")
    img = cv2.imread("media/tem.jpg")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,3)
    model = cv2.face.LBPHFaceRecognizer_create()
    try:
        model.read('faces_LBPH.yml')
        f = open('member.txt',"r")
        
        names= f.readline().split((','))
    except:
        buildface.bface()

    for(x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        face_img = cv2.resize(gray[y:y + h,x: x+w],(400,400))
        
        try:
            val = model.predict(face_img)
            if val[1]<50:
                print('welcom '+ names[val[0]]+' login!',val[1])
                return 2
            else:
                    return 0
        except:
            return 1