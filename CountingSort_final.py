from os import read, startfile, times
from tkinter import DISABLED
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import random
from random import randint
from compare import compare_algorithms
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

def countingSort(arr, exp1): 
    step=0
    n = len(arr) 
    
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
    
    # initialize count array as 0 
    count = [0] * (10) 
    step+=3
    
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (int(arr[i])/exp1) 
        count[int((index)%10)] += 1
        step+=3
    
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
        step+=1
    
    # Build the output array 
    i = n-1
    step+=1
    while i>=0: 
        index = (int(arr[i])/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[int((index)%10)] -= 1
        i -= 1
        step+=3
    
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    step+=1
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
        step+=1
    return step
def get_steps():
    temp1=readFile()
    n=10
    exp=1
    for z in range (0,10000):
        if n >=3000:
            break
        for i in range (0,n):
            s = temp1[i]
            arr_n.append(s)
        count=countingSort(arr_n,exp)
        x.append(n)
        y.append(count)
        n+=50
        arr_n.clear()
        
    return x,y

def get_counting_notation():
    n=10
    for z in range (0,10000):
        if n >=3000:
            break 
        x1_time=n
        y1_time=n+1000 # 1000 is highest random number can be reached
        x1.append(x1_time)
        y1.append(y1_time)
        n+=50  
    return x1,y1
def plot_counting_steps():
    exp=1
    temp=readFile()
    n=10
    for z in range (0,10000):
        if n >=3000:
            break
        for i in range (0,n): #reading data from file and append in small array
            s = temp[i]
            arr_n.append(s)
        count=countingSort(arr_n,exp)
        x.append(n)
        y.append(count)
        n+=50
        arr_n.clear()
    plt.plot(x,y,label='CountingSort Steps')
    plt.xlabel("n")
    plt.ylabel("f(n)")
    plt.legend()
    plt.show()    
    x.clear()
    y.clear()
def plot_counting_steps_notation() :
    x,y = get_steps()
    x_time,y_time =get_counting_notation()
    plt.plot(x,y,label='CountingSort steps ') 
    plt.plot(x_time, y_time , label='CountingSort Notation')
    plt.title('CountingSort')
    plt.xlabel("n")
    plt.ylabel("f(n)")
    plt.legend()
    plt.show()
    x1.clear()
    y1.clear()
def compare_counting(btn):
    x,y = get_steps()
    name='CountingSort steps'
    compare_algorithms(x,y,name)
    btn.config(state=DISABLED)