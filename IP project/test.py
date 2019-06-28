import numpy as np
import cv2

img = cv2.imread('image 1.jpg')
(width,height)=img.shape[:2]
img=cv2.resize(img,(int(height/10),int(width/10)))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.1, 10)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)
    
cv2.imshow('Corner',img)
print(corners)

