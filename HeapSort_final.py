import random
from random import randint
from tkinter import DISABLED
import matplotlib.pyplot as plt
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
def heapify(arr, n, i ):
    count=0
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
    count+=3
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
        count+=1
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
        count+=1
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        count+=1
        # Heapify the root.
        count+=heapify(arr, n, largest)
    return count      

# The main function to sort an array of given size


def heapSort(arr):
    count=0
    n = len(arr)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        count+=heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        count+=heapify(arr, i, 0)
    return count
def get_steps():
    temp=readFile()
    n=10
    for z in range (0,10000):
        if n >=3000:
            break
        for i in range (0,n):
            s = temp[i]
            arr_n.append(s)
        count=heapSort(arr_n)
        x.append(n)
        y.append(count)
        n+=50
        arr_n.clear()   
    return x,y
def get_heap_notation():
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
def plot_heap_steps():
    temp=readFile()
    n=10
    for z in range (0,10000):
        if n >=3000:
            break
        for i in range (0,n): #reading data from file and append in small array
            s = temp[i]
            arr_n.append(s)
        count=heapSort(arr_n)
        x.append(n)
        y.append(count)
        n+=50
        arr_n.clear()
    plt.plot(x,y,label='HeapSort Steps')
    plt.xlabel("n")
    plt.ylabel("f(n)")
    plt.legend()
    plt.show()
    x.clear()
    y.clear()
def plot_heap_steps_notation():
    x,y=get_steps()
    x_time,y_time=get_heap_notation()
    plt.plot(x,y,label='Heap steps') 
    plt.plot(x_time, y_time , label='Heap Notation O(nlgn)')
    plt.title('HeapSort')
    plt.xlabel("n")
    plt.ylabel("f(n)")
    plt.legend()
    plt.show()
    x1.clear()
    y1.clear()
def compare_heap(btn):
    x,y = get_steps()
    name='HeapSort steps'
    compare_algorithms(x,y,name)
    btn.config(state=DISABLED)