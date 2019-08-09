import cv2

img=cv2.imread('image 1.jpg')
(width,height)=img.shape[:2]
img=cv2.resize(img,(int(height/10),int(width/10)))
blur=cv2.blur(img,(11,11))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thr=cv2.threshold(gray,210,255,cv2.THRESH_BINARY)
contours,hierachy=cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

	cv2.drawContours(img,[cnt],0,(0,255,0),2)

cv2.imshow('IMG',img)
cv2.imshow('THR',thr)
