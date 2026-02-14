#Contour detection in webcam feed using OpenCV
import cv2 as cv
import numpy as np

# start  video capture
VideoCapture = cv.VideoCapture(0)
while True:
    #reading frame from webcam
    isTrue, frame=VideoCapture.read()
    #convert to grayscale
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #blur the image using GaussianBlur
    blur=cv.GaussianBlur(gray,(5,5),0)
    # detect edges using Canny
    canny=cv.Canny(blur,50,150)
    #find contours in the edged image
    contours, hierarchy=cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    cv.drawContours(frame,contours,-1,(0,255,0),2)
    cv.putText(frame,'Number of contours: '+str(len(contours)),(10,30),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
    cv.imshow('Contours',frame)
    if cv.waitkey(0) & 0xFF==ord('s'):
        cv.imwrite('Hello',frame)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
VideoCapture.release()
cv.destroyAllWindows()


