
"""
Created on Wed Oct 31 19:54:46 2018

@author: adria
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy import fftpack
from scipy.fftpack import fft, fftfreq
###Sacado de https://matplotlib.org/users/colormapnorms.html###
### Sacado de https://www.scipy-lectures.org/intro/scipy/auto_examples/solutions/plot_fft_image_denoise.html###
arbol = plt.imread('Arboles.png')
fourier_arbol = np.fft.fft(arbol)
plt.figure()
plt.imshow(np.abs(fourier_arbol), norm=LogNorm(vmin=2)) ##Escala 
plt.colorbar()
plt.savefig('CaipaAdriana_FT2D.pdf')
 
r, c = fourier_arbol.shape # r y c to son el numero de filas y columnas del arreglo.
a_filter = 25#Filtro que escogi 
fourier_arbol[:,a_filter:r-a_filter] = 0 #Volver ceros columnas aplicando el filtro
fourier_arbol[a_filter:r-a_filter,:] = 0 #Volver ceros las filas aplicando el filtro
plt.figure()
plt.imshow(np.abs(fourier_arbol), norm=LogNorm(vmin=2))
plt.colorbar()
plt.savefig('CaipaAdriana_FT2D_filtrada.pdf')

filtro = fftpack.ifft2(fourier_arbol)
plt.figure()
plt.imshow(abs(filtro), plt.cm.gray)
plt.savefig('CaipaAdriana_Imagenfiltrada.pdf') #Creo que hay un error, la imagen que salees totalemnte gris.