# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 08:42:04 2020

@author: mathe
"""

  
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

n = np.arange(0, 9)
l = np.size(n)
s = np.zeros(l)
ind = np.where(n==0)
s[ind] = 1

plt.stem(n,s)
plt.title('Impulso Unitario')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

with open("impulso.pcm", "wb") as new_file:
    for x in s:
        new_file.write(x)
new_file.close()