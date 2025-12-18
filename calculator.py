# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 20:19:27 2025

@author: Binu
"""

import tkinter as tk
from tkinter import Entry
#disp_var=None

disp_var=None    
first=None
oper=None

def button_click(num):
    current=disp_var.get()
    disp_var.set(current+str(num))
def button_clear():
    disp_var.set("")
def operation(op):
    global first, oper
    first=float(disp_var.get())
    oper=op
    disp_var.set("")
def equal():
    global first,oper
    second=float(disp_var.get())
    if oper=='+':
        result=first+second
    elif oper=='-':
        result=first-second
    elif oper=='*':
        result=first*second
    elif oper=='/':
        result=first/second
    else:
        result=first**second
    disp_var.set(str(result))

# Create window    
window=tk.Tk()
window.geometry('300x400')
window.title('Basic Calculator')
disp_var=tk.StringVar()    

# Input section
inp=Entry(window,width=30,borderwidth=5,justify='right',textvariable=disp_var)
inp.pack()

# Numbers and operators
b=tk.Button(window,text='1',width="10",command=lambda:button_click(1))
b.pack()
b.place(x=20,y=40)
b=tk.Button(window,text='2',width="10",command=lambda:button_click(2))
b.pack()
b.place(x=100,y=40)
b=tk.Button(window,text='3',width="10",command=lambda:button_click(3))
b.pack()
b.place(x=180,y=40)
b=tk.Button(window,text='4',width="10",command=lambda:button_click(4))
b.pack()
b.place(x=20,y=65)
b=tk.Button(window,text='5',width="10",command=lambda:button_click(5))
b.pack()
b.place(x=100,y=65)
b=tk.Button(window,text='6',width="10",command=lambda:button_click(6))
b.pack()
b.place(x=180,y=65)
b=tk.Button(window,text='7',width="10",command=lambda:button_click(7))
b.pack()
b.place(x=20,y=90)
b=tk.Button(window,text='8',width="10",command=lambda:button_click(8))
b.pack()
b.place(x=100,y=90)
b=tk.Button(window,text='9',width="10",command=lambda:button_click(9))
b.pack()
b.place(x=180,y=90)
b=tk.Button(window,text='0',width="10",command=lambda:button_click(0))
b.pack()
b.place(x=20,y=115)
b=tk.Button(window,text='.',width="10",command=lambda:button_click('.'))
b.pack()
b.place(x=100,y=115)
b=tk.Button(window,text='+',width="10",command=lambda:operation("+"))
b.pack()
b.place(x=180,y=115)
b=tk.Button(window,text='-',width="10",command=lambda:operation("-"))
b.pack()
b.place(x=20,y=140)
b=tk.Button(window,text='*',width="10",command=lambda:operation("*"))
b.pack()
b.place(x=100,y=140)
b=tk.Button(window,text='/',width="10",command=lambda:operation("/"))
b.pack()
b.place(x=180,y=140)
b=tk.Button(window,text='^',width="10",command=lambda:operation("^"))
b.pack()
b.place(x=20,y=165)
b=tk.Button(window,text='C',width="10",command=button_clear)
b.pack()
b.place(x=100,y=165)
b=tk.Button(window,text='=',width="10",command=equal)
b.pack()
b.place(x=180,y=165)

window.mainloop()