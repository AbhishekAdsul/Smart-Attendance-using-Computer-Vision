from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.geometry("750x640+0+0")
        self.root.title("face Recognition System")
        self.root.bind('<Return>',self.enter_func)
        self.root.wm_iconbitmap("Smart.ico")


        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()


        img_top=Image.open(r"images/image8.jpg")
        img_top=img_top.resize((200,70),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        Title_label=Label(main_frame,bd=3,relief=RIDGE,anchor='nw',width=730,compound=LEFT,image=self.photoimg_top,text='Chat Bot',font=('arial',30,'bold'),fg='violet',bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()
        
        btn_frame=Frame(self.root,bd=4,bg='white',width=610)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)
        
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',15,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',16,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',16,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)
        
        self.msg=''
        self.label_2=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label_2.grid(row=1,column=1,padx=5,sticky=W)


        #=======================function Declaration==================================

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if(self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_2.config(text=self.msg,fg='red')
        
        else:
            self.msg=''
            self.label_2.config(text=self.msg,fg='red')

        if(self.entry.get()=="hello"):
            self.text.insert(END,"\n\n"+"Bot:Hi")

        elif(self.entry.get()=="hi"):
            self.text.insert(END,"\n\n"+"Bot:Hello")

        elif(self.entry.get()=="How are you?"):
            self.text.insert(END,"\n\n"+"Bot:fine and you")

        elif(self.entry.get()=='Fantastic'):
            self.text.insert(END,"\n\n"+"Bot:Nice to Hear")

        elif(self.entry.get()=="Who created you?"):
            self.text.insert(END,"\n\n"+"Bot:Abhishek Adsul did using python")

        elif(self.entry.get()=="What is your name?"):
            self.text.insert(END,"\n\n"+"Bot:My name is Smart Attendance")

        elif(self.entry.get()=="Can you speak marathi"):
            self.text.insert(END,"\n\n"+"Bot:I'm still learning it..")
        
        elif(self.entry.get()=="What is machine learning?"):
            self.text.insert(END,"\n\n"+"Bot:Machine learning is a type \nof artificial intelligence (AI) \nthat enables systems to learn \nand improve from experience \nwithout being explicitly programmed.\n It involves developing algorithms \nthat can receive input data \nand use statistical analysis \nto predict an output while \nupdating the algorithms as new \ndata is collected. Machine learning can \nbe used to develop complex models \nand systems that can serve a variety \nof purposes, including predicting \noutcomes and detecting patterns.")

        elif(self.entry.get()=="How does face recognition work?"):
            self.text.insert(END,"\n\n"+"Bot:Face recognition works by using \na combination of computer vision \nand machine learning algorithms\n to identify a person's face by \ncomparing facial features from \na digital image with a database \nof faces. The process typically \nbegins by extracting facial features \nfrom an image or video of a face. ")

        elif(self.entry.get()=="How does facial recognition work step by step?"):
            self.text.insert(END,"\n\n"+"Bot:Step 1: Capture an image of the face. \n\nStep 2: Pre-process the image, which includes\n adjusting the brightness and \ncontrast of the image, cropping\n the image so it only contains \nthe face, and converting it \nto a digital format.\n\nStep 3: Extract facial features from the\n pre-processed image. This is done\n by finding the eyes, nose, \nand mouth, and creating a mathematical\n model of the face, which is \ncalled a facial template.")

        elif(self.entry.get()=="How many countries use facial recognition?"):
            self.text.insert(END,"\n\n"+"Bot:It is difficult to estimate \nhow many countries use facial recognition\n technology because many countries\n do not publicly disclose their \nuse of this technology. However,\n it is estimated that over 70 countries \nare currently using facial \nrecognition technology.")

        elif(self.entry.get()=="What is python programming?"):
            self.text.insert(END,"\n\n"+"Bot:Python is a high-level,\n interpreted, open-source programming language.\n It is a multi-paradigm language that \nsupports both object-oriented and\n functional programming. \nIt is used for web development, scripting,\n data analysis, artificial intelligence,\n and scientific computing. ")

        elif(self.entry.get()=="What is chatbot?"):
            self.text.insert(END,"\n\n"+"Bot:A chatbot is an artificial intelligence (AI)\n program that simulates interactive \nhuman conversation by using key pre-calculated\n user phrases and auditory or text-based signals. \nChatbots are often used in applications \nsuch as customer service, information gathering,\n online shopping, and online gaming.")

        elif(self.entry.get()=="Why there is need of Smart Attendance?"):
            self.text.insert(END,"\n\n"+"Bot:Smart Attendance is a tool \nused to help organizations track and \nmonitor employee attendance. \nIt can provide real-time data and analytics\n to help managers and supervisors \nquickly identify attendance problems\n and take corrective action.\nSmart Attendance can make the process \nof tracking attendance easier \nand more efficient, \nsaving organizations time and money.")

        elif(self.entry.get()=="Why there is need of Face recognition attendance?"):
            self.text.insert(END,"\n\n"+"Bot:It is a highly secure and \naccurate system that allows employers\n to keep track of employee hours, \nwhile also providing the convenience of \nautomated attendance tracking.\n Face recognition attendance can save employers \ntime and money, improve accuracy, \nand reduce the risk of fraud employee.")

        elif(self.entry.get()=="What is Smart Attendance?"):
            self.text.insert(END,"\n\n"+"Smart Attendance using facial recognition\n is a biometric-based technology that\n uses facial recognition to \nautomatically identify and track \nattendance of individuals in an organization \nor institution. It uses facial recognition \nalgorithms to compare images of faces to a \ndatabase of known faces and then generates\n an attendance report based on the comparison.")

        elif(self.entry.get()=="What is Face Recognition Attendance System"):
            self.text.insert(END,"\n\n"+"Bot:Hello")

        elif(self.entry.get()=="Where we can use Smart Attendance?"):
            self.text.insert(END,"\n\n"+"Bot:Smart Attendance can be used \nin a variety of settings, such as schools,\n businesses, and organizations. \nIn schools, it can be used to track\n students' attendance and performance, \nwhile in businesses and organizations, \nit can be used to monitor employee attendance \nand productivity.")

        elif(self.entry.get()=="How we can develop Smart Attendance System?"):
            self.text.insert(END,"\n\n"+"Bot:1.Create a Database of Students \n2. Install Security Cameras \n3.Develop Algorithm \n 4.Implement the System\n5. Monitor Attendance")

        elif(self.entry.get()=="How we can develop Face Recognition System?"):
            self.text.insert(END,"\n\n"+"Bot:1.Create a Database of Students \n2. Install Security Cameras \n3.Develop Algorithm \n 4.Implement the System\n5. Monitor Attendance")

        elif(self.entry.get()=="What are the steps to use Smart Attendance efficiently?"):
            self.text.insert(END,"\n\n"+"Bot:1.save the information of student\nIn the Student window in Smart Attendance\n2.Take the photo sample of student\n3.Train the photo sample data\n4.Open the face detector window\n and start detecting the faces of student\n5.Manage the attendance in Attendance window")

        elif(self.entry.get()=="bye"):
            self.text.insert(END,"\n\n"+"Bot:Thank you for chatting")

        else:
            self.text.insert(END,"\n\n"+"Bot:Hello")
        

        































if __name__=="__main__":
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()