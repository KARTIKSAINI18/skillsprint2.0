import cv2
import numpy as np

#img = cv2.imread("modi.jpg")
#cv2.imshow("image",img)


#print(img)
#print(type(img))
#print(img.shape)
#cap=cv2.VideoCapture(0)
#while True:
    #ret,frame=cap.read()

    #cv2.imshow("webcam",frame)
    #if cv2.waitKey(1)==ord("q"):
        #break

#cap.release()
#cv2.destroyAllWindows()
#img=cv2.imread("modi.jpg")
#img2=cv2.resize(img,(540,480))
#print(img.shape)
#print(img2.shape)
#img3=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
#cv2.imshow("image",img)
#imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("image grayscale",imggray)
#imgbur=cv2.GaussianBlur(imggray,(9,9),0)
#imgcanny=cv2.Canny(imggray,100,100)
#cv2.imshow("image gray",imggray)
#img=np.zeros((512,512,3),np.uint8)
#cv2.line(img,(0,0),(512,512),(255,90,40),2)
#cv2.rectangle(img,(100,100),(300,300),(0,255,0),cv2.FILLED)
#cv2.rectangle(img,(100,100),(300,300),(0,255,0),2)

#cv2.circle(img,(206,206),50,(203, 192, 255),0)
#cv2.putText(img,"ONE",(200,300),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
#cv2.putText(img,"ONE",(200,300),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)


#import datetime as dt

#cap=cv2.VideoCapture(0)

#while True:
    #ret, frame = cap.read()
    #date_time=str(dt.datetime.now())
    #frame=cv2.putText(frame,date_time,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
    #cv2.imshow("Video",frame)
    #if cv2.waitKey(1)==ord("q"):
        #break

#cap.release()
# Read two images
image1 = cv2.imread('modi.jpg')
image2 = cv2.imread('meloni.jpg')

# Ensure that both images have the same height
rows, cols, channels = image1.shape
image2 = cv2.resize(image2, (int(image2.shape[1] * rows / image2.shape[0]), rows))

# Resize the first image to match the width of the second image
image1 = cv2.resize(image1, (image2.shape[1], rows))

# Merge images
merged_image = np.concatenate((image1, image2), axis=1)

# Display the merged image
cv2.imshow('Merged Image', merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.destroyAllWindows()

#cv2.imshow("Image",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.waitKey(0)

