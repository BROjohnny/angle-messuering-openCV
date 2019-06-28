import cv2
import numpy as np

img = cv2.imread('image 3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
_, contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
k = 2

if len(contours)==1:
    for i in range (0,1000):
        kernel = np.ones((1,k),np.uint8)
        erosion = cv2.erode(threshold,kernel,iterations = 1)
        _, contours, hierarchy = cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        if len(contours) == 1:
            k+=1
        if len(contours) == 2:
            break
        if len(contours) > 2:
            print('more than one contour')

x,y,w,h = cv2.boundingRect(contours[0])
cv2.rectangle(threshold,(x-k,y-k),(x+w+k,y+h+k), 0, 1)
_, contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0,0,255), 2)

#Object1
v = np.matrix([[0], [1]])
rect = cv2.minAreaRect(contours[0])

#determine angle
if rect[1][0] > rect[1][1]:
    ang = (rect[2] + 90)* np.pi / 180
else:
    ang = rect[2]* np.pi / 180
rot = np.matrix([[np.cos(ang), -np.sin(ang)],[np.sin(ang), np.cos(ang)]])
rv = rot*v

#draw angle line
lineSize = max(rect[1])*0.45                #length of line
p1 = tuple(np.array(rect[0] - lineSize*rv.T)[0].astype(int))
p2 = tuple(np.array(rect[0] + lineSize*rv.T)[0].astype(int))
cv2.line(img, p1, p2, (255,0,0), 2)

#Object2
if len(contours) > 1:
    rect = cv2.minAreaRect(contours[1])

    #determine angle
    if rect[1][0] > rect[1][1]:
        ang = (rect[2] + 90)* np.pi / 180
    else:
        ang = rect[2]* np.pi / 180
    rot = np.matrix([[np.cos(ang), -np.sin(ang)],[np.sin(ang), np.cos(ang)]])
    rv = rot*v

    #draw angle line
    lineSize = max(rect[1])*0.45                #length of line
    p1 = tuple(np.array(rect[0] - lineSize*rv.T)[0].astype(int))
    p2 = tuple(np.array(rect[0] + lineSize*rv.T)[0].astype(int))
    cv2.line(img, p1, p2, (255,0,0), 2)


#save output img

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
