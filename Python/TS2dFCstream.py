#!/usr/bin/env python
# coding: utf-8

# In[3]:

# This function takes as input "time-series", size of window "W", and the value of shifting the window "lag", to calculate the dynamic functional connectivity stream "dFCstream" as output

# inputs: TS(t,n) --> rows are t different time-points
#                     columns are n different regions
#         W       --> size of window to slide
#         lag     --> shifting value, default is lag = W
#         frmt    --> '2D' (default) provides a [l]x[F] dFCstream (FC vector over time) where l = n(n-1)/2 is
#                      the number of links for n regions and F is the number frames depending on value of (t,W,lag)
#                     '3D' provides a [n]x[n]x[F] dFCstream (FC matrix over time)
#
#
# Example: dfcstream = TS2dFCstream(ts,10,10,'2D')
# Example: dfcstream = TS2dFCstram(ts,10,None,'2D')
# these two examples compute the dFCstream with window size 10 and without overlap between windows.
# since lag assumes a value equal to the default one. The above syntax is equivalent to the simpler version in below:
# Example: dfcstream = TS2dFCstream(ts,10)

# Reference: Lucas Arbabyazd et al. (2020) MethodsX

import numpy as np
from TS2FC import TS2FC

def TS2dFCstream(*args):
    
    TS = args[0]
    
    if len(args) == 1:
        return print('Prove at least a window size!')
    
    if len(args) == 2:
        W = args[1]
        lag = W
        frmt = '2D'
    if len(args) == 3:
        W = args[1]
        lag = args[2]
        frmt = '2D'
    if len(args) == 4:
        W = args[1]
        frmt = args[3]
        if args[2]!=None:
            lag = args[2]
        else:
            lag = W   
      
        
    t = TS.shape[0]
    n = TS.shape[1]
    l = int(n*(n-1)/2)
    
    wstart = 0
    wstop = W
    k = 0
    while (wstop <= t):
        wstart = wstart + lag
        wstop = wstop + lag
        k = k + 1
    
    kmax = k
    
    if frmt == '2D':
        dFCstream = np.zeros((l,kmax))

        wstart = 0
        wstop = W
        k = 0
        while (wstop <= t):
            dFCstream[:,k] = TS2FC(TS[wstart:wstop,:],'1D')
            wstart = wstart + lag
            wstop = wstop +lag
            k = k + 1

        return dFCstream
    
    else:
        dFCstream = np.zeros((n,n,kmax))
        
        wstart = 0
        wstop = W
        k = 0
        while (wstop <= t):
            dFCstream[:,:,k] = TS2FC(TS[wstart:wstop,:],'2D')
            wstart = wstart + lag
            wstop = wstop +lag
            k = k + 1
        
        return dFCstream