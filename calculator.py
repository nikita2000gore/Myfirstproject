import tkinter as tk
from tkinter import *

val=""

def click(number):
    global val
    val = val+str(number)
    data.set(val)
    
def sum():
    global val
    val = str(eval(val))
    data.set(val)

def clear():
    global val
    val=""
    data.set(val)

cal = tk.Tk()
cal.title("Calculator")
cal.geometry("300x500")
cal.resizable(0, 0)

data=tk.StringVar()
label1 = Label(cal,text="Label",anchor=SE,font=("Verdana",20),textvariable=data,background= "#ffffff",fg="#000000")
label1.pack(expand=True,fill="both")

row1 = Frame(cal, bg="#000000")
row1.pack(expand = True, fill="both")

row2 = Frame(cal)
row2.pack(expand = True, fill="both")

row3 = Frame(cal)
row3.pack(expand = True, fill="both")

row4 = Frame(cal)
row4.pack(expand = True, fill="both")


btn1 = Button(row1, text="7",font=("Verdana",22),relief=GROOVE, border=0,command=lambda:click(7))
btn1.pack(side=LEFT, expand= True, fill="both")

btn2 = Button(row1, text="8",font=("Verdana",22),relief=GROOVE, border=0,command=lambda:click(8))
btn2.pack(side=LEFT, expand= True, fill="both")

btn3 = Button(row1, text="9",font=("Verdana",22),relief=GROOVE, border=0,command=lambda:click(9))
btn3.pack(side=LEFT, expand= True, fill="both")

btn4 = Button(row1, text="+",font=("Verdana",22),relief=GROOVE, border=0,command=lambda:click("+"))
btn4.pack(side=LEFT, expand= True, fill="both")



btn1 = Button(row2, text="4",font=("Verdana",22),relief=GROOVE, border=0,command=lambda:click(4))
btn1.pack(side=LEFT, expand= True, fill="both")

btn2 = Button(row2, text="5",font=("Verdana",22),relief=GROOVE, border=0,command=lambda:click(5))
btn2.pack(side=LEFT, expand= True, fill="both")

btn3 = Button(row2, text="6",font=("Verdana",22),relief=GROOVE, border=0,command=lambda:click(6))
btn3.pack(side=LEFT, expand= True, fill="both")

btn4 = Button(row2, text="-",font=("Verdana",22),relief=GROOVE, border=0,command=lambda:click("-"))
btn4.pack(side=LEFT, expand= True, fill="both")



btn1 = Button(row3, text="1",font=("Verdana",22),relief=GROOVE, border=0,command=lambda:click(1))
btn1.pack(side=LEFT, expand= True, fill="both")

btn2 = Button(row3, text="2",font=("Verdana",22),relief=GROOVE, border=0,command=lambda:click(2))
btn2.pack(side=LEFT, expand= True, fill="both")

btn3 = Button(row3, text="3",font=("Verdana",22),relief=GROOVE, border=0,command=lambda:click(3))
btn3.pack(side=LEFT, expand= True, fill="both")

btn4 = Button(row3, text="*",font=("Verdana",22),relief=GROOVE, border=0,command=lambda:click("*"))
btn4.pack(side=LEFT, expand= True, fill="both")



btn1 = Button(row4, text="C",font=("Verdana",22),relief=GROOVE, border=0,command=clear)
btn1.pack(side=LEFT, expand= True, fill="both")

btn2 = Button(row4, text="0",font=("Verdana",22),relief=GROOVE, border=0,command=lambda:click(0))
btn2.pack(side=LEFT, expand= True, fill="both")

btn3 = Button(row4, text="=",font=("Verdana",22),relief=GROOVE, border=0,command=sum)
btn3.pack(side=LEFT, expand= True, fill="both")

btn4 = Button(row4, text="/",font=("Verdana",22),relief=GROOVE, border=0,command=lambda:click("/"))
btn4.pack(side=LEFT, expand= True, fill="both")

cal.mainloop()
