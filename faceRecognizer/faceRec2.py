import face_recognition
import cv2
image = face_recognition.load_image_file('/home/nvidia-nano/Desktop/pyCD/faceRecognizer/demoImages/unknown/u13.jpg')
face_locations = face_recognition.face_locations(image)
print(face_locations)
image =cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
for (row1,col1,row2,col2) in face_locations:
    cv2.rectangle(image,(col1,row1),(col2,row2),(0,255,0),2)
cv2.imshow('window',image)
if(cv2.waitKey(0)==ord('q')):
    cv2.destroyAllWindows()