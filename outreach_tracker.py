import customtkinter
import tkinter as tk
from tkinter import messagebox
import string
import os

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
resaltion="1980x1024"
root=customtkinter.CTk()
root.geometry(resaltion)

root.title("Outreach Tracker")


path="D:\\tracker\\"

a=list(string.ascii_letters)
b=list(string.punctuation)
l=a+b



def button1_back():  
    try:
        
        for j in entry1.get():
            if j in l :
                messagebox.showinfo("Error", "Only Can Input Numbers!")
                break
        for j in entry2.get():   
            if  j in l:
                messagebox.showinfo("Error", "Only Can Input Numbers!")
                break

        if entry1.get()=="":
            messagebox.showinfo("Error", "Enter The Year!")
       
        
        if entry2.get() == "":
            attempts=0
            meeting_set=0
            cliend_closed=0
            revenue=0
            
            for i in range(1,13):
                try:
                    file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(i),"r")
                    value=file.readlines()
                    file.close
                    entry19.delete(0,"end")
                    entry19.insert(10,value)
                    attempts=attempts+int(entry19.get())

                    file=open(path+"Cold_call_metting_set_"+str(entry1.get())+"_"+str(i),"r")
                    value=file.readlines()
                    file.close
                    entry20.delete(0,"end")
                    entry20.insert(10,value)
                    meeting_set=meeting_set+int(entry20.get())

                    file=open(path+"Cold_call_clined_closed_"+str(entry1.get())+"_"+str(i),"r")
                    value=file.readlines()
                    file.close
                    entry21.delete(0,"end")
                    entry21.insert(10,value)
                    cliend_closed=cliend_closed+int(entry21.get())

                    file=open(path+"Cold_call_revenue_"+str(entry1.get())+"_"+str(i),"r")
                    value=file.readlines()
                    file.close
                    entry22.delete(0,"end")
                    entry22.insert(10,value)
                    revenue=revenue+int(entry22.get())


                    
                    file=open(path+"Cold_e_mail_attempets_"+str(entry1.get())+"_"+str(i),"r")
                    value=file.readlines()
                    file.close
                    entry19.delete(0,"end")
                    entry19.insert(10,value)
                    attempts=attempts+int(entry19.get())

                    file=open(path+"Cold_e_mail_metting_set_"+str(entry1.get())+"_"+str(i),"r")
                    value=file.readlines()
                    file.close
                    entry20.delete(0,"end")
                    entry20.insert(10,value)
                    meeting_set=meeting_set+int(entry20.get())

                    file=open(path+"Cold_e_mail_clined_closed_"+str(entry1.get())+"_"+str(i),"r")
                    value=file.readlines()
                    file.close
                    entry21.delete(0,"end")
                    entry21.insert(10,value)
                    cliend_closed=cliend_closed+int(entry21.get())

                    file=open(path+"Cold_e_mail_revenue_"+str(entry1.get())+"_"+str(i),"r")
                    value=file.readlines()
                    file.close
                    entry22.delete(0,"end")
                    entry22.insert(10,value)
                    revenue=revenue+int(entry22.get())

                    file=open(path+"Cold_Massiging_attempets_"+str(entry1.get())+"_"+str(i),"r")
                    value=file.readlines()
                    file.close
                    entry19.delete(0,"end")
                    entry19.insert(10,value)
                    attempts=attempts+int(entry19.get())
    
                    file=open(path+"Cold_Massiging_metting_set_"+str(entry1.get())+"_"+str(i),"r")
                    value=file.readlines()
                    file.close
                    entry20.delete(0,"end")
                    entry20.insert(10,value)
                    meeting_set=meeting_set+int(entry20.get())

                    file=open(path+"Cold_Massiging_clined_closed_"+str(entry1.get())+"_"+str(i),"r")
                    value=file.readlines()
                    file.close
                    entry21.delete(0,"end")
                    entry21.insert(10,value)
                    cliend_closed=cliend_closed+int(entry21.get())

                    file=open(path+"Cold_Massiging_revenue_"+str(entry1.get())+"_"+str(i),"r")
                    value=file.readlines()
                    file.close
                    entry22.delete(0,"end")
                    entry22.insert(10,value)
                    revenue=revenue+int(entry22.get())
                    
                    entry3.delete(0,"end")
                    entry4.delete(0,"end")
                    entry5.delete(0,"end")
                    entry6.delete(0,"end")
                    entry7.delete(0,"end")
                    entry8.delete(0,"end")
                    entry9.delete(0,"end")
                    entry11.delete(0,"end")
                    entry12.delete(0,"end")
                    entry13.delete(0,"end")
                    entry14.delete(0,"end")
                    entry15.delete(0,"end")
                    entry16.delete(0,"end")
                    entry17.delete(0,"end")
                    entry18.delete(0,"end") 
                except FileNotFoundError:
                    continue      
            entry19.delete(0,"end")
            entry20.delete(0,"end")
            entry21.delete(0,"end")
            entry22.delete(0,"end")
            entry19.insert(10,attempts)
            entry20.insert(10,meeting_set)
            entry21.insert(10,cliend_closed)
            entry22.insert(10,revenue)
            entry23.delete(0,"end")
            result=int(entry21.get())/int(entry19.get())*100
            entry23.insert(10,str(result)+"%")
            
        
        elif int(entry2.get())>12:  
            messagebox.showinfo("Error","invalid input Only Can Chosse Month From 1 To 12")
        elif int(entry2.get())<1 :
            messagebox.showinfo("Error","invalid input Only Can Chosse Month From 1 To 12")
                
        file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"r")
        value=file.readlines()
        file.close
        entry3.delete(0)
        entry3.insert(10,value) 
        file=open(path+"Cold_call_metting_set_"+str(entry1.get())+"_"+str(entry2.get()),"r")
        value=file.readlines()
        file.close
        entry4.delete(0)
        entry4.insert(10,value) 
        file=open(path+"Cold_call_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()),"r")
        value=file.readlines()
        file.close
        entry5.delete(0)
        entry5.insert(10,value)
        file=open(path+"Cold_call_revenue_"+str(entry1.get())+"_"+str(entry2.get()),"r")
        value=file.readlines()
        file.close
        entry6.delete(0)
        entry6.insert(10,value)
        file=open(path+"Cold_e_mail_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"r")
        value=file.readlines()
        file.close
        entry8.delete(0)
        entry8.insert(10,value) 
        file=open(path+"Cold_e_mail_metting_set_"+str(entry1.get())+"_"+str(entry2.get()),"r")
        value=file.readlines()
        file.close
        entry9.delete(0)
        entry9.insert(10,value) 
        file=open(path+"Cold_e_mail_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()),"r")
        value=file.readlines()
        file.close
        entry11.delete(0)
        entry11.insert(10,value)
        file=open(path+"Cold_e_mail_revenue_"+str(entry1.get())+"_"+str(entry2.get()),"r")
        value=file.readlines()
        file.close
        entry12.delete(0)
        entry12.insert(10,value)
        file=open(path+"Cold_Massiging_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"r")
        value=file.readlines()
        file.close
        entry14.delete(0)
        entry14.insert(10,value) 
        file=open(path+"Cold_Massiging_metting_set_"+str(entry1.get())+"_"+str(entry2.get()),"r")
        value=file.readlines()
        file.close
        entry15.delete(0)
        entry15.insert(10,value) 
        file=open(path+"Cold_Massiging_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()),"r")
        value=file.readlines()
        file.close
        entry16.delete(0)
        entry16.insert(10,value)
        file=open(path+"Cold_Massiging_revenue_"+str(entry1.get())+"_"+str(entry2.get()),"r")
        value=file.readlines()
        file.close
        entry17.delete(0)
        entry17.insert(10,value)
        
                
    except FileNotFoundError:
        messagebox.showinfo("Error","There is No Data With This Date")   
    
       
    

def button2_back():
    for j in entry1.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            break
    for j in entry2.get():   
        if  j in l:
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            break
        
    if entry1.get()=="":
        messagebox.showinfo("Error", "Enter The Year!")
        
    if entry2.get() == "":
        messagebox.showinfo("Error", "Enter The Month!")
            
    if int(entry2.get())>12:  
        messagebox.showinfo("Error","invalid input Only Can Chosse Month From 1 To 12")
    elif int(entry2.get())<1 :
        messagebox.showinfo("Error","invalid input Only Can Chosse Month From 1 To 12")
    
    open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w") 
    open(path+"Cold_call_metting_set_"+str(entry1.get())+"_"+str(entry2.get()),"w") 
    open(path+"Cold_call_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    open(path+"Cold_call_revenue_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    open(path+"Cold_e_mail_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    open(path+"Cold_e_mail_metting_set_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    open(path+"Cold_e_mail_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    open(path+"Cold_e_mail_revenue_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    open(path+"Cold_Massiging_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    open(path+"Cold_Massiging_metting_set_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    open(path+"Cold_Massiging_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    open(path+"Cold_Massiging_revenue_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    
    open(path+"Cold_call_attempets_"+str(entry1.get())+"_","w") 
    open(path+"Cold_call_metting_set_"+str(entry1.get())+"_","w") 
    open(path+"Cold_call_clined_closed_"+str(entry1.get())+"_","w")
    open(path+"Cold_call_revenue_"+str(entry1.get())+"_","w")
    open(path+"Cold_e_mail_attempets_"+str(entry1.get())+"_","w")
    open(path+"Cold_e_mail_metting_set_"+str(entry1.get())+"_","w")
    open(path+"Cold_e_mail_clined_closed_"+str(entry1.get())+"_","w")
    open(path+"Cold_e_mail_revenue_"+str(entry1.get())+"_","w")
    open(path+"Cold_Massiging_attempets_"+str(entry1.get())+"_","w")
    open(path+"Cold_Massiging_metting_set_"+str(entry1.get())+"_","w")
    open(path+"Cold_Massiging_clined_closed_"+str(entry1.get())+"_","w")
    open(path+"Cold_Massiging_revenue_"+str(entry1.get())+"_","w")  
    
    

    entry3.delete(0,"end")
    entry4.delete(0,"end")
    entry5.delete(0,"end")
    entry6.delete(0,"end")
    entry7.delete(0,"end")
    entry8.delete(0,"end")
    entry9.delete(0,"end")
    entry11.delete(0,"end")
    entry12.delete(0,"end")
    entry13.delete(0,"end")
    entry14.delete(0,"end")
    entry15.delete(0,"end")
    entry16.delete(0,"end")
    entry17.delete(0,"end")
    entry18.delete(0,"end")
    entry19.delete(0,"end")
    entry20.delete(0,"end")
    entry21.delete(0,"end")
    entry22.delete(0,"end")
    entry23.delete(0,"end")

        

def button3_back():
    
    
    
    for j in entry3.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry3.delete(0,"end")
            entry3.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry3.get())
            file.close
            break
        
    for j in entry4.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry4.delete(0,"end")
            entry4.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry4.get())
            file.close
            break
        
    for j in entry5.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry5.delete(0,"end")
            entry5.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry5.get())
            file.close
            break
        
    for j in entry6.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry6.delete(0,"end")
            entry6.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry6.get())
            file.close
            break
        
    for j in entry8.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry8.delete(0,"end")
            entry8.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry8.get())
            file.close
            break
        
    for j in entry9.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry9.delete(0,"end")
            entry9.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry9.get())
            file.close
            break
        
    for j in entry11.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry11.delete(0,"end")
            entry11.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry11.get())
            file.close
            break
        
    for j in entry12.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry12.delete(0,"end")
            entry12.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry12.get())
            file.close
            break
        
    for j in entry14.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry14.delete(0,"end")
            entry14.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry14.get())
            file.close
            break
        
    for j in entry15.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry15.delete(0,"end")
            entry15.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry15.get())
            file.close
            break
        
    for j in entry16.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry16.delete(0,"end")
            entry16.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry16.get())
            file.close
            break



    for j in entry17.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry17.delete(0,"end")
            entry17.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry17.get())
            file.close
            break
        
    file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    file.write(entry3.get())
    file.close
    file=open(path+"Cold_call_metting_set_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    file.write(entry4.get())
    file.close
    file=open(path+"Cold_call_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    file.write(entry5.get())
    file.close
    file=open(path+"Cold_call_revenue_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    file.write(entry6.get())
    file.close
    file=open(path+"Cold_e_mail_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    file.write(entry8.get())
    file.close
    file=open(path+"Cold_e_mail_metting_set_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    file.write(entry9.get())
    file.close
    file=open(path+"Cold_e_mail_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    file.write(entry11.get())
    file.close
    file=open(path+"Cold_e_mail_revenue_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    file.write(entry12.get())
    file.close
    file=open(path+"Cold_Massiging_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    file.write(entry14.get())
    file.close 
    file=open(path+"Cold_Massiging_metting_set_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    file.write(entry15.get())
    file.close 
    file=open(path+"Cold_Massiging_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    file.write(entry16.get())
    file.close
    file=open(path+"Cold_Massiging_revenue_"+str(entry1.get())+"_"+str(entry2.get()),"w")
    file.write(entry17.get())
    file.close
    
    if int(entry2.get()) >12  :
        messagebox.showinfo("Error", "invalid input Only Can Chosse Month From 1 To 12")
        os.remove(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_call_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_call_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_call_revenue_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_e_mail_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_e_mail_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_e_mail_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_e_mail_revenue_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_Massiging_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_Massiging_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_Massiging_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_Massiging_revenue_"+str(entry1.get())+"_"+str(entry2.get()))                    
        
    if int(entry2.get())<1:
        messagebox.showinfo("Error", "invalid input Only Can Chosse Month From 1 To 12")
        os.remove(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_call_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_call_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_call_revenue_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_e_mail_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_e_mail_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_e_mail_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_e_mail_revenue_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_Massiging_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_Massiging_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_Massiging_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
        os.remove(path+"Cold_Massiging_revenue_"+str(entry1.get())+"_"+str(entry2.get()))
    
    for j in entry2.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            os.remove(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_call_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_call_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_call_revenue_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_revenue_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_revenue_"+str(entry1.get())+"_"+str(entry2.get()))  
            os.remove(path+"Cold_Massiging_revenue_"+str(entry1.get())+"_"+str(entry2.get()))                    
                  
            break


    for j in entry1.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            os.remove(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_call_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_call_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_call_revenue_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_revenue_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_revenue_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_revenue_"+str(entry1.get())+"_"+str(entry2.get()))                    
                    
            break

        if entry2.get() >12  :
            messagebox.showinfo("Error", "invalid input Only Can Chosse Month From 1 To 12")
            os.remove(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_call_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_call_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_call_revenue_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_revenue_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_revenue_"+str(entry1.get())+"_"+str(entry2.get()))                    
        
        if entry2.get()<1:
            messagebox.showinfo("Error", "invalid input Only Can Chosse Month From 1 To 12")
            os.remove(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_call_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_call_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_call_revenue_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_e_mail_revenue_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_attempets_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_metting_set_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_clined_closed_"+str(entry1.get())+"_"+str(entry2.get()))
            os.remove(path+"Cold_Massiging_revenue_"+str(entry1.get())+"_"+str(entry2.get()))



def button4_back():
    
    for j in entry19.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry19.delete(0,"end")
            entry19.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry19.get())
            file.close
            entry23.delete(0,"end")
            break
        
    for j in entry20.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry20.delete(0,"end")
            entry20.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry20.get())
            file.close
            entry23.delete(0,"end")
            break
        
    for j in entry21.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry21.delete(0,"end")
            entry21.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry21.get())
            file.close
            entry23.delete(0,"end")
            break
        
    for j in entry22.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry22.delete(0,"end")
            entry22.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry22.get())
            file.close
            entry23.delete(0,"end")
            break
    
    
    
    entry19.delete(0,"end")
    entry19.insert(10,int(entry3.get())+int(entry8.get())+int(entry14.get()))
    entry20.delete(0,"end")
    entry20.insert(10,int(entry4.get())+int(entry9.get())+int(entry15.get()))
    entry21.delete(0,"end")
    entry21.insert(10,int(entry5.get())+int(entry11.get())+int(entry16.get()))
    entry22.delete(0,"end")
    entry22.insert(10,int(entry6.get())+int(entry12.get())+int(entry17.get()))
    value=int(entry21.get())/int(entry19.get())*100
    entry23.delete(0,"end")
    entry23.insert(10,str(value)+"%")

   
    

def calc1():
    

    
    for j in entry3.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry3.delete(0,"end")
            entry3.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry3.get())
            file.close
            entry7.delete(0,"end")
            break
        
    for j in entry4.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry4.delete(0,"end")
            entry4.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry4.get())
            file.close
            entry7.delete(0,"end")
            break
        
    for j in entry5.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry5.delete(0,"end")
            entry5.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry5.get())
            file.close
            entry7.delete(0,"end")
            break
        
    for j in entry6.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry6.delete(0,"end")
            entry6.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry6.get())
            file.close
            entry7.delete(0,"end")
            break
        
        
    percent1=int(entry5.get())
    percent2=int(entry3.get())
    result=percent1/percent2*100
    entry7.delete(0,"end")
    entry7.insert(10,str(result)+"%")
    

def calc2():
    


    for j in entry8.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry8.delete(0,"end")
            entry8.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry8.get())
            file.close
            entry13.delete(0,"end")
            break
        
    for j in entry9.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry9.delete(0,"end")
            entry9.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry9.get())
            file.close
            entry13.delete(0,"end")
            break
        
    for j in entry11.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry11.delete(0,"end")
            entry11.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry11.get())
            file.close
            entry13.delete(0,"end")
            break
        
    for j in entry12.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry12.delete(0,"end")
            entry12.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry12.get())
            file.close
            entry13.delete(0,"end")
            break
        
    percent1=int(entry11.get())
    percent2=int(entry8.get())
    result=percent1/percent2*100
    entry13.delete(0,"end")
    entry13.insert(10,str(result)+"%")  
        
def calc3():
  
    
    for j in entry14.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry14.delete(0,"end")
            entry14.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry14.get())
            file.close
            entry18.delete(0,"end")
            break
        
    for j in entry15.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry15.delete(0,"end")
            entry15.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry15.get())
            file.close
            entry18.delete(0,"end")
            break
        
    for j in entry16.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry16.delete(0,"end")
            entry16.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry16.get())
            file.close
            entry18.delete(0,"end")
            break
        
    for j in entry17.get():
        if j in l :
            messagebox.showinfo("Error", "Only Can Input Numbers!")
            entry17.delete(0,"end")
            entry17.insert(0,0)
            file=open(path+"Cold_call_attempets_"+str(entry1.get())+"_"+str(entry2.get()),"w")
            file.write(entry17.get())
            file.close
            entry18.delete(0,"end")
            break

    percent1=int(entry16.get())
    percent2=int(entry14.get())
    result=percent1/percent2*100
    entry18.delete(0,"end")
    entry18.insert(10,str(result)+"%")
    
frame=customtkinter.CTkFrame(master=root,)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label=customtkinter.CTkLabel(master=frame,text="Outreach Tracker",font=("Roborto",24))
label.pack(pady=12)

entry1=customtkinter.CTkEntry(master=frame,placeholder_text="enter the year")
entry1.place(y=65,x=550)
entry2=customtkinter.CTkEntry(master=frame,placeholder_text="enter the month")
entry2.place(x=700,y=65)

label1=customtkinter.CTkLabel(master=frame,text="")
label1.pack(pady=12,padx=10)

button1=customtkinter.CTkButton(master=frame,text="upload",command=button1_back)
button1.place(x=550,y=100)
button6=customtkinter.CTkButton(master=frame,text="new",command=button2_back)
button6.place(x=700,y=100)

label2=customtkinter.CTkLabel(master=frame,text="")
label2.pack(pady=12,padx=10)


entry_label1=customtkinter.CTkLabel(master=frame,text="Cold Call",font=("Roborto",18))
entry_label1.place(y=150,x=80)



entry3=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry3.place(y=190,x=130)

entry3_label=customtkinter.CTkLabel(master=frame,text="attempts:",font=("Roborto",16))
entry3_label.place(y=190,x=60)


entry4=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry4.place(y=240,x=130)
entry4_label=customtkinter.CTkLabel(master=frame,text="meetings set:",font=("Roborto",16))
entry4_label.place(y=240,x=30)



entry5=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry5.place(y=290,x=130)
entry5_label=customtkinter.CTkLabel(master=frame,text="clined closed:",font=("Roborto",16))
entry5_label.place(y=290,x=30)


entry6=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry6.place(y=340,x=130)
entry6_label=customtkinter.CTkLabel(master=frame,text="revenue:",font=("Roborto",16))
entry6_label.place(y=340,x=60)



button2=customtkinter.CTkButton(master=frame,text="Calc",command=calc1)
button2.place(y=400,x=80)
entry7=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry7.place(y=460,x=80)

entry7_label=customtkinter.CTkLabel(master=frame,text="metting to clintes:",font=("Roborto",16))
entry7_label.place(y=430,x=80)

entry_label2=customtkinter.CTkLabel(master=frame,text="Cold E_Mail",font=("Roborto",18))
entry_label2.place(y=150,x=380)



entry8=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry8.place(y=190,x=440)

entry8_label=customtkinter.CTkLabel(master=frame,text="attempts:",font=("Roborto",16))
entry8_label.place(y=190,x=370)


entry9=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry9.place(y=240,x=440)
entry9_label=customtkinter.CTkLabel(master=frame,text="meetings set:",font=("Roborto",16))
entry9_label.place(y=240,x=330)



entry11=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry11.place(y=290,x=440)
entry11_label=customtkinter.CTkLabel(master=frame,text="clined closed:",font=("Roborto",16))
entry11_label.place(y=290,x=330)


entry12=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry12.place(y=340,x=440)
entry12_label=customtkinter.CTkLabel(master=frame,text="revenue:",font=("Roborto",16))
entry12_label.place(y=340,x=360)



button3=customtkinter.CTkButton(master=frame,text="Calc",command=calc2)
button3.place(y=400,x=380)
entry13=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry13.place(y=460,x=380)

entry13_label=customtkinter.CTkLabel(master=frame,text="metting to clintes:",font=("Roborto",16))
entry13_label.place(y=430,x=380)


entry_label3=customtkinter.CTkLabel(master=frame,text="Cold Massiging",font=("Roborto",18))
entry_label3.place(y=150,x=680)

entry14=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry14.place(y=190,x=730)

entry14_label=customtkinter.CTkLabel(master=frame,text="attempts:",font=("Roborto",16))
entry14_label.place(y=190,x=650)


entry15=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry15.place(y=240,x=730)
entry15_label=customtkinter.CTkLabel(master=frame,text="meetings set:",font=("Roborto",16))
entry15_label.place(y=240,x=630)



entry16=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry16.place(y=290,x=730)
entry16_label=customtkinter.CTkLabel(master=frame,text="clined closed:",font=("Roborto",16))
entry16_label.place(y=290,x=630)


entry17=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry17.place(y=340,x=730)
entry17_label=customtkinter.CTkLabel(master=frame,text="revenue:",font=("Roborto",16))
entry17_label.place(y=340,x=650)



button4=customtkinter.CTkButton(master=frame,text="Calc",command=calc3)
button4.place(y=400,x=680)
entry18=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry18.place(y=460,x=680)

entry18_label=customtkinter.CTkLabel(master=frame,text="metting to clintes:",font=("Roborto",16))
entry18_label.place(y=430,x=680)


entry_label4=customtkinter.CTkLabel(master=frame,text="sammary",font=("Roborto",18))
entry_label4.place(y=150,x=1030)

entry19=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry19.place(y=190,x=1080)

entry19_label=customtkinter.CTkLabel(master=frame,text="attempts:",font=("Roborto",16))
entry19_label.place(y=190,x=980)


entry20=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry20.place(y=240,x=1080)
entry20_label=customtkinter.CTkLabel(master=frame,text="meetings set:",font=("Roborto",16))
entry20_label.place(y=240,x=960)



entry21=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry21.place(y=290,x=1080)
entry21_label=customtkinter.CTkLabel(master=frame,text="clined closed:",font=("Roborto",16))
entry21_label.place(y=290,x=960)


entry22=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry22.place(y=340,x=1080)
entry22_label=customtkinter.CTkLabel(master=frame,text="revenue:",font=("Roborto",16))
entry22_label.place(y=340,x=980)




entry23=customtkinter.CTkEntry(master=frame,placeholder_text="0")
entry23.place(y=400,x=1080)

entry23_label=customtkinter.CTkLabel(master=frame,text="metting to clintes:",font=("Roborto",16))
entry23_label.place(y=400,x=950)


button5=customtkinter.CTkButton(master=frame,text="Save",command=button3_back)
button5.place(y=550,x=580)



button7=customtkinter.CTkButton(master=frame,text="sammary",command=button4_back)
button7.place(y=450,x=1030)


root.mainloop()


