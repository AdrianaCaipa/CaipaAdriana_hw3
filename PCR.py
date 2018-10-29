import numpy as np
import matplotlib.pyplot as plt 
from numpy import linalg as LA

##Almecene los datos###
datos_numeros= np.genfromtxt('http://ftp.cs.wisc.edu/math-prog/cpo-dataset/machine-learn/cancer/WDBC/WDBC.dat',delimiter=',')
etiqueta= np.genfromtxt('http://ftp.cs.wisc.edu/math-prog/cpo-dataset/machine-learn/cancer/WDBC/WDBC.dat',delimiter=',',dtype='str')


datos_nuevos = np.delete(datos_numeros,1,1)
#print datos_nuevos

x=np.zeros(datos_nuevos.shape)
for i in range(datos_nuevos.shape[1]):
	promedio=np.mean(datos_nuevos[:,i])
	x[:,i]=datos_nuevos[:,i]-promedio
	desviacion= (np.var(datos_nuevos[:,i]))**(0.5)
	x[:,i]= x[:,i]/desviacion
	
matriz_cov=np.zeros([datos_nuevos.shape[1],datos_nuevos.shape[1]])	
for i in range(datos_nuevos.shape[1]):
	for j in range(datos_nuevos.shape[1]):
		matriz_cov[i,j]= np.sum(x[:,i]*x[:,j])/(datos_nuevos.shape[1]-1)
		
print matriz_cov

###Autovalores y autovectores###
w,v=LA.eig(matriz_cov)
for i in range(len(w)):
	
	print "El valor propio es",w[i]
	print "El vector propio es",v[i]  

###
