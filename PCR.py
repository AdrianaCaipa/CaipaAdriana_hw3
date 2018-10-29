import numpy as np
import matplotlib.pyplot as plt 

##Almecene los datos###
datos_numeros= np.genfromtxt('http://ftp.cs.wisc.edu/math-prog/cpo-dataset/machine-learn/cancer/WDBC/WDBC.dat',delimiter=',')
etiqueta= np.genfromtxt('http://ftp.cs.wisc.edu/math-prog/cpo-dataset/machine-learn/cancer/WDBC/WDBC.dat',delimiter=',',dtype='str')


datos_nuevos = np.delete(datos_numeros,1,1)
print datos_nuevos

x=np.zeros(datos_nuevos.shape)
for i in range(datos_nuevos.shape[1]):
	promedio=np.mean(datos_nuevos[:,i])
	x[:,i]=datos_nuevos[:,i]-promedio
	desviacion= (np.var(datos_nuevos[:,i]))**(0.5)
	x[:,i]= x[:,i]/desviacion
	print x[:,i]
	
	
