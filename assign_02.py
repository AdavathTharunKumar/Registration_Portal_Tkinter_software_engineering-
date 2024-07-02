import os 
import re
from tkinter import * 
import tkinter.messagebox as tmsg

class kgpdata(Tk):
    def __init__(self):
        super().__init__()
        self.title("Dynamic Views Example")
        self.geometry("400x200")
        self.create_first_page()
    def create_first_page(self):
        self.label1=Label(text="enter your choice")
        self.label1.pack()
        self.button1=Button(text="create new data",command=self.create_page_2)
        self.button1.pack()
        self.button2=Button(text="use existing data",command=self.create_page_3)
        self.button2.pack()
    def creating_file(self,filename): 
        try:
           with open(filename, 'w') as f: 
               pass  
        except IOError: 
           print("Error: could not create file " + filename)
    def create_page_2(self):
        self.button1.destroy()
        self.label1.destroy()
        self.button2.destroy()
        self.creating_file("teacher")
        self.creating_file("ugstudent")
        self.creating_file("pgstudent")
        self.creating_file("removed")
        self.create_page_3()
    def create_page_3(self):
        self.button1.destroy()
        self.label1.destroy()
        self.button2.destroy()
        self.label2=Label(text="gmail")
        self.label3=Label(text="password")
        self.label2.grid(row=1,column=1)
        self.label3.grid(row=2,column=1)
        self.gmail=StringVar()
        self.password=StringVar()
        self.box1=Entry(textvariable=self.gmail)
        self.box1.grid(row=1,column=2)
        self.box2=Entry(textvariable=self.password)
        self.box2.grid(row=2,column=2)
        self.button3=Button(text="submit",command=lambda :self.check_gmail(self.password.get(),self.gmail.get()))
        self.button3.grid(row=3,column=1)
        self.button4=Button(text="signin",command=self.signin_portal)
        self.button4.grid(row=3,column=2)
    def signin_portal(self):
       self.label2.destroy()
       self.label3.destroy()
       self.box1.destroy()
       self.box2.destroy()
       self.button3.destroy()
       self.button4.destroy()
       self.label4=Label(text="gmail")
       self.label5=Label(text="password")
       self.label4.grid(row=1,column=1)
       self.label5.grid(row=2,column=1)
       self.gmail1=StringVar()
       self.password1=StringVar()
       self.box5=Entry(textvariable=self.gmail1)
       self.box5.grid(row=1,column=2)
       self.box6=Entry(textvariable=self.password1)
       self.box6.grid(row=2,column=2)  
       p=len(self.password1.get() )
       self.button5=Button(text="teacher",command= lambda :self.check(self.password1.get(),self.gmail1.get(),1,p))
       self.button6=Button(text="ugstudent",command=lambda :self.check(self.password1.get(),self.gmail1.get(),2,p))
       self.button7=Button(text="phdstudent",command=lambda :self.check(self.password1.get(),self.gmail1.get(),3,p))
       self.button5.grid(row=3,column=1)
       self.button6.grid(row=3,column=3)
       self.button7.grid(row=3,column=5)
    def passport(self,password,gmail):
       
       if  not len(password) in [8,9,10,11,12]:
         return 1
       if not any(char.isupper() for char in password):
         return 1
       if not any(char.isdigit() for char in password):
        return 1
       if not any(char in ["!","@","#","$","%","&","*"] for char in password ):
        return 1
       if  any(char in [" "] for char in password ):
        return 1
       if  not "@gmail.com" in gmail :
          return 1
       return 0 
    def check( self,password,gmail,a,p):
       q=self.passport(password,gmail)
       if q==0 :
          if a==1:
            self.adding_into_teachers(password,gmail)
            self.label4.destroy()
            self.label5.destroy()
            self.box5.destroy()
            self.box6.destroy()
            self.button5.destroy()
            self.button6.destroy()
            self.button7.destroy()
            self.create_page_3()
          if a==2:
            self.adding_into_ugstudent(password,gmail)
            self.label4.destroy()
            self.label5.destroy()
            self.box5.destroy()
            self.box6.destroy()
            self.button5.destroy()
            self.button6.destroy()
            self.button7.destroy()
            self.create_page_3()
          if a==3 :
            self.adding_into_phdstudent(password,gmail)
            self.label4.destroy()
            self.label5.destroy()
            self.box5.destroy()
            self.box6.destroy()
            self.button5.destroy()
            self.button6.destroy()
            self.button7.destroy()
            self.create_page_3()
       else :
            self.label4.destroy()
            self.label5.destroy()
            self.box5.destroy()
            self.box6.destroy()
            self.button5.destroy()
            self.button6.destroy()
            self.button7.destroy()
            p=tmsg.showinfo("your either password format or gmail format is wrong")
            self.signin_portal()   
    def adding_into_teachers(self,password,gmail):
        try:
            with open("teacher", 'a') as f:
               f.write(gmail+"\n")
               f.write(password+"\n")
               f.write("0"+"\n")  
        except IOError: 
           print("Error: could not create file " + "teacher")
    def adding_into_ugstudent(self,password,gmail):
        try:
            with open("ugstudent", 'a') as f:
               f.write(gmail+"\n")
               f.write(password+"\n") 
               f.write("0"+"\n")  
        except IOError: 
           print("Error: could not create file " + "ugstudent")
    def adding_into_phdstudent(self,password,gmail):
        try:
            with open("phdstudent", 'a') as f:
               f.write(gmail+"\n")
               f.write(password+"\n")
               f.write("0"+"\n")    
        except IOError: 
           print("Error: could not create file " + "phdstudent")
    def hold(self):
             k=tmsg.showinfo("this id is blocked because you have given incorect password for three times")
             self.label2.destroy()
             self.label3.destroy()
             self.box1.destroy()
             self.box2.destroy()
             self.button3.destroy()
             self.button4.destroy()
             self.create_page_3()
    def new (self):
             self.label2.destroy()
             self.label3.destroy()
             self.box1.destroy()
             self.box2.destroy()
             self.button3.destroy()
             self.button4.destroy()
             p=tmsg.showinfo("no such id present")
             self.create_page_3()
    def check_gmail(self,password,gmail):
        if "gmail.com" in gmail :
             id=gmail  
             t=-1
             data=[]
             try:
                with open("removed", 'r') as f: 
                  data= f.readlines() 
                  data=[line.strip() for line in data] 
             except IOError: 
                 print("Error: could not create file " + "removed")
             if id in data :
              t=data.index(id)
              self.hold()
             else:
                try:
                   with open("teacher", 'r') as f:
                    data= f.readlines() 
                    data=[line.strip() for line in data] 
                except IOError: 
                      print("Error: could not create file " + "teacher")
                if id in data :
                  t=data.index(id)
                  self.mainfunct(data,t,"teacher",password)
                else:
                    
                    try:
                        with open("ugstudent", 'r') as f: 
                         data= f.readlines() 
                         data=[line.strip() for line in data]  
                    except IOError: 
                       print("Error: could not create file " + "ugstudent")
                    if id in data :
                       t=data.index(id)
                       self.mainfunct(data,t,"ugstudent",password)
                    else:
                        try:
                         with open("phdstudent", 'r') as f: 
                               data= f.readlines() 
                               data=[line.strip() for line in data]
                        except IOError: 
                           print("Error: could not create file " + "phdstudent")
                        if id in data :
                           t=data.index(id)
                           self.mainfunct(data,t,"phdstudent",password) 
                        else:
                           print("hello")
                           self.new()    
        else :
             self.label2.destroy()
             self.label3.destroy()
             self.box1.destroy()
             self.box2.destroy()
             self.button3.destroy()
             self.button4.destroy()
             p=tmsg.showinfo("your either password format or gmail format is wrong")
             self.create_page_3()      
    def value_check(self,password,gmail,data,filename,t):
       q=self.passport(password,gmail)
       if q==0:
          data[t]=gmail
          data[t+1]=password
          data[t+2]="0"
          with open(filename, "w") as file:
            for item in data:
              file.write(item + "\n")
          self.label10.destroy()
          self.label11.destroy()
          self.box10.destroy()
          self.box21.destroy()
          self.button14.destroy()
          self.create_page_3()
       else:
          self.label10.destroy()
          self.label11.destroy()
          self.box10.destroy()
          self.box21.destroy()
          self.button14.destroy()
          self.create_page_3()
          p=tmsg.showinfo("either your password or gmail is in incorect format")
          print("hello")
          self.edit_profile(data,t,filename)  
    def edit_profile(self,data,t,filename):
       self.button3.destroy()
       self.button8.destroy()
       self.button9.destroy()
       self.button40.destroy()
       self.label10=Label(text="gmail")
       self.label11=Label(text="password")
       self.label10.grid(row=1,column=1)
       self.label11.grid(row=2,column=1)
       self.gmail10=StringVar()
       self.password10=StringVar()
       self.box10=Entry(textvariable=self.gmail10)
       self.box10.grid(row=1,column=2)
       self.box21=Entry(textvariable=self.password10)
       self.box21.grid(row=2,column=2)
       print("hello1")
       self.button3.destroy()
       self.button14=Button(text="register",command=lambda :self.value_check(self.password10.get(),self.gmail10.get(),data,filename,t))
       self.button14.grid(row=3,column=1)
    def create(self):
       self.button8.destroy()
       self.button9.destroy()
       self.button40.destroy()
       self.create_page_3()
    def remove_profile(self,data,t,filename):
       data.pop(t)
       data.pop(t)
       data.pop(t)
       with open(filename, "w") as file:
            for item in data:
              file.write(item + "\n")
       self.button8.destroy()
       self.button9.destroy()
       self.button40.destroy()
       self.create_page_3()       
    def mainfunct(self,data,t,filename,password):
      if not data[t+1]==password:
          data[t+2]=str(int(data[t+2])+1)
          with open(filename, "w") as file:
            for item in data:
              file.write(item + "\n")
          if data[t+2]=="3":
             k=tmsg.showinfo("this id is blocked because you have given incorect password for three times")
             with open("removed", "a") as file:
                file.write(data[t] + "\n")
             self.label2.destroy()
             self.label3.destroy()
             self.box1.destroy()
             self.box2.destroy()
             self.button3.destroy()
             self.button4.destroy()
             self.create_page_3()
          else :
             k=tmsg.showinfo("incorrect password")
             self.label2.destroy()
             self.label3.destroy()
             self.box1.destroy()
             self.box2.destroy()
             self.button3.destroy()
             self.button4.destroy()
             self.create_page_3()
      else : 
             data[t+2]="0"
             self.label2.destroy()
             self.label3.destroy()
             self.box1.destroy()
             self.box2.destroy()
             self.button3.destroy()
             self.button4.destroy()
             self.button8=Button(text="want to edit your profile",command=lambda: self.edit_profile(data,t,filename))
             self.button9=Button(text="login in page",command=lambda: self.create())
             self.button40=Button(text="remove account",command=lambda: self.remove_profile(data,t,filename))
             self.button40.grid(row=3,column=10)
             self.button8.grid(row=1,column=10)
             self.button9.grid(row=2,column=10)
if __name__ == "__main__":
    signed_in = False
    app = kgpdata()
    app.mainloop()




    