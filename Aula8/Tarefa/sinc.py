# -*- coding: utf-8 -*-
"""
Created on Mon Nov 4 18:23:17 2020

@author: mathe
"""

import numpy as np
import matplotlib.pyplot as plt


sample_rate = 8000
fc = 100

i = np.arange(-0.1, 0.1, 1/sample_rate)

# função sinc do livro cap 16 pag 285
w_i = np.sin(2*np.pi*fc*i)/(i*np.pi)

plt.figure("Gráficos",figsize=(15,15))
    
plt.subplot(111)
plt.grid(1)
plt.plot(i, w_i)