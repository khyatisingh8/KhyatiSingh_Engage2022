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
import childDetail
from childDetail import child
import os
import Face_Recognition
from Face_Recognition import Face_RecogitionClass
import train 
from train import train_img
import link
from link import useful_links

class Face_Recogition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1230x700+0+0")
        self.root.title("Face Recognition Software")

        
        #bg img
        img3=Image.open(r"Image\1.png")
        img3=img3.resize((1230,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1230,height=700)  


        main_frame=Frame(bg_img,bd=0,bg="white")
        main_frame.place(x=0,y=0,width=1230, height=35)
    
        main_frame=Frame(bg_img,bd=0,bg="white")
        main_frame.place(x=0,y=0,width=1230, height=35)

        

        home_btn=Button(main_frame,text="Home",width=20,font=("times new roman",13,"bold"),bg="White",fg="black")
        home_btn.grid(row=0,column=0)

        Register_btn=Button(main_frame,text="Register",command=self.child_detail,width=20,font=("times new roman",13,"bold"),bg="White",fg="black")
        Register_btn.grid(row=0,column=1)

        Face_Recognition_btn=Button(main_frame,text="Face Recognition",command=self.face_data,width=20,font=("times new roman",13,"bold"),bg="white",fg="black")
        Face_Recognition_btn.grid(row=0,column=2)

        photos_btn=Button(main_frame,text="Photos",command=self.open_img,width=20,font=("times new roman",13,"bold"),bg="white",fg="black")
        photos_btn.grid(row=0,column=3)

        contact_btn=Button(main_frame,text="Train Data",command=self.train_data,width=20,font=("times new roman",13,"bold"),bg="white",fg="black")
        contact_btn.grid(row=0,column=4)

        train_btn=Button(main_frame,text="Exit",command=self.iexit,width=18,font=("times new roman",13,"bold"),bg="white",fg="black")
        train_btn.grid(row=0,column=5)



        b1_btn=Button(self.root,text="Useful Links",command=self.links,width=27,font=("times new roman",10,"bold"),bg="purple",fg="white")
        b1_btn.place(x=160,y=440,width=150,height=40)


    def child_detail(self):
            self.new_window=Toplevel(self.root)
            self.app=child(self.new_window)


    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_RecogitionClass(self.new_window)

    def open_img(self):
        os.startfile("IMAGE_Record")

    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=train_img(self.new_window)

    def links(self):
            self.new_window=Toplevel(self.root)
            self.app=useful_links(self.new_window)



    def iexit(self):
            self.iexit=messagebox.askyesno("Face Regonition","Are you sure exit the system")
            if self.iexit>0:
               self.root.destroy()

            else:
                return

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recogition_System(root)
    root.mainloop()