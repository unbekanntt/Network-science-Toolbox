#!/usr/bin/env python
# coding: utf-8

# In[1]:

# This function takes as input the '3D' dFCstream and convert it to '2D' dFCstream.


# Reference: Lucas Arbabyazd et al. (2020) MethodsX

import numpy as np
import itertools

def Vec2Matrix(dFCstream_2D):
    
    if len(dFCstream_2D.shape)==3:
        return print('You do not need this function since your dFCstream is alread 3D')
    
    l = dFCstream_2D.shape[0]
    t = dFCstream_2D.shape[1]
    n = int((1 +  np.sqrt(1+8*l)) / 2)
    CN = np.array(list(itertools.combinations(range(n), 2)))
    dFCstream_3D = np.zeros((n,n,t))
    
    for i in range(l):
        dFCstream_3D[CN[i,0],CN[i,1],:] = dFCstream_2D[i,:]
        
    
    dFCstream_3D = dFCstream_3D + np.transpose(dFCstream_3D, (1,0,2))    
    
    return dFCstream_3D



