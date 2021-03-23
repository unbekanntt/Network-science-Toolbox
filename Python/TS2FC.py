#!/usr/bin/env python
# coding: utf-8

# In[1]:

# This function takes as input the "time-series" and optional "format" to calculate static functional connectivity (FC) as output. 

# inputs: TS(t,n) --> rows are t different time-points
#                     columns are n different regions
#         frmt    --> '2D' (default) provides a square [n]x[n] FC matrix
#                     '1D' provides the upper-triangular portion of the FC matrix as [n(n-1)/2]x[1] column vector
# Example: fc = TS2FC(ts,'1D')

# Reference: Lucas Arbabyazd et al. (2020) MethodsX

import numpy as np

def TS2FC(*args):
        
    TS = args[0]
    
    if len(args) < 2:
        frmt = '2D'
    else:
        frmt = args[1] 
        
    
    n = TS.shape[1]
    xo = np.triu_indices(n, k = 1)
    
    FCm = np.corrcoef(TS.T)
    np.fill_diagonal(FCm, 0)
    FCv = FCm[xo]
    
    if frmt == '2D':
        return FCm
    else:
        return FCv