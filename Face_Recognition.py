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
from cv2 import cvtColor
import mysql.connector
import cv2
import numpy as np

class Face_RecogitionClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1230x700+0+0")
        self.root.title("Face Recognition Software")


        title_lbl=Label(self.root,text="Face Recognition", font=("times new roman",33,"bold"),bg="dark blue",fg="white")
        title_lbl.place(x=0,y=10,width=1230,height=50)

        #bg img
        img3=Image.open(r"Image\recognition.jpg")
        img3=img3.resize((1230,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1230,height=700)  

        #button
        b1_btn=Button(self.root,text="Face Recognizing",width=27,font=("times new roman",20,"bold"),bg="dark blue",fg="white")
        b1_btn.place(x=330,y=580,width=550,height=60)



    #face recognition

    def face_rec(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)


            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(np.get_array_wrap[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="@Brunococo8",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select Child_Name from registration where Aadhar_Number="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select Gauradian_Name from registration where Aadhar_Number="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Mobile_Number from registration where Aadhar_Number="+str(id))
                m=my_cursor.fetchone()
                m="+".join(m)



                if confidence>77:

                    cv2.putText(img,f"Child_Name{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Gaurdian_Name{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Mobile_Number{m}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                else:
                    
                    cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face{m}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascase_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img)

            if cv2.waitKey(1)==13:
                break
            video_cap.realease()
            cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_RecogitionClass(root)
    root.mainloop()