import random
from random import randint
from tkinter import DISABLED
import matplotlib.pyplot as plt
import math
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

def merge(arr, l, m, r):
    count=0
    n1 = m - l + 1
    n2 = r - m
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
        count+=1
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        count+=1
        
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            count+=2
        else:
            arr[k] = R[j]
            j += 1
            count+=1
        k += 1
        count+=1
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        count+=3
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        count+=3
# l is for left index and r is right index of the
# sub-array of arr to be sorted
    return count
 
def mergeSort(arr, l, r):
    count=0
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
        # Sort first and second halves
        count=mergeSort(arr, l, m)
        count+=mergeSort(arr, m+1, r)
        count+=merge(arr, l, m, r)
    return count

def get_steps():
    n=10
    temp=readFile()
    for z in range (0,10000):
        arr_n.clear()
        if n >=3000:
            break
        for i in range (0,n):
            s = temp[i]
            arr_n.append(s)     
        count=mergeSort(arr_n,0,n-1)
        x.append(n)
        y.append(count)
        n+=50
        arr_n.clear()
    return x,y
def get_merge_notation():
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
def plot_merge_steps():
    temp=readFile()
    n=10
    for z in range (0,10000):
        if n >=3000:
            break
        for i in range (0,n): #reading data from file and append in small array
            s = temp[i]
            arr_n.append(s)
        count=mergeSort(arr_n,0,n-1)
        x.append(n)
        y.append(count)
        n+=50
        arr_n.clear()
    plt.plot(x,y,label='MergeSort Steps')
    plt.xlabel("n")
    plt.ylabel("f(n)")
    plt.legend()
    plt.show()
    x.clear()
    y.clear()
def plot_merge_steps_notation():
    x,y = get_steps()
    x_time,y_time =get_merge_notation()
    plt.plot(x,y,label='Merge steps ') 
    plt.plot(x_time, y_time , label='Merge Notation O(nlgn)')
    plt.title('MergeSort')
    plt.xlabel("n")
    plt.ylabel("f(n)")
    plt.legend()
    plt.show()
    x1.clear()
    y1.clear()
def compare_mergee(btn):
    x,y = get_steps()
    name = 'MergeSort steps'
    compare_algorithms(x,y,name)
    btn.config(state=DISABLED)
   