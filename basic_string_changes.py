# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:07:55 2016

@author: Olivia
"""
student_email,student_id,student_name="odorencz@bu.edu","U04947088","Olivia Dorencz"

                  
def dashify(x):                                         #dashify
    for z in range(len(x)-1):
        print(x[z],"- " ,end='')                        #add dashes between letters
    for z in range((len(x)-1),len(x)):                  #final dash
        print(x[z])




def ishappy(h):    
    release=("1","4")                               #1 is goal and 4 indicates cycling
    b=str(sum((int(x)**2 for x in str(h))))         #sum of digits squared
    while b not in release:
        release += tuple(b)
        return(ishappy(b))                          #adds number to release 
    if b in release:                                #if in release either cycling or 1
        if int(b)==1:
            return("true")                          #happy
        else:
            return("false")                         #not happy



def perfect(p):
    number=int(p)                                   #convert given from str to int
    maboi=list([1])                                 #list of factors
    for i in range(1,number):
        y=(number/i)                                #divides number by all numbers beneath it
        z=y-round(y)                                #check for integer as result
        if z==0 and y!=number:                      #include factors does not include number
            maboi.append(y)
        else:
            pass
    if sum(maboi)==number:
        return("true")
    else:
        return("false")                              


    
def pyramid(s):
    height=int(s)                                       #convert from str to int
    b=height-height+1                                   #*'s per row
    while b<=(2*height-1):
        print(" "*(height-b//2),"*"*b)                  #prints rows
        b=b+2

