# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 07:46:19 2020

@author: mathe
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, log10, exp

plt.figure("Figura 1",figsize=(15,8))

#Definindo omega
w = np.arange(0, pi, pi/1000)

#Questão A
"""
                -1,2
H(z) =  3 ----------------
           (z-0,5)(z-0,9)

"""
num_m = 3 * (1*exp(-1j*w) - 1.2)
den_m = (exp(-1j*w) - 0.5) * (exp(-1j*w) - 0.9)
plt.subplot(311)
plt.title("Questão A")
plt.grid(1)
plt.plot(w, 20 * log10(abs(num_m/den_m)), color='green')
plt.xticks(np.arange(0, 3.1, 0.5))
plt.yticks(np.arange(0, 25.1, 5))


#Questão B
"""
                z
H(z) =  ----------------
         (z-0,9)(z-1,2)

"""
num_m = exp(-1j*w)
den_m = (exp(-1j*w) - 0.9) * (exp(-1j*w) - 1.2)
plt.subplot(312)
plt.title("Questão B")
plt.grid(1)
plt.plot(w, 20 * log10(abs(num_m/den_m)), color='blue')
plt.xticks(np.arange(0, 3.1, 0.5))
plt.yticks(np.arange(-10, 35.1, 10))


#Questão C
"""
                z
H(z) =  ----------------
         z^2 + z + 0,41

"""
num_m = (exp(-1j*w) + 0.9)
den_m = exp(-2j*w) + exp(-1j*w) + 0.41
plt.subplot(313)
plt.title("Questão C")
plt.grid(1)
plt.plot(w, 20 * log10(abs(num_m/den_m)), color='black')
plt.xticks(np.arange(0, 3.1, 0.5))
plt.yticks(np.arange(-15, 10.1, 5))


plt.tight_layout()
# Salvando os gráficos
plt.savefig("graficos.png", format="png")
plt.show()

