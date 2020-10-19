# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 07:14:31 2020

@author: mathe
"""

import numpy as np
import matplotlib.pyplot as plt

#Definindo parâmetros
sample_rate = 8000
media_len = 8
media_buf = np.zeros(media_len)

read_path = "../Sweep10_3600.pcm"
with open(read_path, 'rb') as file:
    buf = file.read()
    data_i = np.frombuffer(buf, dtype='int16')
    #data_i = [8,6,4,2]
    data_len = len(data_i)

    #Salvando o valor da entrada em outra variável
    data_o = np.zeros_like(data_i)

    #Simulando o funcionamento dos blocos de media movel
    for i in range(data_len):
        media_buf[0] = data_i[i]
        m = np.sum(media_buf)/media_len
        data_o[i] = m
        buf = media_buf[0:media_len-1]
        media_buf[1:media_len] = buf

#Arrumando o tempo do plot
t = np.arange(0, data_len/sample_rate, 1 / sample_rate)


plt.figure("media_movel", figsize=(15,8))
#Plotando a entrada
plt.subplot(211)
plt.title("Entrada")
plt.plot(t,data_i)
#plt.stem(t,data_i)
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")

#Plotando a média
plt.subplot(212)
plt.title("Média móvel")
plt.plot(t,data_o)
#plt.stem(t,data_o)
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")

plt.tight_layout()


file_name = "../media_movel_result.pcm"
with open(file_name, 'wb') as file:
    for i in data_o:
        file.write(i)
