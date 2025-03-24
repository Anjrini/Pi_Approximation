# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 10:40:35 2025

@author: Mustafa anjrini
"""

import numpy as np

n=100000000
z=2+(2*n-1)**2/(2+(2*n+1)**2)
for i in range(n-1,1,-1):
    z=2+(2*i-1)**2/z
    
z # Printing the value of the approximation

np.pi # Printing the value of the actual Pi


