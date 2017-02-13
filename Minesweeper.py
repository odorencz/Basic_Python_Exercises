# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 14:29:44 2016

@author: Olivia
"""
import tkinter as tk
import numpy as np
import random
from functools import partial 
import collections

class App:
    
 
    
    def mine(self, gameover):
        gameover.lift()
        print ("sup")    
   
    def notmine(self,dic,inde):
        z=(dic[inde])
        z.grid_remove()
        print("hey")
        
    
    
    def __init__(self, root):
        frame = tk.Canvas(root,width=241,height=280)
        frame.grid(row=0,column=0)
        
        self.label1 = tk.Label(frame, text="Minesweeper")
        self.label1.grid(row = 0, column = 0, columnspan = 10)
        
        
        
        
       
        zlist=[]
        for i in range(10):
            for x in range(10):            
                zlist.append((x+1,i))
        print(zlist)
        random.shuffle(zlist)
        
        
        qlist=sorted(zlist)    
        
        minelist=zlist[:12]
        notminelist=zlist[12:]
        
        zerolist=[]
        
        positionlist=[]
        for i in range(2,102):
            positionlist.append(i)
        
        for i in range(90):
            i=0
            zerolist.append(i)
           
        
        buttondict= dict()
        minedict=dict()
        touchbuttondict=dict()
        minenodict=dict()
        buttonnodict=dict()
        newdict=dict()        
        numberdict=dict()
        otherbuttondict=dict()        
        circlesdict=dict()        
        xdict=dict()        
        
        self.gameover=tk.Label(frame,text= "GAME OVER!", font=("arial bold", 15), bg="red", fg="white", height=2,width=12, relief="ridge", highlightthickness=5,highlightcolor="white") 
        self.gameover.grid(row=5,column=2, rowspan=2, columnspan=6)
       
       
        print(qlist)
        for i in qlist:
            touchbuttondict.update({i: qlist.index(i)})
       
        
        for i in minelist:
            x=i[1]
            y=i[0]
            q=zlist.index(i)
            xmarkk=tk.Label(frame,text="X")
            xmarkk.grid(column=x, row=y)
            
            xmarkk=tk.Label(frame,text="X")
            xmarkk.grid(column=x, row=y)
            
            self.minebtn = tk.Button(frame,width=2,height=1, command=partial(self.mine, self.gameover))
            self.minebtn.grid(column=x, row=y,sticky="nsew")
                     
            
            minedict.update({zlist.index(i) : self.minebtn})
            minenodict.update({self.minebtn : touchbuttondict[i]+1})
           
            xdict.update({zlist.index(i): xmarkk})
        
      
            
        for i in notminelist:
            x=i[1]
            y=i[0]
            self.rect=tk.Canvas(frame, width=28,height=28)
            self.rect.grid(row=y, column=x)
            self.btn= tk.Button(frame,width=2,height=1,command=partial(self.notmine,buttondict,zlist.index(i)))
            self.btn.grid(column=x, row=y,sticky="nsew")
            buttondict.update({ zlist.index(i) : self.btn})
            buttonnodict.update({self.btn : touchbuttondict[i]+1})
            
        for x in minenodict:
            newdict.update({minenodict[x]:"mine"})
        for x in buttonnodict:
            newdict.update({buttonnodict[x]:"ur good"})
        
        for x in range(1,101):
            left=x-1
            right=x+1
            up=x-10
            down=x+10
            sleft=str(left)
            stx=str(x)
            stright=str(right)
            numberdict.update({x : 0})
           
            if left>0 and left<101:            
                if len(sleft)>1:
                    if sleft[1]!="0":
                        if newdict[left]=="mine":
                            numberdict[x] += 1
                else:
                    if newdict[left]=="mine":
                        numberdict[x] += 1
            if right>0 and right<101:
                if len(stx)>1:                
                    if stx[1]!= "0":                   
                        if newdict[right]=="mine":
                            numberdict[x] +=1
                else:
                    if newdict[right]=="mine":
                        numberdict[x] += 1
            if up>0 and up<101:
                if newdict [up]=="mine":
                    numberdict[x] += 1
            if down>0 and down<101:
                if newdict[down]=="mine":
                    numberdict[x] += 1
        
        
        for x in numberdict:
            for q in touchbuttondict:
                if touchbuttondict[q]==(x-1):
                    r=q[0]
                    c=q[1]
                    z=numberdict[x]
                    self.numbers=tk.Label(frame,text=z)
                    self.numbers.grid(row=r,column=c)
                
        for x in buttondict:
            buttondict[x].lift()
        for x in minedict:
            minedict[x].lift()
        for x in otherbuttondict:
            x.lift()
    
base = tk.Tk()

app = App(base)

base.mainloop()