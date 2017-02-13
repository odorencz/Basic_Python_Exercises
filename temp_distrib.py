# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:21:15 2016

@author: Olivia
"""
import numpy as np
import matplotlib as plt
def single_step(D,T_current):
    import numpy as np
    T=list(T_current)
    L=len(T) 
    change0=D*(T[1]-T[0])
    changeL=D*(T[L-2]-T[L-1])
    T_change=[change0]
    for k in range(L-1):
        if k!=0 and k<(L-1):  
            changerest = D*(T[k+1]-T[k]) + D*(T[k-1]-T[k])
            T_change.append(changerest)
    T_change.append(changeL)
    Treal=np.array(T_change)
    Ttemp=T_current+Treal
    return(Ttemp)

def stats(T):
    import numpy as np
    averagez=np.average(T)
    stdev=np.std(T)
    return(averagez,stdev)

T=np.zeros(51)
T[25]=100
print(single_step(.2,single_step(.2,T)))