from os import read, startfile, times
from tkinter import DISABLED
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np
from random import randint
from compare import compare_algorithms
rand_array = [] #large array that holds 10,000 numbers
arr_n = [] # small array will be varying in size
x =[] # array to hold the numbers on x-axis
y =[] #array to hold steps on y-axis
x1=[] #array to hold numbers on x_axis
y1=[] #array to hold notation on y-axis
name='' # indicates name of sorting algorithm
def Generate_randomArray(): #generate random numbers & put them in array     
    for i in range(10000):
        rand_array.append(randint(1,1000))       
def writeInfile(): #put the array values and save them in file
    filerandom= open("random1.txt","w")
    for i in range (10000):
        filerandom.write(rand_array)
        filerandom.write("\n")
    filerandom.close()
def readFile():
    fileObj = open("random1.txt", "r")  # opens the file in read mode 
    words = fileObj.read().splitlines()  # puts the file into an array fileObj.close()
    return words    
def selection_sort(lst):
    count=0
    n = len(lst)
    for i in range(n - 1):
        min = i
        count+=2
        for j in range(i + 1, n):
            if(lst[j] < lst[min]):
                min = j
                count+=2        
        lst[i], lst[min] = lst[min], lst[i]
        count+=1
    return count
def get_steps():
    temp=readFile()
    n=10
    for z in range (0,10000):
        if n >=3000:
            break
        for i in range (0,n): #reading data from file and append in small array
            s = temp[i]
            arr_n.append(s)
        count=selection_sort(arr_n)
        x.append(n)
        y.append(count)
        n+=50
        arr_n.clear()
    return x,y
def plot_selection_steps():
    temp=readFile()
    n=10
    for z in range (0,10000):
        if n >=3000:
            break
        for i in range (0,n): #reading data from file and append in small array
            s = temp[i]
            arr_n.append(s)
        count=selection_sort(arr_n)
        x.append(n)
        y.append(count)
        n+=50
        arr_n.clear()
    plt.plot(x,y,label='SelectionSort Steps')
    plt.xlabel("n")
    plt.ylabel("f(n)")
    plt.legend()
    plt.show()
    x.clear()
    y.clear()
def get_selection_notation():
    n=10
    for z in range (0,10000):
        if n >=3000:
            break
        x1_time=n
        y1_time=pow(n, 2)
        x1.append(x1_time)
        y1.append(y1_time)
        n+=50 
    return x1,y1
    
def plot_selection_steps_notation() :
    x,y = get_steps()
    x_time,y_time =get_selection_notation()
    plt.plot(x,y,label='Selection steps ') 
    plt.plot(x_time, y_time , label='Selection Notation O(n^2)')
    plt.title('SelectionSort')
    plt.xlabel("n")
    plt.ylabel("f(n)")
    plt.legend()
    plt.show()
    x1.clear()
    y1.clear()
    
def compare_selection(btn):
    x,y = get_steps()
    name='SelectionSort steps'
    compare_algorithms(x,y,name)
    btn.config(state=DISABLED)
