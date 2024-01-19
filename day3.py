import cv2
import numpy as np
framewidth=640
frameheight=480
cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
def empty(x):
    pass

cv2.namedWindow("parameters")
cv2.createTrackbar("threshold","parameters",100,255,empty)
cv2.createTrackbar("threshold2","parameters",200,255,empty)

def get_contours(img_dilate,img_contours):
    contours,hierarchy=cv2.findcontours(img_dilate,cv2.RET_EXTERNAL,cv2.RETR_EXTERNAL,cv2)


    cv2.drawContours(img_contours,ont,-1,(0,255,0),3)
    peri=cv2.approxPolyDp(cnt,)



while (True) :
    ret,img=cap.read()
    img_contours=img.copy()
    img_blur=cv2.GaussianBlur(img,(7,7),4)
    img_grey = cv2.cvtColor(img_blur, cv2.COLOR_BRG2GRAY)
    t1=cv2.getTrackbarpos("threshold","parameters")
    t2=cv2.getTrackbar("threshold2","parameters")
    img_canny = cv2.Canny(img_canny, 100, 200)
    kernel = np.ones(5, 5, np.uint8)

    img_dilate = cv2.dilate(img_canny, kernel, iterateions=1)
    get_contours(img_dilate,img_contours=img_contours)

    output = nphstack([img_grey, img_canny, img_dilate])
    if cv2.waitKey(1)==ord("q"):
        break

cap.release()
cv2.closeAllwindows()
