import cv2,time
from cv2 import GaussianBlur
video=cv2.VideoCapture(0,cv2.CAP_DSHOW)
a=0
first_frame=None
while True:
    a+=1
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)
    ret,thresh_delta=cv2.threshold(delta_frame,60,255,cv2.THRESH_BINARY)
    thresh_delta=cv2.dilate(thresh_delta,None,iterations=0)
    (cnts,_)=cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            continue
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),7)
    cv2.imshow("Gray scale",gray)
    cv2.imshow("delta",delta_frame)
    cv2.imshow("thresh",thresh_delta)
    cv2.imshow("Motion Detection",frame)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()