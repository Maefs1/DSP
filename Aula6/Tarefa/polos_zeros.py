# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 04:57:42 2020

@author: mathe
"""

import numpy as np
from zplane import zplane

"""
        Z^2 + 1.5Z + 2
D(Z) =  --------------
             Z^2
"""
#Definindo os valores
num = np.array([1, 1.5, 2])
den = np.array([1, 0, 0])

#Chamando a funcao para calcular as raizes
num_roots = np.roots(num)
den_roots = np.roots(den)

print("Zeros: ")
print(num_roots)
print("Polos: ")
print(den_roots)

#Chamando zplane para mostrar os polos e zero
zplane(num, den)
