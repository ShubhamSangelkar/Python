#pip install tk
#pip install os-sys

from tkinter import *
import os 

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")

st =Tk()
st.title("ShutDown App")
st.geometry("400x400")
st.config(bg="Red")

#Restart
A=Button(st,text="Restart",font=("Time New Roman",25,"bold"),relief=RAISED,cursor="plus",
    command=restart)
A.place(x=125,y=50,height=50,width=150)

#Restart Time
B=Button(st,text="Restart Time",font=("Time New Roman",25,"bold"),relief=RAISED,cursor="plus",
    command=restart_time)
B.place(x=95,y=130,height=50,width=210)

#Log-Out
C=Button(st,text="Log-Out",font=("Time New Roman",25,"bold"),relief=RAISED,cursor="plus",
    command=logout)
C.place(x=110,y=210,height=50,width=170)

#ShutDown
C=Button(st,text="ShutDown",font=("Time New Roman",25,"bold"),relief=RAISED,cursor="plus",
    command=shutdown)
C.place(x=110,y=300,height=50,width=170)


st.mainloop()
