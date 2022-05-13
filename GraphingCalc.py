
import tkinter as tk
from matplotlib.animation import Animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
import sys

from sqlalchemy import true




#[1]Create our GUI window
root = tk.Tk()
root.title("Graphing Calculator")
root.configure(bg='black')



#[2]Create text_Fileds

#--Function text_field
b_fx=tk.Label(root,text="F(X) =", font='Helvetica 10 bold',padx=8,fg="white",bg="black").grid(row=0,column=0)
e=tk.Entry(root,width=45,borderwidth=5)
e.grid(row=0,column=1,columnspan=5,padx=5,pady=5)
#-------------------------------------------------

#--min(x) text_field
e_min=tk.Entry(root,width=5)
e_min.grid(row=5,column=1)
#--------------------------------------------------

#--max(x) text_field
e_max=tk.Entry(root,width=5)
e_max.grid(row=5,column=3)
Flag=False
#-------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------    Functionalities    ------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

#[3]define functions

def Click_button(Number):
    curr=e.get()
    e.delete(0,tk.END)
    e.insert(0,str(curr)+str(Number))
#--------------------------------------------------------

def CLR():
    e.delete(0,tk.END)
    e_min.delete(0,tk.END)
    e_max.delete(0,tk.END)
    plt.clf()
    plt.close()
    
#--------------------------------------------------------

def Func(op):
    curr=e.get()
    e.delete(0,tk.END)
    e.insert(0,str(curr)+op) 
#--------------------------------------------------------

def f(x):
    y=[]
    test=e.get()
    test=test.replace('^','**').replace(' ','').replace("X","x")    
    try:
        y=(eval(test,{"x":x})) 

    except Exception as error:
        messagebox.showerror("error!",str(error.args[0]))

    return y
#-------------------------------------------------------------------------------------------------------------------

def Validate():
    if not e.get():
        messagebox.showerror("error!","please enter the function first")
        return False
    if not e_min.get():
        messagebox.showerror("error!","enter minimum number of x")
        return False
    if not e_max.get():
        messagebox.showerror("error!","enter maximum number of x")
        return False
    if float(e_min.get())>=float(e_max.get()):
        messagebox.showerror("error!","enter Max(x) greater than Min(x)")
        return False
    return True  
#------------------------------------------------------------------------------------------------------------------- 
def DivByZero(): 
    if ((e.get().find('/x')!=-1 or e.get().find('/X')!=-1) and (float(e_min.get())<=0) and (float(e_max.get())>=0)):
        messagebox.showerror("Alert!","You are dividing by zero")
        return False

    return True  
 #------------------------------------------------------------------------------------------------------------------
def ZeroExp():
    if e.get().find("/(")!=-1:
        st=e.get()[e.get().index("/(")+2:e.get().index(")")]
        xlist=np.arange(float(e_min.get()),float(e_max.get())+.1,.1)
        for i in xlist:
            y=eval(st,{"x":i})
            if(y==0):
                return i   
    return -1

def Calculate():
    if(Validate()):
        if(DivByZero()):
            if ZeroExp()== -1:  #shyaka
                xlist=np.arange(float(e_min.get()),float(e_max.get())+.1,.1)  # .1 space between any two points on x_axis
                ylist=f(xlist)
                plt.plot(xlist,ylist,label=e.get())
            else:
                x1list=np.arange(float(e_min.get()),ZeroExp(),.1)
                x2list=np.arange(ZeroExp(),float(e_max.get())+.1,.1)
                y1list=f(x1list)
                y2list=f(x2list)
                plt.axvline(ZeroExp(), color='red',linestyle="--")
                plt.plot(x1list,y1list,label=e.get()+f" ({ZeroExp()}-)")
                plt.plot(x2list,y2list,label=e.get()+f" ({ZeroExp()}+)")
        else:
            if float(e_min.get())==0:
                xlist=np.arange(0.01,float(e_max.get())+.1,.1)  
                ylist=f(xlist)
                plt.plot(xlist,ylist,label=e.get())    
            
            elif float(e_max.get())==0:
                xlist=np.arange(float(e_min.get()),-0.01+.1,.1)  
                ylist=f(xlist)
                plt.plot(xlist,ylist,label=e.get()) 

            else:    
                x1list=np.arange(float(e_min.get()),0,.1)
                x2list=np.arange(0,float(e_max.get())+.1,.1)
                y1list=f(x1list)
                y2list=f(x2list)
                plt.axvline(0, color='red',linestyle="--")
                plt.plot(x1list,y1list,label=e.get()+" (0-)")
                plt.plot(x2list,y2list,label=e.get()+" (0+)")         

        plt.title('Result')
        plt.xlabel("X")
        plt.ylabel("F(X)")
        plt.axhline(0, color='black',linestyle="--")
        plt.axvline(0, color='black',linestyle="--") 
        plt.legend()
        plt.show()
        

