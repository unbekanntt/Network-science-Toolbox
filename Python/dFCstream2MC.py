#!/usr/bin/env python
# coding: utf-8

# In[1]:

# This function takes as input the 2D or 3D "dFCstream" calculated from TS2dFCstream function and returns meta-connectivity (MC) as output. 


# Example: mc = dFCstream2MC(dfcstream)

# Reference: Lucas Arbabyazd et al. (2020) MethodsX

import numpy as np
from Matrix2Vec import Matrix2Vec

def dFCstream2MC(dFCstream):
    
    if len(dFCstream.shape)==3:
        FCstr=Matrix2Vec(dFCstream)
        
    if len(dFCstream.shape)==2:
        FCstr=dFCstream
        
        
    if FCstr.shape[0] > 20000:
        return print('Caution! If number of your parcellation > 200 regions, this function may take one minutes, instead you can only calculate trimers of MC, using dFCstream2Tri function!')
    
    MC = np.corrcoef(FCstr)
    MC = MC - np.eye(MC.shape[0])
    return MC