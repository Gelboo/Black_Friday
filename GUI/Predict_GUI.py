from tkinter import *
import cv2
from PIL import Image, ImageTk
import threading


def close():
    global root
    root.destroy()

def predict():
    global user_id,Product_ID,Gender,Age,Occupation,City_Category,Stay_In_City,Marital_Status,Product_Category_1,Product_Category_2,Product_Category_3
    user_id_text = user_id.get("1.0",'end-1c')
    Product_ID_text = Product_ID.get("1.0",'end-1c')
    Gender_text = Gender.get("1.0",'end-1c')
    Age_text = Age.get("1.0",'end-1c')
    Occupation_text = Occupation.get("1.0",'end-1c')
    City_Category_text = City_Category.get("1.0",'end-1c')
    Stay_In_City_text = Stay_In_City.get("1.0",'end-1c')
    Marital_Status_text = Marital_Status.get("1.0",'end-1c')
    Product_Category_1_text = Product_Category_1.get("1.0",'end-1c')
    Product_Category_2_text = Product_Category_2.get("1.0",'end-1c')
    Product_Category_3_text = Product_Category_3.get("1.0",'end-1c')

    test = [user_id_text,Product_ID_text,Gender_text,Age_text,Occupation_text,City_Category_text,Stay_In_City_text,Marital_Status_text,Product_Category_1_text,Product_Category_2_text,Product_Category_2_text]
    print(test)

root = Tk()
root.bind('<Escape>', lambda e: root.quit())
root.attributes('-fullscreen', True)
root.configure(background='black')


title = Label(root,text='Enter Value To Predict Salary',bg='black',fg='red',font='Calibria 50')

user_id_title = Label(root,text='User_ID',bg='black',fg='blue',font='Calibria 30')
user_id = Text(root,height=1,width=40,font='Calibria 19')
Product_ID_title = Label(root,text='Product_ID',bg='black',fg='blue',font='Calibria 30')
Product_ID = Text(root,height=1,width=40,font='Calibria 19')
Gender_title = Label(root,text='Gender',bg='black',fg='blue',font='Calibria 30')
Gender = Text(root,height=1,width=40,font='Calibria 19')
Age_title = Label(root,text='Age',bg='black',fg='blue',font='Calibria 30')
Age = Text(root,height=1,width=40,font='Calibria 19')
Occupation_title = Label(root,text='Occupation',bg='black',fg='blue',font='Calibria 30')
Occupation = Text(root,height=1,width=40,font='Calibria 19')
City_Category_title = Label(root,text='City_Category',bg='black',fg='blue',font='Calibria 30')
City_Category = Text(root,height=1,width=40,font='Calibria 19')
Stay_In_City_title = Label(root,text='Stay_In_City',bg='black',fg='blue',font='Calibria 30')
Stay_In_City = Text(root,height=1,width=40,font='Calibria 19')
Marital_Status_title = Label(root,text='Marital_Status',bg='black',fg='blue',font='Calibria 30')
Marital_Status = Text(root,height=1,width=40,font='Calibria 19')
Product_Category_1_title = Label(root,text='Product_Category_1',bg='black',fg='blue',font='Calibria 30')
Product_Category_1 = Text(root,height=1,width=40,font='Calibria 19')
Product_Category_2_title = Label(root,text='Product_Category_2',bg='black',fg='blue',font='Calibria 30')
Product_Category_2 = Text(root,height=1,width=40,font='Calibria 19')
Product_Category_3_title = Label(root,text='Product_Category_3',bg='black',fg='blue',font='Calibria 30')
Product_Category_3 = Text(root,height=1,width=40,font='Calibria 19')

predict_btn = Button(root,text='Predict Purchase',font='Calibria 20',bg='red',fg='white',command=predict)

title.place(x=380,y=10)
y_period = 80
y_start = 100
user_id_title.place(x=300,y=y_start+(0*y_period))
user_id.place(x=720,y=y_start+(0*y_period))
Product_ID_title.place(x=300,y=y_start+(1*y_period))
Product_ID.place(x=720,y=y_start+(1*y_period))
Gender_title.place(x=300,y=y_start+(2*y_period))
Gender.place(x=720,y=y_start+(2*y_period))
Age_title.place(x=300,y=y_start+(3*y_period))
Age.place(x=720,y=y_start+(3*y_period))
Occupation_title.place(x=300,y=y_start+(4*y_period))
Occupation.place(x=720,y=y_start+(4*y_period))
City_Category_title.place(x=300,y=y_start+(5*y_period))
City_Category.place(x=720,y=y_start+(5*y_period))
Stay_In_City_title.place(x=300,y=y_start+(6*y_period))
Stay_In_City.place(x=720,y=y_start+(6*y_period))
Marital_Status_title.place(x=300,y=y_start+(7*y_period))
Marital_Status.place(x=720,y=y_start+(7*y_period))
Product_Category_1_title.place(x=300,y=y_start+(8*y_period))
Product_Category_1.place(x=720,y=y_start+(8*y_period))
Product_Category_2_title.place(x=300,y=y_start+(9*y_period))
Product_Category_2.place(x=720,y=y_start+(9*y_period))
Product_Category_3_title.place(x=300,y=y_start+(10*y_period))
Product_Category_3.place(x=720,y=y_start+(10*y_period))

predict_btn.place(x=1600,y=1000)

root.mainloop()
