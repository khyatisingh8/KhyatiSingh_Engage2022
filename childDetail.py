from distutils.util import execute
from logging import root
from optparse import Values
from re import L
import tkinter
from tkinter import*
from tkinter import ttk
from turtle import title, update
import PIL
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class child:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1230x700+0+0")
        self.root.title("Face Recognition Software")


        #==========Variables===========
        self.var_Gaurdian_Name=StringVar()
        self.var_mobileNo=StringVar()
        self.var_EmailId=StringVar()
        self.var_Address=StringVar()
        self.var_state=StringVar()
        self.var_pincode=StringVar()
        self.var_RegistrationNo=StringVar()
        self.var_Child_Name=StringVar()
        self.var_CAge=StringVar()
        self.var_Gender=StringVar()
        self.var_BirthMark=StringVar()



        #bg img
        img3=Image.open(r"F:\Face_Regonition\Image\black.png")
        img3=img3.resize((1230,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
 
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1230,height=700)  

        title_lbl=Label(bg_img,text="Child Tracking Informations", font=("times new roman",33,"bold"),bg="dark blue",fg="white")
        title_lbl.place(x=0,y=10,width=1230,height=50)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=70,width=1190, height=650)
 
        left_frame=LabelFrame(main_frame,bd=1,bg="purple",relief=RIDGE,text="Registration",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=575,height=580)
        
        #Gaurdian Details
        Gaurdian_Detail_frame=LabelFrame(left_frame,bd=1,bg="light pink",relief=RIDGE,text="Gaurdian Details",font=("times new roman",12,"bold"))
        Gaurdian_Detail_frame.place(x=10,y=10,width=550,height=275)
        
        #GuardianName
        GuardianName_label=Label(Gaurdian_Detail_frame,text="Name:",font=("times new roman",13,"bold"),bg="white",fg="black")
        GuardianName_label.grid(row=0,column=0,padx=10,pady=8,sticky=W)
        
        GuardianName_entry=ttk.Entry(Gaurdian_Detail_frame,textvariable=self.var_Gaurdian_Name,width=30,font=("times new roman",13,"bold"))
        GuardianName_entry.grid(row=0,column=1,padx=10,pady=8,sticky=W)
        
        #Mobile_Number
        MobileNo_label=Label(Gaurdian_Detail_frame,text="Mobile_Number:",font=("times new roman",13,"bold"),bg="white",fg="black")
        MobileNo_label.grid(row=1,column=0,padx=10,pady=8,sticky=W)

        MobileNo_entry=ttk.Entry(Gaurdian_Detail_frame,textvariable=self.var_mobileNo,width=20,font=("times new roman",13,"bold"))
        MobileNo_entry.grid(row=1,column=1,padx=10,pady=8,sticky=W)
        
        #Email_Id
        EmailId_label=Label(Gaurdian_Detail_frame,text="Email_Id:",font=("times new roman",13,"bold"),bg="white",fg="black")
        EmailId_label.grid(row=2,column=0,padx=10,pady=8,sticky=W)

        EmailId_entry=ttk.Entry(Gaurdian_Detail_frame,textvariable=self.var_EmailId,width=30,font=("times new roman",13,"bold"))
        EmailId_entry.grid(row=2,column=1,padx=10,pady=8,sticky=W)
        
        #Address
        Address_label=Label(Gaurdian_Detail_frame,text="Address:",font=("times new roman",13,"bold"),bg="white",fg="black")
        Address_label.grid(row=3,column=0,padx=10,pady=8,sticky=W)

        Address_entry=ttk.Entry(Gaurdian_Detail_frame,textvariable=self.var_Address,width=40,font=("times new roman",13,"bold"))
        Address_entry.grid(row=3,column=1,padx=10,pady=8,sticky=W)
        
        #state
        State_label=Label(Gaurdian_Detail_frame,text="State:",font=("times new roman",13,"bold"),bg="white",fg="black")
        State_label.grid(row=4,column=0,padx=10,pady=8,sticky=W)

        State_entry=ttk.Entry(Gaurdian_Detail_frame,width=20,textvariable=self.var_state,font=("times new roman",13,"bold"))
        State_entry.grid(row=4,column=1,padx=10,pady=8,sticky=W)
        
        #Pin_Code
        PinCode_label=Label(Gaurdian_Detail_frame,text="Pin_Code:",font=("times new roman",13,"bold"),bg="white",fg="black")
        PinCode_label.grid(row=5,column=0,padx=10,pady=8,sticky=W)

        PinCode_entry=ttk.Entry(Gaurdian_Detail_frame,textvariable=self.var_pincode,width=10,font=("times new roman",13,"bold"))
        PinCode_entry.grid(row=5,column=1,padx=10,pady=8,sticky=W)
        
        #child Details
        child_detail_frame=LabelFrame(left_frame,bd=1,bg="pink",relief=RIDGE,text="Child Details",font=("times new roman",12,"bold"))
        child_detail_frame.place(x=10,y=300,width=550,height=240)

        #Child Description
        Child_Name_label=Label(child_detail_frame,text="Name:",font=("times new roman",13,"bold"),bg="white",fg="black")
        Child_Name_label.grid(row=0,column=0,padx=10,pady=8,sticky=W)
        
        Child_Name_entry=ttk.Entry(child_detail_frame,textvariable=self.var_Child_Name,width=20,font=("times new roman",13,"bold"))
        Child_Name_entry.grid(row=0,column=1,padx=10,pady=8,sticky=W)

        #Child Age
        Child_age_label=Label(child_detail_frame,text="Age:",font=("times new roman",13,"bold"),bg="white",fg="black")
        Child_age_label.grid(row=1,column=0,padx=10,pady=8,sticky=W)
        
        Child_age_entry=ttk.Entry(child_detail_frame,textvariable=self.var_CAge,width=5,font=("times new roman",13,"bold"))
        Child_age_entry.grid(row=1,column=1,padx=10,pady=8,sticky=W)

        #Child gender
        Child_gender_label=Label(child_detail_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white",fg="black")
        Child_gender_label.grid(row=2,column=0,padx=10,pady=8,sticky=W)
        
        Child_gender_combo=ttk.Combobox(child_detail_frame,textvariable=self.var_Gender,width=10,font=("times new roman",13,"bold"),state="readonly")
        Child_gender_combo["values"]=("Select","Female","Male","Other")
        Child_gender_combo.current(0)
        Child_gender_combo.grid(row=2,column=1,padx=10,pady=8,sticky=W)

        #Registration_Number 
        RegistrationNo_label=Label(child_detail_frame,text="Registration_Number:",font=("times new roman",13,"bold"),bg="white",fg="black")
        RegistrationNo_label.grid(row=3,column=0,padx=10,pady=8,sticky=W)

        RegistrationNo_entry=ttk.Entry(child_detail_frame,textvariable=self.var_RegistrationNo,width=20,font=("times new roman",13,"bold"))
        RegistrationNo_entry.grid(row=3,column=1,padx=10,pady=8,sticky=W)

        #Child Description
        Child_Description_label=Label(child_detail_frame,text="Identification:    ",font=("times new roman",13,"bold"),bg="white",fg="black")
        Child_Description_label.grid(row=4,column=0,padx=10,pady=8,sticky=W)
        
        Child_Descritpion_entry=ttk.Entry(child_detail_frame,textvariable=self.var_BirthMark,width=30,font=("times new roman",13,"bold"))
        Child_Descritpion_entry.grid(row=4,column=1,padx=10,pady=8,sticky=W)

        #right frame
        right_frame=LabelFrame(main_frame,bd=1,bg="light pink",relief=RIDGE,text="Registration",font=("times new roman",12,"bold"))
        right_frame.place(x=595,y=10,width=575,height=580)


        #Right img
        img_Right=Image.open(r"Image\face.jpg")
        img_Right=img_Right.resize((560,250),Image.ANTIALIAS)
        self.photoimg_Right=ImageTk.PhotoImage(img_Right)

        f_lbl=Label(right_frame,image=self.photoimg_Right)
        f_lbl.place(x=5,y=10,width=560,height=250) 

        #image frame
        image_frame=LabelFrame(right_frame,bd=1,bg="white",relief=RIDGE,text="Child Photo Registration",font=("times new roman",12,"bold"))
        image_frame.place(x=5,y=265,width=563,height=120)

        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(image_frame,text="Take Photo_Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=1,column=0)

        
        radiobtn2=ttk.Radiobutton(image_frame,text="No Photo_Sample",variable=self.var_radio1,value="No")
        radiobtn2.grid(row=1,column=1)

        #Button frame1
        btn_frame=Frame(image_frame,bd=1,relief=RIDGE)
        btn_frame.place(x=0,y=20,width=568,height=37)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=13,font=("times new roman",13,"bold"),bg="purple",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=13,font=("times new roman",13,"bold"),bg="purple",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=13,font=("times new roman",13,"bold"),bg="purple",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times new roman",13,"bold"),bg="purple",fg="white")
        reset_btn.grid(row=0,column=3)

        #Button frame
        btn_frame1=Frame(image_frame,bd=1,relief=RIDGE)
        btn_frame1.place(x=0,y=57,width=560,height=37)

        Capture_btn=Button(btn_frame1,text="Take a Photo_Sample",command=self.generate_dataset,width=27,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Capture_btn.grid(row=0,column=0)

        update1_btn=Button(btn_frame1,text="Update a Photo_Sample",width=27,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update1_btn.grid(row=0,column=1)

    
    #==============Search System================
        search_frame=LabelFrame(right_frame,bd=1,bg="pink",relief=RIDGE,text="Search Desk",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=380,width=563,height=65)   

        
        search_label=Label(search_frame,text="Search by:",font=("times new roman",13,"bold"),bg="white",fg="black")
        search_label.grid(row=0,column=0,padx=10,pady=8,sticky=W)

        search_combo=ttk.Combobox(search_frame,width=10,font=("times new roman",13,"bold"),state="readonly")
        search_combo["values"]=("Select","Child_Name","Registration_Number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=8,sticky=W)
    
        search_btn=Button(search_frame,text="Search",command=self.generate_dataset,width=8,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)

        showall_btn=Button(search_frame,text="Show All",command=self.generate_dataset,width=8,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4)

    #==========Table frame===========
        table_frame=LabelFrame(right_frame,bd=1,bg="pink",relief=RIDGE,text="Search Desk",font=("times new roman",12,"bold"))
        table_frame.place(x=5,y=450,width=563,height=100)

        scroll_barx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_bary=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.detail_table=ttk.Treeview(table_frame,column=("Gaurdian_Name","Mobile_Number","Email_Id","Address","State","Pin_Code","Child_Name","Age","Gender","Registration_Number","Birth_Mark","Photo_Sample"),xscrollcommand=scroll_barx.set,yscrollcommand=scroll_bary.set)
        scroll_barx.pack(side=BOTTOM,fill=X)
        scroll_bary.pack(side=RIGHT,fill=Y)
        scroll_barx.config(command=self.detail_table.xview)
        scroll_bary.config(command=self.detail_table.yview)

        self.detail_table.heading("Child_Name",text="Child_Name")
        self.detail_table.heading("Age",text="Age")
        self.detail_table.heading("Gender",text="Gender")
        self.detail_table.heading("Birth_Mark",text="Birth_Mark")
        self.detail_table.heading("Gaurdian_Name",text="Gaurdian_Name")
        self.detail_table.heading("Mobile_Number",text="Mobile_Number")
        self.detail_table.heading("Email_Id",text="Email_Id")
        self.detail_table.heading("Address",text="Address")
        self.detail_table.heading("State",text="State")
        self.detail_table.heading("Pin_Code",text="Pin_Code")
        self.detail_table.heading("Registration_Number",text="Registration_Number")
        self.detail_table.heading("Photo_Sample",text="Photo_Sample Status")
        self.detail_table["show"]="headings"


        self.detail_table.column("Child_Name",width=100)
        self.detail_table.column("Age",width=30)
        self.detail_table.column("Gender",width=50)
        self.detail_table.column("Birth_Mark",width=100)
        self.detail_table.column("Gaurdian_Name",width=100)
        self.detail_table.column("Mobile_Number",width=100)
        self.detail_table.column("Email_Id",width=100)
        self.detail_table.column("Address",width=100)
        self.detail_table.column("State",width=50)
        self.detail_table.column("Pin_Code",width=100)
        self.detail_table.column("Registration_Number",width=50)
        self.detail_table.column("Photo_Sample",width=100)
         
        
        self.detail_table.pack(fill=BOTH,expand=1)
        self.detail_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    #==============Function Declaration=========
    def add_data(self):  
        if self.var_Gaurdian_Name.get()=="" or self.var_mobileNo.get()=="" or  self.var_EmailId.get()=="" or self.var_Address.get()=="" or self.var_state.get()=="" or self.var_pincode.get()=="" or self.var_RegistrationNo.get()=="" or self.var_Child_Name.get()=="" or self.var_CAge.get()=="" or self.var_Gender=="Select" or self.var_BirthMark.get()=="":
             messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@Brunococo8",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into registration values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_Gaurdian_Name.get(),self.var_mobileNo.get(),self.var_EmailId.get(),self.var_Address.get(),self.var_state.get(),self.var_pincode.get(),self.var_Child_Name.get(),self.var_CAge.get(),self.var_Gender.get(),self.var_RegistrationNo.get(),self.var_BirthMark.get(),self.var_radio1.get() ))
            
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Child Registration has been done Successfully!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #==============fetch data===========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Brunococo8",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from registration")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.detail_table.delete(*self.detail_table.get_children())
            for i in data:
                self.detail_table.insert("",END,values=i)
        conn.commit()
        conn.close()

    #==============get cursor==============
    def get_cursor(self,event=""):
        cursor_focus=self.detail_table.focus()
        content=self.detail_table.item(cursor_focus)
        data=content["values"]

        
        self.var_Gaurdian_Name.set(data[0])
        self.var_mobileNo.set(data[1])
        self.var_EmailId.set(data[2])
        self.var_Address.set(data[3])
        self.var_state.set(data[4])
        self.var_pincode.set(data[5]) 
        self.var_Child_Name.set(data[6])
        self.var_CAge.set(data[7])
        self.var_Gender.set(data[8])
        self.var_RegistrationNo.set(data[9])
        self.var_BirthMark.set(data[10])              
        self.var_radio1.set(data[11])


    
    
    #================Update function===============
    def update_data(self):
        if self.var_Gaurdian_Name.get()=="" or self.var_mobileNo.get()=="" or  self.var_EmailId.get()=="" or self.var_Address.get()=="" or self.var_state.get()=="" or self.var_pincode.get()=="" or self.var_RegistrationNo.get()=="" or self.var_Child_Name.get()=="" or self.var_CAge.get()==""  or self.var_Gender=="Select" or self.var_BirthMark.get()=="":
             messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                 Update=messagebox.askyesno("Update","Do you want to update these details",parent=self.root)
                 if Update>1:
                     conn=mysql.connector.connect(host="localhost",username="root",password="@Brunococo8",database="face_recognition")
                     my_cursor=conn.cursor()
                     my_cursor.execute("update registration set Gaurdian_Name=%s,Mobile_Number=%s,Email_Id=%s,Address=%s,State=%s,Pin_Code=%s,Child_Name=%s,Age=%s,Gender=%s,Birth_Mark=%s,Photo_Sample=%s where Registration_Number=%s",(self.var_Gaurdian_Name.get(),self.var_mobileNo.get(),self.var_EmailId.get(),self.var_Address.get(),self.var_state.get(),self.var_pincode.get(),self.var_Child_Name.get(),self.var_CAge.get(),self.var_Gender.get(),self.var_BirthMark.get(),self.var_radio1.get(),self.var_RegistrationNo.get()==id+1))
                     conn.commit()
                     self.fetch_data()
                     conn.close()
                 else:
                     if not Update:
                         return
                 messagebox.showinfo("Success","Details have been Updated Successfully",parent=self.root)
                 conn.commit()
                 self.fetch_data()
                 conn.close()
            except Exception as es:
                 messagebox.messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


     #delete function
    def delete_data(self):
        if self.var_RegistrationNo.get()=="":
           messagebox.showerror("Error","Registration_Number must be required",parent=self.root)
        else:
             try:
                 self.delete_data=messagebox.askyesno("Registration Detail Delete Page","Do you want to delete this information",parent=self.root)
                 if self.delete_data>1:
                     conn=mysql.connector.connect(host="localhost",username="root",password="@Brunococo8",database="face_recognition")
                     my_cursor=conn.cursor()
                     sql="delete from where student_id=%s"
                     val=(self.var_RegistrationNo.get(),)
                     my_cursor.execute(sql,val)
                 else:
                    if not self.delete_data:
                         return
                 conn.commit() 
                 self.fetch_data()
                 self.reset_data()
                 conn.close()
                 messagebox.showinfo("Delete","Successfully Delete Details",parent=self.root)
             except Exception as es:
                 messagebox.messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #Reset
    def reset_data(self):
        self.var_Gaurdian_Name.set("")
        self.var_mobileNo.set("")
        self.var_EmailId.set("")
        self.var_Address.set("")
        self.var_state.set("")
        self.var_pincode.set("")
        self.var_RegistrationNo.set("")
        self.var_Child_Name.set("")
        self.var_CAge.set("")
        self.var_Gender.set("Select")
        self.var_RegistrationNo.set("")
        self.var_BirthMark.set("")
    
    
    #============== Generate data set / Take Photo_Sample==============
    def generate_dataset(self):
        if self.var_Gaurdian_Name.get()=="" or self.var_mobileNo.get()=="" or  self.var_EmailId.get()=="" or self.var_Address.get()=="" or self.var_state.get()=="" or self.var_pincode.get()=="" or self.var_RegistrationNo.get()=="" or self.var_Child_Name.get()=="" or self.var_CAge.get()=="" or self.var_BirthMark.get()=="":
             messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@Brunococo8",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select* from registration")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update registration set Gaurdian_Name=%s,Mobile_Number=%s,Email_Id=%s,Address=%s,State=%s,Pin_Code=%s,Child_Name=%s,Age=%s,Gender=%s,Birth_Mark=%s,Photo_Sample=%s where Registration=%s",(self.var_Gaurdian_Name.get(),self.var_mobileNo.get(),self.var_EmailId.get(),self.var_Address.get(),self.var_state.get(),self.var_pincode.get(),self.var_Child_Name.get(),self.var_CAge.get(),self.var_RegistrationNo.get(),self.var_BirthMark.get(),self.var_radio1.get(),self.var_RegistrationNo.get()))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #============= data on face frontals from opencv==========

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):
                    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(grey,1.3,5)

                    for(x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,face_frame=cap.read()
                    if face_crop(face_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_crop(face_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="IMAGE_Record/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!")

            except Exception as es:
                 messagebox.messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)




                     

        

if __name__ == "__main__":
    root=Tk()
    obj=child(root)
    root.mainloop()