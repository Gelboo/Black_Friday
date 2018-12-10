from tkinter import *
import cv2
from PIL import Image, ImageTk
from threading import Thread
import time
import subprocess

def openn(threadname,delay):
    time.sleep(delay)
    subprocess.call("python Predict_GUI.py" , shell=True)

def destroy(threadname,delay):
    global root
    time.sleep(delay)
    root.destroy()
    t = threading.currentThread()
    t.exit()
def goPredict():
    t1 = Thread( target=openn,args=("Thread-1", 0, ) )
    t2 = Thread( target=destroy,args=("Thread-2", 0, ))
    t1.start()
    t2.start()
def close():
    global root
    root.destroy()


root = Tk()
root.bind('<Escape>', lambda e: root.quit())
root.attributes('-fullscreen', True)
root.configure(background='black')


title_img = cv2.imread('Black.jpg')
title_img = cv2.cvtColor(title_img,cv2.COLOR_BGR2RGB)
title_img = cv2.resize(title_img,(1000,800))
title_img = Image.fromarray(title_img)
title_img = ImageTk.PhotoImage(title_img)


title = Label(root,image=title_img,text='',borderwidth=0)

predict_btn = Button(root,text='Go To Prediction',bg='green',fg='black',width=20,height=5,font='Calibria 20',command=goPredict)
close_btn = Button(root,text='Close',bg='red',fg='black',width=20,height=5,font='Calibria 20',command=close)

title.place(x=400,y=0)
predict_btn.place(x=400,y=800)
close_btn.place(x=1000,y=800)

root.mainloop()
