from tkinter import*
from tkinter import Button
import tkinter as tk
from os import read, startfile
from PIL import Image,ImageTk
import matplotlib.pyplot as plt
counter=0
x_axis1 = []
y_axis1 = []
x_axis2 = []
y_axis2 = []
name1=''
name2=''
def compare_algorithms(x,y,name):
    if(counter==0):
        globals()['x_axis1'] = x
        globals()['y_axis1'] = y
        globals()['name1'] = name
        globals()['counter'] += 1
    elif(counter==1): 
        globals()['x_axis2'] = x
        globals()['y_axis2'] = y
        globals()['name2'] = name
        globals()['counter'] += 1
    if(counter==2):
        plt.plot(x_axis1,y_axis1,label=name1)
        plt.plot(x_axis2,y_axis2,label=name2)
        plt.xlabel('n numbers')
        plt.ylabel ('steps taken')
        plt.legend()
        plt.show()
        x_axis1.clear()
        y_axis1.clear()
        x_axis2.clear()
        y_axis2.clear()
        globals()['counter']=0