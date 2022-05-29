from distutils.util import execute
from logging import root
from optparse import Values
from re import L
from tkinter import*
from tkinter import ttk
from turtle import title, update
import PIL
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import main
from main import Face_Recogition_System

class useful_links:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1230x700+0+0")
        self.root.title("Face Recognition Software")


    #bg img
        img3=Image.open(r"Image\LINK.png")
        img3=img3.resize((1230,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1230,height=700) 

        Title_Link1_lbl=Label(self.root,text="Online Registration for Child Care Institution", font=("times new roman",33,"bold"),bg="dark blue",fg="white")
        Title_Link1_lbl.place(x=0,y=150,width=1230,height=50)

        
        Link1_lbl=Label(self.root,text="http://164.100.163.212/cciregistration/index.php", font=("times new roman",23,"bold"),bg="dark blue",fg="white")
        Link1_lbl.place(x=0,y=200,width=1230,height=50)

        #buttons

        home_btn=Button(self.root,text="Home",command=self.Home,width=27,font=("times new roman",20,"bold"),bg="blue",fg="white")
        home_btn.place(x=1050,y=20,width=150,height=40)


    def Home(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recogition_System(self.new_window)




if __name__ == "__main__":
    root=Tk()
    obj=useful_links(root)
    root.mainloop()