import cv2
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
img=cv2.imread('face_detect.png',1)
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
faces=face_cascade.detectMultiScale(img,scaleFactor=1.05,minNeighbors=10)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),-1)
resized=cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))
imshow("detected_face",resized)
waitKey(0)
destroyAllWindows()