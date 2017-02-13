# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:04:48 2016

@author: Olivia
"""

def letters(S):     #question 1
    S=str(S)
    one_each_text= "".join([chr(i) for i in range(ord('a'),ord('a')+26)]) #given. provides alphabet
    lower_upper_text= one_each_text+one_each_text.upper()                   #upper and lower
    lower_upper_text=str(lower_upper_text)                                  
    lowercase=str(S.lower())                                                #everything is lowercase
    letterslist=list()
    for i in one_each_text:
        q=lowercase.count(i)                                                #count each letter
        letterslist.append(int(q))                                          #add to list
    return(letterslist)


def bar_print(L26,height):
    most=max(L26)    
    if most==height:                        #skip scaling
        newletterslist=L26
    else:                                   #scale to height
        j=most/height        
        newletterslist=list()
        for i in L26: 
            z=i/j
            newletterslist.append(int(z))  #new list of scaled numbers
    while height!=0:        
        crazyletters=list()                 #next line goes here
        starstring=str()                    #each individual row
        for i in newletterslist:
            if int(i)==height:              #adds star if value
                starstring += " * "
                crazyletters.append(int(i)-1)
            else:                           #adds space if no value
                starstring += "   "
                crazyletters.append(int(i))
        newletterslist=crazyletters         
        print(starstring)
        height=height-1                     #cycle through all heights
    print(" A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z ")

bar_print(letters("aaaaaskdjfsdkjfskdfjsldkjfds"),12)       

def dot(L1,L2):
    dots=list()    
    a=L1[0]*L2[0]           #each value
    b=L1[1]*L2[1]
    c=L1[2]*L2[2]
    dots.append(a)
    dots.append(b)
    dots.append(c)
    dotproduct=sum(dots)    #dot product 
    return(dotproduct)

def cross(L1,L2):
    crossproduct=list()                 #lists values
    a=L1[1]*L2[2]-L1[2]*L2[1]           #i
    b=-(L1[0]*L2[2]-L1[2]*L2[0])        #j
    c=L1[0]*L2[1]-L1[1]*L2[0]           #k
    crossproduct.append(a)
    crossproduct.append(b)
    crossproduct.append(c)
    return(crossproduct)

def flatten(L):
    newvariables=list()
    for i in L:
        if type(i)==list:
            for j in i:
                newvariables.append(j)      #replace i with values in i
        if type(i)!=list:
            newvariables.append(i)
    for i in newvariables:
        z=type(i)
        typelist=list()
        typelist.append(z)
        typeliststr=str(typelist)       #convert to string to check for "list"
        while "list" in typeliststr:    #cycle until list no longer in list
            return(flatten(newvariables))       
    return(newvariables)        