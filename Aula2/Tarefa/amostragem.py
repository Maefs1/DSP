# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 00:24:33 2020

@author: mathe
"""

import numpy as np
import matplotlib.pyplot as plt


#Sinal analogico
Dt = 5*(10**(-5))
t = np.arange(-5*10**-3, 5*10**-3, Dt)

#Plota o sinal analógico
f = 400
xa = np.sin(2*np.pi*f*t)

plt.subplot(2,1,1)
plt.title("Sinal")
plt.plot(t*1000, xa)
plt.xlabel('Tempo [ms]')
plt.ylabel('xa(t)')
plt.grid(1)

#Sinal discreto
Fs = 8000
Ts = 1/Fs
n = np.arange(-20, 20, 1)
xd = np.sin(2*np.pi*n*f/Fs)
plt.stem(n*Ts*1000, xd, 'r');



#Plota sinal amostrado
plt.subplot(2,1,2)
plt.stem(n,xd)
plt.title('Sinal amostrado')
plt.xlabel('Amostras')
plt.ylabel('x[n]')
plt.grid(1)

plt.tight_layout()