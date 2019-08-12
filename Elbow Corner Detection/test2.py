import numpy as np
import cv2
p=1000
a=0
t=0
img = cv2.imread('image 3.jpg')
(width,height)=img.shape[:2]
img=cv2.resize(img,(int(height/10),int(width/10)))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thr=cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
gray2 = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray2, 10, 0.1, 10)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)
    #cv2.circle(gray,(x,y),10,255,-1)
    #cv2.circle(thr,(x,y),7,0,-1)
    if(x > 140 and x < 300):
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        print(x,y)

    if(x > 140 and x < 300):
        if(p > x):
            p=x
            q=y
    
    if(x > 140 and x < 300):
        if(t < y):
            s = x
            t = y

    if(x > 140 and x < 300):
        if(a < x):
            a=x
            b=y   
    
    
print(p,q) #wam patte tiynwa point eka
print(s,t) #kapena point eka
print(a,b) #dakuna tiynwa point eka

#cv2.circle(img,(137,156),3,(0,0,255),-1)
#cv2.circle(img,(247,143),3,(0,0,255),-1)
#cv2.circle(img,(167,174),3,(0,0,255),-1)
cv2.imshow('normalCorner',img)
#cv2.imshow('grayCorner',gray)
#cv2.imshow('THR',thr)
print(corners)