#-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------   ( GUI )    ------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

#[4] Define Buttons

#-For Numbers
b1=tk.Button(root,text="1",font='Helvetica 12 bold',padx=25,pady=9,command=lambda:Click_button(1),fg="black",bg="gray").grid(row=3,column=0)
b2=tk.Button(root,text="2",font='Helvetica 12 bold',padx=25,pady=9,command=lambda:Click_button(2),fg="black",bg="gray").grid(row=3,column=1)
b3=tk.Button(root,text="3",font='Helvetica 12 bold',padx=25,pady=9,command=lambda:Click_button(3),fg="black",bg="gray").grid(row=3,column=2)
#-------------------------------------------------------------------------------------------------------------------
b4=tk.Button(root,text="4",font='Helvetica 12 bold',padx=25,pady=9,command=lambda:Click_button(4),fg="black",bg="gray").grid(row=2,column=0)
b5=tk.Button(root,text="5",font='Helvetica 12 bold',padx=25,pady=9,command=lambda:Click_button(5),fg="black",bg="gray").grid(row=2,column=1)
b6=tk.Button(root,text="6",font='Helvetica 12 bold',padx=25,pady=9,command=lambda:Click_button(6),fg="black",bg="gray").grid(row=2,column=2)
#-------------------------------------------------------------------------------------------------------------------
b7=tk.Button(root,text="7",font='Helvetica 12 bold',padx=25,pady=9,command=lambda:Click_button(7),fg="black",bg="gray").grid(row=1,column=0)
b8=tk.Button(root,text="8",font='Helvetica 12 bold',padx=25,pady=9,command=lambda:Click_button(8),fg="black",bg="gray").grid(row=1,column=1)
b9=tk.Button(root,text="9",font='Helvetica 12 bold',padx=25,pady=9,command=lambda:Click_button(9),fg="black",bg="gray").grid(row=1,column=2)
#-------------------------------------------------------------------------------------------------------------------
b0=tk.Button(root,text="0",font='Helvetica 12 bold',padx=95,pady=8,command=lambda:Click_button(0),fg="black",bg="gray")
b0.grid(row=4,column=0,columnspan=3)
#-------------------------------------------------------------------------------------------------------------------


#-For Fuctionality buttons
b_add=tk.Button(root,text="+",font='Helvetica 12 bold',padx=25,pady=10,command=lambda:Func("+"),fg="black",bg="gray").grid(row=1,column=3)
b_sub=tk.Button(root,text="-",font='Helvetica 12 bold',padx=25,pady=10,command=lambda:Func("-"),fg="black",bg="gray").grid(row=1,column=4)
b_mul=tk.Button(root,text="*",font='Helvetica 12 bold',padx=26.5,pady=10,command=lambda:Func("*"),fg="black",bg="gray").grid(row=2,column=3)
b_div=tk.Button(root,text="/",font='Helvetica 12 bold',padx=25,pady=10,command=lambda:Func("/"),fg="black",bg="gray").grid(row=2,column=4)
b_pow=tk.Button(root,text="^",font='Helvetica 12 bold',padx=25,pady=10,command=lambda:Func("^"),fg="black",bg="gray").grid(row=3,column=3)
b_X=tk.Button(root,text="X",font='Helvetica 12 bold',padx=23,pady=10,command=lambda:Func("x"),fg="blue",bg="gray").grid(row=3,column=4)
b_clr=tk.Button(root,text="Clear",font='Helvetica 10 bold',padx=50,pady=8,command=CLR,fg="red",bg="gray").grid(row=4,column=3,columnspan=2)
#-------------------------------------------------------------------------------------------------------------------

#-For min(x) and max(x)
b_min=tk.Label(root,text="Min(X)=",font='Helvetica 10 bold',fg="white",bg="black",padx=8,pady=10).grid(row=5,column=0)
b_max=tk.Label(root,text="Max(X)=",font='Helvetica 10 bold',fg="white",bg="black",padx=8,pady=10).grid(row=5,column=2)
#--------------------------------------------------------------------------------------------------------------------

#-For Graph Button
b_calc=tk.Button(root,text="Graph",font='Helvetica 12 bold',padx=100,pady=10,command=Calculate,fg="black",bg="gray")
b_calc.grid(row=6,column=0,columnspan=6)
#--------------------------------------------------------------------------------------------------------------------

#End of GUI loop 
root.mainloop()
#--------------
 