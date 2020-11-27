# -*- coding: utf-8 -*-
"""
Created on Tue Nov 8 07:21:47 2020

@author: mathe
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

def kernelLowPass(M, h, Fc, K = 1):
    for i in range(M):
        if i-M/2 == 0:
            h[i] = 2 * np.pi * Fc * K
        else:
            h[i] = K * (np.sin(2*np.pi*Fc*(i - M / 2))/(i-M/2)) * (0.42-0.5*np.cos((2*np.pi*i)/M) + 0.08*np.cos((4*np.pi*i)/M))
    return h
        
Fs = 8000
Fc = 1960
Bw = 200

# Normalizando
Bw = Bw / Fs
Fc = Fc / Fs
M = 4 / Bw
M = int(M)

h = np.zeros(M)
h = kernelLowPass(M, h, Fc)

soma = 0
for i in range(M):
    soma = soma + h[i]

for i in range(M):
    h[i] = h[i] / soma
    
# Inverte o filtro para transformar em PA
h = -h
h[int(M/2)] += 1
    
with open('coeficientesPA.dat', 'w') as f:
    for x in h:
        f.write(str(x.astype(np.float16))+",\n")
        
read_path = "Sweep_3800.pcm"
with open(read_path, 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    data_o = np.convolve(h, data_i)
    data_o = data_o.astype(dtype='int16')

t = np.arange(0, data_len/Fs, 1 / Fs)

plt.figure("Gráficos",figsize=(15,12))

plt.subplot(411)
plt.title("Entrada")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(t, data_i[: len(t)])

plt.subplot(412)
plt.title("Saída")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(t, data_o[: len(t)], color='purple')

[w, h] = freqz(h, worN=Fs, fs=1)

plt.subplot(413)
plt.title("Resposta em frequência")
plt.xlabel("Número de amostras")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(w, abs(h), color='black')

plt.subplot(414)
plt.title("Resposta em frequência (dB)")
plt.xlabel("Frequência")
plt.ylabel("Amplitude")
plt.grid(1)
plt.plot(w, 20*np.log10(abs(h)), color='black')

plt.tight_layout()


file_name = "resultadoPA.pcm"
with open(file_name, 'wb') as f:
    for d in data_o:
        f.write(d)