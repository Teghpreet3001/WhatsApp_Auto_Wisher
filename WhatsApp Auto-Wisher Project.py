#!/usr/bin/env python
# coding: utf-8

# ## WhatsApp Auto-Wisher Project
# 
# THE INTERN ACADEMY 
# 
# Task 2: Whatsapp Auto Wisher
# 
# Team Name: PyChamps
# 
# Domain: Python Projects
# 

# ### Problem Statement:
# Now-a-days we are watching that it has become a trend to message in whatsapp and wish birthdays, anniversaries or any special occasion. But yesterday was my friend’s birthday and I forget to wish him. You need to automate WhatsApp and set the date and time at which the wish of occasion will be automatically sent to the person you want. Create a user interface also with it.
# 
# ### Features of the project:
# 
# Softwares Used: In this project, we have used Python Programming Language (Version-3.7 and IDE-Jupyter Notebook) and its built in libraries like pymysql (Database Management)and Tkinter (GUI Development).The project also explores MySQL through phpMyAdmin (Server-127.0.0.1) and uses a subset of queries to work in between Python and MySQL softwares.
# 
# Working: ON successfully running the code, an interface asking for your name and the birthday wish you to send. After submitting the form, it takes you to a interface where all you do is confirm sending you message by pressing enter. The code automatically picks up the name and phone number of the person from the database and sends the wish via WhatsApp. 
# 
# GUI Development: We have used tkinter Python Library for presentable/attractive GUI developement. Alongside using tkinter options like Frame, Buttons, Labels, Headings and Entries, we use used the keyword 'self' with all functions to avoid the attribute error from occuring. 
# 
# MySQL: Using the XAMPP Control Panel (Version-3.3.0), we have created a table 'contact' in the database 'whatsapp' using MySQL through phpMyAdmin (Server-127.0.0.1). The columns along with their datatypes are SNo int(2), Name	varchar(20), Birth_Date	varchar(4), Phone_No bigint(10). 
# 
# OS Module: We have used the OS module in Python to provide functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc. The module links our source to WhatsApp Operating System.
# 

# In[1]:


pip install pymysql


# In[12]:


import datetime
import os
from tkinter import *
import pymysql

now=str(datetime.date.today())
Today=now[8:10]+now[5:7]
print(Today)

class wisher:
    def __init__(self):
        self.root = Tk()
        self.root.title('WhatsApp AutoWisher Project')
        
        self.root.geometry('700x400')
        self.root.resizable(False,False)
        self.root.configure(bg='#6cf542')
        
        self.heading = Label(self.root, text='WhatsAPP AutoWisher', font=('Times New Roman',40,'bold'),bg='#03a116',fg='white')
        self.heading.place(x=0,y=30,relwidth=1)
        
        self.f1 = Frame(self.root, bg="#6cf542")
        self.f1.place(x=0,y=100,relheight=1,relwidth=1)
        
        self.name = Label(self.f1,text='Enter your Name :',font=('Times New Roman',16,''),bg="#6cf542",fg='black')
        self.name.place(x=70,y=50)
        
        self.entermail = Entry(self.f1,bg="white",fg='black')
        self.entermail.place(x=240,y=50,height=35,width=400)
        
        self.password = Label(self.f1,text='Enter your Message',font=('Times New Roman',16,''),bg="#6cf542",fg='black')
        self.password.place(x=70,y=100)
        
        self.enterpass = Entry(self.f1,bg="white",fg='black')
        self.enterpass.place(x=240,y=100,height=35,width=400)
        
        self.b1 = Button(self.f1,text='Send wish!',command = self.send, fg='#044970',font=('Glacial Indiffernece',14,''),bg='#b5f7c6')
        self.b1.place(x=70,y=150,width=570,height=35)
        
        self.root.mainloop()
        
    def send(self) :
        mycon = pymysql.connect(host="localhost",user="root",password="",database ="whatsapp")
        mycursor = mycon.cursor()
        mycursor.execute(f"SELECT * FROM contact WHERE Birth_Date = {Today}")
        list1 = mycursor.fetchall()
        for i in list1:
            print(i)
        input("Simply press enter to send wish. Make sure to connect to internet!")
        for i in list1:
            os.system(f"start https://web.whatsapp.com/send?phone=91{i[3]}^&text=HAPPY%20BIRTHDAY%20{i[1]}")
            
ob = wisher()  


# In[ ]:




