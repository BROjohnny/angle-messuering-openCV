import tkinter as tk
from PIL import Image,ImageTk
import cv2
from tkinter import *

win=tk.Tk()
win.title('elbowMaster')

width=800
height=500
font1='TimesNewRoman 15 bold'

	
def clear():
	global img1,img_draw
	canvas1.delete('all')
	img1=PIL.Image.new('RGB',(width,height),(0,0,0))
	img_draw=ImageDraw.Draw(img1)
	
	pass
	
def predict():
	
	img_array=np.array(img1)
	
	img_array=cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)
	
	img_array=cv2.resize(img_array,(8,8))
	img_array_flat=img_array.ravel() #2D array into 1D array
	
	img_array_flat=(img_array_flat/255.0)*15.0
	
	result=clsfr.predict([img_array_flat])
	label_predict.config(text='Predicted Digit: '+str(result))
	
	pass

##my_image = PhotoImage(file='image 3.jpg')
##canvas.create_image(0,0,anchor=NW,image=my_image)


canv = Canvas(win, width=600, height=600, bg='blue')
canv.pack()

imge = PhotoImage(file="janidu jayasanka.jpg")
(width,height)=imge.shape[:2]
img=cv2.resize(imge,(int(height/10),int(width/10)))

canv.create_image(0,0, image=img, anchor=NW)

button_predict=tk.Button(win,text='Predict',bg='green',fg='white',font=font1,command=predict)
button_predict.grid(row=1,column=1,padx=3)

button_clear=tk.Button(win,text='Clear',bg='green',fg='white',font=font1,command=clear)
button_clear.grid(row=1,column=2,padx=3)

button_exit=tk.Button(win,text='Exit',bg='green',fg='white',font=font1,command=win.destroy)
button_exit.grid(row=1,column=3,padx=3)
