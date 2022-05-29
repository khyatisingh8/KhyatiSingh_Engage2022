from tkinter import*
from tkinter import ttk
import PIL
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class train_img:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1230x700+0+0")
        self.root.title("Face Recognition Software")


        title_lbl=Label(self.root,text="Train Data Set", font=("times new roman",33,"bold"),bg="dark blue",fg="white")
        title_lbl.place(x=0,y=10,width=1230,height=50)

        #bg img
        img3=Image.open(r"Image\train.jpg")
        img3=img3.resize((1230,720),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=61,width=1230,height=700)  



        #buttons

        b1_btn=Button(self.root,text="Train Data",width=27,font=("times new roman",20,"bold"),bg="blue",fg="white")
        b1_btn.place(x=0,y=640,width=1230,height=60)




    def train_classifier(self):
        data_dir=("IMAGE_Record")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].splits('.'[1]))

            faces.append(imageNp)
            id.np.append(id)
            cv2.imshow("Train",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)



    #==========Train the classifier============

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")





if __name__ == "__main__":
    root=Tk()
    obj=train_img(root)
    root.mainloop()