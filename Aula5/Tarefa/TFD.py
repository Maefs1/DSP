# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 04:44:17 2020

@author: mathe
"""

import numpy as np
import matplotlib.pyplot as plt
"""
                    1
 X(e^jw) =     ------------
                1 - ae^-jw
"""
#modulo = variacao do w
#

#Definindo o valor de a
a = 0.5

#Definindo o valor de omega
w = np.arange(-1*np.pi, np.pi, np.pi/100)

#Definindo a equacao
D = 1 - a * np.exp(-1j*w)
X = 1 / D

#Chamando funcao para calcular
Modulo_X = np.abs(X)
Fase_X = np.angle(X)

#Ajustando o tamanho do plot
plt.figure("TFD", figsize=(15,8))
    
plt.subplot(211)
plt.title("Módulo", color='green')
plt.grid(1)
plt.plot(w, Modulo_X, color='green')
    
plt.subplot(212)
plt.title("Fase", color='red')
plt.grid(1)
plt.plot(w, Fase_X, color='red')
    
plt.tight_layout()

#Salvando o plot
plt.savefig("Módulo_Fase.png", format="png")

plt.show()