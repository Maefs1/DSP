# -*- coding: utf-8 -*-
"""
Created on Mon Nov 2 20:48:41 2020

@author: mathe
"""

import numpy as np
import matplotlib.pyplot as plt

M = 500
Fc = 0.04
K = 1

h = np.zeros(M)

for i in range(M):
    if i-M/2 == 0:
        h[i] = 2 * np.pi * Fc * K
    else:
        h[i] = K * (np.sin(2*np.pi*Fc*(i - M / 2))/(i-M/2)) * (0.42-0.5*np.cos((2*np.pi*i)/M) + 0.08*np.cos((4*np.pi*i)/M))
 
        
plt.figure("Gráficos",figsize=(15,8))
    
plt.title("Filtro kernel")
plt.xlabel("Amostras")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(h)




