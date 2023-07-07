#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 17:52:21 2023

@author: sethguzman
"""

import numpy as np
import matplotlib.pyplot as plt

#define a function that computes the n+1 

def aliens(F, n):
    
    """
    Parameters
    ----------
    F : float array
        F(n) is the fibonochi number
    N : integer
        index into F
    
    Returns
    -------
    F(n+1), othe [n+1] st fibonnaci number
    
    """
    print(F[n-1], F[n-2])
    F[n] = F[n-1] + F[n-2]
    return F[n]


def aliens2(F, n):
    
    
    
    
    if len(F) < 2:
        print('F is not long enonugh')
        return(0)
     
        F.append(F[n-1]+F[n-2])
        return F[n]
    
    
if __name__ == "__main__":
    
        
        # first use an array
        
        
        F = np.zeros(100)
        F[0] = 0
        F[1] = 1
        
        for n in range (2, 19):
            F[n] = aliens(F, n)
            
            
        d =  []
        for n in range (2, 19):
            d.append(F[n]/F[n-1])
            
        
                
        plt.plot(d, '.') 
        plt.title('golden')
        plt.xlabel('ratio numbers')
        plt.ylabel('golden ratio')
        plt.grid()
                
                
                
                
                
                