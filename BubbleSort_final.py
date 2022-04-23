from random import randint
from tkinter import DISABLED
from compare import compare_algorithms
import matplotlib.pyplot as plt
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
def bubbleSort(A):
    steps=0
    for j in range(0, len(A)):
        steps+=1
        for i in range (0, len(A) - 1):
            steps+=1
            if A[i] > A[i+1]:
                steps+=3
                swap = A[i]
                A[i] = A[i+1]
                A[i+1] = swap
    return steps
def get_steps():
    temp=readFile()
    n=10
    for z in range (0,10000):
        if n >=3000:
            break
        for i in range (0,n):
            s = temp[i]
            arr_n.append(s)
        count=bubbleSort(arr_n)
        x.append(n)
        y.append(count)
        n+=50
        arr_n.clear() 
    return x,y
def get_bubble_notation():
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
def plot_bubble_steps():
    temp=readFile()
    n=10
    for z in range (0,10000):
        if n >=3000:
            break
        for i in range (0,n):
            s = temp[i]
            arr_n.append(s)
        count=bubbleSort(arr_n)
        x.append(n)
        y.append(count)
        n+=50
        arr_n.clear()
    plt.plot(x,y,label='BubbleSort Steps')
    plt.xlabel("n")
    plt.ylabel("f(n)")
    plt.legend()
    plt.show()     
    x.clear()
    y.clear()
def plot_bubble_steps_notation() :
    x,y = get_steps()
    x_time,y_time =get_bubble_notation()
    plt.plot(x,y,label='BubbleSort steps') 
    plt.plot(x_time, y_time , label='BubbleSort Notation O(n^2)')
    plt.title('BubbleSort')
    plt.xlabel("n")
    plt.ylabel("f(n)")
    plt.legend()
    plt.show()
    x1.clear()
    y1.clear()
def compare_bubble(btn):
    x,y = get_steps()
    name='BubbleSort steps'
    compare_algorithms(x,y,name)
    btn.config(state=DISABLED)