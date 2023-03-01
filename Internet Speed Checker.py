#pip install tk,
#pip install speedtest-cli

from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+" Mbps"
    up = str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp=Tk()
sp.title("Internet Speed Meter")
sp.geometry("400x400")
sp.config(bg="white")   

lab = Label(sp,text="Internet Speed Test",font=("Algerian",20,"bold"),fg="Red",bg="white")
lab.place(x=50,y=40,height=30,width=300)

lab = Label(sp,text="Download Speed",font=("Time New Roman",16,"bold"),fg="Blue",bg="white")
lab.place(x=50,y=90,height=30,width=300)

lab_down = Label(sp,text="00",font=("Time New Roman",20,"bold"),fg="Red",bg="white")
lab_down.place(x=50,y=130,height=30,width=300)

lab = Label(sp,text="Upload Speed",font=("Time New Roman",16,"bold"),fg="Blue",bg="white")
lab.place(x=50,y=180,height=30,width=300)

lab_up = Label(sp,text="00",font=("Time New Roman",20,"bold"),fg="Red",bg="white")
lab_up.place(x=50,y=220,height=30,width=300)

button = Button(sp,text="Check Speed",font=("Aldhabi",20,"bold"),fg="Red",bg="Yellow",relief=RAISED,command=speedcheck)
button.place(x=50,y=280,height=30,width=300)

sp.mainloop()