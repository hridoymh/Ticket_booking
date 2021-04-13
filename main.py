from tkinter import *
import sqlite3








class Train:
    def __init__(self,name):
        self.name = name
        self.seats = list()
        for i in range(25):
            self.seats.append([0,0,0,0])

    def check(self,c):
        for i in range(25):
            if self.seats[i][c] == 0:
                sl[i].config(bg="#90ee90")
            else:
                sl[i].config(bg="#de1738")

    def book(self,coach,s1,s2,s3,s4):
        if s1!=0:
            s1= s1-1
            self.seats[s1][coach]=1
        if s2 != 0:
            s2 = s2 - 1
            self.seats[s2][coach] = 1
        if s3 != 0:
            s3 = s3 - 1
            self.seats[s3][coach] = 1
        if s4 != 0:
            s4 = s4 - 1
            self.seats[s4][coach] = 1

ban = Train("BANALATA")
pad = Train("PADMA")




def tck():
    tn.config(text="%s(%s)" % (tSelect.get(), cSelect.get()))
    c = 0
    if cSelect.get()=="B":
        c = 1
    elif cSelect.get()=="C":
        c=2
    elif cSelect.get()=="D":
        c=3


    if tSelect.get()=="BANALATA":
        ban.check(c)
    else:
        pad.check(c)





def book():

    c = 0
    if cSelect.get() == "B":
        c = 1
    elif cSelect.get() == "C":
        c = 2
    elif cSelect.get() == "D":
        c = 3

    if tSelect.get()=="BANALATA":
        ban.book(c,seat1.get(),seat2.get(),seat3.get(),seat4.get())
        ban.check(c)
    else:
        pad.book(c,seat1.get(),seat2.get(),seat3.get(),seat4.get())
        pad.check(c)

    msg()


def msg():
    msg_w = Tk()
    msg_w.title("Congratulation!")
    
    Label(msg_w,text="Congratulation! Your ticket/s are booked successfully.").pack()
    Label(msg_w, text=" ").pack()
    Label(msg_w, text="Train: "+tSelect.get()).pack()
    Label(msg_w, text="Coach: "+cSelect.get()).pack()
    Label(msg_w, text="Seat Range: "+str(seat1.get())+","+str(seat2.get())+","+str(seat3.get())+","+str(seat4.get())).pack()
    Label(msg_w, text="Phone: "+phone.get()).pack()
    Label(msg_w, text=" ").pack()


    msg_w.mainloop()




root = Tk()
root.title("Ticket booking.")
icon = PhotoImage(file="train.png")
root.iconphoto(False,icon)

h=600
w=900

root.geometry("%dx%d" % (w,h))
root.resizable(0,0)




topF = Frame(root,bg="#f08080",height=100,width=900)
topF.pack(side=TOP)

header = Label(topF,text="Book Your Ticket",font="Arial 20 bold",)
header.place(x=320,y=25)




leftF = Frame(root,bg="gray",height=500,width=400)
leftF.pack(side=LEFT)

tn = Label(leftF,text="Train Name(X)",font="Arial 10 bold")
tn.place(x=120,y=20)

tFrame = Frame(leftF,bg="white",height=420,width=300)
tFrame.place(x=50,y=60)


sl = list()

for i in range(6):
    n=i+1
    y0 = 10
    g = 70

    sl.append(Button(tFrame,text=str(i*4+1),bd=2, height=2, width=5,state="disabled"))
    sl[-1].place(x=10,y=y0+ g*i)
    sl.append(Button(tFrame,text=str(i*4+2),bd=2, height=2, width=5,state="disabled"))
    sl[-1].place(x=60,y=y0+ g*i)
    sl.append(Button(tFrame,text=str(i*4+3),bd=2, height=2, width=5,state="disabled"))
    sl[-1].place(x=190,y=y0+ g*i)
    sl.append(Button(tFrame,text=str(i*4+4),bd=2, height=2, width=5,state="disabled"))
    sl[-1].place(x=240,y=y0+ g*i)


sl.append(Button(tFrame,text=str(25),bd=2, height=2, width=5,state="disabled"))
sl[-1].place(x=125,y=360)



tSelect = StringVar()
tSelect.set("Select")
cSelect = StringVar()
cSelect.set("Select")

rightF = Frame(root,bg="white",height=500,width=500)
rightF.pack(side=RIGHT)

r_head = Label(rightF, text="Enter your Info",font="Arial 15 bold")
r_head.place(x=150,y=20)

tl = Label(rightF,text="Train:",font="Arial 10 bold")
tl.place(x=100,y=100)
tDrop = OptionMenu(rightF,tSelect,"BANALATA", "PADMA")
tDrop.place(x=200,y=100)

cl = Label(rightF,text="Coach:",font="Arial 10 bold")
cl.place(x=100,y=150)
cDrop = OptionMenu(rightF,cSelect,"A", "B","C","D")
cDrop.place(x=200,y=150)

tsrc = Button(rightF,text="Check", command=tck)
tsrc.place(x=150,y=190)


seat1 = IntVar()
seat2 = IntVar()
seat3 = IntVar()
seat4 = IntVar()

cl = Label(rightF,text="Seat:",font="Arial 10 bold")
cl.place(x=100,y=250)
cDrop = OptionMenu(rightF,seat1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
cDrop.place(x=200,y=250)
cDrop = OptionMenu(rightF,seat2,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
cDrop.place(x=250,y=250)
cDrop = OptionMenu(rightF,seat3,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
cDrop.place(x=300,y=250)
cDrop = OptionMenu(rightF,seat4,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
cDrop.place(x=350,y=250)

nl = Label(rightF,text="Name:",font="Arial 10 bold")
nl.place(x=100,y=300)

name_e = Entry(rightF)
name_e.place(x=200,y=300)

pl = Label(rightF,text="Phone:",font="Arial 10 bold")
pl.place(x=100,y=350)

phone = Entry(rightF)
phone.place(x=200,y=350)

bookb = Button(rightF,text="Book", command=book)
bookb.place(x=150,y=400)




root.mainloop()