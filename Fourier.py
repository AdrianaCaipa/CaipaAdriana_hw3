# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 20:50:05 2018

@author: adria
"""

import numpy as np 
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from scipy import interpolate 

senal= np.genfromtxt('signal.dat', delimiter = ',')
incompletos= np.genfromtxt('incompletos.dat',delimiter=',')

fourier=np.zeros(senal.shape[0])+0*1j

arreglo=np.arange(senal.shape[0])
for k in range (senal.shape[0]):
	fourier[k]=np.sum(senal[:,1]*np.exp((-2*1j*np.pi*k*(arreglo)/senal.shape[0])))
dt= senal[2,0]-senal[1,0]
print (dt)
frecuencias=np.fft.fftfreq(senal.shape[0],dt)

plt.figure()
plt.plot(frecuencias,abs(fourier))

plt.savefig('CaipaAdriana_TF.pdf')
plt.figure()
plt.plot(senal[:,0],senal[:,1])
plt.savefig("CaipaAdriana_Signal.pdf")
print ("Mayores frecuencias en 383.3, 237,138.5")

valores=np.zeros(frecuencias.shape[0])
for i in range(frecuencias.shape[0]):
	if abs(frecuencias[i])<=1000:
		valores[i]=1

valores1= fourier*valores
inversa= np.fft.ifft(valores1)
plt.figure()
plt.plot(senal[:,0],inversa)
plt.savefig('CaipaAdriana_filtrada.pdf')

print ("No se puede realizar la transformada de Fourier de los datos incompletos porque presentan distintas frecuencias")

x_tabla= incompletos[:,0]
y_tabla= incompletos[:,1]
x1=np.linspace(0.000390625,0.028515625,512)
###Interpolacion de datos incompletos###
def interpolacion_cuad(x1,x_tabla,y_tabla):
    funcion_cuadratica=interpolate.interp1d(x_tabla,y_tabla,kind = "quadratic")
    return (funcion_cuadratica(x1))
def interpolacion_cub(x1,x_tabla,y_tabla):
    funcion_cubica=interpolate.interp1d(x_tabla,y_tabla,kind= "cubic")
    return (funcion_cubica(x1))

dt=x1[2]-x1[1]
fourier1= np.fft.fft(interpolacion_cuad(x1,x_tabla,y_tabla))
fourier2= np.fft.fft(interpolacion_cub(x1,x_tabla,y_tabla))

frecuencias1=np.fft.fftfreq(x1.shape[0],dt)
frecuencias2=np.fft.fftfreq(x1.shape[0],dt)
#######Grafica fourier###
plt.figure()
plt.subplot(311)
plt.plot(frecuencias, fourier,c='m', label = 'Fourier senal')
plt.legend()
plt.subplot(312)
plt.plot(frecuencias1, fourier1,c='c', label = 'Interpola cuad')
plt.legend()
plt.subplot(313)
plt.plot(frecuencias2, fourier2,c='r', label = 'Interpola cub')
plt.legend()
plt.savefig("CaipaAdriana_TF_Interpola.pdf")

#####Filtro 1000Hz####
print ("Los valores mas alejados del cero cambian mucho la amplitud, comparando la interpolacion cuadratica, cubica y la senal")

valores_2=np.zeros(frecuencias.shape[0])
for i in range(frecuencias.shape[0]):
	if abs(frecuencias[i])<=1000:
		valores_2[i]=1
        
valores_nuevos= fourier*valores_2
inversa1= np.fft.ifft(valores_nuevos)

valores_3=np.zeros(frecuencias1.shape[0])
for i in range(frecuencias1.shape[0]):
	if abs(frecuencias1[i])<=1000:
		valores_3[i]=1
        
valores_nuevos1= fourier*valores_3
inversa2= np.fft.ifft(valores_nuevos1)
      
        
valores_4=np.zeros(frecuencias2.shape[0])
for i in range(frecuencias2.shape[0]):
	if abs(frecuencias2[i])<=1000:
		valores_4[i]=1
        
valores_nuevos2= fourier*valores_4
inversa3= np.fft.ifft(valores_nuevos2)
  

plt.figure()
plt.subplot(311)
plt.plot(senal[:,0],inversa1,c='m', label = 'Fourier senal')
plt.legend()
plt.subplot(312)
plt.plot(senal[:,0],inversa2,c='c', label = 'Interpola cuad')
plt.legend()
plt.subplot(313)
plt.plot(senal[:,0],inversa3,c='r', label = 'Interpola cub')
plt.title('Filtro 1000Hz')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.savefig("CaipaAdriana_2Filtros1000Hz.pdf")
#####Filtro 500Hz####
valores_5=np.zeros(frecuencias.shape[0])
for i in range(frecuencias.shape[0]):
	if abs(frecuencias[i])<=500:
		valores_5[i]=1
        
valores_nuevos3= fourier*valores_5
inversa4= np.fft.ifft(valores_nuevos3)

valores_6=np.zeros(frecuencias1.shape[0])
for i in range(frecuencias1.shape[0]):
	if abs(frecuencias1[i])<=500:
		valores_6[i]=1
        
valores_nuevos4= fourier*valores_6
inversa5= np.fft.ifft(valores_nuevos4)

valores_7=np.zeros(frecuencias2.shape[0])
for i in range(frecuencias2.shape[0]):
	if abs(frecuencias2[i])<=500:
		valores_7[i]=1
        
valores_nuevos5= fourier*valores_7
inversa6= np.fft.ifft(valores_nuevos5)

plt.figure()
plt.subplot(311)
plt.plot(senal[:,0],inversa4,c='m', label = 'Fourier senal')
plt.legend()
plt.subplot(312)
plt.plot(senal[:,0],inversa5,c='c', label = 'Interpola cuad')
plt.legend()
plt.subplot(313)
plt.plot(senal[:,0],inversa6,c='r', label = 'Interpola cub')
plt.title('Filtro 500Hz')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()

plt.savefig("CaipaAdriana_2Filtros.pdf")
