"""
Demo of the errorbar function
"""
# -*- coding: utf-8 -*-

from pylab import*
import numpy
import matplotlib.pyplot as plt


# Dual
x = (0,1)
#	 Single 	 Dual
y = [129.748485, 221,151515 ]  # media
yerr = [9.851692, 11,779749]  # desvio padrao
width = 0.15 

fig = plt.figure()
#ax = plt.axes()
#fig, ax = plt.subplots()

#plt.xticks(np.arange(min(x), max(x)+1, 1.0), x)
# standard error bars
bar1 = plt.bar(x[0], y[0], width=0.60,color='r',  label='Largura de banda única', yerr=yerr[0])

bar2 = plt.bar(x[1], y[1], width=0.60,  color='b',  label='Maior largura de banda',  yerr=yerr[1], hatch="/", edgecolor='black')


plt.xlabel('ID do Nó')
plt.ylabel('Pacotes recebidos por segundo (pcts/s)')
plt.xticks(x, ('Nó 0', 'Nó 0'))
plt.legend()

plt.show()