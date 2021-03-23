#!/usr/bin/env python
# coding: utf-8

# In[1]:

# This function takes as input the 2D or 3D "dFCstream" calculated from TS2dFCstream function and returns dynamic functional connectivity (dFC) as output. 


# Example: dfc = dFCstream2MC(dfcstream)

# Reference: Lucas Arbabyazd et al. (2020) MethodsX

import numpy as np
from Matrix2Vec import Matrix2Vec

def dFCstream2dFC(dFCstream):
    
    if len(dFCstream.shape)==3:
        FCstr=Matrix2Vec(dFCstream)
        
    if len(dFCstream.shape)==2:
        FCstr=dFCstream
    
    
    if FCstr.shape[1] > 20000:
        return print('Caution! If length of your dFCstream > 20,000 time-points, this function may take one minutes, if you persist, please comment me!')
    
    dFC = np.corrcoef(FCstr.T)
    
    return dFC