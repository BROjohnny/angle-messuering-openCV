import numpy as np
import cv2

img = cv2.imread('image 1.jpg')
(width,height)=img.shape[:2]
img=cv2.resize(img,(int(height/10),int(width/10)))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray2 = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray2, 10, 0.1, 10)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)
    cv2.circle(gray,(x,y),10,255,-1)
    

cv2.circle(img,(149,177),3,(0,0,255),-1)
cv2.circle(img,(277,191),3,(0,0,255),-1)
cv2.circle(img,(253,212),3,(0,0,255),-1)
cv2.imshow('normalCorner',img)
cv2.imshow('grayCorner',gray)
print(corners)



