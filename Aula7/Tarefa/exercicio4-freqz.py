# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 08:04:31 2020

@author: mathe
"""

from scipy.signal import freqz
from numpy import log10
import matplotlib.pyplot as plt

plt.figure("Figura 1",figsize=(15,8))

#Questão A
"""
                z - 1,2
H(z) =  3 ----------------
           (z-0,5)(z-0,9)

"""
num_m =   [3,-3.6]
den_m = [1, -1.4, 0.45]
w, h = freqz(num_m, den_m)
plt.subplot(3, 1, 1)
plt.title("Questão A")
plt.plot(w, 20 * log10(abs(h)), color='green')
plt.grid()

#Questão B
"""
                z
H(z) =  ----------------
         (z-0,9)(z-1,2)

"""
num_m = [1, 0]
den_m = [1, -2.1, 1.08]
w, h = freqz(num_m, den_m)
plt.subplot(3, 1, 2)
plt.title("Questão B")
plt.plot(w, 20 * log10(abs(h)), color='blue')
plt.grid()

#Questão C
"""
                z
H(z) =  ----------------
         z^2 + z + 0,41

"""
num_m = [1, 0.9]
den_m = [1, 1, 0.41]
w, h = freqz(num_m, den_m)
plt.subplot(3, 1, 3)
plt.title("Questão C")
plt.plot(w, 20 * log10(abs(h)), color='black')
plt.grid()

plt.tight_layout()
# Salvando os gráficos
plt.savefig("graficos_freqz.png", format="png")
plt.show()