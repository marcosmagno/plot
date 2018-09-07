"""
Demo of the errorbar function
"""
# -*- coding: utf-8 -*-
from pylab import *
import numpy
import matplotlib.pyplot as plt


# Dual
x = (0,1)
#	 Single 	 Dual
y = [1.818988, 1.563357 ]  # media
yerr = [0.844069, 0.814921]  # desvio padrao
width = 0.15 

fig = plt.figure()
#ax = plt.axes()
#fig, ax = plt.subplots()

#plt.xticks(np.arange(min(x), max(x)+1, 1.0), x)
# standard error bars
bar1 = plt.bar(x[0], y[0], width=0.60,color='r',  label='Um celular', yerr=yerr[0])

bar2 = plt.bar(x[1], y[1], width=0.60,  color='b',  label='Dois celulares',  yerr=yerr[1], hatch="/", edgecolor='black')
#plt.yticks(labelsize=40)
plt.ylabel(r"$y$",fontsize=12)
plt.xlabel(r"$y$",fontsize=12)

plt.xlabel('Node ID')
plt.ylabel('Bitrate Mb/s')
plt.xticks(x, ('Um celular', 'Dois celulares'))
plt.legend()

plt.show()
