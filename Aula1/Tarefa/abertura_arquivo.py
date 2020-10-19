# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 23:19:25 2020

@author: mathe
"""
import numpy as np
import matplotlib.pyplot as plt


#Lendo arquivo
with open("alo.pcm",'rb' ) as file:
    fid = file.read()
    file.close
    data_i = np.frombuffer(fid, dtype='int16')
    data_len = len(data_i)
    

plt.subplot(211)
plt.title("Sinal de entrada")
plt.grid(1)
plt.plot(data_i)

#Criando ganho
a = .5

# Processando a entrada
data_o = np.ones_like(data_i)
for i in range (data_len):
    data_o[i] = data_i[i] * a
    
plt.subplot(212)
plt.title("Sinal de saída")
plt.grid(1)
plt.plot(data_o)

plt.tight_layout()

#Salvando arquivo
with open("aloSaida.pc", 'wb') as new_file:
    for data in data_o:
        new_file.write(data)
    new_file.close()
    

#Salvando o plot
plt.savefig("grafico_sinais.png", format='png')
    

    