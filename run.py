#CODED BY RHG1954
#GMAIL:ryangraichi255@gmail.com


#################### MPORTS ##############################
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from tkinter import messagebox
########################## GUI ###########################

root=Tk()
root.title("BOOT SPEAK")
root.geometry("600x600+350+60")
root.resizable(False,False)
root.configure(bg="#305065")



engine = pyttsx3.init()


def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if (text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
            
        else:
            engine.setProperty('rate', 60)
            setvoice()

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text , 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text , 'text.mp3')
            engine.runAndWait()
    if (text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()



    
def para():
    messagebox.showinfo("BOOT ", "PERSONAL INFORMATION \n NAME:RYAN GRAICHI \n AGE : 19 ANS \n\n\n NAME PROGRAME: BOOT SPEAK \n DATE CREATED: 2022-02-24 \n ORIGINAL PROGRAME \n CONTACT ME \n\n\n WEBSITE https://hack-tools-shop.blogspot.com \n FB RHG OR RYANGRAICHI \n GMAIL rayanegraichi15@gmail.com \n\n Numiro: 0553827690 THANKS FOR DOWNLOADING THE PROGRAME")






######################## ICON ######################

image_icon=PhotoImage(file="DATA/R/speak.png")
root.iconphoto(False,image_icon)


######################### TOP FRAME ##################

Top_frame=Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file="DATA/R/speaker logo.png")
Label(Top_frame,image=Logo,bg="white").place(x=10,y=5)


Label(Top_frame,text="BOOT SPEAK",font="arial 15 bold",bg="white",fg="black").place(x=100,y=30)

###########
text_area=Text(root,font="Robot 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=580,height=250)



Label(root,text="VOICE",font="arial 14 bold",bg="#305065",fg="white").place(x=50,y=470)
Label(root,text="SPEED",font="arial 14 bold",bg="#305065",fg="white").place(x=200,y=470)
Label(root,text="SPEAK",font="arial 14 bold",bg="#305065",fg="white").place(x=350,y=470)
Label(root,text="DWONLOAD",font="arial 14 bold",bg="#305065",fg="white").place(x=450,y=470)

Label(root,text="                                                                ",font="arial 10 bold",bg="white",fg="black").place(x=350,y=580)
Label(root,text="                                                                ",font="arial 10 bold",bg="white",fg="black").place(x=0,y=580)

Label(root,text="CODED BY RHG",font="arial 10 bold",bg="white",fg="black").place(x=250,y=580)


gender_combobox=Combobox(root,values=['MALE','Famale'],font="arial 10",state='r',width=10)
gender_combobox.place(x=50,y=500)
gender_combobox.set('Male')

speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 10",state='r',width=10)
speed_combobox.place(x=200,y=500)
speed_combobox.set('Normal')


on=PhotoImage(file="DATA/R/speak.png")
button=Button(root,image=on,bd=0,bg="#305065",activebackground="white",command=speaknow)
button.pack(padx=50,pady=50)
button.place(x=365,y=491)

off=PhotoImage(file="DATA/R/download.png")
button2=Button(root,image=off,bd=0,bg="#305065",activebackground="white",command=download)
button2.pack(padx=50,pady=50)
button2.place(x=480,y=491)


image8=PhotoImage(file="DATA/R/5.png")
pause=Button(root,image=image8,bd=0,bg="#fff", command = para)
pause.place(x=520,y=30)






root.mainloop()
