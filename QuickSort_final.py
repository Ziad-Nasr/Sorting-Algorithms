from tkinter import DISABLED
from matplotlib import pyplot as plt
from random import randint
from compare import compare_algorithms
import math
rand_array = []
x =[]
y =[]
x1=[]
y1=[]
arr_n = []
name=''
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

def partition(start, end, array):
    steps=0
    # Initializing pivot's index to start
    pivot_index = start 
    pivot = array[pivot_index]
    steps+=2
    # This loop runs till start pointer crosses 
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
        
        # Increment the start pointer till it finds an 
        # element greater than  pivot 
        while start < len(array) and array[start] <= pivot:
            start += 1
            steps+=1
        # Decrement the end pointer till it finds an 
        # element less than pivot
        while array[end] > pivot:
            end -= 1
            steps+=1
        
        # If start and end have not crossed each other, 
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
            steps+=1
    
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
    steps+=1
   
    # Returning end pointer to divide the array into 2
    return end,steps
    
# The main function that implements QuickSort 
def quick_sort(start, end, array):
    steps=0
    u=0
    if (start < end):
        
        # p is partitioning index, array[p] 
        # is at right place
        p,u = partition(start, end, array)
        steps+=u 
        # Sort elements before partition 
        # and after partition
        steps+=quick_sort(start, p - 1, array)
        steps+=quick_sort(p + 1, end, array)
    return steps

def get_steps():
    steps=0
    temp=readFile()
    n=10
    for z in range (0,10000):
        if n >=3000:
            break
        for i in range (0,n):
            s = temp[i]
            arr_n.append(s)
        steps=quick_sort(0,n-1,arr_n)
        x.append(n)
        y.append(steps)
        n+=50
        arr_n.clear()
    return x,y
def get_quick_notation():
    n=10
    for z in range (0,10000):
        if n >=3000:
            break
        x1_time=n
        y1_time=n*(math.log2(n))
        x1.append(x1_time)
        y1.append(y1_time)
        n+=50
    return x1,y1
def plot_quick_steps():
    temp=readFile()
    n=10
    for z in range (0,10000):
        if n >=3000:
            break
        for i in range (0,n): #reading data from file and append in small array
            s = temp[i]
            arr_n.append(s)
        count=quick_sort(0,n-1,arr_n)
        x.append(n)
        y.append(count)
        n+=50
        arr_n.clear()
    plt.plot(x,y,label='QuickSort Steps')
    plt.xlabel("n")
    plt.ylabel("f(n)")
    plt.legend()
    plt.show()    
    x.clear()
    y.clear()
def plot_quick_steps_notation() :
    x,y = get_steps()
    x_time,y_time =get_quick_notation()
    plt.plot(x,y,label='Quick steps ') 
    plt.plot(x_time, y_time , label='Quick Notation O(nlgn)')
    plt.title('QuickSort')
    plt.xlabel("n")
    plt.ylabel("f(n)")
    plt.legend()
    plt.show()
    x1.clear()
    y1.clear()
def compare_quick(btn):
    x,y = get_steps()
    name='QuickSort steps'
    compare_algorithms(x,y,name)
    btn.config(state=DISABLED)