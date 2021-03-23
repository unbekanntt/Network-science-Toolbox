#!/usr/bin/env python
# coding: utf-8

# In[1]:

# This function takes as input the '3D' dFCstream and convert it to '2D' dFCstream.


# Reference: Lucas Arbabyazd et al. (2020) MethodsX

import numpy as np

def Matrix2Vec(dFCstream_3D):
    
    if len(dFCstream_3D.shape)==2:
        return print('You do not need this function since your dFCstream is alread 2D')
    
    n = dFCstream_3D.shape[0]
    l = n*(n-1)/2
    F = dFCstream_3D.shape[2]
    xo = np.triu_indices(n, k = 1)
    
    dFCstream_2D = np.zeros((int(l), int(F)));
                  
    for f in range(F):
        fc = dFCstream_3D[:,:,f]
        dFCstream_2D[:,f] = fc[xo]
        
    return dFCstream_2D



