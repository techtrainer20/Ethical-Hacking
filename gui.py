import socket
from tkinter import *

window=Tk()

window.configure(bg="green")

w=window.winfo_screenwidth();
h=window.winfo_screenheight();
window.geometry("%dx%d+0+0"%(w,h))

def portscanner():
    host =(e1.get())
    port = int(e2.get())
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if sock.connect_ex((host,port)):
        print("port {} is closed".format(port))
        messageVar = Message(window,text = "port {} is closed".format(port),bg="red")
        messageVar.config(bg="blue")
        messageVar.place(x="300",y="200")
    else:
        print("port {} is opened".format(port))
        messageVar = Message(window,text = "port {} is open".format(port),bg="red")
        messageVar.config(bg="blue")
        messageVar.place(x="300",y="200")
        
e3=Label(window,text="VICKY ANGRY IP SCANNER",bg="yellow")
e3.place(x="200",y="80")
f1 = Label(window,text="Enter the Target IP:")
f1.place(x="90",y="100")
e1 = Entry(window)
e1.place(x="200",y="100")
f2 = Label(window,text="Enter the PORT Number:")
f2.place(x="50",y="150")
e2 = Entry(window)
e2.place(x="200",y="150")
##port = int(input("Enter the port Number:"))

b=Button(window,text="SCAN",command=portscanner)
b.place(x="250",y="200")
#portscanner(port)
window.mainloop()
