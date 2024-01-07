from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("Smart.ico")

        title_lbl=Label(self.root,text="DEVELOPERS",font=("times new roman",35,"bold"),bg="pink",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"images/image22.jpg")
        img_top=img_top.resize((1530,745),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1530,height=745)


        #Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1250,y=0,width=250,height=300)

        #Developer 1
        img_top1=Image.open(r"images/image25.jpg")
        img_top1=img_top1.resize((200,230),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=20,y=0,width=200,height=220)

        dep_label=Label(main_frame,text="Abhishek Adsul",font=("times new roman",20,"bold"),fg="blue",bg="pink")
        dep_label.place(x=24,y=220)
     
      




        
    

    
























if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()