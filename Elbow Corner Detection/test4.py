import numpy as np
import cv2
import math

p=1000
a=0
t=0
img = cv2.imread('image 1.jpg')
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
    
def line1m(p,q,s,t,a,b):
    m1=(q - t)/(p - s)
    m2=(b - t)/(a - s)
    print(m1,m2)
    o = (m1 -m2)/(1 + (m1*m2))
    print (o)
    print(math.tan(o))
    M = m1*m2
    return M
    return o

def checkconer(o,M):
    if(M == (-1)):
        print ("perfect shot. \n")
    elif(o < math.tan(math.pi/2)):
        print ("Try Again! \nYour elbow angel is greater than 90 degrees.")
    elif(o > math.tan(math.pi/2)):
        print ("Try Again! \nYour elbow angel is less than 90 degrees.")
print(p,q) #wam patte tiynwa point eka
print(s,t) #kapena point eka
print(a,b) #dakuna tiynwa point eka
cv2.line(img,(p,q),(s,t),(50,249,222),2)
cv2.line(img,(a,b),(s,t),(50,249,222),2)
o = line1m(p,q,s,t,a,b)
M = line1m(p,q,s,t,a,b)
checkconer(o,M)


#90 degree
cv2.circle(img,(137,177),3,(0,0,2),-1) #meka wenas karanne
cv2.circle(img,(121,204),3,(0,255,0),-1)
cv2.circle(img,(137,204),3,(255,0,0),-1)



print (math.tan(math.pi))
cv2.imshow('normalCorner',img)
#cv2.imshow('grayCorner',gray)
#cv2.imshow('THR',thr)
print(corners)



