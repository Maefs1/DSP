# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 08:22:37 2020

@author: mathe
"""

import numpy as np
import matplotlib.pyplot as plt

#conta de teste 20*log10(11000/16384)

#Criando variáveis
media_buf = np.zeros(2)
saida = 0

#
Fc = 1000
Fs = 8000

#Calculando Omega
wc = 2*np.pi*Fc     #6280

# F'
F1 = 2 * Fs     #16000

# coeficientes
a = wc/(F1+wc)
b = (wc-F1)/(F1+wc)

read_path = "sen_1k.pcm"
with open(read_path, 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    data_o = np.zeros_like(data_i)

    for i in range(data_len):
        media_buf[0] = data_i[i]

        m = a*media_buf[0] + a*media_buf[1] - b*saida
        saida = m     
        data_o[i] = m
        media_buf[1:2] = media_buf[0:1]


print("Valor de a: " ,a)
print("Valor de b: " ,b)



plt.figure("Gráficos",figsize=(25,12))

plt.subplot(211)
plt.title("Entrada")
plt.xlabel("Frequência")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(data_i)


plt.subplot(212)
plt.title("Saida")
plt.ylabel("Amplitude")
plt.xlabel("Frequência")
plt.grid(1)
plt.plot(data_o)
plt.xticks(np.arange(0, 40001, 1000))

plt.tight_layout()



file_name = "Sweep10_3600_result.pcm"
with open(file_name, 'wb') as f:
    for d in data_o:
        f.write(d)
    
plt.show()
