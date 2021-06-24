from threading import Thread
import cv2
import time
import numpy as np
import face_recognition
import pickle
dtav =0 # dtimeaverage
font =cv2.FONT_HERSHEY_SIMPLEX
with open('train.pkl','rb') as f: # trained faces
    Names = pickle.load(f)
    Encodings=pickle.load(f)
w = int(640)
h = int(480)
flip = 2

class vStream:
    def __init__(self,src,width,height):
        self.width = width
        self.height = height
        self.capture = cv2.VideoCapture(src)
        self.thread = Thread(target=self.update,args=())
        self.thread.daemon=True
        self.thread.start()
    def update(self):
        while True:
            ret, self.frame = self.capture.read()
            self.frame_resized = cv2.resize(self.frame,(self.width,self.height))
    def getFrame(self):
        return self.frame_resized

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(w)+', height='+str(h)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
       
cam1 = vStream(1,w,h) # webCam
cam2 = vStream(camSet,w,h) # piCam
scaleFactor = .3
while True:
    try:
        myFrame1 = cam1.getFrame() # webCamFrame
        myFrame2 = cam2.getFrame() # piCamFrame
        myFrame3 = np.hstack((myFrame1,myFrame2))
        # face_recogition = RGB | cv2 = BGR
        frameRGB=cv2.cvtColor(myFrame3,cv2.COLOR_BGR2RGB)
        frameRGBsmall = cv2.resize(frameRGB,(0,0),fx=scaleFactor,fy=scaleFactor)
        facePositions = face_recognition.face_locations(frameRGBsmall,model='cnn')
        allEncodings = face_recognition.face_encodings(frameRGBsmall,facePositions)
        for(top,right,bottom,left), face_encoding in zip(facePositions,allEncodings):
            name='Unknown'
            matches = face_recognition.compare_faces(Encodings,face_encoding)
            if(True) in matches:
                first_match_index=matches.index(True)
                name = Names[first_match_index]
                print(name)
            top=int(top/scaleFactor)
            left=int(left/scaleFactor)
            right=int(right/scaleFactor)
            bottom=int(bottom/scaleFactor)
            cv2.rectangle(myFrame3,(left,top),(right,bottom),(0,0,255),2)
            cv2.putText(myFrame3,name,(left,top-6),font,.60,(0,255,0),2)
        cv2.imshow('sync',myFrame3)
        
    except:
        print('frame not readed')
    if cv2.waitKey(1)==ord('q'):
        cam1.capture.release()
        cam2.capture.release()
        cv2.destroyAllWindows()
        exit(1)
        break
