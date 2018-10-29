import numpy as np 
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

senal= np.genfromtxt('signal.dat', delimiter = ',')
incompletos= np.genfromtxt('incompletos.dat',delimiter=',')

fourier=np.zeros(senal.shape[0])

arreglo=np.arange(senal.shape[0])
for k in range (senal.shape[0]):
	fourier[k]=np.sum(senal[:,1]*np.exp((-2*1j*np.pi*k*(arreglo)/senal.shape[0])))
dt= senal[1,0]-senal[2,0]
print dt
frecuencias=np.fft.fftfreq(senal.shape[0],dt)
	
plt.figure()
plt.plot(frecuencias,fourier)
plt.show()
#plt.savefig('CaipaAdriana_TF.pdf')
plt.figure()
plt.plot(senal[:,0],senal[:,1])
plt.savefig("CaipaAdriana_Signal.pdf")
print "Mayores frecuencias en 383.3, 237,138.5"
